# c_ Wrapper:
#     ___ - ____, object
#         ____.wrapped _ o..                  # Save object
#
#     ___ -g ____ attrname
#         print('Trace:', a..                # Trace fetch
#         r_ getattr ____.w.. a...   # Delegate fetch
#
# # NOTE: in the following, use list(x.keys()) for Python 3.X
# # (list() was not used in the first printing of the book
#
# # from trace import Wrapper
# x = ? 1, 2, 3                         # Wrap a list
# ?.a.. 4                                 # Delegate to list method
# #
# print ?.w..                                  # Print my member
# #
# x = ? 'a' 1, 'b' 2
# print li.. x.k..                        # Delegate to dictionary method
#
