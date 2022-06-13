# _______ c__
# _______ __
# ____ u__.r.. _______ u..
# ____ c.. _______ d..
#
# BATTLE_DATA __.p...j..('/tmp', 'battle-table.csv')
# __ n.. __.p...i.. ?
#     u..('https://bit.ly/2U3oHft' ?
#
#
# ___ _create_defeat_mapping
#     """Parse battle-table.csv building up a defeat_mapping dict
#        with keys = attackers / values = who they defeat.
#     """
#     result d.. d..
#     w__ o.. ? __ b
#         reader c__.D.. b
#         ___ row __ ?
#             ? ? Attacker ?
#     r.. ?
#
#
# ___ get_winner player1 player2 defeat_mapping_ N..
#     """Given player1 and player2 determine game output returning the
#        appropriate string:
#        Tie
#        Player1
#        Player2
#        (where Player1 and Player2 are the names passed in)
#
#        Raise a ValueError if invalid player strings are passed in.
#     """
#     ? ? o. _?
#     __ ?1 n.. __ ? o. ?2 n.. __ ?
#         r.. V...
#     r.. win : ?1
#             lose : ?2
#             draw : Tie ? ?1 ?2
