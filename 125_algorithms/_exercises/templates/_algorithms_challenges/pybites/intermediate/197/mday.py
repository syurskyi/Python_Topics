from datetime import date


___ get_mothers_day_date(year):
   """Given the passed in year int, return the date Mother's Day
      is celebrated assuming it's the 2nd Sunday of May."""
   day_counter = 1
   mothers_day = date(year, 5, day_counter)

   sunday_count = 0
   while sunday_count < 2:
      __ mothers_day.weekday() == 6:
         sunday_count += 1
         day_counter += 1
      else:  
         day_counter += 1

      __ sunday_count == 2:
         break
      mothers_day = mothers_day.replace(day=day_counter)
   return mothers_day


# if __name__ == "__main__":
#    print(get_mothers_day_date(2014))