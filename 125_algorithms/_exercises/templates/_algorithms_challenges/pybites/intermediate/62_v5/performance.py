____ f.. _______ wraps
____ t___ _______ L.., S..

____ time _______ time


___ timing(f
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""

    @wraps(f)
    ___ wrapper $ $$:
        start = time()
        result = f $ $$
        end = time()
        duration = end - start
        print _*Elapsed time {f.__name__}: {duration}')
        r.. duration, result

    r.. wrapper


@timing
___ contains(sequence: L..[i..], num: i..) __ b..:
    ___ n __ sequence:
        __ n __ num:
            r.. T..
    r.. F..


@timing
___ contains_fast(sequence: S..[i..], num: i..) __ b..:
    r.. num __ sequence


@timing
___ ordered_list_max(sequence: L..[i..]) __ i..:
    r.. m..(sequence)


@timing
___ ordered_list_max_fast(sequence: L..[i..]) __ i..:
    r.. sequence[-1]


@timing
___ list_concat(sequence: L..[s..]) __ s..:
    bigstr = ''
    ___ i __ sequence:
        bigstr += s..(i)
    r.. bigstr


@timing
___ list_concat_fast(sequence: L..[s..]) __ s..:
    r.. ''.j..(sequence)


@timing
___ list_inserts(n: i..) __ L..[i..]:
    lst    # list
    ___ i __ r..(n
        lst.insert(0, i)
    r.. lst


@timing
___ list_inserts_fast(n: i..) __ L..[i..]:
    r.. [v ___ v __ r..(n)][::-1]


@timing
___ list_creation(n: i..) __ L..[i..]:
    lst    # list
    ___ i __ r..(n
        lst.a..(i)
    r.. lst


@timing
___ list_creation_fast(n: i..
    y.. ____ (v ___ v __ r..(n))
