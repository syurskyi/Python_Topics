____ collections _______ Counter

___ major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    r.. Counter(numbers).most_common()[0][0], Counter(numbers).most_common()[-1][0]