# ____ l.. ______ L..
# ____ some_module ______ Some
# ______ ?
#
#
# c_ App
#     ___  -
#         logger _ ?.gL.. 'app_name'
#
#     ___ do_something
#         ?.d.. 'Cut off by logger.setLevel'
#         ?.w.. 'Log only to file'
#         ?.e.. 'log to both file and console'
#
#
# # Customize how the logger behaves
# log _ L..
# ?.s..
#
# my_app _ A..
# ?.d..
#
# my_some _ S..
# ?.d..
#
# # Log to Console
# # 2018-03-08 21:29:42,846 - app.py - E. - log to both file and console
# # 2018-03-08 21:29:42,846 - some_module.py - CRITICAL - Something c.. happend
#
# # Log to my_app.log
# # 2018-03-08 21:29:42,846 - app.py - WARNING - Log only to file
# # 2018-03-08 21:29:42,846 - app.py - E. - log to both file and console
# # 2018-03-08 21:29:42,846 - some_module.py - CRITICAL - Something c.. happend
