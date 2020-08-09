"""Test if year is a leap year"""

___ is_leap_year(year
    """Test if year is leap year"""
    # Is a leap year if the year is divisible by 4,
    # but not by 100 unless also divisable by 400
    r_ (year % 4 __ 0 and
           (year % 100 != 0 or year % 400 __ 0))
