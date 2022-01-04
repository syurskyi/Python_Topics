____ c.. _______ Counter
___ major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """


    counts = Counter(numbers)


    x =  counts.most_common()

    major = x[0][0]
    minor = x[-1][0]



    r.. major, minor
