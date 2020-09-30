#!python3
#date_compare.py is a quick script to calculate how many days fall between two dates

from dateutil.parser ______ parse


___ date_entry(
    date1 = parse(input("Please enter the first date in format mm/dd/year:"))
    date2 = parse(input("Please enter the second date in format mm/dd/year:"))
    
    date1_date = date1.date()
    date2_date = date2.date()
    
    days = date_calc(date1_date, date2_date)
    r_ days

     
___ date_calc(d1, d2
    __ d1 > d2:
        days = d1 - d2
    ____
        days = d2 - d1
    r_ days  


__  -n __ "__main__":
    days = date_entry()
    print("\n %s day(s) between these two dates." % (days.days))