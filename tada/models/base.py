import json
from typing import Any, Dict

from pydantic import BaseModel

from ..conversion import RAWConvertable, JSONConvertable

class ConvertableModel(BaseModel, RAWConvertable, JSONConvertable):
    """
    mixin json conversion,
    uses raw conversion implementation by derived classes
    """

    def to_raw(obj: BaseModel) -> Any:
        return obj.dict()

    @classmethod
    def from_raw(cls, raw: Any) -> 'ConvertableModel':
        return cls(**raw)

    def to_json(obj: RAWConvertable) -> str:
        return json.dumps(obj.to_raw())

    @classmethod
    def from_json(cls, string: str) -> 'ConvertableModel':
        return cls.from_raw(json.loads(string))


class Model(ConvertableModel):
    pass
