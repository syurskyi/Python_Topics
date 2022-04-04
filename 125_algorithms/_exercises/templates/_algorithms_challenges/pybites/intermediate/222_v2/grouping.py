_______ types
____ i.. _______ islice


___ group(iterable, n
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """

    results    # list
    iterable = l..(iterable)
    ___ i __ r..(0,l..(iterable),n
        results.a..(l..(islice(iterable,i,i+n)))

    r.. results



    r.. l..(islice(iterable,0,l..(iterable),n


__ _____ __ _____
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)
