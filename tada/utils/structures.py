from inspect import getmro
from typing import Type, List

import pydantic

def restrict_field_types(
    cls: Type[pydantic.BaseModel],
    types: List[object]
) -> None:
    for k, v in cls.__fields__.items():
        # not a good way of runtime polymorphism check at all
        if not any(t in getmro(v.type_) for t in types):
            raise TypeError(
                f"'{k}' field is not of Section type "
                "or subclass, but is '{str(v)}'"
            )

class BaseModel(pydantic.BaseModel):
    pass
