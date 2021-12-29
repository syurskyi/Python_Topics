____ calendar _______ Calendar


___ meetup_day(year, month, weekday, schedule):
    candidates = [date ___ date __ Calendar().itermonthdates(year, month)
                  __ date.month __ month and date.strftime('%A') __ weekday]

    __ schedule __ 'teenth':
        r.. find_teenth(candidates)
    ____:
        r.. find(candidates, schedule)


___ find_teenth(candidates):
    ___ date __ candidates:
        __ date.day >= 13 and date.day <= 19:
            r.. date


___ find(candidates, schedule):
    index = -1 __ schedule __ 'last' ____ int(schedule[0]) - 1
    r.. candidates[index]
