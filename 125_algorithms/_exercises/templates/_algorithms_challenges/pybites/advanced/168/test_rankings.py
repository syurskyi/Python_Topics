# _______ p__
#
# ____ ? _______ ? ? ? ?
#
# more_names [
#     ("rey", 287),
#     ("bob", 293),
#     ("dan", 296),
#     ("darren", 298),
#     ("david", 313),
#     ("sebastian", 323),
#     ("ed", 368),
#     ("veronica", 410),
#     ("valentine", 441),
#     ("tyler", 450),
#     ("steve", 468),
#     ("doug", 469),
#     ("noah", 470),
# ]
# FIRST_NINJAS  ? $ninja ___ ? __ z.. ? ?
# SECOND_NINJAS ? @? ___ ? __ ?
#
#
# ___ _create_ranks ninjas_ N..
#     ranking ?
#     __ ? __ N..
#         r.. ?
#
#     ___ ninja __ ?
#         ?.a.. ?
#     r.. ?
#
#
# ?p__.f..
# ___ first_ninjas
#     r.. ?
#
#
# ?p__.f..
# ___ second_ninjas
#     r.. ?
#
#
# ?p__.f..
# ___ ninja_ranks
#     ranking ?
#     ___ ? __ F..
#         ?.a.. ?
#     r.. ?
#
#
# ___ test_ninja_class_empty_init_raises_exception
#     w__ p__.r.. T..
#         ?
#
#
# # required class behavior
#
#
# ___ test_ninja_class_and_membership first_ninjas
#     ninja1 ? "snow", 283
#     ninja2 ? "natalia", 282
#     ninja3 ? "okken", 70
#     ... ? __ ?
#     ... ? __ ?
#     ... ? __ ?
#
#
# ___ test_ninja_str_output first_ninjas capfd
#     print ? 1
#     output ?.r .. 0 .s..
#     ... ? __ "[282] natalia"
#     print? 3
#     output ?.r .. 0 .s..
#     ... ? __ "[263] maquina"
#
#
# # starting len of ninja rankings
#
#
# ___ test_first_ninja_ranks_in_object ninja_ranks
#     ... l.. ? __ 11
#
#
# ___ test_dumping_lowest_ranking_fist_ninjas ninja_ranks
#     a.. ?.d..
#     e.. ? n.. _ sam  b.._195
#     ... a.. __ e..
#     ... l.. ? __ 10
#
#
# # highest / lowest ninjas in rankings
#
#
# ___ test_highest_ranking_no_arg ninja_ranks
#     a.. ?.h..
#     e.. ? n.._ snow b.._283
#     ... a.. __ e..
#
#
# ___ test_lowest_ranking_no_arg ninja_ranks
#     a.. ?.l..
#     e.. ? n.. _ sam  b.._195
#     ... a.. __ e..
#
#
# ___ test_lowest_ranking_with_arg ninja_ranks
#     a.. ?.l.. 3
#     e..
#         ? n.. _ sam  b.._195,
#         ? n.._ sara b.._196
#         ? n.._ james b.._197
#
#     ... a.. __ e..
#
#
# ___ test_adding_a_ninja ninja_ranks
#     ?.a.. ? n.._ sam b.._195
#     ... l.. ? __ 12
#
#
# ___ test_lowest_ranking_after_adding_more_ninjas ninja_ranks
#     a.. ?.l.. 3
#     e..
#         ? n.. _ sam  b.._195
#         ? n.._ sara b.._196
#         ? n.._ james b.._197
#
#     ... a.. __ e..
#
#     # now add the ninjas of first_ninja_ranks
#     ___ ninja __ S..
#         ?.a.. ?
#
#     # check highest, they should have been added
#     a.. ?.h.. 3
#     e..
#         ? n.._ noah b.._470
#         ? n.._ doug b.._469
#         ? ?_steve ?_468
#
#     ... a.. __ e..
#
#
# # pairing of ninjas
#
#
# ___ test_pairing_with_no_arg ninja_ranks
#     a.. ?.p..
#     ... l.. a.. __ 3
#
#     e.. ? ?_natalia ?_282 ? ?_ sara b.._196
#     ... a.. 1 __ e..
#
#
# ___ test_pairing_with_count_arg ninja_ranks
#     a.. ?.p.. 5
#     ... l.. a.. __ 5
#
#     e.. ? ?_snow ?_283
#                 ? ?_ sam ?_195
#     ... a.. 0 __ e..
#
#     e.. ? ?_maria ?_255
#                 ? n.._kenneth b.._216
#     ... a.. -1 __ e..