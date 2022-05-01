____ d__ _______ d__, d__

____ d__.r.. _______ r..

START_DATE ? 2018, 11, 1
MIN_DAYS_TO_COUNT_AS_MONTH 10
MONTHS_PER_YEAR 12


___ calc_months_passed year month day
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    ___
        in_date d__ y.._? m.._?d.._day)
        __ date year month day) < START_DATE:
            r.. V...
        months_passed 0
        difference_dt r..(date year month day), START_DATE)
        #print(difference_dt.years, difference_dt.months, difference_dt.days)
        __ difference_dt.days >_ M..
            months_passed difference_dt.months + 1
        ____
            months_passed difference_dt.months
        __ difference_dt.years > 0
            months_passed += difference_dt.years * M..
        r.. months_passed
    ______ V..
        r.. V...
        


#print(calc_months_passed(2018, 13, 11))