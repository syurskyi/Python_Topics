# _______ p__
#
# ____ ? _______ ?
#
#
# ___ test_wagner_verdi
#     # materializing to list to support generator as return
#     wagner_verdi l.. ? "wagner", "verdi"
#     ... l.. ? __ 10
#     ... "Otello" n.. __ ?
#
#
# ___ test_verdi_wagner
#     verdi_wagner l.. ? "verdi", "wagner"
#     ... l.. ?__ 11
#
#     # premiere after Wagner's death (composed in 1833)
#     ... "The Fairies" n.. __ ?
#
#
# ___ test_beethoven_wagner
#     beethoven_wagner l.. ? "beethoven", "wagner"
#     ... l.. ? __ 0
#
#
# ___ test_wagner_beethoven
#     wagner_beethoven l.. ? "wagner", "beethoven"
#     ... l.. ? __ 0
#
#
# ___ test_beethoven_mozart
#     beethoven_mozart l.. ? "beethoven", "mozart"
#     ... l.. ? __ 5
#     ... "Apollo and Hyacinth" n.. __ ?
#
#
# ___ test_non_listed_composer
#     w__ p__.r.. V...
#         l.. ? "verdi", "dvorak"
#
#
# ___ test_non_listed_guest
#     # a guest must be in the list of composers
#     w__ p__.r.. V...
#         l.. ? "dvorak", "verdi"a