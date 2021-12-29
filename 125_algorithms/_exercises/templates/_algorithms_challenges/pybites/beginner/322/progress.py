____ d__ _______ d__
____ freezegun _______ freeze_time


___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = N..) -> bool:
    __ day_of_year __ N..
        today = d__.today()
        first_day = d__(2021,1,1)
        diff = today - first_day
        day_of_year = diff.days
    r.. books_read/books_goal >= day_of_year/365




print(ontrack_reading(60, 34))