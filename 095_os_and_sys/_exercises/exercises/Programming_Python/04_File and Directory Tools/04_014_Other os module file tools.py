# import __
# __.c.m.'spam.txt', 0o777) # enable all accesses
#
# __.r.n. _'C:\temp\spam.txt'  _'C:\temp\eggs.txt' # from, to
# __.r.m. _'C:\temp\spam.txt' # delete file?
# # WindowsError: [Error 2] The system cannot find the file specified: 'C:\\temp\\...'
# # ######################################################################################################################
#
# __.r.m. _'C:\temp\eggs.txt'
#
# o.... spam.txt _ .w... Hello stat world\n # +1 for \r added
# # 17
# # ######################################################################################################################
#
# ________ __
# info = __.st.. _'C:\temp\spam.txt')
# ?
# # nt.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0,
# # st_size=18, st_atime=1267645806, st_mtime=1267646072, st_ctime=1267645806)
# # ######################################################################################################################
#
# ?.st_mode, ?.st_size # via named-tuple item attr names
# # (33206, 18)
# # ######################################################################################################################
#
# ______ stat
# ? st__.S._M.. ? st__.S._S.. # via stat module presets
# # (33206, 18)
# # ######################################################################################################################
#
# ?.S_I.D. info.s._m. ?.S_I R.info.s._m.
# # (False, True)
# # ######################################################################################################################
#
# path = r'C:\temp\spam.txt'
# __.pa__.i.d. ? __.pa__.i.f. ? __.pa_.g.s. ?
# # (False, True, 18)
# # ######################################################################################################################