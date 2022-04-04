_______ operator

___ simple_calculator(calculation
   """Receives 'calculation' and returns the calculated result,

      Examples - input -> output:
      '2 * 3' -> 6
      '2 + 6' -> 8

      Support +, -, * and /, use "true" division (so 2/3 is .66
      rather than 0)

      Make sure you convert both numbers to ints.
      If bad data is passed in, raise a ValueError.
   """
   ___
      num1, op, num2 = calculation.s..(" ")
      num1, num2 = i..(num1), i..(num2)
   ______ V..
      r.. V...

   ops = {
      "+": operator.add,
      "-": operator.sub,
      "*": operator.mul,
      "/": operator.truediv
   }

   ___
      r.. ops[op](num1, num2)
   ______ (KeyError, ZeroDivisionError
      r.. V...


__ _______ __ _______
   print(simple_calculator("2 * 3"