____ d__ _______ d__

____ dateutil.parser _______ p..

# work with a static date for tests, real use = datetime.now()
NOW d__(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR 52


___ get_number_books_read(books_per_year_goal: i..,
                          at_date: s.. N..) __ i..:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    in_date NOW __ at_date __ N.. ____ p..(at_date)
    __ books_per_year_goal <_ 0 o. in_date < NOW:
        r.. V...
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
    r.. i..((in_date.isocalendar()[1]/52)*books_per_year_goal)



#print(NOW)
print(get_number_books_read(52, 'Sunday, March 18th, 2019'
#get_number_books_read(52)