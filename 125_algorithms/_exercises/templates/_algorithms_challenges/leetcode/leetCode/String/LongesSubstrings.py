"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

找到最长的子字符串。

基本思路是逐个遍历若不在new里则添加进里面，如果在new里则表示已经发生了重复，那么会对比目前的new与之前保存的子字符串长度哪个较大，
保存较大的。新的new则为发生重复的字符串直到最后+新数据。`pkwk`遍历到第二个k时new此时会变成`wk`。

因为是子字符串并不是子序列，所以这样做是可行的。

时间复杂度 O(n)

测试用例：
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


"""

c.. Solution o..
    ___ lengthOfLongestSubstring  s
        """
        :type s: str
        :rtype: int
        """
        __ n.. s:
            r_ 0
        
        longestSubstringLength = 1
        
        new = s[0]
        
        ___ data __ s[1:]:
            __ data n.. __ new:
                new += data
                c_

            # repeated.
            __ l..(new) > longestSubstringLength:
                longestSubstringLength = l..(new)

            new = new[new.index(data)+1:] + data

        __ l..(new) > longestSubstringLength:
            r_ l..(new)
        
        r_ longestSubstringLength