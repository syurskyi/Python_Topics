____ d__ _______ date
_______ unittest

____ meetup _______ meetup_day


c_ MeetupTest(unittest.TestCase
    ___ test_monteenth_of_may_2013
        assertEqual(date(2013, 5, 13),
                         meetup_day(2013, 5, 'Monday', 'teenth'

    ___ test_saturteenth_of_february_2013
        assertEqual(date(2013, 2, 16),
                         meetup_day(2013, 2, 'Saturday', 'teenth'

    ___ test_first_tuesday_of_may_2013
        assertEqual(date(2013, 5, 7),
                         meetup_day(2013, 5, 'Tuesday', '1st'

    ___ test_second_monday_of_april_2013
        assertEqual(date(2013, 4, 8),
                         meetup_day(2013, 4, 'Monday', '2nd'

    ___ test_third_thursday_of_september_2013
        assertEqual(date(2013, 9, 19),
                         meetup_day(2013, 9, 'Thursday', '3rd'

    ___ test_fourth_sunday_of_march_2013
        assertEqual(date(2013, 3, 24),
                         meetup_day(2013, 3, 'Sunday', '4th'

    ___ test_last_thursday_of_october_2013
        assertEqual(date(2013, 10, 31),
                         meetup_day(2013, 10, 'Thursday', 'last'

    ___ test_last_wednesday_of_february_2012
        assertEqual(date(2012, 2, 29),
                         meetup_day(2012, 2, 'Wednesday', 'last'


__ _____ __ _____
    unittest.main()
