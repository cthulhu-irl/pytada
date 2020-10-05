from inspect import getmro
from typing import (
    Optional, Any, Dict, Tuple, Type, Callable, ClassVar, List
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

    def __init__(
        self,
        fieldschema_factory=FieldSchema,
        **fields: FieldSchema
    ) -> None:
        self.fieldschema_factory = fieldschema_factory
        self.fields = fields

        for k, v in fields.items():
            setattr(self, k, v)

    def from_fields(self, fields: Dict[str, ModelField]) -> 'SectionSchema':
        for field_name, field in fields.items():
            extra = field.field_info.extra

            field_schema = extra.get(
                FieldSchema.FIELD_SCHEMA, None)

            typeconv = extra.get(FieldSchema.TYPECONV, None)
            field_schema = field_schema or \
                self.fieldschema_factory(
                    required=field.required,
                    name=field.field_info.title or field.name,
                    typeclass=field.type_,
                    typeconv=typeconv,
                    help=field.field_info.description or '',
                    default=field.get_default()
                )

            self.fields[field_name] = field_schema
            setattr(self, field_name, field_schema)

        return self

class Section(BaseModel):
    NAME: ClassVar[str] = "default"

    class Config:
        validate_assignment = True

    @classmethod
    def section_schema(cls) -> SectionSchema:
        instance = SectionSchema(FieldSchema)
        return SectionSchema.from_fields(instance, cls.__fields__)

class Config(BaseModel):

    def __init_subclass__(cls) -> None:
        cls.restrict_field_types([Section])

    @classmethod
    def restrict_field_types(cls, types: List[object]) -> None:
        for k, v in cls.__fields__.items():
            # not a good way of runtime polymorphism check at all
            if not any(t in getmro(v.type_) for t in types):
                raise TypeError(
                    f"'{k}' field is not of Section type "
                    "or subclass, but is '{str(v)}'"
                )

    @property
    def sections(self) -> Dict[str, Type[Section]]:
        return {
            k: getattr(self, k) for k in self.__fields_set__
        }
