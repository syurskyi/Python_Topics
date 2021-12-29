_______ calendar
____ datetime _______ date


___ weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    bday_weekday = calendar.weekday(date.year, date.month, date.day)
    weekdays = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}
    r.. weekdays[bday_weekday]