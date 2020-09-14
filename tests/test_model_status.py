import pytest

from tada.models.status import Status

def test_string_conversion():
    assert Status(Status.STRINGS[0]).index == 0
    assert Status(Status.STRINGS[1]).index == 1
    assert Status(Status.STRINGS[2]).index == 2

def test_int_conversion():
    assert str(Status(Status.TODO)) == Status.STRINGS[0]
    assert str(Status(Status.DOING)) == Status.STRINGS[1]
    assert str(Status(Status.DONE)) == Status.STRINGS[2]

    with pytest.raises(ValueError) as excinfo:
        Status(-1)
    assert 'Status representative' in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        Status(3)
    assert 'Status representative' in str(excinfo.value)

def test_comparison():
    assert Status(0) < Status(1)
    assert Status(0) <= Status(1)
    assert Status(0) != Status(1)
    assert Status(2) == Status(2)
    assert Status(2) > Status(0)
    assert Status(2) >= Status(2)

def test_self_conversion():
    assert Status(Status(Status.TODO)) == Status(Status.TODO)
