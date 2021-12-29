____ user _______ User


___ test_bob_lowercase():
    bob = User('bob', 'belderbos')
    ... bob.get_full_name __ 'Bob Belderbos'
    ... bob.username __ 'bbelderb'  # lowercase!
    ... str(bob) __ 'Bob Belderbos (bbelderb)'
    ... repr(bob) __ 'User("bob", "belderbos")'


___ test_julian_mixed_case():
    bob = User('julian', 'Sequeira')
    ... bob.get_full_name __ 'Julian Sequeira'
    ... bob.username __ 'jsequeir'  # lowercase!
    ... str(bob) __ 'Julian Sequeira (jsequeir)'
    ... repr(bob) __ 'User("julian", "Sequeira")'


___ test_tania_title_name():
    bob = User('Tania', 'Courageous')
    ... bob.get_full_name __ 'Tania Courageous'  # aka PyBites Ninja
    ... bob.username __ 'tcourage'  # lowercase!
    ... str(bob) __ 'Tania Courageous (tcourage)'
    ... repr(bob) __ 'User("Tania", "Courageous")'


___ test_noah_use_dunder_in_repr():
    """Make sure repr does not have the class
       name hardcoded.
       Also tests for a shorter surname.
    """
    class SpecialUser(User):
        pass

    noah = SpecialUser('Noah', 'Kagan')
    ... noah.get_full_name __ 'Noah Kagan'
    ... noah.username __ 'nkagan'  # lowercase!
    ... str(noah) __ 'Noah Kagan (nkagan)'

    # it should show the subclass!
    ... repr(noah) __ 'SpecialUser("Noah", "Kagan")'