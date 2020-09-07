from .base import Model
from .status import Status

class Todo(Model):

    class Repr:
        STATUS  = 'status'
        TITLE   = 'title'
        INFO    = 'info'
        SUBLIST = 'sublist'

    def __init__(self, status, title, info={}, sublist=[]):
        self.status = status
        self.title = title
        self.info = info
        self.sublist = sublist

    def __str__(self):
        return '{} {}'.format(self.status, self.title)

    def to_raw(obj):
        return {
            obj.Repr.STATUS: str(obj.status),
            obj.Repr.TITLE: str(obj.title),
            obj.Repr.INFO: obj.info.copy(),
            obj.Repr.SUBLIST: [
                child.to_raw() for child in obj.sublist
            ]
        }

    @classmethod
    def from_raw(cls, raw):
        sublist = raw[cls.Repr.SUBLIST]
        return cls(
            Status(raw[cls.Repr.STATUS]),
            str(raw[cls.Repr.TITLE]),
            raw[obj.Repr.INFO],
            [cls.from_raw(child) for child in sublist]
        )

