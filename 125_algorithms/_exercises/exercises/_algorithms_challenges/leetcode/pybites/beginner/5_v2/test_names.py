# ____ names _______  N.. d..
#                    s.. s..
#
# PY_CONTENT_CREATORS  ['brian okken', 'michael kennedy', 'trey hunner',
#                        'matt harrison', 'julian sequeira', 'dan bader',
#                        'michael kennedy', 'brian okken', 'dan bader']
#
#
# ___ test_dedup_and_title_case_names
#     names  ? ?
#     ... ?.c.. 'Bob Belderbos' __ 1
#     ... ?.c.. 'julian sequeira' __ 0
#     ... ?.c.. 'Brad Pitt' __ 1
#     ... l.. ? __ 10
#     ... a..(n.t.. __ ? ___ ? __ N..
#
#
# ___ test_dedup_and_title_case_names_different_names_list
#     actual  s.. ? ?
#     expected  ['Brian Okken', 'Dan Bader', 'Julian Sequeira',
#                 'Matt Harrison', 'Michael Kennedy', 'Trey Hunner']
#     ... ? __ ?
#
#
# ___ test_sort_by_surname_desc
#     names  ? ?
#     ... ? 0 __ 'Julian Sequeira'
#     ... ? -1 __ 'Alec Baldwin'
#
#
# ___ test_sort_by_surname_desc_different_names_list
#     names  ? ?
#     ... ? 0 __ 'Julian Sequeira'
#     ... ? -1 __ 'Dan Bader'
#
#
# ___ test_shortest_first_name
#     ... ? ? __ 'Al'
#
#
# ___ test_shortest_first_name_different_names_list
#     ... ? ? __ 'Dan'
