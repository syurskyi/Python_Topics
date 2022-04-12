____ ca__ _______ Calendar


___ meetup_day(year, month, day_of_the_week, which
    candidates [date
                  ___ date __ Calendar().itermonthdates(year, month)
                  __ date.month __ month
                  __ date.s..('%A') __ day_of_the_week]
    r.. _choice(which)(candidates)


___ _choice(which
    __ which __ 'teenth':
        r.. l.... dates: next(d ___ d __ dates __ 13 <_ d.day <_ 19)

    ix -1 __ (which __ 'last') ____ (i..(which 0 - 1)
    r.. l.... dates: dates[ix]
