# ___ generate                  # Fails prior to Python 2.2, works later
#     c_ Spam:
#         count = 1
#         ___ method ____        # Name Spam not visible:
#             print S_.c..    # not local (def), global (module), built-in
#     r_ Sp..
#
# g___.m..
#
# # C:\python\examples> python nester.py
# # ...error text omitted...
# #     Print(Spam.count)            # Not local (def), global (module), built-in
# # NameError: Spam
#
#
#
# ___ generate
#     gl... S..                 # Force Spam to module scope
#     c_ Sp..
#         count = 1
#         ___ method ____
#             print ?.c..   # Works: in global (enclosing module)
#     r_ S...
#
# ge__.me..             # Prints 1
#
#
#
# ___ generate
#     r_ S..
#
# c_ Spam                    # Define at top level of module
#     count = 1
#     ___ method ____
#         print S__.c..      # Works: in global (enclosing module)
#
# g__.m..
#
#
#
# ___ generate
#     c_ Spam
#         count = 1
#         ___ method ____
#             print(____. -c.c..      # Works: qualify to get class
#     r_ S...
#
# g__.m..
