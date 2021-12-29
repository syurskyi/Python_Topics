____ datetime _______ datetime

____ dateutil.parser _______ parse

# work with a static date for tests, real use = datetime.now()
NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52
START_DATE = datetime(2018, 12, 24)


___ get_number_books_read(books_per_year_goal: int,
                          at_date: s.. = N..) -> int:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    at_date = at_date o. s..(NOW)
    target = parse(at_date)

    __ target < START_DATE o. books_per_year_goal < 1:
        raise ValueError()

    week_diff = (target.date() - START_DATE.date()).days // 7

    r.. int(week_diff / WEEKS_PER_YEAR * books_per_year_goal)
