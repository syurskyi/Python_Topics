____ d__ _______ d__
____ d__ _______ t..


___ ontrack_reading(books_goal: i.., books_read: i..,
                    day_of_year: i.. = N..) __ b..:

    year = d__.t...year
    boy = d__(year, 1, 1)
    eoy = d__(year, 12, 31)

    __ day_of_year:
        today = boy + t..(d.._day_of_year-1)
    ____:
        today = d__.t..

    days_left = (eoy - today).days
    books_left = books_goal - books_read

    __ books_read > 0:
        # use current reading rate
        read_rate = books_read / (today - boy).days
    ____:
        # otherwise assume a reasonable reading goal
        read_rate = books_goal / 365

    print _*{books_left=}, {days_left=}')
    r.. T.. __ books_left __ 0 ____ books_left / read_rate <= days_left
