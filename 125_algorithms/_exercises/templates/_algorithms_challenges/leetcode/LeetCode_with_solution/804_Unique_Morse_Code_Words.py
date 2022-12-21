Morse_tab = [".-","-...","-.-.",
             "-..",".","..-.","--.","....",
             "..",".---","-.-",".-..","--",
             "-.","---",".--.","--.-",".-.",
             "...","-","..-","...-",".--",
             "-..-","-.--","--.."]

c_ Solution o..
    # https://leetcode.com/problems/unique-morse-code-words/solution/
    ___ uniqueMorseRepresentations  words
        """
        :type words: List[str]
        :rtype: int
        """
        __ l.. words) __ 0:
            r_ 0
        ans_set = s..()
        ___ word __ words:
            morsed = ""
            ___ c __ word:
                morsed += Morse_tab[o.. c) - o.. 'a')]
            
            ans_set.add(morsed)
        r_ l.. ans_set)
