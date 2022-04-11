____ d__ _______ date

____ dateutil.relativedelta _______ relativedelta

START_DATE date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH 10
MONTHS_PER_YEAR 12


___ calc_months_passed(year, month, day
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

    new_date date(year,month,day) # will re

    __ new_date < START_DATE:
        r.. V...



    x  = relativedelta(new_date,START_DATE)


    r.. MONTHS_PER_YEAR * x.years + x.months + (1 __ x.days >_ MIN_DAYS_TO_COUNT_AS_MONTH ____ 0)






__ _______ __ _______

    calc_months_passed(2019,1,16)


