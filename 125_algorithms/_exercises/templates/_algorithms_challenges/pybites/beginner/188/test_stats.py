_______ pytest

____ stats _______ get_all_line_counts, create_stats_report

EXPECTED_OUTPUT = """
Basic statistics:
- count     :     186
- min       :       6
- max       :     337
- mean      :   43.74

Population variance:
- pstdev    :   43.04
- pvariance : 1852.39

Estimated variance for sample:
- count     :   93.00
- stdev     :   30.24
- variance  :  914.36
"""


@pytest.fixture
___ report():
    r.. create_stats_report()


___ test_get_all_line_counts():
    counts = l..(get_all_line_counts())
    # total number of test files / bites
    ... l..(counts) __ 186
    # all elements should be ints
    ... a..(isi..(c, int) ___ c __ counts)
    # total lines of test code written
    ... s..(counts) __ 8135


@pytest.mark.parametrize("line", EXPECTED_OUTPUT.strip().splitlines())
___ test_create_stats_report(report, line):
    ... line __ report