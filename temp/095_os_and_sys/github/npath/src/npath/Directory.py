# ____ .P.. ______ P..
#
# ____ .F.. ______ F..
#
# c_ Directory F..
#
#
#     ??
#     ___ is_file
#         r_ F..
#
#
#     ??
#     ___ is_dir
#         r_ T..
#
#
#     ??
#     ___ parent
#         r_ F.. ?
#
#
#     ??
#     ___ files
#         ___ path __ ?
#             y.. F.. ?
#
#
#     ??
#     ___ dirs
#         ___ path __ ?
#             y.. F.. ?
#
#
#     ??
#     ___ all
#         ___ o __ f..
#             y.. o
#         ___ o __ d..
#             y.. o
#
#
#     ___ walk
#         '''
#         Return all file objects under a given path recursively
#
#         All paths are made relative to this directory.
#
#         :return: FileObject (File, Directory, UnknownFileObject)
#         '''
#         ___ path __ s___ D..  . ?
#             y.. F.. ?.m..
#
#
#     ___ find f.._N.. d.._N..
#         ___ child __ w..
#             __ ?.i_f..
#                 __ f.. __ N.. o. f.. __ T..
#                     y.. ?
#             ____ ?.i_d..
#                 __ d.. __ N.. o. d.. __ T..
#                     y.. ?
