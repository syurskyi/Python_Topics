"""
Happy New Year! How many books do you aim to read this year?

In this Bite you will complete ontrack_reading that takes the amount of books you want to read (books_goal),
the amount of books read (books_read) and the day of the year (day_of_year, if None or not provided,
it defaults to today, that is the offset in days into the year right now).
The function returns a bool signifying if you are on track or not.

Here is how it works in the REPL:

>>> from progress import ontrack_reading
>>> ontrack_reading(60, 0, 3)
False
>>> ontrack_reading(60, 0)  # same as previous statement, today = 3rd of Jan
False
>>> ontrack_reading(60, 1, 3)
True
>>> ontrack_reading(10, 10, 365)
True
Note: you need to pip install freezegun if you want to run the tests locally.
"""

from datetime import datetime

def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    pass
