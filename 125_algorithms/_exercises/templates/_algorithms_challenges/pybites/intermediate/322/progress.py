____ datetime _______ datetime


___ ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = N..) -> bool:

    days_in_year = 365
    
    __ day_of_year __ N..
        day_of_year = datetime.today().timetuple().tm_yday

    __ books_goal != books_read and books_read != 0:
        book_per_days = days_in_year / books_goal
        remaining_days = days_in_year - day_of_year

        __ (books_goal - books_read) * book_per_days < remaining_days :
            r.. True

    __ books_goal __ books_read and day_of_year <= days_in_year:
        r.. True

    r.. False


# if __name__ == "__main__":
#     print(ontrack_reading(60, 2, 3))
#     print(ontrack_reading(60, 0, 3))
#     print(ontrack_reading(60, 0.5, 3))
#     print(ontrack_reading(30, 16, 180))
#     print(ontrack_reading(30, 8, 180))