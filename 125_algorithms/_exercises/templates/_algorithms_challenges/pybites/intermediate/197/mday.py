____ d__ _______ date


___ get_mothers_day_date(year
   """Given the passed in year int, return the date Mother's Day
      is celebrated assuming it's the 2nd Sunday of May."""
   day_counter = 1
   mothers_day = date(year, 5, day_counter)

   sunday_count = 0
   w.... sunday_count < 2:
      __ mothers_day.weekday() __ 6:
         sunday_count += 1
         day_counter += 1
      ____:
         day_counter += 1

      __ sunday_count __ 2:
         _____
      mothers_day = mothers_day.r..( d.._day_counter)
   r.. mothers_day


# if __name__ == "__main__":
#    print(get_mothers_day_date(2014))