c_ Solution:
    ___ lengthOfLongestSubstring(, s: st.) -> int:
        m _ {}
        left _ 0
        right _ 0
        ans _ 0
        n _ le.(s)
        w___(left<n a.. right<n
            el _ s[right]
            __(el __ m
                left _ ma.(left,m[el]+1)
            m[el] _ right
            ans _ ma.(ans,right-left+1)
            right+_1
        r_ ans