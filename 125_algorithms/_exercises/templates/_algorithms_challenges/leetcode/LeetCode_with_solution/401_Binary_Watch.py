c_ Solution o..
    ___ readBinaryWatch  num):
        """
        :type num: int
        :rtype: List[str]
        """
        r_ ['%d:%02d' % (h, m)
            ___ h __ r.. 12) ___ m __ r.. 60)
            __ (bin(h) + bin(m)).count('1') __ num]



