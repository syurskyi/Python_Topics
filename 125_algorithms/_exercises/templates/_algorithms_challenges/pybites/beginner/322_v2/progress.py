____ d__ _______ d__
_______ d__ as dt


___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = N..) -> bool:
    

    __ books_read __ 0:
        r..  False


    __ day_of_year __ N..
        day_of_year = int(dt.date.today().strftime("%j"))



    days_per_book = 365/books_goal

    
    current_rate = day_of_year/books_read


    r.. current_rate <= days_per_book







