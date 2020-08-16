# ______ __
#
#
# c_ Path o..
#     '''Work with os.path as an object'''
#
#     ___  -  @parms @@
#         str_parms _ st. p ___ ? __ ?
#         __path _ __.pa__.j.. @?
#
#         __relative_to _ N..
#
#         # Collect relative_to off first path parm __ we can
#         ___
#             __r.. _ p.. 0 .__r..
#         _____ A..
#             __r.. _ N..
#
#         ___ k, v __ li.. k__.i..
#             __ ? __ 'relative_to'
#                 __ ? __ no. N..
#                     __r.. _ P.. ?
#             ____
#                 r_ E.. "Unknown keyword argument: s"  ?
#
#
#     ___ __str__
#         r_ __path
#
#     ??
#     ___ s
#         '''Alias to __str__()'''
#         r_ st.
#
#     ___ __repr__
#         r_ "Path('@')"  __p..
#
#
#     ??
#     ___ effective_path_str
#         '''Path being pased to os.path'''
#         __ __r.. __ N..
#             r_ ?
#         ____
#             r_ __.pa__.j.. st. __r.. ?
#
#
#     ??
#     ___ _compare_str
#         '''String for comparison.  See .__eq__()'''
#         __ __r.. __ N..
#             pa__ _ st.
#         ____
#             pa__ _ __.pa__.j.. st. __r.. st.
#
#         # Normalize path seperators
#         path _ P__.n.. ?
#
#         r_ ?
#
#
#     ?s..
#     ___ normalize_path_sep path
#         r_ pa__.re.. '/' __.pa__.s.. .re.. '\\' __.pa__.s..
#
#
#     ___ -e  other
#         '''
#         Paths are equal __ their string values are equal adjusted for os.sep
#
#         So:
#           - a/b/c == a\b\c
#           - /a/b/c != a/b/c (even __ both paths point to the same place)
#
#         If a path has a .rel_root value, that will be combined with the
#         string value before comparing.  So:
#
#           - 'c' relative to '/a/b' == '/a/b/c' relative to None
#
#         :param other: Another path or string
#         :return:
#         '''
#         ___
#              r_ ?._c.. __ _c..
#         _____ A..
#             a _ P__.n.. st. ?
#             r_ a __ _c..
#
#
#     ___ -h
#         r_ ? __p..
#
#
#     ___ -n  other
#         r_ no. -e ?
#
#
#     ??
#     ___ rel_root
#         '''The path that this path is relative to (__ relative)'''
#         __ i..
#             __ __r.. __ no. N..
#                 r_ __r..
#             ____
#                 r_ __.pa__.a.. __.c..
#         r_ N..
#
#
#     ??
#     ___ is_relative
#         __ le. __? > 0
#             __ __? 0 __ '/' '\\'
#                 r_ F..
#             ____ __? 1|3 __ ':\\' ':/'
#                 r_ F..
#             r_ T..
#         r_ N..
#
#
#     ??
#     ___ is_absolute
#         r_ no. i_r..
#
#
#     ___ make_relative_to root
#         '''Create a new path object which is same path relative to this'''
#         root _ st. ?
#
#         path _ st.
#         __ __r_t __ no. N..
#             path _ __.pa__.j.. st. __r.. ?
#
#         __ no. pa__.s_w.. ?
#             r_ V..  "@ cannot be represented relative to @"
#                 ? ?
#         rel_path _ ? le. ? + 1: # +1 to get dir sep.  Ever want otherwise?
#         r_ P.. ? r_t_r..
#
#
#     ??
#     ___ exists
#         r_ __.pa__.exists(effective_path_str)
#
#     ??
#     ___ is_file
#         r_ __.pa__.isfile(effective_path_str)
#
#     ??
#     ___ is_dir
#         r_ __.pa__.isdir(effective_path_str)
#
#     ??
#     ___ is_link
#         r_ __.pa__.islink(effective_path_str)
#
#
#     ??
#     ___ abs
#         __ is_relative:
#             __ __relative_to __ no. N..:
#                 r_ Path(__relative_to, __path)
#             ____
#                 r_ Path(__.pa__.abspath(__path))
#         ____
#             r_ Path(__.pa__.abspath(__path))
#
#     ??
#     ___ basename
#         r_ __.pa__.basename(__path)
#
#     ??
#     ___ parent
#         r_ Path(__.pa__.dirname(__path))
#
#
#     ??
#     ___ splitext
#         prefix, ext _ __.pa__.splitext(__path)
#         __ ext __ no. N.. and ext[0] __ '.':
#             ext _ ext[1:]
#         r_ prefix, ext
#
#     ??
#     ___ prefix
#         r_ splitext[0]
#
#     ??
#     ___ ext
#         r_ splitext[1]
#
#     ___ split
#         r_ st.(norm).split(__.sep)
#
#     ___ has_ext(, *exts):
#         r_ ext.lower() __ set([e.lower() ___ e __ exts])
#
#     ??
#     ___ norm
#         r_ Path(__.pa__.normpath(__path))
#
#
#     ___ j..(, *paths):
#         paths _ [__path, ] + [st.(p) ___ p __ paths]
#         r_ Path(__.pa__.j..(*paths), relative_to_self.__relative_to)
#
#
#     ??
#     ___ all
#         ___ p __ dirs:
#             y.. p
#         ___ p __ files:
#             y.. p
#
#
#     ___ list_dir
#         r_ __.listdir(effective_path_str)
#
#     ___ samefile(, other):
#         ___
#             r_ __.pa__.samefile(effective_path_str, st.(other))
#         _____ AttributeError:
#             r_ AttributeError("os.path.samefile() only available for Unix")
#         _____ FileNotFoundError:
#             # Keeping this behaviour since I think this is how Python 2 worked.
#             # May let this exception bubble up in the future __ file doesn't exist
#             r_ F..
#
#     ??
#     ___ dirs
#         ___ name __ list_dir():
#             child _ j..(name)
#             __ child.is_dir:
#                 y.. child
#
#
#     ___ startswith(, pa__):
#         path_parts _ Path(pa__).split()
#         my_parts _ split()
#         r_ my_parts[:le.(path_parts)] __ path_parts
#
#
#     ??
#     ___ files
#         ___ name __ list_dir
#             child _ j..(name)
#             __ child.is_file:
#                 y.. child
#
#
#     ___ find
#         r_ walk()
#
#
#     ___ walk
#         '''
#         Return all sub directories and files recursivly
#
#         Returned paths are RelativePath
#         '''
#         ___ dirpath, dirnames, filenames __ __.walk(st.(abs)):
#             ___ name __ dirnames:
#                 y.. Path(dirpath, name).make_relative_to(abs)
#             ___ name __ filenames:
#                 y.. Path(dirpath, name).make_relative_to(abs)
#
#
#
#
