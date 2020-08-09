gestures = ['wink', 'double blink', 'close your eyes', 'jump']


___ handshake(s
    s = list(sanitize(s))
    s.reverse()
    seq = []
    lim = le.(s) __ le.(s) <= le.(gestures) else le.(gestures)
    ___ i1 in range(lim
        __ s[i1] __ '1':
            seq.append(gestures[i1])
    __ le.(s) __ 5:
        seq.reverse()
    r_ seq


___ code(seq
    __ not seq or set(seq) - set(gestures
        r_ '0'
    s = find_subseq(seq)
    __ not s:
        s = ['1'] + find_subseq(reversed(seq))
    r_ "".join(s)


___ sanitize(s
    __ not(isinstance(s, int) or isinstance(s, str)):
        raise TypeError('Unknown type')
    __ isinstance(s, int
        __ s < 0:
            r_ ""
        s = bin(s)[2:]
    ____ set(s) - set(['0', '1']
        r_ ""
    __ le.(s) > 5:
        raise ValueError('Binary string too long')
    r_ "0" * (le.(gestures) - le.(s)) + s


___ find_subseq(seq
    idx = 0
    s = []
    ___ g in seq:
        __ g not in gestures[idx:]:
            r_ []
        newidx = gestures.index(g, idx) + 1
        s.extend(['0'] * (newidx - idx - 1) + ['1'])
        idx = newidx
    s.reverse()
    r_ s
