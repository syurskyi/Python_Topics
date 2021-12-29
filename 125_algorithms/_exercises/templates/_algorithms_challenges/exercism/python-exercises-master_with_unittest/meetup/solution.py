from calendar import Calendar


___ meetup_day(year, month, day_of_the_week, which):
    candidates = [date
                  for date in Calendar().itermonthdates(year, month)
                  __ date.month == month
                  __ date.strftime('%A') == day_of_the_week]
    return _choice(which)(candidates)


___ _choice(which):
    __ which == 'teenth':
        return lambda dates: next(d for d in dates __ 13 <= d.day <= 19)

    ix = -1 __ (which == 'last') else (int(which[0]) - 1)
    return lambda dates: dates[ix]
