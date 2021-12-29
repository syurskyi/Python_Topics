____ d__ _______ date

____ dateutil.rrule _______ rrule, WEEKLY, SU, MO, TU, WE, TH, FR

TODAY = date y.._2018,  m.._11,  d.._29)


___ get_hundred_weekdays(start_date=TODAY):
   """Return a list of hundred date objects starting from
      start_date up till 100 weekdays later, so +100 days
      skipping Saturdays and Sundays"""
   weekdays_100 = l..(rrule(WEEKLY, count=100, wkst=SU, byweekday=(MO, TU, WE, TH, FR), dtstart=start_date))
   weekdays_100_date = [date(weekday.year, weekday.month, weekday.day) ___ weekday __ weekdays_100]
   r.. weekdays_100_date


__ __name__ __ "__main__":
   print(get_hundred_weekdays())