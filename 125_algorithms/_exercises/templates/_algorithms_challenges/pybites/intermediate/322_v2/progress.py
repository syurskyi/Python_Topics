____ d__ _______ d__
____ d__ _______ t..


___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = N..) -> bool:

    year = d__.today().year
    boy = d__(year, 1, 1)
    eoy = d__(year, 12, 31)

    __ day_of_year:
        today = boy + t..(days=day_of_year-1)
    ____:
        today = d__.today()

    days_left = (eoy - today).days
    books_left = books_goal - books_read

    __ books_read > 0:
        # use current reading rate
        read_rate = books_read / (today - boy).days
    ____:
        # otherwise assume a reasonable reading goal
        read_rate = books_goal / 365

    print(f'{books_left=}, {days_left=}')
    r.. True __ books_left __ 0 ____ books_left / read_rate <= days_left
