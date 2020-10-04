from typing import (
    Optional, Any, Dict, Tuple, Type, Callable, ClassVar
)

from pydantic import BaseModel, ValidationError, validator
from pydantic.fields import ModelField

class FieldSchema(BaseModel):
    FIELD_SCHEMA: ClassVar[str] = 'field_schema'
    TYPECONV: ClassVar[str] = 'typeconv'

    required: bool
    name: str
    typeclass: Any
    typeconv: Optional[Callable[[Any], Any]] = None
    help: Optional[str] = ''
    default: Optional[Any] = None

class SectionSchema(object):

    def __init__(self, **fields: FieldSchema):
        self.fields = fields

        for k, v in fields.items():
            setattr(self, k, v)

    @classmethod
    def from_fields(cls, fields: Dict[str, ModelField]) -> 'SectionSchema':
        ret = cls()

        for field_name, field in fields.items():
            extra = field.field_info.extra

            field_schema = extra.get(
                FieldSchema.FIELD_SCHEMA, None)

            typeconv = extra.get(FieldSchema.TYPECONV, None)
            field_schema = field_schema or \
                FieldSchema(
                    required=field.required,
                    name=field.field_info.title or field.name,
                    typeclass=field.type_,
                    typeconv=typeconv,
                    help=field.field_info.description or '',
                    default=field.get_default()
                )

            setattr(ret, field_name, field_schema)

        return ret

class Section(BaseModel):
    NAME: ClassVar = "default"

    class Config:
        validate_assignment = True

    @classmethod
    def section_schema(cls) -> SectionSchema:
        return SectionSchema.from_fields(cls.__fields__)

class Config(BaseModel):

    def __init__(self, *args: Any, **kwargs: Section) -> None:
        super(Config, self).__init__(*args, **kwargs)

    @property
    def sections(self) -> Dict[str, Type[Section]]:
        return {
            k: getattr(self, k) for k in self.__fields_set__
        }
