# _______ p__
#
# ____ ? _______ ?
#
# FILES ('bite.html commands.sh out_grepped pytest_testrun.out '
#          'pytest_timings.out test_timings.py timings-template.py '
#          'timings.py').s..
#
#
# ?p__.m__.p. "filter_str, expected", [
#    ('bite1',  'bite1' ),
#    ('Bite',  'bite1' ),
#    ('pybites',  'bite1' ),
#    ('test',  'test' ),
#    ('test2',  'test' ),
#    ('output',  'output' ),
#    ('o$tput',  'output' ),
#    ('nonsense',    # list),
#
# ___ test_example_docstring tmp_path filter_str e..
#     # let's create some files in tmp
#     ___ fi __ 'bite1 test output'.s..
#         o.. ? / ? _ .c..
#     a.. ? ? ?
#     ... s.. a.. __ s.. e..
#
#
# ?p__.m__.p. "filter_str, expected", [
#    ('bite.html',  'bite.html' ),
#    ('bite.htm1',  'bite.html' ),
#    ('bit$.htm1',  'bite.html' ),
#    ('bite.txt',  'bite.html' ),
#    ('_timing',  'timings.py', 'test_timings.py' ),
#    ('commando',  'commands.sh' ),
#    ('pytest_testruns.out',  'pytest_testrun.out', 'pytest_timings.out' ),
#    ('out_greped',  'out_grepped' ),
#    ('nonsensical',    # list),
#    ('commands.py',  'commands.sh' ),
#    ('pytest_t',  'pytest_testrun.out', 'pytest_timings.out' ),
#    ('timings-templates.PY',  'timings-template.py' ),
#
# ___ test_other_files tmp_path filter_str e..
#     # let's create some files in tmp
#     ___ fi __ ?
#         o.. ? / ? _ .c..
#     a.. ? ?
#     ... s.. a.. __ s.. e..
