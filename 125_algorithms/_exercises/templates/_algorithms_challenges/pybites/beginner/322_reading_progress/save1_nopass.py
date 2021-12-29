____ d__ _______ d__

today = d__.today()

___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = N..) -> bool:
        day = [day_of_year 
        __ day_of_year ____ today.timetuple().tm_yday][0]
    __ books_read >= books_goal:
        r.. True
    ____:
        reading_speed = 365 / books_goal
        days_left = 365 - day
        books_left = books_goal - books_read
        r.. (days_left / books_left) > reading_speed