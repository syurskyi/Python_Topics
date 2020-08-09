from calendar ______ Calendar


___ meetup_day(year, month, day_of_the_week, which
    candidates = [date
                  for date in Calendar().itermonthdates(year, month)
                  __ date.month __ month
                  __ date.strftime('%A') __ day_of_the_week]
    r_ _choice(which)(candidates)


___ _choice(which
    __ which __ 'teenth':
        r_ lambda dates: next(d for d in dates __ 13 <= d.day <= 19)

    ix = -1 __ (which __ 'last') else (int(which[0]) - 1)
    r_ lambda dates: dates[ix]
