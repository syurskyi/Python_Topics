____ d__ _______ d__


___ ontrack_reading(books_goal: i.., books_read: i..,
                    day_of_year: i.. N..) __ b..:

    days_in_year 365
    
    __ day_of_year __ N..
        day_of_year d__.t...t.. .tm_yday

    __ books_goal !_ books_read a.. books_read !_ 0:
        book_per_days days_in_year / books_goal
        remaining_days days_in_year - day_of_year

        __ (books_goal - books_read) * book_per_days < remaining_days :
            r.. T..

    __ books_goal __ books_read a.. day_of_year <_ days_in_year:
        r.. T..

    r.. F..


# if __name__ == "__main__":
#     print(ontrack_reading(60, 2, 3))
#     print(ontrack_reading(60, 0, 3))
#     print(ontrack_reading(60, 0.5, 3))
#     print(ontrack_reading(30, 16, 180))
#     print(ontrack_reading(30, 8, 180))