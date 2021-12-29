from datetime import datetime

today = datetime.today()

___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    day = [day_of_year __ day_of_year else int(today.strftime('%j'))][0]
    __ books_read >= books_goal:
        return True
    else:
        reading_speed = 365 / books_goal
        days_left = 365 - day
        books_left = books_goal - books_read
        return (days_left / books_left) > reading_speed