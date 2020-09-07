from .base import Model

class Todo(Model):

    def __init__(self, status, title, info={}, sublist=[]):
        self.status = status
        self.title = title
        self.info = info
        self.sublist = sublist

    def __str__(self):
        pass

    def to_raw(obj):
        pass

    @classmethod
    def from_raw(cls, raw):
        pass

