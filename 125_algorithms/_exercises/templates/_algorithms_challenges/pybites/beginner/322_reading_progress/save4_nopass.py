____ d__ _______ d__

today = d__.today()

___ ontrack_reading(books_goal: i.., books_read: i..,
                    day_of_year: i.. = N..) __ bool:
    day = [day_of_year __ day_of_year ____ i..(today.strftime('%j'))][0]
    reading_speed = 365 / books_goal
    days_left = 365 - day
    books_left = books_goal - books_read
    __ books_left __ 0:
        r.. T..
    r.. (days_left / books_left) > reading_speed