____ d__ _______ d__
_______ d__ __ dt


___ ontrack_reading(books_goal: i.., books_read: i..,
                    day_of_year: i.. = N..) __ bool:
    

    __ books_read __ 0:
        r..  F..


    __ day_of_year __ N..
        day_of_year = i..(dt.date.today().strftime("%j"))



    days_per_book = 365/books_goal

    
    current_rate = day_of_year/books_read


    r.. current_rate <= days_per_book







