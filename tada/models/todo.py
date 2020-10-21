from typing import Any, Optional, Dict, List

from pydantic import Field

from .base import Model
from .status import Status

class Todo(Model):

    status: Status
    title: str
    info: Dict[str, str] = Field(default_factory=dict)
    sublist: List['Todo'] = Field(default_factory=list)

    class Repr:
        STATUS = 'status'
        TITLE = 'title'
        INFO = 'info'
        SUBLIST = 'sublist'

    def __init__(
        self,
        status: Status,
        title: str,
        info: Optional[Dict[str, str]] = None,
        sublist: Optional[List['Todo']] = None
    ) -> None:
        Todo.update_forward_refs()
        super(Todo, self).__init__(
            status=status,
            title=title,
            info=info or {},
            sublist=sublist or []
        )

    def __str__(self) -> str:
        return '{} {} - {} info,  {} sublist'.format(
            self.status, self.title,
            len(self.info.keys()), len(self.sublist)
        )

    def __ne__(self, other: 'Todo') -> bool:
        return not (self == other)

    def __eq__(self, other: 'Todo') -> bool:
        ret = self.status == other.status
        ret = ret and self.title == other.title
        ret = ret and self.info == other.info

        if ret and (self.sublist or other.sublist):
            ret = self.sublist == other.sublist

        return ret

    def fix_status(todo: 'Todo') -> 'Todo':
        """
        fixes the status of the given todo and its sublist todos
        according to these rules:
        - a todo's status is determined by its sublist todo,
          unless its sublist is empty,
          then its status is as given.

        - a todo's status is the same as any of its sublist
          if all of its sublist have the same status

        - a todo's status is 'doing' if any of its sublist
          have a different status of another
        """

        if not todo.sublist:
            return todo

        # to avoid mutation
        todo = todo.copy(deep=True)

        todo.sublist = [
            child.fix_status() for child in todo.sublist
        ]

        for i in range(len(todo.sublist)-1):
            if todo.sublist[i].status != todo.sublist[i+1].status:
                todo.status = Status(Status.DOING)

        todo.status = todo.sublist[0].status

        return todo

    def to_raw(obj: 'Todo') -> Dict[str, Any]:
        return {
            obj.Repr.STATUS: str(obj.status),
            obj.Repr.TITLE: str(obj.title),
            obj.Repr.INFO: obj.info.copy(),
            obj.Repr.SUBLIST: [
                child.to_raw() for child in obj.sublist
            ]
        }

    @classmethod
    def from_raw(cls, raw: Any) -> 'Todo':
        sublist = raw[cls.Repr.SUBLIST]
        return cls(
            Status(raw[cls.Repr.STATUS]),
            str(raw[cls.Repr.TITLE]),
            raw[cls.Repr.INFO],
            [cls.from_raw(child) for child in sublist]
        )
