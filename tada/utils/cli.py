from typing import Any, List, Dict

from pydantic import BaseModel, Field, root_validator

from .config import FieldSchema, SectionSchema, Section
from .structures import restrict_field_types

class Option(FieldSchema):
    short_opt: str = ''
    long_opt: str = ''

    @root_validator(pre=True)
    def set_opts_from_name(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        splitted = values.get('name', '').split('|')

        if 0 >= len(splitted) > 2 or not splitted[0]:
            raise ValueError(
                '`name` field does not contain '
                'valid option string'
            )

        if not values.get('short_opt', ''):
            values['short_opt'] = splitted[0]

        if not values.get('long_opt', '') and len(splitted) >= 2:
            values['long_opt'] = splitted[1]

        return values

class Command(Section):
    name: str

    @classmethod
    def section_schema(cls) -> SectionSchema:
        instance = SectionSchema(Option)
        return SectionSchema.from_fields(instance, cls.__fields__)

class CLI(BaseModel):

    def __init_subclass__(cls) -> None:
        restrict_field_types(cls, [Command])
