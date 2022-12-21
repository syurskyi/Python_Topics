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
                str_index.append(-1)
                vowel.append(value)
            ____
                str_index.append(index)
        ___ index __ str_index:
            __ index < 0:
                res.append(vowel[pos])
                pos -= 1
            ____
                res.append(s[index])
        r_ ''.join(res)

