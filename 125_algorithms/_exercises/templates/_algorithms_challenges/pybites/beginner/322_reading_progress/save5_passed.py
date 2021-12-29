____ datetime _______ datetime

___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = N..) -> bool:
    today = datetime.now()
    day = [day_of_year __ day_of_year ____ int(today.strftime('%j'))][0]
    reading_speed = 365 / books_goal
    days_left = 365 - day
    books_left = books_goal - books_read
    __ books_left __ 0:
        r.. True
    r.. (days_left / books_left) > reading_speed