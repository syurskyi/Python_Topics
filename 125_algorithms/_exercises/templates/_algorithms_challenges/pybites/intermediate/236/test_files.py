_______ p__

____ files _______ get_matching_files

FILES = ('bite.html commands.sh out_grepped pytest_testrun.out '
         'pytest_timings.out test_timings.py timings-template.py '
         'timings.py').s..


?p__.m__.p.("filter_str, expected", [
   ('bite1',  'bite1' ),
   ('Bite',  'bite1' ),
   ('pybites',  'bite1' ),
   ('test',  'test' ),
   ('test2',  'test' ),
   ('output',  'output' ),
   ('o$tput',  'output' ),
   ('nonsense', []),
])
___ test_example_docstring(tmp_path, filter_str, expected
    # let's create some files in tmp
    ___ fi __ 'bite1 test output'.s.. :
        o.. tmp_path / fi, 'a').c..
    actual = get_matching_files(tmp_path, filter_str)
    ... s..(actual) __ s..(expected)


?p__.m__.p.("filter_str, expected", [
   ('bite.html',  'bite.html' ),
   ('bite.htm1',  'bite.html' ),
   ('bit$.htm1',  'bite.html' ),
   ('bite.txt',  'bite.html' ),
   ('_timing',  'timings.py', 'test_timings.py' ),
   ('commando',  'commands.sh' ),
   ('pytest_testruns.out',  'pytest_testrun.out', 'pytest_timings.out' ),
   ('out_greped',  'out_grepped' ),
   ('nonsensical', []),
   ('commands.py',  'commands.sh' ),
   ('pytest_t',  'pytest_testrun.out', 'pytest_timings.out' ),
   ('timings-templates.PY',  'timings-template.py' ),
])
___ test_other_files(tmp_path, filter_str, expected
    # let's create some files in tmp
    ___ fi __ FILES:
        o.. tmp_path / fi, 'a').c..
    actual = get_matching_files(tmp_path, filter_str)
    ... s..(actual) __ s..(expected)
