_______ unittest

____ clock _______ Clock


c_ ClockTest(unittest.TestCase):
    # Test creating a new clock with an initial time.
    ___ test_on_the_hour
        assertEqual(s..(Clock(8, 0)), '08:00')

    ___ test_past_the_hour
        assertEqual(s..(Clock(11, 9)), '11:09')

    ___ test_midnight_is_zero_hours
        assertEqual(s..(Clock(24, 0)), '00:00')

    ___ test_hour_rolls_over
        assertEqual(s..(Clock(25, 0)), '01:00')

    ___ test_hour_rolls_over_continuously
        assertEqual(s..(Clock(100, 0)), '04:00')

    ___ test_sixty_minutes_is_next_hour
        assertEqual(s..(Clock(1, 60)), '02:00')

    ___ test_minutes_roll_over
        assertEqual(s..(Clock(0, 160)), '02:40')

    ___ test_minutes_roll_over_continuously
        assertEqual(s..(Clock(0, 1723)), '04:43')

    ___ test_hour_and_minutes_roll_over
        assertEqual(s..(Clock(25, 160)), '03:40')

    ___ test_hour_and_minutes_roll_over_continuously
        assertEqual(s..(Clock(201, 3001)), '11:01')

    ___ test_hour_and_minutes_roll_over_to_exactly_midnight
        assertEqual(s..(Clock(72, 8640)), '00:00')

    ___ test_negative_hour
        assertEqual(s..(Clock(-1, 15)), '23:15')

    ___ test_negative_hour_rolls_over
        assertEqual(s..(Clock(-25, 0)), '23:00')

    ___ test_negative_hour_rolls_over_continuously
        assertEqual(s..(Clock(-91, 0)), '05:00')

    ___ test_negative_minutes
        assertEqual(s..(Clock(1, -40)), '00:20')

    ___ test_negative_minutes_roll_over
        assertEqual(s..(Clock(1, -160)), '22:20')

    ___ test_negative_minutes_roll_over_continuously
        assertEqual(s..(Clock(1, -4820)), '16:40')

    ___ test_negative_hour_and_minutes_both_roll_over
        assertEqual(s..(Clock(-25, -160)), '20:20')

    ___ test_negative_hour_and_minutes_both_roll_over_continuously
        assertEqual(s..(Clock(-121, -5810)), '22:10')

    # Test adding and subtracting minutes.
    ___ test_add_minutes
        assertEqual(s..(Clock(10, 0).add(3)), '10:03')

    ___ test_add_no_minutes
        assertEqual(s..(Clock(6, 41).add(0)), '06:41')

    ___ test_add_to_next_hour
        assertEqual(s..(Clock(0, 45).add(40)), '01:25')

    ___ test_add_more_than_one_hour
        assertEqual(s..(Clock(10, 0).add(61)), '11:01')

    ___ test_add_more_than_two_hours_with_carry
        assertEqual(s..(Clock(0, 45).add(160)), '03:25')

    ___ test_add_across_midnight
        assertEqual(s..(Clock(23, 59).add(2)), '00:01')

    ___ test_add_more_than_one_day
        assertEqual(s..(Clock(5, 32).add(1500)), '06:32')

    ___ test_add_more_than_two_days
        assertEqual(s..(Clock(1, 1).add(3500)), '11:21')

    ___ test_subtract_minutes
        assertEqual(s..(Clock(10, 3).add(-3)), '10:00')

    ___ test_subtract_to_previous_hour
        assertEqual(s..(Clock(10, 3).add(-3)), '10:00')

    ___ test_subtract_more_than_an_hour
        assertEqual(s..(Clock(10, 3).add(-30)), '09:33')

    ___ test_subtract_across_midnight
        assertEqual(s..(Clock(10, 3).add(-70)), '08:53')

    ___ test_subtract_more_than_two_hours
        assertEqual(s..(Clock(0, 0).add(-160)), '21:20')

    ___ test_subtract_more_than_two_hours_with_borrow
        assertEqual(s..(Clock(6, 15).add(-160)), '03:35')

    ___ test_subtract_more_than_one_day
        assertEqual(s..(Clock(5, 32).add(-1500)), '04:32')

    ___ test_subtract_more_than_two_days
        assertEqual(s..(Clock(2, 20).add(-3000)), '00:20')

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
