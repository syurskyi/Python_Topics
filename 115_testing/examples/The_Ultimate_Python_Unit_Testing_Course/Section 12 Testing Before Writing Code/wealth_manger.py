"""
@author: Mohammad Mahjoub
@date: May, 25, 2018
This class is going to calculate how many years will it take to generate passive for a given income from renting apts.
"""
import math


class Calculator:
    def __init__(self, passive_income_desired_yearly, yearly_savings, starting_year,
                 price_of_one_apt, price_of_renting_one_apt):
        if isinstance(starting_year, int):
            self._passive_income_desired_yearly = passive_income_desired_yearly
            self._yearly_savings = yearly_savings
            self._starting_year = starting_year
            self._years_needed = starting_year
            self._price_of_one_apt = price_of_one_apt
            self._price_of_renting_one_apt = price_of_renting_one_apt
            self._answer = dict()
            self._calculate()
        else:
            raise TypeError("Make sure that the year input is an integer")    
            
    """
        @:arg This method has no arguments
    """
    def _calculate(self):
        apt_number_owned = 0
        income_reached = 0
        while self._passive_income_desired_yearly >= (apt_number_owned * self._price_of_renting_one_apt):
            frac, whole = math.modf((self._yearly_savings + income_reached) / self._price_of_one_apt)
            if whole > 0:
                income_reached += self._yearly_savings
                income_reached -= whole * self._price_of_one_apt  # pay for many apartment
                apt_number_owned += whole  # own the apt.
                income_reached += (apt_number_owned * self._price_of_renting_one_apt)
            else:
                income_reached += self._yearly_savings
                income_reached += (apt_number_owned * self._price_of_renting_one_apt)
            
            self._answer[self._starting_year] = [apt_number_owned, round(income_reached)]
            self._starting_year += 1
        
    def get_years_needed(self):
        return self._starting_year - self._years_needed

    def get_results(self):
        return self._answer
    
    def get_apartments_needed(self):
        key = max(self._answer, key=int)  # get the greatest key in the self._answer dictionary.
        value = self._answer[key]  # get the value of the greatest key in the self._answer dictionary.
        number_of_apartments = value[0]  # get the greatest
        return number_of_apartments
    
    def get_net_worth(self):
        return self.get_apartments_needed() * self._price_of_one_apt
    
    def print_results(self):
        print("The passive income desired yearly is ${0}, "
              "the yearly investments is ${1}, "
              "the price of every apt is ${2}, "
              "the price for renting every apt is ${3},"
              " the net worth is ${4}"
              .format(self._passive_income_desired_yearly, self._yearly_savings, self._price_of_one_apt,
                      self._price_of_renting_one_apt, self.get_net_worth()))
        for k, v in self._answer.items():
            print("Year number: {0}, Apt number owned {1} Passive Income ${2}"
                  .format(k, v[0], round(v[1])))
        print("You can reach a passive income of ${0}, but it will take: {1} years"
              .format(self._passive_income_desired_yearly, self._starting_year - self._years_needed))
        print("You have to invest ${0} every year ".format(self._yearly_savings))
        print("")



