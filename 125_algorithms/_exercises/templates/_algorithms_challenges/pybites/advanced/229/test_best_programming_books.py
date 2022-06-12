# _______ p__
#
# ____ ? _______ ? ? ?
#
#
# ?p__.f.. s.._"session"
# ___ dummy_book
#     t.. "Python Testing with pytest"
#     a.. "Okken, Brian"
#     y.. 2017
#     r.. 1
#     r.. 5
#     r.. ? ? ? ? ? ?
#
#
# ?p__.f.. s.._"session"
# ___ python_books
#     data ?
#     __ isi.. ? l..
#         r.. ?
#     r.. l.. ?
#
#
# ___ test_book_class_incorrectly
#     w__ p__.r.. T..
#         B..
#
#
# ___ test_book_class dummy_book
#     ... ?.t.. __ "Python Testing with pytest"
#     ... ?.a.. __ "Okken, Brian"
#     ... ?.y.. __ 2017
#     ... ?.r.. __ 1
#     ... ?.r.. __ 5
#
#
# ___ test_book_class_str dummy_book
#     a.. s.. ?
#     e.. ("[001] Python Testing with pytest (2017)"
#                 "\n      Okken, Brian 5.0")
#     ... a.. __ e..
#
#
# ___ test_load_data python_books
#     ... l.. ? __ 36
#     ... ? 0 .a.. __ "Bader, Dan"
#     ... ? -1 .t.. __ "Python for Tweens and Teens"
#     ... ? 10 .r.. __ 4.66
#
#
# ?p__.m__.p.
#     "index, expected",
#     [
#         (0, "[001] Python Tricks (2017)"),
#         (1, "      Bader, Dan 4.74"),
#         (2, "[002] Mastering Deep Learning Fundamentals with Python (2019)"),
#         (3, "      Wilson, Richard 4.7"),
#         (4, "[006] Python Programming (2019)"),
#         (5, "      Fedden, Antony Mc 4.68"),
#         (6, "[007] Python Programming (2019)"),
#         (7, "      Mining, Joseph 4.68"),
#         (8, "[009] A Smarter Way to Learn Python (2017)"),
#         (9, "      Myers, Mark 4.66"),
#         (10, "[010] Python Crash Course (2019)"),
#         (11, "      Robert, Antonio 4.66"),
#         (12, "[011] PYTHON PROGRAMMING (2019)"),
#         (13, "      Campbell, Clive 4.66"),
#         (14, "[012] Python Programming (2019)"),
#         (15, "      Harvard, Chris 4.66"),
#         (16, "[013] Python Programming (2019)"),
#         (17, "      Samelson, Steven 4.66"),
#         (18, "[014] Python Programming (2019)"),
#         (19, "      James, Thomas 4.65"),
#
#
# ___ test_display_books python_books index e.. capfd
#     ? ? y.._2017
#     output ?.r .. 0 .s..
#     ... ? ? __ e..
#
#
# ?p__.m__.p.
#     "limit, expected", [(40, 72), (53, 72), (69, 72), (100, 72), (1000, 72)]
#
# ___ test_display_books_plus python_books limit e.. capfd
#     ? ? l.._?
#     output ?.r .. 0 .s..
#     ... l.. ?  __ e..