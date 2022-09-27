c_ Solution o..
    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     # check every char
    #     if len(s) != len(t):
    #         return False
    #     check = [False] * len(s)
    #     for i in range(len(s)):
    #         if check[i]:
    #             continue
    #         temp = s.count(s[i])
    #         if temp != t.count(t[i]):
    #             return False
    #         if temp >= 2:
    #             for j in range(i + 1, len(s)):
    #                 if s[j] == s[i]:
    #                     check[j] = True
    #                     if t[j] != t[i]:
    #                         return False
    #         check[i] = True
    #     return True

    ___ isIsomorphic  s, t):
        __ l.. s) != l.. t):
            r_ F..
        ls = l.. s)
        mapStoT = [0] * 127
        mapTtoS = [0] * 127
        ___ i __ r.. ls):
            s_num, t_num = o.. s[i]), o.. t[i])
            __ mapStoT[s_num] __ 0 and mapTtoS[t_num] __ 0:
                mapStoT[s_num] = t_num
                mapTtoS[t_num] = s_num
            ____ mapTtoS[t_num] != s_num or mapStoT[s_num] != t_num:
                r_ F..
        r_ T..

