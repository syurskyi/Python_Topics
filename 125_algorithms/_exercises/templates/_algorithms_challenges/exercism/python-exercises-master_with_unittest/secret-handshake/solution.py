gestures =  'wink', 'double blink', 'close your eyes', 'jump'


___ handshake(s
    s = l..(sanitize(s
    s.r..
    seq    # list
    lim = l..(s) __ l..(s) <_ l..(gestures) ____ l..(gestures)
    ___ i1 __ r..(lim
        __ s[i1] __ '1':
            seq.a..(gestures[i1])
    __ l..(s) __ 5:
        seq.r..
    r.. seq


___ code(seq
    __ n.. seq o. s..(seq) - s..(gestures
        r.. '0'
    s = find_subseq(seq)
    __ n.. s:
        s =  '1'  + find_subseq(r..(seq
    r.. "".j..(s)


___ sanitize(s
    __ n..(isi..(s, i..) o. isi..(s, s..:
        r.. T..('Unknown type')
    __ isi..(s, i..
        __ s < 0:
            r.. ""
        s = bin(s)[2:]
    ____ s..(s) - s..( '0', '1'
        r.. ""
    __ l..(s) > 5:
        r.. V...('Binary string too long')
    r.. "0" * (l..(gestures) - l..(s + s


___ find_subseq(seq
    idx = 0
    s    # list
    ___ g __ seq:
        __ g n.. __ gestures[idx:]:
            r.. []
        newidx = gestures.i.. g, idx) + 1
        s.e..  '0'  * (newidx - idx - 1) +  '1' )
        idx = newidx
    s.r..
    r.. s
