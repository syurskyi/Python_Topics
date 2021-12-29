from datetime import datetime

today = datetime.today()

def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    day = [day_of_year if day_of_year else int(today.strftime('%j'))][0]
    reading_speed = 365 / books_goal
    days_left = 365 - day
    books_left = books_goal - books_read
    if books_left == 0:
        return True
    return (days_left / books_left) > reading_speed