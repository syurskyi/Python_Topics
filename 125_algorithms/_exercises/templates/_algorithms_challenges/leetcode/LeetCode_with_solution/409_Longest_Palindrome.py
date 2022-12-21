c_ Solution:
    # https://leetcode.com/problems/longest-palindrome/solution/
    # def longestPalindrome(self, s):
    #     ans = 0
    #     for v in collections.Counter(s).itervalues():
    #         ans += v / 2 * 2
    #         if ans % 2 == 0 and v % 2 == 1:
    #             ans += 1
    #     return ans
    ___ longestPalindrome  s
        ans = 0
        char_map  # dict
        ___ c __ s:
            char_map[c] = char_map.get(c, 0) + 1
        ___ c __ char_map.keys(
            __ char_map[c] % 2 __ 0:
                ans += char_map.pop(c)
            ____
                ans += char_map[c] / 2 * 2
        __ l.. char_map) != 0:
            ans += 1
        r_ ans