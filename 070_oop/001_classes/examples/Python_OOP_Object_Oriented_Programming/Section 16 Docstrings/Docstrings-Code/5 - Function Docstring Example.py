def frequency_dict(data):
    """Return a dictionary with the number of occurences of each value in the list.

    Create a dictionary that maps each element of the list (key)
    to the number of times if occurs in the list (value).

    Args:
        data: A list of values of an immutable data type.
            These values can be integers, booleans, tuples, or strings.

    Return:
        A dictionary mapping each value (key) with its frequency.
        For example, this function call:

        a = [1, 6, 2, 6, 2]

        returns this dictionary:

        {1:1, 6:2, 2:2}

    Raise:
        ValueError: if the list is empty.
    """
    if not data:
        raise ValueError("The list cannot be empty")
    
    freq = {}
    
    for elem in data:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1

    return freq
