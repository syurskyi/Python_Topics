___ simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

    
    
       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """


    operations = {'+': l.... x,y: x + y,'-': l.... x,y: x-y,'*': l.... x,y: x * y,'/': l.... x,y: x/y}
    
    ___ is_numeric(x):

        try:
            float(x)
            i..(x)
        except:
            r.. F..
        ____:
            r.. T..
    

    values = calculation.s..
    print(values)
    __ is_numeric(values[0]) a.. is_numeric(values[2]) a.. values[1] __ operations:
        operation = operations[values[1]]
        try:
            r.. operation(float(values[0]),float(values[2]))
        except ZeroDivisionError:
            raise ValueError("Division by zero")


    raise ValueError("Invalid Operation")





