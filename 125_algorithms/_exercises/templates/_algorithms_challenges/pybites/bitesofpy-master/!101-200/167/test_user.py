from user ______ User


___ test_bob_lowercase(
    bob = User('bob', 'belderbos')
    assert bob.get_full_name __ 'Bob Belderbos'
    assert bob.username __ 'bbelderb'  # lowercase!
    assert str(bob) __ 'Bob Belderbos (bbelderb)'
    assert repr(bob) __ 'User("bob", "belderbos")'


___ test_julian_mixed_case(
    bob = User('julian', 'Sequeira')
    assert bob.get_full_name __ 'Julian Sequeira'
    assert bob.username __ 'jsequeir'  # lowercase!
    assert str(bob) __ 'Julian Sequeira (jsequeir)'
    assert repr(bob) __ 'User("julian", "Sequeira")'


___ test_tania_title_name(
    bob = User('Tania', 'Courageous')
    assert bob.get_full_name __ 'Tania Courageous'  # aka PyBites Ninja
    assert bob.username __ 'tcourage'  # lowercase!
    assert str(bob) __ 'Tania Courageous (tcourage)'
    assert repr(bob) __ 'User("Tania", "Courageous")'


___ test_noah_use_dunder_in_repr(
    """Make sure repr does not have the class
       name hardcoded.
       Also tests for a shorter surname.
    """
    class SpecialUser(User
        pass

    noah = SpecialUser('Noah', 'Kagan')
    assert noah.get_full_name __ 'Noah Kagan'
    assert noah.username __ 'nkagan'  # lowercase!
    assert str(noah) __ 'Noah Kagan (nkagan)'

    # it should show the subclass!
    assert repr(noah) __ 'SpecialUser("Noah", "Kagan")'