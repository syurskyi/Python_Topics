import inspect

import pytest

from person import Person, Father, Mother, Child


@pytest.fixture
def person():
    return Person()


@pytest.fixture
def dad():
    return Father()


@pytest.fixture
def mom():
    return Mother()


@pytest.fixture
def child():
    return Child()


def test_string_repr_person(person):
    a__ str(person) == 'I am a person'


def test_string_repr_dad(dad):
    a__ str(dad) == 'I am a person and cool daddy'


def test_string_repr_mom(mom):
    a__ str(mom) == 'I am a person and awesome mom'


def test_string_repr_child(child):
    a__ str(child) == 'I am the coolest kid'


def test_mro_of_person():
    a__ Person.__mro__ == (Person, object)


def test_mro_of_dad():
    a__ Father.__mro__ == (Father, Person, object)


def test_mro_of_mom():
    a__ Mother.__mro__ == (Mother, Person, object)


def test_mro_of_child():
    a__ Child.__mro__ == (Child, Father, Mother, Person, object)


def test_subclass_person():
    a__ issubclass(Person, object)


def test_subclass_dad():
    a__ issubclass(Father, Person)
    a__ issubclass(Father, object)


def test_subclass_mom():
    a__ issubclass(Mother, Person)
    a__ issubclass(Mother, object)


def test_subclass_child():
    a__ issubclass(Child, Father)
    a__ issubclass(Child, Mother)
    a__ issubclass(Child, Person)
    a__ issubclass(Child, object)


def test_use_inheritance():
    # dry code!
    # should not duplicate substr in subclass
    substr = 'I am a person'
    for src in (inspect.getsource(Father),
                inspect.getsource(Mother)):
        a__ substr not in src