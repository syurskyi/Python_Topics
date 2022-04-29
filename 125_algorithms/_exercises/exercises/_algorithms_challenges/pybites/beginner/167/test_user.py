# ____ ? _______ ?
#
#
# ___ test_bob_lowercase
#     bob  ? 'bob', 'belderbos'
#     ... ?.g.. __ 'Bob Belderbos'
#     ... ?.u.. __ 'bbelderb'  # lowercase!
#     ... s.. ? __ 'Bob Belderbos (bbelderb)'
#     ... r..  ? __ 'User("bob", "belderbos")'
#
#
# ___ test_julian_mixed_case
#     bob  ? 'julian', 'Sequeira'
#     ... ?.g.. __ 'Julian Sequeira'
#     ... ?.u.. __ 'jsequeir'  # lowercase!
#     ... s.. ? __ 'Julian Sequeira (jsequeir)'
#     ... r.. ? __ 'User("julian", "Sequeira")'
#
#
# ___ test_tania_title_name
#     bob  ? 'Tania', 'Courageous'
#     ... ?.g.. __ 'Tania Courageous'  # aka PyBites Ninja
#     ... ?.u.. __ 'tcourage'  # lowercase!
#     ... s.. ? __ 'Tania Courageous (tcourage)'
#     ... r.. ? __ 'User("Tania", "Courageous")'
#
#
# ___ test_noah_use_dunder_in_repr
#     """Make sure repr does not have the class
#        name hardcoded.
#        Also tests for a shorter surname.
#     """
#     c_ SpecialUser U..
#         p..
#
#     noah  SpecialUser('Noah', 'Kagan')
#     ... ?.g.. __ 'Noah Kagan'
#     ... ?.u.. __ 'nkagan'  # lowercase!
#     ... s.. ? __ 'Noah Kagan (nkagan)'
#
#     # it should show the subclass!
#     ... r.. ? __ 'SpecialUser("Noah", "Kagan")'