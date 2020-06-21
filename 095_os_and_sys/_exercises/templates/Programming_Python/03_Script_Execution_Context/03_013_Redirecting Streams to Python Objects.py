# #C:\...\PP4E\System\Streams> python
# f____ teststreams _____ interact
# ##### interact()    # for testing need activate this line and deactivate other
# # Hello stream world
# #Enter a number>2
# # 2 squared is 4
# # Enter a number>3
# # 3 squared is 9
# # Enter a number^Z
# # Bye
#
# f____ redirect _____ redirect
# (result, output) = redirect(interact, (), {}, '4\n5\n6\n')
# print(result)
# # None
# # ######################################################################################################################
#
# print(output)
# # 'Hello stream world\nEnter a number>4 squared is 16\nEnter a number>5 squared
# # is 25\nEnter a number>6 squared is 36\nEnter a number>Bye\n'
#
# # for line in output.splitlines(): print(line)
#
# # Hello stream world
# # Enter a number>4 squared is 16
# # Enter a number>5 squared is 25
# # Enter a number>6 squared is 36
# # Enter a number>Bye
#
# # from PP4E.System.more import more
# # more(output)
# # Hello stream world
# # Enter a number>4 squared is 16
# # Enter a number>5 squared is 25
# # ######################################################################################################################