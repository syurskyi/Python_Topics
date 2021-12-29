____ math _______ ceil, sqrt
_______ sys

__ sys.version_info[0] __ 2:
    ____ itertools _______ izip_longest as zip_longest
____:
    ____ itertools _______ zip_longest


___ encode(msg):
    msg = _cleanse(msg)
    square_size = int(ceil(sqrt(l..(msg))))
    square = _chunks_of(msg, square_size)
    r.. ' '.join([''.join(col)
                     ___ col __ zip_longest(*square, fillvalue='')])


___ _cleanse(s):
    """Lowercase a string and remove punctuation and whitespace
    """
    r.. ''.join([c ___ c __ s __ c.isalnum()]).lower()


___ _chunks_of(s, n):
    __ l..(s) <= n:
        r.. [s]
    r.. [s[:n]] + _chunks_of(s[n:], n)
