from datetime import datetime

from dateutil.parser import parse

# work with a static date for tests, real use = datetime.now()
NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52


def get_number_books_read(books_per_year_goal: int,
                          at_date: str = None) -> int:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    in_date = NOW if at_date is None else parse(at_date)
    if books_per_year_goal <= 0 or in_date < NOW:
        raise ValueError
    # TODOs

    # 1. use dateutil's parse to convert at_date into a
    # datetime object

    # 2. check books_per_year_goal and at_date and raise
    # a ValueError if goal <= 0 or at_date in the past (< NOW)

    # 3. check the offset of at_date in the year ("week of the
    # year" - e.g. whatweekisit.com) and based on the books_per_year_goal,
    # calculate the number of books that should have been read / completed
    #print(in_date)
    #print(type(in_date.isocalendar()[1]))
    return int((in_date.isocalendar()[1]/52)*books_per_year_goal)



#print(NOW)
print(get_number_books_read(52, 'Sunday, March 18th, 2019'))
#get_number_books_read(52)