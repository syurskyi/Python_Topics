# _______ c__
# _______ __
# ____ u__.r.. _______ u..
# ____ c.. _______ d..
#
# TMP __.g.. TMP  /tmp
# DATA 'battle-table.csv'
# BATTLE_DATA __.p...j.. ? ?
# __ n.. __.p...i.. ?
#     u..
#         _*https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
#         ?
#
#
#
# ___ _create_defeat_mapping
#     """Parse battle-table.csv building up a defeat_mapping dict
#        with keys = attackers / values = who they defeat.
#     """
#     defeat_map d.. l..
#     w__ o.. ? __ f
#         rows l.. c__.D.. ?
#
#     ___ row __ ?
#         ? ? Attacker k ___ ? v __ ?.i.. __ ? __ win
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
#
#     __ ?1 n.. __ ? o. ?2 n.. __ ?
#         r.. V...('Invalid player string')
#
#     __ ?1 __ ?2
#         r.. Tie
#     ____
#         __ ?1 __ ? ?2
#             r.. ?2
#         ____
#             r.. ?1
