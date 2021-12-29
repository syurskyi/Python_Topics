import calendar
#from datetime import date

#weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    #return weekdays[calendar.weekday(date.year, date.month, date.day)]
    return calendar.day_name[date.weekday()]


#print(weekday_of_birth_date(date(1965, 4, 4)))