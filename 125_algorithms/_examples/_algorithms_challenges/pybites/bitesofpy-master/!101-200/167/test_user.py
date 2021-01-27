from user import User


def test_bob_lowercase():
    bob = User('bob', 'belderbos')
    a__ bob.get_full_name == 'Bob Belderbos'
    a__ bob.username == 'bbelderb'  # lowercase!
    a__ str(bob) == 'Bob Belderbos (bbelderb)'
    a__ repr(bob) == 'User("bob", "belderbos")'


def test_julian_mixed_case():
    bob = User('julian', 'Sequeira')
    a__ bob.get_full_name == 'Julian Sequeira'
    a__ bob.username == 'jsequeir'  # lowercase!
    a__ str(bob) == 'Julian Sequeira (jsequeir)'
    a__ repr(bob) == 'User("julian", "Sequeira")'


def test_tania_title_name():
    bob = User('Tania', 'Courageous')
    a__ bob.get_full_name == 'Tania Courageous'  # aka PyBites Ninja
    a__ bob.username == 'tcourage'  # lowercase!
    a__ str(bob) == 'Tania Courageous (tcourage)'
    a__ repr(bob) == 'User("Tania", "Courageous")'


def test_noah_use_dunder_in_repr():
    """Make sure repr does not have the class
       name hardcoded.
       Also tests for a shorter surname.
    """
    class SpecialUser(User):
        pass

    noah = SpecialUser('Noah', 'Kagan')
    a__ noah.get_full_name == 'Noah Kagan'
    a__ noah.username == 'nkagan'  # lowercase!
    a__ str(noah) == 'Noah Kagan (nkagan)'

    # it should show the subclass!
    a__ repr(noah) == 'SpecialUser("Noah", "Kagan")'