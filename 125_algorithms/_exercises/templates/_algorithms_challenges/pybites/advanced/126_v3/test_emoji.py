# ____ ? _______ ? ?
#
#
# ___ test_what_means_emoji_found
#     ? 🐶 .l.. __ dog face
#     ? 🏋 .l.. __ weight lifter
#     ? 🌇 .l.. __ sunset over buildings
#
#
# ___ test_what_means_emoji_not_found
#     ... ? aaa .l.. __ not found
#
#
# ___ test_find_matches capfd
#     ? sun
#     output ?.r .. 0].l..
#     # some of the results you should get back
#     ... sunrise __ ?
#     ... 🌅 __ ?
#     ... sunset over buildings __ ?
#     ... 🌇 __ ?
#     ... sun with face __ ?
#     ... 🌻 __ ?
#
#
# ___ test_find_no_match capfd
#     ? awesome
#     output ?.r .. 0].l..
#     ... n.. ?.s.. o. no matches __ ?.l..