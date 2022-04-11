____ belts _______ BeltStats, ninja_belts, get_total_points


___ test_get_total_points_given_belts
    ... get_total_points(ninja_belts) __ 2675


___ test_get_total_points_more_belts
    more_belts d..(brown=BeltStats(400, 2),
                      black=BeltStats(600, 5

    # this way to dict merge is >= 3.5 (PEP 448)
    ninja_belts_updated {**ninja_belts, **more_belts}

    ... get_total_points(ninja_belts_updated) __ 6475