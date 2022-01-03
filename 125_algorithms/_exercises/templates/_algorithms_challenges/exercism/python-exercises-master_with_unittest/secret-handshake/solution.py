gestures = ['wink', 'double blink', 'close your eyes', 'jump']


___ handshake(s):
    s = l..(sanitize(s))
    s.reverse()
    seq    # list
    lim = l..(s) __ l..(s) <= l..(gestures) ____ l..(gestures)
    ___ i1 __ r..(lim):
        __ s[i1] __ '1':
            seq.a..(gestures[i1])
    __ l..(s) __ 5:
        seq.reverse()
    r.. seq


___ code(seq):
    __ n.. seq o. set(seq) - set(gestures):
        r.. '0'
    s = find_subseq(seq)
    __ n.. s:
        s = ['1'] + find_subseq(reversed(seq))
    r.. "".j..(s)


___ sanitize(s):
    __ n..(isi..(s, int) o. isi..(s, s..)):
        raise TypeError('Unknown type')
    __ isi..(s, int):
        __ s < 0:
            r.. ""
        s = bin(s)[2:]
    ____ set(s) - set(['0', '1']):
        r.. ""
    __ l..(s) > 5:
        raise ValueError('Binary string too long')
    r.. "0" * (l..(gestures) - l..(s)) + s


___ find_subseq(seq):
    idx = 0
    s    # list
    ___ g __ seq:
        __ g n.. __ gestures[idx:]:
            r.. []
        newidx = gestures.index(g, idx) + 1
        s.extend(['0'] * (newidx - idx - 1) + ['1'])
        idx = newidx
    s.reverse()
    r.. s
