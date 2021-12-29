"""Tax Bracket Calculator

Here is the break-down on how much a US citizen's income was
taxed in 2019

      $0 - $9,700   10%
  $9,701 - $39,475  12%
 $39,476 - $84,200  22%
 $84,201 - $160,725 24%
$160,726 - $204,100 32%
$204,101 - $510,300 35%
$510,301 +          37%

For example someone earning $40,000 would
pay $4,658.50, not $40,000 x 22% = $8,800!

    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50

More detail can be found here:
https://www.nerdwallet.com/blog/taxes/federal-income-tax-brackets/

Sample output from running the code in the if/main clause:

          Summary Report
==================================
 Taxable Income:        40,000.00
     Taxes Owed:         4,658.50
       Tax Rate:           11.65%

         Taxes Breakdown
==================================
    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50
"""
from dataclasses import dataclass, field
from typing import List, NamedTuple

Bracket = NamedTuple("Bracket", [("end", int), ("rate", float)])
Taxed = NamedTuple("Taxed", [("amount", float), ("rate", float), ("tax", float)])
BRACKET = [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]


class Taxes:
    """Taxes class

    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.

    """

    OUTPUT_WIDTH = 34

    ___ __init__(self,salary,bracket=BRACKET):
        self.salary = salary
        self.income = salary
        self.bracket = bracket
        self.taxes_owed = self.taxes


    ___ __str__(self) -> str:
        """Summary Report

        Returns:
            str -- Summary report

            Example:

                      Summary Report          
            ==================================
             Taxable Income:        40,000.00
                 Taxes Owed:         4,658.50
                   Tax Rate:           11.65%
        """
        n= 34


        s = f"{'Summary Report':^34}\n"

        s += '=' * 34 + '\n'

        values = [("Taxable Income:",f"{self.salary:,.2f}"),("Taxes Owed:",f"{self.taxes:,.2f}"),("Tax Rate:",f"{self.tax_rate:.2f}%")]

        largest_left_length = len(values[0][0]) + 1
        largest_right_length = len(str(int(self.salary))) + 4
        spaces = 32 - (largest_left_length + largest_right_length)

        for i,(string,value) in enumerate(values,1):
            t = ' ' * spaces
            s += f' {string:>{largest_left_length}}{t}{value:>{largest_right_length}}\n'

        return s





        



    ___ report(self):
        """Prints taxes breakdown report"""
        print(self)


        print(f"{'Taxes Breakdown':^{self.OUTPUT_WIDTH}}")
        print("=" * self.OUTPUT_WIDTH)

        largest_amount = largest_tax =  float("-inf")
        for amount,rate,tax in self.tax_amounts:
            largest_amount = max(largest_amount,int(amount))
            largest_tax = max(largest_tax,int(tax))
    
        
        largest_amount = len(str(largest_amount))
        largest_amount += 16
        largest_tax = len(str(largest_tax))
        largest_tax += 4

        middle = self.OUTPUT_WIDTH - 3 - (largest_amount + 11) - (largest_tax + 4)
        spaces = ' ' * 5
        for amount,rate,tax in self.tax_amounts:
            left_string = f"{amount:,.2f} x {rate:.2f} ="
            print(f"{left_string:>{largest_amount}}{spaces}{tax:>{largest_tax},.2f}")
        
        print('-' *self.OUTPUT_WIDTH)


        print(f"{'Total =':>{largest_amount}}{spaces}{self.taxes_owed:>{largest_tax},.2f}")

        


    @property
    ___ taxes(self) -> float:
        """Calculates the taxes owed

        As it's calculating the taxes, it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        self.tax_amounts = []
        self.taxes_owed =0 
        
        value = self.salary
        previous_end = 0
        leave = False
        for end,rate in self.bracket:
            __ value >= end:
                tax_paid = end - previous_end
            else:
                tax_paid = value - previous_end
                leave = True
            

            tax_owed = tax_paid * rate
            #value -= tax_owed
            self.taxes_owed += tax_owed
            tax_amount = Taxed(tax_paid,rate,tax_owed)
            self.tax_amounts.append(tax_amount)
            previous_end = end
            __ leave:
                break




        return self.taxes_owed



    @property
    ___ total(self) -> float:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """
        return self.taxes_owed

    @property
    ___ tax_rate(self) -> float:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        return round(self.taxes_owed / self.salary * 100,2)


__ __name__ == "__main__":
    salary = 40_000
    t = Taxes(salary)
    print(t)
    t.report()
