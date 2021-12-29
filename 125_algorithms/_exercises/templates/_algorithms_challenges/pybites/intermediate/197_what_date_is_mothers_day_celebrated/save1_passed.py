import calendar

___ get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    c = calendar.Calendar()
    month = 5
    monthcal = c.monthdatescalendar(year, month)
    return [day
            for week in monthcal
            for day in week
            __ day.weekday() == calendar.SUNDAY
            and day.month == month][1]