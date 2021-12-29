from datetime import date

from dateutil.rrule import rrule, WEEKLY, SU, MO, TU, WE, TH, FR

TODAY = date(year=2018, month=11, day=29)


___ get_hundred_weekdays(start_date=TODAY):
   """Return a list of hundred date objects starting from
      start_date up till 100 weekdays later, so +100 days
      skipping Saturdays and Sundays"""
   weekdays_100 = list(rrule(WEEKLY, count=100, wkst=SU, byweekday=(MO, TU, WE, TH, FR), dtstart=start_date))
   weekdays_100_date = [date(weekday.year, weekday.month, weekday.day) for weekday in weekdays_100]
   return weekdays_100_date


__ __name__ == "__main__":
   print(get_hundred_weekdays())