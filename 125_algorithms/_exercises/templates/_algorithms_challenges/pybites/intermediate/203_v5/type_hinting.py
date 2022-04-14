____ dataclasses _______ dataclass


@dataclass
c_ Employee:
    """Simple Employee class

    :param first_name: String of first name
    :param last_name: String of last name
    :param days_of_week: Integer of how many days per week worked
    :param hours_per_day: Float of hours worked per day
    :param wage: Float of hourly pay
    :param weekly_pay: Property which returns a string for weekly pay
    """
    first_name: s..
    last_name: s..
    days_per_week: i..
    hours_per_day: f__
    wage: f__

    # def __init__(self, first_name: str, last_name: str, days_per_week: int,
    #              hours_per_day: float, wage: float):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.days_per_week = days_per_week
    #     self.hours_per_day = hours_per_day
    #     self.wage = wage

    ___ _rounder  number: f__, places: i..) __ s..
        """Rounds a number the specified number of places

        :param number: Float of number of round
        :param places: Integer of places to round to
        :return: String representation of the rounded number in US $
        """
        amount r..(number, places)
        r.. f"${amount:0.2f}"

    $
    ___ weekly_pay(self) __ s..
        """Returns amount of weekly pay in US currency

        For instance: $250.75
        """
        total_hours hours_per_day * days_per_week
        total_wage total_hours * wage
        r.. _rounder(total_wage, 2)


__ _______ __ _______
    coder Employee("Joe", "Blow", 5, 8, 18.0)
    print(coder.weekly_pay)
