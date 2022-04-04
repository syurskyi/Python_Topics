____ f.. _______ wraps
____ time _______ time
____ typing _______ Deque, List, Set, Generator


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
___ contains(sequence: List[i..], num: i..) __ b..:
    ___ n __ sequence:
        __ n __ num:
            r.. T..
    r.. F..


@timing
___ contains_fast(sequence: Set[i..], num: i..) __ b..:
    __ num __ sequence:
        r.. T..
    r.. F..


@timing
___ ordered_list_max(sequence: List[i..]) __ i..:
    r.. m..(sequence)


@timing
___ ordered_list_max_fast(sequence: List[i..]) __ i..:
    r.. sequence[-1]


@timing
___ list_concat(sequence: List[s..]) __ s..:
    bigstr = ''
    ___ i __ sequence:
        bigstr += s..(i)
    r.. bigstr


@timing
___ list_concat_fast(sequence: List[s..]) __ s..:
    r.. ''.j..(sequence)


@timing
___ list_inserts(n: i..) __ List[i..]:
    lst: List[i..]    # list
    ___ i __ r..(n
        lst.insert(0, i)
    r.. lst


@timing
___ list_inserts_fast(n: i..) __ Deque[i..]:
    queue = Deque()
    ___ i __ r..(n
        queue.appendleft(i)
    r.. queue


@timing
___ list_creation(n: i..) __ List[i..]:
    lst    # list
    ___ i __ r..(n
        lst.a..(i)
    r.. lst


@timing
___ list_creation_fast(n: i..) __ Generator[i.., N.., N..]:
    ___ i __ r..(n
        y.. i