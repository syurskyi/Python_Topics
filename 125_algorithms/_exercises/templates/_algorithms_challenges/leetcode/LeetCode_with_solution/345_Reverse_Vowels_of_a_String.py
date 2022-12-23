c_ Solution o..
    ___ reverseVowels  s
        """
        :type s: str
        :rtype: str
        """
        str_index =    # list
        vowel =    # list
        res =    # list
        pos = -1
        ___ index, value __ e.. s
            __ value __ 'aeiouAEIOU':
                str_index.a.. -1)
                vowel.a.. value)
            ____
                str_index.a.. index)
        ___ index __ str_index:
            __ index < 0:
                res.a.. vowel[pos])
                pos -= 1
            ____
                res.a.. s[index])
        r_ ''.join(res)

