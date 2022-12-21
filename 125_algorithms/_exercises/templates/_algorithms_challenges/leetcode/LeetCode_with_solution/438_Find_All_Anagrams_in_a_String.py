c_ Solution o..
    ___ findAnagrams  s, p
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res =    # list
        __ s is N.. or p is N.. or l.. s) __ 0 or l.. p) __ 0:
            r_ res
        char_map = [0] * 256
        ___ c __ p:
            char_map[o.. c)] += 1
        left, right, count = 0, 0, l.. p)
        w.. right < l.. s
            __ char_map[o.. s[right])] >= 1:
                count -= 1
            char_map[o.. s[right])] -= 1
            right += 1
            __ count __ 0:
                res.append(left)
            __ right - left __ l.. p
                __ char_map[o.. s[left])] >= 0:
                    count += 1
                char_map[o.. s[left])] += 1
                left += 1
        r_ res

    # def findAnagrams(self, s, p):
    #     if len(s) < len(p):
    #         return []
    #     res = []
    #     p_len = len(p)
    #     bit_map = []
    #     for _ in range(26):
    #         bit_map.append(0)
    #     for c in p:
    #         bit_map[ord(c) - ord('a')] += 1
    #     s_p = str(bit_map)
    #     for i in range(26):
    #         bit_map[i] = 0
    #     for i in range(p_len - 1):
    #         bit_map[ord(s[i]) - ord('a')] += 1
    #     for i in range(p_len - 1, len(s)):
    #         bit_map[ord(s[i]) - ord('a')] += 1
    #         if i - p_len >= 0:
    #             bit_map[ord(s[i - p_len]) - ord('a')] -= 1
    #         if str(bit_map) == s_p:
    #             res.append(i - p_len + 1)
    #     return res

    # def findAnagrams(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: List[int]
    #     """
    #     res = []
    #     pCounter = collections.Counter(p)
    #     sCounter = collections.Counter(s[:len(p)-1])
    #     for i in range(len(p)-1,len(s)):
    #         sCounter[s[i]] += 1   # include a new char in the char_map
    #         if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
    #             res.append(i-len(p)+1)   # append the starting index
    #         sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
    #         if sCounter[s[i-len(p)+1]] == 0:
    #             del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
    #     return res
