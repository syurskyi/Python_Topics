# # coding: utf-8
#
# c_ Document o..
#     ___ show
#         r_ N...
#
#
# c_ ODFDocument D..
#     ___ show
#         print('Open document format')
#
#
# c_ MSOfficeDocument D..
#     ___ show
#         print('MS Office document format')
#
#
# c_ Application o..
#     ___ create_document type_
#         # параметризованный фабричный метод `create_document`
#         r_ N...
#
#
# c_ MyApplication A..
#     ___ create_document type_
#         __ ? __ 'odf'
#             r_ O..
#         ____ ? __ 'doc'
#             r_ M..
#
#
# app = M..
# ?.c_d.. odf .s..  # Open document format
# ?.c_d.. doc .s..  # MS Office document format