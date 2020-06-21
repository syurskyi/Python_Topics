
______ u__

____ theatre ______ SeatFinder

# Note: A is the front row, so A6 is the 6th seat on the front row

c_ SeatFinderTest?.?
    ___ test_prefer_near_the_front
        finder _ SeatFinder(available_seats_{"A6", "B6", "C7"})
        seats _ finder.find_seats(1)
        a.. seats __ {"A6"}

    ___ test_finds_adjacent_seats_when_more_than_one_requested
        finder _ SeatFinder(available_seats_{"A6", "A8", "C6", "C7"})
        seats _ finder.find_seats(2)
        a.. seats __ {"C6", "C7"}

    ___ test_finds_separate_seats_when_adjacent_not_available
        finder _ SeatFinder(available_seats_{"A6", "B6", "C7"})
        seats _ finder.find_seats(2)
        a.. seats __ {"B6", "A6"}

    ___ test_find_seats_fails_when_not_enough_available
        finder _ SeatFinder(available_seats_{"A6", "B6", "C7"})
        seats _ finder.find_seats(5)
        a.. seats __ {}
        
    ___ test_find_seats_for_wheelchair_users_on_front_row
        finder _ SeatFinder(available_seats_{"A1W", "A6", "A7", "C7"})
        seats _ finder.find_seats(1, wheelchair_count_1)
        a.. seats __ {"A1W"}
    