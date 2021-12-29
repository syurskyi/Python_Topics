_______ operator

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
   try:
      num1, op, num2 = calculation.split(" ")
      num1, num2 = int(num1), int(num2)
   except ValueError:
      raise ValueError

   ops = {
      "+": operator.add,
      "-": operator.sub,
      "*": operator.mul,
      "/": operator.truediv
   }

   try:
      r.. ops[op](num1, num2)
   except (KeyError, ZeroDivisionError):
      raise ValueError


__ __name__ __ "__main__":
   print(simple_calculator("2 * 3"))