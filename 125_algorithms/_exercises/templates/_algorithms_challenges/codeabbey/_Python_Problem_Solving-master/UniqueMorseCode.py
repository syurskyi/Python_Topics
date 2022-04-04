c_ Solution:
    ___ uniqueMorseRepresentations  words: L..[s..]) __ i..:
        tab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store_trans    # list
        ___ i __ words:
            s__ = ''
            ___ j __ i:
                ind = o..(j) - 97
                s__ += tab[ind]
            __ s__ n.. __ store_trans:
                store_trans.a..(s__)
        r.. l..(store_trans)