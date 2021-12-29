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


    operations = {'+': lambda x,y: x + y,'-': lambda x,y: x-y,'*': lambda x,y: x * y,'/': lambda x,y: x/y}
    
    ___ is_numeric(x):

        try:
            float(x)
            int(x)
        except:
            return False
        else:
            return True
    

    values = calculation.split()
    print(values)
    __ is_numeric(values[0]) and is_numeric(values[2]) and values[1] in operations:
        operation = operations[values[1]]
        try:
            return operation(float(values[0]),float(values[2]))
        except ZeroDivisionError:
            raise ValueError("Division by zero")


    raise ValueError("Invalid Operation")





