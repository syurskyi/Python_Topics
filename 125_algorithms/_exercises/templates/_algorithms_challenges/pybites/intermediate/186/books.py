____ d__ _______ d__
____ m__ _______ f..
____ dateutil.parser _______ p..

# work with a static date for tests, real use = datetime.now()
NOW = d__(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52


___ get_number_books_read(books_per_year_goal: i..,
                          at_date: s.. = N..) __ i..:
   """Based on books_per_year_goal and at_date, return the
      number of books that should have been read.
      If books_per_year_goal negative or 0, or at_date is in the
      past, raise a ValueError."""
   at_date = at_date o. s..(NOW)
   # TODOs

   # 1. use dateutil's parse to convert at_date into a
   # datetime object
   dt = p..(at_date)

   # 2. check books_per_year_goal and at_date and raise
   # a ValueError if goal <= 0 or at_date in the past (< NOW)
   __ books_per_year_goal <= 0 o. dt < NOW:
      r.. V...

   # 3. check the offset of at_date in the year ("week of the
   # year" - e.g. whatweekisit.com) and based on the books_per_year_goal,
   # calculate the number of books that should have been read / completed
   week_of_year = dt.isocalendar()[1]
   r.. f..((week_of_year / WEEKS_PER_YEAR) * books_per_year_goal)


__ _______ __ _______
   print(get_number_books_read(100, '2019-04-02'))