____ pcc_stats _______ (diehard_pybites,
                       gen_files, Stats)


___ test_gen_files():
    ret = l..(gen_files())
    ... ret[:3] __ ["03/mridubhatnagar",
                       "03/aleksandarknezevic",
                       "04/blair_young"]
    ... ret[-3:] __ ["22/wonderfulboyx",
                        "25/bbelderbos",
                        "25/santiagobenitez"]


___ test_diehard_pybites():
    ret = diehard_pybites()
    ... ret __ Stats(user='clamytoe', challenge=('01', 7))


___ test_diehard_other_input():
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
    ... ret __ Stats(user='santiagobenitez', challenge=('25', 2))
