_______ datetime


___ print_header():
    print('---------------------------')
    print('      BIRTHDAY APP')
    print('---------------------------')
    print()


___ get_birthday_from_user():
    print("When were you born? ")
    year  i..(input("Year [YYYY]: "))
    month  i..(input("Month [MM]: "))
    day  i..(input("Day [DD]: "))

    birthday  datetime.date(year, month, day)
    r.. birthday


___ compute_days_between_dates(original_date, target_date):
    this_year  datetime.date(target_date.year, original_date.month, original_date.day)

    dt  this_year - target_date
    r.. dt.days


___ print_birthday_information(days):
    __ days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    ____ days > 0:
        print("Your birthday is in {} days!".format(days))
    ____:
        print("Happy birthday!!!")


___ main():
    print_header()
    bday  get_birthday_from_user()
    today  datetime.date.today()
    number_of_days  compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
