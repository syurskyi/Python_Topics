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

    s = 0
    
    try:
        for num in filter(lambda x: x % 2 == 0,numbers):
            s += num
    except Exception as e:
        logger.exception(f'Bad inputs: {numbers}')
        raise

    else:
        logger.info(f"Input: {numbers} -> output: {s}")
        return s



