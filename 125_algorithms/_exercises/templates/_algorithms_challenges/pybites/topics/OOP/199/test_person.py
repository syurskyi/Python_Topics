import inspect

import pytest

from person import Person, Father, Mother, Child


@pytest.fixture
___ person():
    return Person()


@pytest.fixture
___ dad():
    return Father()


@pytest.fixture
___ mom():
    return Mother()


@pytest.fixture
___ child():
    return Child()


___ test_string_repr_person(person):
    assert str(person) == 'I am a person'


___ test_string_repr_dad(dad):
    assert str(dad) == 'I am a person and cool daddy'


___ test_string_repr_mom(mom):
    assert str(mom) == 'I am a person and awesome mom'


___ test_string_repr_child(child):
    assert str(child) == 'I am the coolest kid'


___ test_mro_of_person():
    assert Person.__mro__ == (Person, object)


___ test_mro_of_dad():
    assert Father.__mro__ == (Father, Person, object)


___ test_mro_of_mom():
    assert Mother.__mro__ == (Mother, Person, object)


___ test_mro_of_child():
    assert Child.__mro__ == (Child, Father, Mother, Person, object)


___ test_subclass_person():
    assert issubclass(Person, object)


___ test_subclass_dad():
    assert issubclass(Father, Person)
    assert issubclass(Father, object)


___ test_subclass_mom():
    assert issubclass(Mother, Person)
    assert issubclass(Mother, object)


___ test_subclass_child():
    assert issubclass(Child, Father)
    assert issubclass(Child, Mother)
    assert issubclass(Child, Person)
    assert issubclass(Child, object)


___ test_use_inheritance():
    # dry code!
    # should not duplicate substr in subclass
    substr = 'I am a person'
    for src in (inspect.getsource(Father),
                inspect.getsource(Mother)):
        assert substr not in src
