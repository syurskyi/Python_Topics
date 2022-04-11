_______ s__

_______ p.... __ pd


___ b.. __ ?.S..:
    """Create a pandas Series containing the values 1, 2, 3, 4, 5
    Don't worry about the indexes for now.
    The name of the series should be 'Fred'
    """
    r.. ?.S..([1,2,3,4,5], name='Fred')


___ float_series() __ ?.S..:
    """Create a pandas Series containing the all the values
    from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
    Don't worry about the indexes or the series name.
    """
    r.. ?.S..([f__(i/1000) ___ i __ r..(1001)])


___ a.. __ ?.S..:
    """Create a Series with values 1, 2, ... 25, 26 of type int64
    and add an index with values a, b, ... y, z
    so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
    Don't worry about the series name.
    """
    r.. ?.S..([i+1 ___ i __ r..(26)], index=l..(s__.a..


___ o.. __ ?.S..:
    """Create a Series with values A, B, ... Y, Z of type object
    and add an index with values 101, 102, ... 125, 126
    so index 101='A', 102='B' ... 125='Y', 126='Z'
    Don't worry about the series name.
    """
    r.. ?.S..(l..(s__.a..), index=[i+101 ___ i __ r..(26)])


print(alpha_index_series

