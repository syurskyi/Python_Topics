# _______ p__
#
# ____ ? _______ c.. S.. U..
#
#
# ___ _count_suits deck suit
#     r.. l.. card ___ ? __ deck __ ?.s.. __ ?
#
#
# ___ _count_suitcard deck suit name
#     r.. s.. 1 ___ c.. __ d.. __ ?.s. __ s..
#                a.. s.. c__.n.. __ ?
#
#
# ?p__.f.. scope="module"
# ___ deck
#     r.. ?
#
#
# ___ test_create_uno_deck_len deck
#     ... l.. ? __ 108
#
#
# ___ test_create_uno_deck_type deck
#     ... t.. ? __ l..
#     ... a.. t.. c.. __ U.. ___ c.. __ ?
#
#
# ?p__.m__.p. "suit, count", [
#     ('Red', 25),
#     ('Green', 25),
#     ('Yellow', 25),
#     ('Blue', 25),
#     (N.., 8),  # wild cards don't have an associated suit
#
# ___ test_create_uno_deck_suit_distribution deck suit count
#     ... _? ? ? __ ?
#
#
# ?p__.m__.p. "name, count", [
#     ('0', 1), ('1', 2), ('2', 2), ('3', 2), ('4', 2),
#     ('5', 2), ('6', 2), ('7', 2), ('8', 2), ('9', 2),
#     ('Draw Two', 2), ('Skip', 2), ('Reverse', 2),
#
# ___ test_create_uno_deck_suit_cards deck name count
#     ___ suit __ S..
#         _? ? ? ?  __ ?