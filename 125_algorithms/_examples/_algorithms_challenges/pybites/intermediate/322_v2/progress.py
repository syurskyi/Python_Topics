from datetime import datetime
from datetime import timedelta


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:

    year = datetime.today().year
    boy = datetime(year, 1, 1)
    eoy = datetime(year, 12, 31)

    if day_of_year:
        today = boy + timedelta(days=day_of_year-1)
    else:
        today = datetime.today()

    days_left = (eoy - today).days
    books_left = books_goal - books_read

    if books_read > 0:
        # use current reading rate
        read_rate = books_read / (today - boy).days
    else:
        # otherwise assume a reasonable reading goal
        read_rate = books_goal / 365

    print(f'{books_left=}, {days_left=}')
    return True if books_left == 0 else books_left / read_rate <= days_left
