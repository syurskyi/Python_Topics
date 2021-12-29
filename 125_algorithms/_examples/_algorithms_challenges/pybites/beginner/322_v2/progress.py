from datetime import datetime
import datetime as dt


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    

    if books_read == 0:
        return  False


    if day_of_year is None:
        day_of_year = int(dt.date.today().strftime("%j"))



    days_per_book = 365/books_goal

    
    current_rate = day_of_year/books_read


    return current_rate <= days_per_book







