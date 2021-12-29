from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:

    days_in_year = 365
    
    if day_of_year == None:
        day_of_year = datetime.today().timetuple().tm_yday

    if books_goal != books_read and books_read != 0:
        book_per_days = days_in_year / books_goal
        remaining_days = days_in_year - day_of_year

        if (books_goal - books_read) * book_per_days < remaining_days :
            return True

    if books_goal == books_read and day_of_year <= days_in_year:
        return True

    return False


# if __name__ == "__main__":
#     print(ontrack_reading(60, 2, 3))
#     print(ontrack_reading(60, 0, 3))
#     print(ontrack_reading(60, 0.5, 3))
#     print(ontrack_reading(30, 16, 180))
#     print(ontrack_reading(30, 8, 180))