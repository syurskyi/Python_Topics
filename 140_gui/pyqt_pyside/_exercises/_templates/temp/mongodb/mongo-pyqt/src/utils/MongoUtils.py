# ______ __ ____
# c_ MongoUtils o..
#     '''
#     classdocs
#     '''
#
#
#     ___  -
#         '''
#         Constructor
#         '''
#     ___ preview col queryjson page limit sort
#         skipNum _ p.. - 1 * l..
#         __ le. qj__.i.. > 0
#             query _ ____.d.. qj__
#         ____
#             query _ ""
#
#         __ sort __ N..
#             r_ "db."+c..+".find("+q..+").limit("+st. l.. +").skip("+st. sN.. +")"
#         ____
#             sortStr _ ____.d.. so..
#             r_ "db."+c..+".find("+q..+").sort("+soS..+").limit("+st. l.. +").skip("+st. sN..+")"
#
#
#
#     ___ parse mongostmt
#         pattern _ __.c.. _*db\.([\.a-zA-Z0-9]+)\.find\(({.*})\)')
#         match _ ?.m.. m__.r.. "'", "\""
#         __ ?
#             jsonstr _ m__.g.. 2
#             r_ m__.g.. 1 ____.l.. ?
#         r_ N..
#
# __ _______ __ ________
#     ?
#
#