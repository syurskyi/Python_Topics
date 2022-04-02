____ d__ _______ d__
____ freezegun _______ freeze_time


___ ontrack_reading(books_goal: i.., books_read: i..,
                    day_of_year: i.. = N..) __ b..:
    __ day_of_year __ N..
        today = d__.today()
        first_day = d__(2021,1,1)
        diff = today - first_day
        day_of_year = diff.days
    r.. books_read/books_goal >= day_of_year/365




print(ontrack_reading(60, 34))