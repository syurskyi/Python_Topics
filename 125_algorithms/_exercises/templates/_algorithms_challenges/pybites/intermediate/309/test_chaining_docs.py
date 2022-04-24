# _______ p__
#
# ____ ? _______ ?
#
#
# EOL_PUNCTUATION ".!?"
#
# DOCS {
#     "four-liner": (
#         ?
#         .a.. "first"
#         .a.. "fourth"
#         .a.. "third", 1
#         .a.. "second", 1
#
#     "tale":
#         ?
#         .a.. "This is the tale of a dwarf."
#         .a.. ""
#         .a.. "A dwarf you ask?"
#         .a.. "Yes, a dwarf and not any dwarf, so you know!"
#     )
#     "complex":
#         ?
#         .a.. "My second sentence."
#         .a.. "My first sentence."
#         .s.. 0, 1
#         .a.. "Introduction", 0
#         .a.. "!", 0
#         .a.. ""
#         .a.. "My second paragraph."
#         .m.. [1, 2]
#
#     "edgy":
#         ?.a.. "" .s.. 0, 0 .m..  0.a.. ".", 0
#
#     "full-case":
#         ?
#         .a.. "1"  # 1
#         .a.. "2", 0  # 2\n1
#         .a.. "3", 1  # 2\n3\n1
#         .s.. 0, 1  # 3\n2\n1
#         .s.. 1, 2  # 3\n1\n2
#         .s.. 2, 1  # 3\n2\n1
#         .m.. [0, 2]  # 3 1\n2
#         .m.. [0, 1]  # 3 1 2
#
#     "punctuation":
#         ?
#         .a.. ""
#         .a.. ".", 0
#         .a.. "!", 0
#         .a.. "?", 0
#         .a.. "."
#         .a.. "?", 1 # ?\n?
#
#
#
# ?p__.f..
# ___ doc request
#     """Factory method for test documents"""
#     r.. D__.g.. ?.p.. D..
#
#
# ?p__.m__.p.
#     "doc, expected",
#
#         ("complex", ?
#
#     indirect_ "doc"
#
# ___ test_correct_return_type doc e..
#     ... isi.. ? e..
#
#
# ?p__.m__.p.
#     "doc, expected",
#
#         ("tale", 4
#         ("complex", 4
#         ("four-liner", 4
#         ("edgy", 1
#         ("full-case", 1
#         ("punctuation", 2
#
#     indirect=["doc"]
#
# ___ test_len_implementation doc e..
#     ... l.. ? __ e..
#
#
# ?p__.m__.p.
#     "doc, expected",
#
#        "tale", 21
#        "complex", 10
#        "four-liner", 4
#        "edgy", 0
#        "full-case", 3
#        "punctuation", 0
#
#     indirect=["doc"
#
# ___ test_word_count_implementation doc e..
#     ... ?.w.. __ e..
#
#
# ?p__.m__.p.
#     "doc, expected",
#
#         ("four-liner", "first\nsecond\nthird\nfourth"),
#         (
#             "tale",
#             "This is the tale of a dwarf.\n\nA dwarf you ask?\nYes, a dwarf and not any dwarf, so you know!",
#         ),
#         (
#             "complex",
#             "Introduction!\nMy first sentence. My second sentence.\n\nMy second paragraph.",
#         ),
#         ("edgy", "."),
#         ("full-case", "3 1 2"),
#         ("punctuation", "?\n?"),
#     ],
#     indirect=["doc"],
#
# ___ test_correct_chaining doc e..
#     ... s.. ? __ e..
#
#
# ?p__.m__.p.
#     "doc, expected",
#
#
#             "tale",
#             s..
#
#                     "this",
#                     "is",
#                     "the",
#                     "tale",
#                     "of",
#                     "a",
#                     "dwarf",
#                     "you",
#                     "ask",
#                     "yes",
#                     "and",
#                     "not",
#                     "any",
#                     "so",
#                     "know",
#
#             )
#
#
#             "complex",
#             s.. "my", "first", "second", "sentence", "introduction", "paragraph"]
#
#         ("edgy" ||
#         ("full-case", ["1", "2", "3"
#         ("punctuation" ||
#
#     indirect=["doc"],
#
# ___ test_words_property doc e..
#     ... ?.w.. __ e..