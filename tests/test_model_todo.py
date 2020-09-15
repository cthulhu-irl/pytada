from tada.models.todo import Todo
from tada.models.status import Status

raw = {
    Todo.Repr.STATUS: 'x',
    Todo.Repr.TITLE: 'example',
    Todo.Repr.INFO: {
        'info': 'this is a test',
        'note': 'it contains two children nodes'
    },
    Todo.Repr.SUBLIST: [
        {
            Todo.Repr.STATUS: '+',
            Todo.Repr.TITLE: 'example 1',
            Todo.Repr.INFO: {
                'info': 'this is part of a test'
            },
            Todo.Repr.SUBLIST: []
        },
        {
            Todo.Repr.STATUS: '-',
            Todo.Repr.TITLE: 'example 2',
            Todo.Repr.INFO: {},
            Todo.Repr.SUBLIST: []
        }
    ]
}


todo = Todo(
    Status('x'),
    'example',
    {
        'info': 'this is a test',
        'note': 'it contains two children nodes'
    },
    [
        Todo(
            Status('+'),
            'example 1',
            {'info': 'this is part of a test'}
        ),
        Todo(Status('-'), 'example 2')
    ]
)

def test_to_raw():
    assert raw == todo.to_raw()

def test_from_raw():
    assert Todo.from_raw(raw) == todo

def test_fix_status():
    todo = Todo.from_raw(raw)
    todo.sublist[1].status = Status('+')

    assert todo.fix_status().status == Status('+')
