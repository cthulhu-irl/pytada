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
        return '{} {} - {} info,  {} sublist'.format(
            self.status, self.title,
            len(self.info.keys()), len(self.sublist)
        )

    def fix_status(todo):
        if not todo.sublist:
            return todo

        todo.sublist = [
            fix_status(child) for child in todo.sublist
        ]

        for i in range(len(todo.sublist)-1):
            if todo.sublist[i].status != todo.sublist[i+1].status:
                todo.status = Status(Status.DOING)

        todo.status = todo.sublist[0].status

        return todo

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

