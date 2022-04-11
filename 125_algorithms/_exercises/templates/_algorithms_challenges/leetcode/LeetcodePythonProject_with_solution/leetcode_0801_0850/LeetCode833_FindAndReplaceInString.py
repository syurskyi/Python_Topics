'''
Created on Jun 9, 2018

@author: tongq
'''
c_ Solution(o..
    ___ findReplaceString  S, indexes, sources, targets
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        s S
        prev 0
        res ''
        ___ ind, source, target __ s..(z..(indexes, sources, targets:
            __ s[ind:ind+l..(source)] __ source:
                res += s[prev:ind]
                res += target
                prev ind + l..(source)
        res += s[prev:]
        r.. res
    
    ___ test
        testCases [
            [
                "abcd",
                [0,2],
                ["a","cd"],
                ["eee","ffff"]
            ],
            [
                "abcd",
                [0,2],
                ["ab","ec"],
                ["eee","ffff"],
            ],
            [
                "vmokgggqzp",
                [3,5,1],
                ["kg","ggq","mo"],
                ["s","so","bfr"],
            ],
            [
                "imidcxiiqjwpvvcocjtskshvmqjnlhsqtezqttmoxuskbmujej",
                [35,6,22,40,17,19,12,2,42,4,8,45,14,29,47,24],
                ["qtt","ii","hv","xu","jt","sk","vv","id","skb","cx","qjw","mu","co","hsqtez","jej","mqjnl"],
                ["idl","vo","yl","pg","efp","vqi","s","wb","mw","gmt","rkqc","kdx","o","vamwgpn","pl","xyvz"],
            ],
        ]
        ___ s, indexes, sources, targets __ testCases:
            res findReplaceString(s, indexes, sources, targets)
            print('res: %s' % res)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
