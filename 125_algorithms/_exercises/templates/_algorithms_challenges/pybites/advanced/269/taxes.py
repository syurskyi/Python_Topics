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
____ d.. _______ d__ f__
____ t___ _______ L.., N..

Bracket N..("Bracket", [("end", i..), ("rate", f__)])
Taxed N..("Taxed", [("amount", f__), ("rate", f__), ("tax", f__)])
BRACKET [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]


c_ Taxes:
    """Taxes class

    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.

    """

    OUTPUT_WIDTH 34

    ___ - ,salary,bracket=BRACKET
        salary salary
        income salary
        bracket bracket
        taxes_owed taxes


    ___ -s ____ __ s..
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


        s f"{'Summary Report':^34}\n"

        s += '=' * 34 + '\n'

        values [("Taxable Income:",f"{salary:,.2f}"),("Taxes Owed:",f"{taxes:,.2f}"),("Tax Rate:",f"{tax_rate:.2f}%")]

        largest_left_length l..(values 0 0 ) + 1
        largest_right_length l..(s..(i..(salary))) + 4
        spaces 32 - (largest_left_length + largest_right_length)

        ___ i,(s__,value) __ e..(values,1
            t ' ' * spaces
            s += f' {s__:>{largest_left_length}}{t}{value:>{largest_right_length}}\n'

        r.. s





        



    ___ report
        """Prints taxes breakdown report"""
        print ____


        print(f"{'Taxes Breakdown':^{OUTPUT_WIDTH}}")
        print("=" * OUTPUT_WIDTH)

        largest_amount largest_tax =  f__("-inf")
        ___ amount,rate,tax __ tax_amounts:
            largest_amount m..(largest_amount,i..(amount
            largest_tax m..(largest_tax,i..(tax
    
        
        largest_amount l..(s..(largest_amount
        largest_amount += 16
        largest_tax l..(s..(largest_tax
        largest_tax += 4

        middle OUTPUT_WIDTH - 3 - (largest_amount + 11) - (largest_tax + 4)
        spaces ' ' * 5
        ___ amount,rate,tax __ tax_amounts:
            left_string f"{amount:,.2f} x {rate:.2f} ="
            print(f"{left_string:>{largest_amount}}{spaces}{tax:>{largest_tax},.2f}")
        
        print('-' *OUTPUT_WIDTH)


        print(f"{'Total =':>{largest_amount}}{spaces}{taxes_owed:>{largest_tax},.2f}")

        


    $
    ___ taxes ____ __ f__:
        """Calculates the taxes owed

        As it's calculating the taxes, it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        tax_amounts    # list
        taxes_owed =0
        
        value salary
        previous_end 0
        leave F..
        ___ end,rate __ bracket:
            __ value >_ end:
                tax_paid end - previous_end
            ____
                tax_paid value - previous_end
                leave T..
            

            tax_owed tax_paid * rate
            #value -= tax_owed
            taxes_owed += tax_owed
            tax_amount Taxed(tax_paid,rate,tax_owed)
            tax_amounts.a..(tax_amount)
            previous_end end
            __ leave:
                _____




        r.. taxes_owed



    $
    ___ total ____ __ f__:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """
        r.. taxes_owed

    $
    ___ tax_rate ____ __ f__:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        r.. r..(taxes_owed / salary * 100,2)


__ _______ __ _______
    salary 40_000
    t Taxes(salary)
    print(t)
    t.report()
