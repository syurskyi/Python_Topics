class Solution:
    ___ uniqueMorseRepresentations(self, words: List[str]) -> int:
        tab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store_trans = []
        for i in words:
            string = ''
            for j in i:
                ind = ord(j) - 97
                string += tab[ind]
            __ string not in store_trans:
                store_trans.append(string)
        r_ le.(store_trans)