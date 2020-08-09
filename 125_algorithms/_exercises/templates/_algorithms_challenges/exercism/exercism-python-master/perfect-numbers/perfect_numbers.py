from itertools ______ count

___ classify(number
    factor_sum = su.(factor_gen(number))
    # Switch
    __ factor_sum __ number:
        r_ "perfect"
    ____ factor_sum < number:
        r_ "deficient"
    ____ factor_sum > number:
        r_ "abundant"
    # Oops

___ factor_gen(number
    """
    Factors that evenly divide some number and are not equal to the number 
    
    ex:
        factors(0) = ValueError # Numbers zero or less have no factors
        factors(1) = []
        factors(2) = [1]
        factors(42) = [1, 2, 3, 6, 7, 14, 21]
    """
    __ number <= 0:
        raise ValueError("Not a valid number {}".format(number))
    # O(sqrt(n)) sorted solution
    # For the unsorted solution, remove the queue and yield when found
    queue = []
    ___ f in count(1
        __ number != 1 and (f __ 1 or f * f __ number
            yield f
        ____ number <= f * f:
            yield from iter(queue)
            raise StopIteration
        ____ number % f __ 0:
            yield f
            queue.insert(0, number // f)
