class Solution:
    ___ uniqueMorseRepresentations(self, words: List[str]) -> int:
        tab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store_trans = []
        ___ i in words:
            string = ''
            ___ j in i:
                ind = ord(j) - 97
                string += tab[ind]
            __ string not in store_trans:
                store_trans.append(string)
        r_ le.(store_trans)