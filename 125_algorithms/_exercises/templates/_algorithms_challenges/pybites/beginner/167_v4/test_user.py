____ user _______ User


___ test_bob_lowercase
    bob = ? 'bob', 'belderbos')
    ... bob.get_full_name __ 'Bob Belderbos'
    ... bob.username __ 'bbelderb'  # lowercase!
    ... s..(bob) __ 'Bob Belderbos (bbelderb)'
    ... r.. (bob) __ 'User("bob", "belderbos")'


___ test_julian_mixed_case
    bob = ? 'julian', 'Sequeira')
    ... bob.get_full_name __ 'Julian Sequeira'
    ... bob.username __ 'jsequeir'  # lowercase!
    ... s..(bob) __ 'Julian Sequeira (jsequeir)'
    ... r.. (bob) __ 'User("julian", "Sequeira")'


___ test_tania_title_name
    bob = ? 'Tania', 'Courageous')
    ... bob.get_full_name __ 'Tania Courageous'  # aka PyBites Ninja
    ... bob.username __ 'tcourage'  # lowercase!
    ... s..(bob) __ 'Tania Courageous (tcourage)'
    ... r.. (bob) __ 'User("Tania", "Courageous")'


___ test_noah_use_dunder_in_repr
    """Make sure repr does not have the class
       name hardcoded.
       Also tests for a shorter surname.
    """
    c_ SpecialUser(User
        p..

    noah = SpecialUser('Noah', 'Kagan')
    ... noah.get_full_name __ 'Noah Kagan'
    ... noah.username __ 'nkagan'  # lowercase!
    ... s..(noah) __ 'Noah Kagan (nkagan)'

    # it should show the subclass!
    ... r.. (noah) __ 'SpecialUser("Noah", "Kagan")'