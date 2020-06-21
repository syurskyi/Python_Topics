# """
# "Subclassing built-in types" section example of subclassing built-in
# dict type.
#
# """
#
#
# c_ DistinctError V..E..
#     """ Raised when duplicate value is being added to a distinctdict"""
#
#
# c_ distinctdict di..
#     """ Dictionary that does not accept duplicate values"""
#     ___ -s key value
#         __ v.. __ ____.v...
#             __ |
#                 |k.. __ ? an. ?|k.. !_ v.. o.
#                 k.. no. __ ?
#             |;
#                 r_ D.. |
#                     "This value already exists for different key"
#                 |
#
#         s___ . -s ?  ?
#
#
# __ _______ __ _______
#     names_to_numbers _ |
#         "one": 1,
#         "two": 2,
#         "uno": 1,
#     |
#
#     ddict _ d..
#     ___ k.. v.. __ ?.it..
#         ___
#             ?|k.. _ v..
#         ______ D...
#             p..
#
#     print("ordinary dictionary:" n..
#     print("distinctdict dictionary:", d..
