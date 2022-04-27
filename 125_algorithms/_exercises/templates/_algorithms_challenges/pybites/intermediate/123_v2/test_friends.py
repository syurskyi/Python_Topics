# ____ ? _______ ? ?
#
#
# ___ test_default_friendships_list
#     user, friends ? ?
#     ... ?__ 'sara'
#     ... s.. l.. ? __  'joyce', 'kevin', 'nick', 'rod'
#
#
# ___ test_different_friendships_list
#     friendships [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
#                    (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
#                    (6, 7), (6, 8), (6, 9)]
#     user, friends ? ?
#     ... ? __ 'joyce'
#     ... s.. l.. ? __  'beverly', 'julian', 'kevin', 'nick',
#                                      'rod', 'sara'
#
#
# ___ test_friendships_list_with_duplicate_names
#     names 'bob bob tim tim julian julian'.s..
#     ids r.. l.. ?
#     users d.. z.. ? ?
#
#     friendships [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3),
#                    (2, 4), (4, 5)]
#     user friends ? ? u.._?
#     ... ? __ 'bob'
#     ... s.. l.. ? __  'bob', 'julian', 'julian', 'tim'
