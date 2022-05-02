# ____ p.. _______ P..
# ____ t.. _______ T..
#
# _______ p__
#
# ____ ? _______ ? ?
#
# BITES_CSV T.. / 'intro_bites.csv'
# INTRO_BITE_STATS """Bite;Difficulty
# Bite 101. f-strings and a simple if/else;3.52
# Bite 102. Infinite loop, input, continue and break;3.59
# Bite 103. Loop through a dictionary and pluralise a word;3.21
# Bite 104. Split and join;2.91
# Bite 105. Slice and dice;5.0
# Bite 106. Strip out vowels and count the number of replacements;4.73
# Bite 107. Filter numbers with a list comprehension;1.89
# Bite 108. Loop over a dict of namedtuples calculating a total score;4.83
# Bite 109. Workout dict lookups and raising an exception;2.75
# Bite 110. Type conversion and exception handling;1.5
# """
#
#
# ?p__.f..
# ___ intro_bites
#     w__ T.. dir_T..
#         w__ o.. ? _ __ f
#             ?.w.. ?
#     r.. ?
#
#
# ?p__.m__.p. "N, expected", [
#     (2,  '88', '31' ),
#     (6,  '88', '31', '50', '90', '179', '98' ),
#     (10,  '88', '31', '50', '90', '179', '98', '190', '42', '69', '40' ),
#
# ___ test_different_args_for_N N e..
#     a.. ? ?
#     # str or int for IDs is fine with us
#     a.. s.. ? ___ i __ a..
#     ... a.. __ e..
#
#
# ?p__.m__.p. "N, expected", [
#     (1,  '105' ),
#     (3,  '105', '108', '106' ),
#     # res is max = size of bites in file:
#     (15,  '105', '108', '106', '102', '101', '103',
#           '104', '109', '107', '110' ),
#
# ___ test_only_intro_bites intro_bites N e..
#     a.. ? ? stats_i..
#     # str or int for IDs is fine with us
#     a.. s.. ? ___ i __ a..
#     ... a.. __ e..