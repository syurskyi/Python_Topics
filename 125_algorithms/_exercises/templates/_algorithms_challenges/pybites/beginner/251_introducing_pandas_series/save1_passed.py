_______ s__
_______ pandas __ pd


___ basic_series() __ pd.Series:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    r.. pd.Series([1, 2, 3, 4, 5], name='Fred')


___ float_series() __ pd.Series:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    r.. pd.Series([x/1000 ___ x __ r..(1001)])

___ alpha_index_series() __ pd.Series:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    alphabet    # list
    numbers    # list
    ___ letter __ r..(97, 123
        alphabet.a..(chr(letter
    ___ number __ r..(1, 27
        numbers.a..(number)
    r.. pd.Series(numbers, index=alphabet)


___ object_values_series() __ pd.Series:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    alphabet    # list
    numbers =[]
    ___ letter __ r..(65, 91
        alphabet.a..(chr(letter
    ___ number __ r..(101, 127
        numbers.a..(number)
    r.. pd.Series(alphabet, index=numbers)