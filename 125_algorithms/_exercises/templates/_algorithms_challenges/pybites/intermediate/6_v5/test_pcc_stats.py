from Previous.pcc_stats import diehard_pybites, Stats


___ test_diehard_pybites():
    res = diehard_pybites()
    assert res == Stats(user='clamytoe', challenge=('01', 7))