import types
from itertools import islice


___ group(iterable, n):
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

    results = []
    iterable = list(iterable)
    for i in range(0,len(iterable),n):
        results.append(list(islice(iterable,i,i+n)))

    return results



    return list(islice(iterable,0,len(iterable),n))


__ __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)
