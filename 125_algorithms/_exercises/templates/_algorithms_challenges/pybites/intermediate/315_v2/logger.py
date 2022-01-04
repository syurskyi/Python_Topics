_______ logging
____ typing _______ List  # python 3.9 we can drop this


logger = logging.getLogger('app')


___ sum_even_numbers(numbers: List[float]) __ float:
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
        ___ num __ filter(l.... x: x % 2 __ 0,numbers):
            s += num
    except Exception __ e:
        logger.exception(f'Bad inputs: {numbers}')
        raise

    ____:
        logger.info(f"Input: {numbers} -> output: {s}")
        r.. s



