# # C:\temp> python
# file = o.. data.txt  # open input file object: 'r' default
# lines = ?.r.l.  # read into line string list
# ___ line i_ ?  # BUT use file line iterator! (ahead)
#     print ? e.._''  # lines have a '\n' at end
#
# # Hello file world!
# # Bye file world.
#
# ?.se.. 0  # go back to the front of file
# ?.r..  # read entire file into string
# # 'Hello file world!\nBye file world.\n'
# # ######################################################################################################################
#
# ?.se.. 0  # read entire file into lines list
# ?.r.l.
# # ['Hello file world!\n', 'Bye file world.\n']
# # ######################################################################################################################
#
# ?.se.. 0
# ?.r.l.  # read one line at a time
# # 'Hello file world!\n'
# # ######################################################################################################################
#
# ?.r.l.
# # 'Bye file world.\n'
# # ######################################################################################################################
#
# ?.r.l.  # empty string at end-of-file
# # ''
# # ######################################################################################################################
#
# ?.se..(0)  # read N (or remaining) chars/bytes
# ?.r. 1 ?.r. 8  # empty string at end-of-file
# # ('H', 'ello fil')
# # ######################################################################################################################