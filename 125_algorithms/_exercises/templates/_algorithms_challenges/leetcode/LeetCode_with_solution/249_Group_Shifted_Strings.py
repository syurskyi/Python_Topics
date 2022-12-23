c_ Solution o..
    ___ groupStrings  strings
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic  # dict
        ___ s __ strings:
            key = hashCode(s)
            try:
                dic[key].a.. s)
            except KeyError:
                dic[key] = [s]
        r_ dic.values()

    ___ hashCode  string
        __ string is N.. or l.. string) __ 0:
            r_ ''
        __ l.. string) __ 1:
            r_ 'a'
        step = abs(o.. string[0]) - o.. 'a'))
        __ step __ 0:
            r_ string
        key = 'a'
        ___ ch __ string[1:]:
            curr = o.. ch) - step
            __ o.. ch) - step < o.. 'a'
                curr += 26
            key += chr(curr)
        r_ key
