# _______ __
# ____ p.. _______ P..
# ____ tempfile _______ T..
#
# _______ p__
#
# ____ ? _______ ?
#
# TMP P.. __.g.. "TMP", "/tmp"
#
#
# ?p__.m__.p. "byte_sizes, size_in_kb, expected", [
#     ([800, 1000, 1200], 1,  '1200' ),
#     ([1024, 1025], 1,  '1024', '1025' ),
#     ([1024, 1025], 1.026, []),
#     ([1000, 1300, 1777, 900], 1.25,  '1300', '1777' ),
#     ([1024, 2047, 2048, 2500], 2,  '2048', '2500' ),
#
# ___ test_get_files byte_sizes size_in_kb e..
#     w__ T.. dir_? __ dirname
#         ___ size __ ?
#             w__ o.. __.p...j.. ? s.. ? __ __ f
#                 ?.w.. __.u.. ?
#
#         a.. __.p...b.. fi ___ ? __
#                   get_files d.. s..
#         ... s.. a.. __ s.. e..