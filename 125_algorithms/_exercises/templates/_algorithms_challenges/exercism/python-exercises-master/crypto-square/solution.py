from ma__ ______ ceil, sqrt
______ sys

__ sys.version_info[0] __ 2:
    from itertools ______ izip_longest as zip_longest
____
    from itertools ______ zip_longest


___ encode(msg
    msg = _cleanse(msg)
    square_size = int(ceil(sqrt(le.(msg))))
    square = _chunks_of(msg, square_size)
    r_ ' '.join([''.join(col)
                     for col in zip_longest(*square, fillvalue='')])


___ _cleanse(s
    """Lowercase a string and remove punctuation and whitespace
    """
    r_ ''.join([c for c in s __ c.isalnum()]).lower()


___ _chunks_of(s, n
    __ le.(s) <= n:
        r_ [s]
    r_ [s[:n]] + _chunks_of(s[n:], n)
