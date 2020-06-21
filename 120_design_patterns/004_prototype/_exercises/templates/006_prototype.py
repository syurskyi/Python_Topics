# """Prototype pattern
# """
# ______ c___
# ____ co.. ______ OD..
#
#
# c_ Book
#
#     ___ - name authors price $$
#         """Examples of kwargs: publisher, length, tags, publication date"""
#         ?  ?
#         ?  ?
#         ?  ?
#         ?. -d .u.. k..
#
#     ___ -s
#         mylist _     # list
#         ordered _ OD.. so.. ?. -d.it..
#         ___ i __ ?.ke..
#             my___.ap.. "@: @".f... ? o..|?
#             __ i __ "price":
#                 my___.ap.. "$"
#             my___.ap.. "\n"
#         r_ "".jo.. m..
#
#
# c_ Prototype
#
#     ___ -
#         ?objects _ di..
#
#     ___ register identifier obj
#         o..|? _ ?
#
#     ___ unregister identifier
#         de. .o..|?
#
#     ___ clone  identifier $$attr
#         found _ .o___.ge. i..
#         __ no. found
#             r_ V.. ("Incorrect object identifier: @".f... i..
#
#         obj _ c___.de.. f..
#         ?. -d .up.. a..
#         r_ ?
#
#
# ___ main
#     b1 _ B..|
#         name_"The C Programming Language",
#         authors_("Brian W. Kernighan", "Dennis M.Ritchie"),
#         price_118,
#         publisher_"Prentice Hall",
#         length_228,
#         publication_date_"1978-02-22",
#         tags_("C", "programming", "algorithms", "data structures"),
#     )
#
#     prototype _ P..
#     cid _ "k&r-first"
#     ?.re.. c.. b.
#     b2 _ ?.cl.. |
#         c..
#         name_"The C Programming Language (ANSI)",
#         price_48.99,
#         length_274,
#         publication_date_"1988-04-01",
#         edition_2,
#     )
#
#     ___ i __ _1 _2
#         print ?
#
#     print("ID b1 : @ !_ ID b2 : @".f... i. _1 i. _2
#
#
# __ ______ __ ______
#     ?
