# ______ ___
# ___ stream i_ ___.s.i., ___.s.o. ___.s.e.
#     print ?.f.n.
# # 012
# # ######################################################################################################################
# 
# ___.s.o..w..('Hello stdio world\n' # write via file method
# # Hello stdio world
# # 18
# # ######################################################################################################################
# 
# _______ __
# __.w.. 1 _'Hello descriptor world\n' # write via os module
# # Hello descriptor world
# # 23
# # ######################################################################################################################
# 
# file = o... _'C:\temp\spam.txt' _ # create external file, object
# ?.w..('Hello stdio file\n') # write via file object method
# ?.fl.. # else __.write to disk first!
# fd _ ?.f.n. # get descriptor from object
# ?
# # 3
# # ######################################################################################################################
# 
# _______ __
# __.w.. ? _'Hello descriptor file\n # write via os module
# ?.cl..
# # C:\temp> type spam.txt # lines from both schemes
# # Hello stdio file
# # Hello descriptor file
# # ######################################################################################################################
# 
