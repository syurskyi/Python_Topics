from calendar ______ Calendar


___ meetup_day(year, month, weekday, schedule
    candidates = [date ___ date in Calendar().itermonthdates(year, month)
                  __ date.month __ month and date.strftime('%A') __ weekday]

    __ schedule __ 'teenth':
        r_ find_teenth(candidates)
    ____
        r_ find(candidates, schedule)


___ find_teenth(candidates
    ___ date in candidates:
        __ date.day >= 13 and date.day <= 19:
            r_ date


___ find(candidates, schedule
    index = -1 __ schedule __ 'last' else int(schedule[0]) - 1
    r_ candidates[index]
