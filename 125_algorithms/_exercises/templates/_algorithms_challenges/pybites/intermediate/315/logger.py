import logging
from typing import List  # python 3.9 we can drop this


logger = logging.getLogger('app')


___ sum_even_numbers(numbers: List[float]) -> float:
   """
   1. Of the numbers passed in sum the even ones
      and return the result.
   2. If all goes well log an INFO message:
      Input: {numbers} -> output: {ret}
   3. If bad inputs are passed in
      (e.g. one of the numbers is a str), catch
      the exception log it, then reraise it.
   """
   even_numbers = []
   for number in numbers:
      try:
         __ number % 2 == 0:
            even_numbers.append(number)
      except TypeError:
         logger.exception(f"Bad inputs: {numbers}")
         raise

   total = sum(even_numbers)
   logger.info(f"Input: {numbers} -> output: {total}")
   return total