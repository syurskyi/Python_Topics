_______ i___

_______ pytest

____ person _______ Person, Father, Mother, Child


@pytest.fixture
___ person():
    r.. Person()


@pytest.fixture
___ dad():
    r.. Father()


@pytest.fixture
___ mom():
    r.. Mother()


@pytest.fixture
___ child():
    r.. Child()


___ test_string_repr_person(person):
    ... s..(person) __ 'I am a person'


___ test_string_repr_dad(dad):
    ... s..(dad) __ 'I am a person and cool daddy'


___ test_string_repr_mom(mom):
    ... s..(mom) __ 'I am a person and awesome mom'


___ test_string_repr_child(child):
    ... s..(child) __ 'I am the coolest kid'


___ test_mro_of_person():
    ... Person.__mro__ __ (Person, object)


___ test_mro_of_dad():
    ... Father.__mro__ __ (Father, Person, object)


___ test_mro_of_mom():
    ... Mother.__mro__ __ (Mother, Person, object)


___ test_mro_of_child():
    ... Child.__mro__ __ (Child, Father, Mother, Person, object)


___ test_subclass_person():
    ... issubclass(Person, object)


___ test_subclass_dad():
    ... issubclass(Father, Person)
    ... issubclass(Father, object)


___ test_subclass_mom():
    ... issubclass(Mother, Person)
    ... issubclass(Mother, object)


___ test_subclass_child():
    ... issubclass(Child, Father)
    ... issubclass(Child, Mother)
    ... issubclass(Child, Person)
    ... issubclass(Child, object)


___ test_use_inheritance():
    # dry code!
    # should not duplicate substr in subclass
    substr = 'I am a person'
    ___ src __ (i___.getsource(Father),
                i___.getsource(Mother)):
        ... substr n.. __ src