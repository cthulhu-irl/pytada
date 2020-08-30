from ..conversion import RAWConvertible, JSONConvertible

class ConvertibleModel(RAWConvertible, JSONConvertible):
    """
    mixin json conversion,
    uses raw conversion implementation by derived classes
    """

    def to_json(obj):
        pass

    @classmethod
    def from_json(cls, string):
        pass

class Model(ConvertibleModel):
    pass

