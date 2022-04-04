_______ logging
____ t___ _______ List  # python 3.9 we can drop this


logger = logging.getLogger('app')


___ sum_even_numbers(numbers: List[f__]) __ f__:
   """
   1. Of the numbers passed in sum the even ones
      and return the result.
   2. If all goes well log an INFO message:
      Input: {numbers} -> output: {ret}
   3. If bad inputs are passed in
      (e.g. one of the numbers is a str), catch
      the exception log it, then reraise it.
   """
   even_numbers    # list
   ___ number __ numbers:
      ___
         __ number % 2 __ 0:
            even_numbers.a..(number)
      ______ T..:
         logger.exception(f"Bad inputs: {numbers}")
         r..

   total = s..(even_numbers)
   logger.info(f"Input: {numbers} -> output: {total}")
   r.. total