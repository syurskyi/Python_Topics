import types
from itertools import islice


def group(iterable, n):
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

    if not isinstance(iterable, types.GeneratorType):
      input = (ele for ele in iterable)
    else:
      input = iterable

    result = []
    while True:
      section = list(islice(input, n))
      if section:
        result.append(section)
      else:
        break

    return result