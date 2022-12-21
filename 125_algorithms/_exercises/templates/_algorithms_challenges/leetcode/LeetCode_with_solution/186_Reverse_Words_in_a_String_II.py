c_ Solution o..
    ___ reverseWords  s
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        ls, pos = l.. s), 0
        __ s is N.. or ls __ 0:
            r_
        reverse(s, 0, ls)
        ___ i __ r.. ls + 1
            __ i __ ls or s[i] __ ' ':
                reverse(s, pos, i)
                pos = i + 1

    ___ reverse  array_s, begin, end
        ___ i __ r..((end - begin) / 2
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]
