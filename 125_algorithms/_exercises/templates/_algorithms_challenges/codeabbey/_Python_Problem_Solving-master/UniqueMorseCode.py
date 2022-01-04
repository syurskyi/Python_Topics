c_ Solution:
    ___ uniqueMorseRepresentations(self, words: List[s..]) __ i..:
        tab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store_trans    # list
        ___ i __ words:
            string = ''
            ___ j __ i:
                ind = ord(j) - 97
                string += tab[ind]
            __ string n.. __ store_trans:
                store_trans.a..(string)
        r.. l..(store_trans)