import json

from ..conversion import RAWConvertible, JSONConvertible

class ConvertibleModel(RAWConvertible, JSONConvertible):
    """
    mixin json conversion,
    uses raw conversion implementation by derived classes
    """

    def to_json(obj):
        return json.dumps(obj.to_raw())

    @classmethod
    def from_json(cls, string):
        return cls.from_raw(json.loads(string))

class Model(ConvertibleModel):
    pass

