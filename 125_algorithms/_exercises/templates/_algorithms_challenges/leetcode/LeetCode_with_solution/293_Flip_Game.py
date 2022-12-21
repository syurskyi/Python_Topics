c_ Solution o..
    ___ generatePossibleNextMoves  s
        """
        :type s: str
        :rtype: List[str]
        """
        # return [s[:i] + "--" + s[i+2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]
        res =    # list
        __ s is N.. or l.. s) __ 0:
            r_ res
        ls = l.. s)
        ___ i __ r.. ls - 1
            __ s[i] __ '+' a.. s[i + 1] __ '+':
                res.append(s[:i] + '--' + s[i + 2:])
        r_ res
