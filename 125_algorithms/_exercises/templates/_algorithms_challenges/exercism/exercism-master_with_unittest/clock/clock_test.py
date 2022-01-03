_______ unittest

____ clock _______ Clock


c_ ClockTest(unittest.TestCase):
    # Test creating a new clock with an initial time.
    ___ test_on_the_hour
        assertEqual('08:00', s..(Clock(8, 0)))

    ___ test_past_the_hour
        assertEqual('11:09', s..(Clock(11, 9)))

    ___ test_midnight_is_zero_hours
        assertEqual('00:00', s..(Clock(24, 0)))

    ___ test_hour_rolls_over
        assertEqual('01:00', s..(Clock(25, 0)))

    ___ test_hour_rolls_over_continuously
        assertEqual('04:00', s..(Clock(100, 0)))

    ___ test_sixty_minutes_is_next_hour
        assertEqual('02:00', s..(Clock(1, 60)))

    ___ test_minutes_roll_over
        assertEqual('02:40', s..(Clock(0, 160)))

    ___ test_minutes_roll_over_continuously
        assertEqual('04:43', s..(Clock(0, 1723)))

    ___ test_hour_and_minutes_roll_over
        assertEqual('03:40', s..(Clock(25, 160)))

    ___ test_hour_and_minutes_roll_over_continuously
        assertEqual('11:01', s..(Clock(201, 3001)))

    ___ test_hour_and_minutes_roll_over_to_exactly_midnight
        assertEqual('00:00', s..(Clock(72, 8640)))

    ___ test_negative_hour
        assertEqual('23:15', s..(Clock(-1, 15)))

    ___ test_negative_hour_rolls_over
        assertEqual('23:00', s..(Clock(-25, 0)))

    ___ test_negative_hour_rolls_over_continuously
        assertEqual('05:00', s..(Clock(-91, 0)))

    ___ test_negative_minutes
        assertEqual('00:20', s..(Clock(1, -40)))

    ___ test_negative_minutes_roll_over
        assertEqual('22:20', s..(Clock(1, -160)))

    ___ test_negative_minutes_roll_over_continuously
        assertEqual('16:40', s..(Clock(1, -4820)))

    ___ test_negative_hour_and_minutes_both_roll_over
        assertEqual('20:20', s..(Clock(-25, -160)))

    ___ test_negative_hour_and_minutes_both_roll_over_continuously
        assertEqual('22:10', s..(Clock(-121, -5810)))

    # Test adding and subtracting minutes.
    ___ test_add_minutes
        assertEqual('10:03', s..(Clock(10, 0).add(3)))

    ___ test_add_no_minutes
        assertEqual('06:41', s..(Clock(6, 41).add(0)))

    ___ test_add_to_next_hour
        assertEqual('01:25', s..(Clock(0, 45).add(40)))

    ___ test_add_more_than_one_hour
        assertEqual('11:01', s..(Clock(10, 0).add(61)))

    ___ test_add_more_than_two_hours_with_carry
        assertEqual('03:25', s..(Clock(0, 45).add(160)))

    ___ test_add_across_midnight
        assertEqual('00:01', s..(Clock(23, 59).add(2)))

    ___ test_add_more_than_one_day
        assertEqual('06:32', s..(Clock(5, 32).add(1500)))

    ___ test_add_more_than_two_days
        assertEqual('11:21', s..(Clock(1, 1).add(3500)))

    ___ test_subtract_minutes
        assertEqual('10:00', s..(Clock(10, 3).add(-3)))

    ___ test_subtract_to_previous_hour
        assertEqual('10:00', s..(Clock(10, 3).add(-3)))

    ___ test_subtract_more_than_an_hour
        assertEqual('09:33', s..(Clock(10, 3).add(-30)))

    ___ test_subtract_across_midnight
        assertEqual('08:53', s..(Clock(10, 3).add(-70)))

    ___ test_subtract_more_than_two_hours
        assertEqual('21:20', s..(Clock(0, 0).add(-160)))

    ___ test_subtract_more_than_two_hours_with_borrow
        assertEqual('03:35', s..(Clock(6, 15).add(-160)))

    ___ test_subtract_more_than_one_day
        assertEqual('04:32', s..(Clock(5, 32).add(-1500)))

    ___ test_subtract_more_than_two_days
        assertEqual('00:20', s..(Clock(2, 20).add(-3000)))

    # Construct two separate clocks, set times, test if they are equal.
    ___ test_clocks_with_same_time
        assertEqual(Clock(15, 37), Clock(15, 37))

    ___ test_clocks_a_minute_apart
        assertNotEqual(Clock(15, 36), Clock(15, 37))

    ___ test_clocks_an_hour_apart
        assertNotEqual(Clock(14, 37), Clock(15, 37))

    ___ test_clocks_with_hour_overflow
        assertEqual(Clock(10, 37), Clock(34, 37))

    ___ test_clocks_with_hour_overflow_by_several_days
        assertEqual(Clock(3, 11), Clock(99, 11))

    ___ test_clocks_with_negative_hour
        assertEqual(Clock(22, 40), Clock(-2, 40))

    ___ test_clocks_with_negative_hour_that_wraps
        assertEqual(Clock(17, 3), Clock(-31, 3))

    ___ test_clocks_with_negative_hour_that_wraps_multiple_times
        assertEqual(Clock(13, 49), Clock(-83, 49))

    ___ test_clocks_with_minute_overflow
        assertEqual(Clock(0, 1), Clock(0, 1441))

    ___ test_clocks_with_minute_overflow_by_several_days
        assertEqual(Clock(2, 2), Clock(2, 4322))

    ___ test_clocks_with_negative_minute
        assertEqual(Clock(2, 40), Clock(3, -20))

    ___ test_clocks_with_negative_minute_that_wraps
        assertEqual(Clock(4, 10), Clock(5, -1490))

    ___ test_clocks_with_negative_minute_that_wraps_multiple_times
        assertEqual(Clock(6, 15), Clock(6, -4305))

    ___ test_clocks_with_negative_hours_and_minutes
        assertEqual(Clock(7, 32), Clock(-12, -268))

    ___ test_clocks_with_negative_hours_and_minutes_that_wrap
        assertEqual(Clock(18, 7), Clock(-54, -11513))


__ __name__ __ '__main__':
    unittest.main()
