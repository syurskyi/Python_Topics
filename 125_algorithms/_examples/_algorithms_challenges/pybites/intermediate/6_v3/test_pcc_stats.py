from pcc_stats import (diehard_pybites,
                       gen_files, Stats)


def test_gen_files():
    ret = list(gen_files())
    assert ret[:3] == ["03/mridubhatnagar",
                       "03/aleksandarknezevic",
                       "04/blair_young"]
    assert ret[-3:] == ["22/wonderfulboyx",
                        "25/bbelderbos",
                        "25/santiagobenitez"]


def test_diehard_pybites():
    ret = diehard_pybites()
    assert ret == Stats(user='clamytoe', challenge=('01', 7))


def test_diehard_other_input():
    ret = diehard_pybites(
        files=[
            "22/wonderfulboyx",
            "25/bbelderbos",  # ignored
            "25/clamytoe",
            "21/wonderfulboyx",
            "25/santiagobenitez",
            "23/santiagobenitez",
            "07/santiagobenitez"
        ])
    assert ret == Stats(user='santiagobenitez', challenge=('25', 2))