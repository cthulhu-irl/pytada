import argparse
import inspect
from typing import Type, List

from pydantic import BaseModel
from pydantic.fields import SHAPE_LIST

from .general import exceptioner

class Command(BaseModel):
    pass

class CLI(BaseModel):
    pass

class ARGVCLIParser(object):
    SHORT_OPT = 'short_opt'
    LONG_OPT = 'long_opt'
    POSITIONAL = 'positional'
    ISFLAG = 'flag'

    def __init__(self, klass: Type['CLI'], prog: str = ''):
        self.klass = klass
        self.handler = argparse.ArgumentParser(prog=prog)

    @classmethod
    def _get_short_opt(cls, field):
        return field.field_info.extra.get(cls.SHORT_OPT, '')

    @classmethod
    def _get_long_opt(cls, field):
        long_opt = field.field_info.extra.get(cls.LONG_OPT, '')
        return long_opt or field.name

    @classmethod
    def _get_help(cls, field):
        return cls.field.field_info.description or ''

    @classmethod
    def _is_positional(cls, field):
        return field.field_info.extra.get(cls.POSITIONAL, False)

    @classmethod
    def _is_flag(cls, field):
        return field.field_info.extra.get(cls.ISFLAG, False)

    @classmethod
    def _is_list(cls, field):
        return field.shape == SHAPE_LIST

    @classmethod
    def _is_command(cls, field):
        # poorman's RTTI polymorphism check :(
        return Command in inspect.getmro(field.type_)

    @classmethod
    def _add_argument(cls, handler, field):
        def raise_type_error(exc):
            raise argparse.ArgumentTypeError(exc.msg)

        positional = cls._get_positional(field)
        isflag = cls._is_flag(field) and not positional
        islist = cls._is_list(field)
        short_opt = cls._get_short_opt(field).strip('-')
        long_opt = cls._get_long_opt(field).strip('-')
        help = cls._get_help(field)
        opts = []

        if not positional:
            if short_opt:
                short_opt = f'-{short_opt}'
                opts.append(short_opt)

            long_opt = f'--{long_opt}'

        opts.append(long_opt)

        action = 'store_true' if isflag else ''
        action = action or ('append' if islist else '')
        action = action or 'store'

        nargs = '' if islist else '?'
        nargs = nargs or field.field_info.max_items or ''
        nargs = nargs or ('+' if field.required else '*')

        return handler.add_argument(
            *opts,
            type=exceptioner(field.validator, raise_type_error),
            help=help,
            dest=field.name,
            action=action,
            required=field.required,
            default=field.default,
            nargs=nargs
        )

    @classmethod
    def _add_command(cls, subparsers, field):
        handler = subparsers.add_parser(
            field.name,
            help=cls._get_help(field),
            aliases=[field.alias]
        )

        return cls._add_fields(handler, field.type_)

    @classmethod
    def _add_fields(cls, handler, model):
        subparsers = handler.add_subparsers()

        for subfield in model.__fields__.values():
            if cls._is_command(subfield):
                cls._add_command(subparsers, subfield)

            else:
                cls._add_argument(handler, subfield)

    def parse(self, argv: List[str]) -> 'CLI':
        self._add_fields(self.handler, self.klass)

        namespace = self.handler.parse_args(argv)

        return self.klass(**vars(namespace))

    def unparse(self, cli: 'CLI') -> List[str]:
        raise NotImplementedError()
