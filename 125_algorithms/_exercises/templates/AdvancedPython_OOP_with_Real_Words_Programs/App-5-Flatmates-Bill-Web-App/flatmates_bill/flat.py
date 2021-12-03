c_ Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """

    ___  -    amount, period):
        amount = amount
        period = period


c_ Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    ___  -    name, days_in_house):
        name = name
        days_in_house = days_in_house

    ___ pays   bill, flatmate2):
        weight = days_in_house / (days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        r_ to_pay