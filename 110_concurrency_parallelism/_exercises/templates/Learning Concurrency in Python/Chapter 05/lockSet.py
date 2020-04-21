# c_ LockedSet set
#     """A set where add(), remove(), and 'in' operator are thread-safe"""
#
#     ___ - $ $$
#         _lock _ L..
#         s__(?, ?).__init__ $ $$
#
#     ___ add elem
#         w__ _?
#             s__ ? ? .a.. ?
#
#     ___ remove elem
#         w__ _?
#             s__ ? ? .r.. ?
#
#     ___ -c elem
#         w__ _l?
#             s__ ? ? . -c ?