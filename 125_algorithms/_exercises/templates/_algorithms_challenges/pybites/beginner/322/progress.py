from datetime import datetime
from freezegun import freeze_time


___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    __ day_of_year is None:
        today = datetime.today()
        first_day = datetime(2021,1,1)
        diff = today - first_day
        day_of_year = diff.days
    return books_read/books_goal >= day_of_year/365




print(ontrack_reading(60, 34))