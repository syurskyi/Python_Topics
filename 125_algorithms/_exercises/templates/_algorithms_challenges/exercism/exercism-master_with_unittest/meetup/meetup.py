from calendar import Calendar


___ meetup_day(year, month, weekday, schedule):
    candidates = [date for date in Calendar().itermonthdates(year, month)
                  __ date.month == month and date.strftime('%A') == weekday]

    __ schedule == 'teenth':
        return find_teenth(candidates)
    else:
        return find(candidates, schedule)


___ find_teenth(candidates):
    for date in candidates:
        __ date.day >= 13 and date.day <= 19:
            return date


___ find(candidates, schedule):
    index = -1 __ schedule == 'last' else int(schedule[0]) - 1
    return candidates[index]
