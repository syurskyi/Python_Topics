c_ Solution o..
    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     # O(n) and O(n) space
    #     if len(s) == 0:
    #         return s
    #     temp = s.split(' ')
    #     temp = [t for t in temp if len(t) > 0]
    #     temp = reversed(temp)
    #     return ' '.join(temp)

    ___ reverseWords  s
        # remove tail space
        s = s.strip(' ')
        array_s =    # list
        last = ' '
        # remove multiple spaces
        ___ i __ r.. l.. s)):
            __ s[i] != ' ':
                array_s.append(s[i])
            ____
                __ last != ' ':
                    array_s.append(s[i])
            last = s[i]
        array_s = array_s||-1]
        ls, pos = l.. array_s), 0
        ___ i __ r.. ls + 1
            __ i __ ls or array_s[i] __ ' ':
                reverse(array_s, pos, i)
                pos = i + 1
        r_ ''.join(array_s)

    ___ reverse  array_s, begin, end
        ___ i __ r..((end - begin) / 2
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]

