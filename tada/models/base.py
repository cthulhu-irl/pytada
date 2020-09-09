import json

from ..conversion import RAWConvertable, JSONConvertable

class ConvertableModel(RAWConvertable, JSONConvertable):
    """
    mixin json conversion,
    uses raw conversion implementation by derived classes
    """

    def to_json(obj):
        return json.dumps(obj.to_raw())

    @classmethod
    def from_json(cls, string):
        return cls.from_raw(json.loads(string))

class Model(ConvertableModel):
    pass

