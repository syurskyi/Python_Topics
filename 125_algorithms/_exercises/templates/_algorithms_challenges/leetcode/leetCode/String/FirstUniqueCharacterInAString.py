"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

给定一个字符串，找到第一个不重复的字符，输出索引，如不存在输出 -1。

思路是直接使用字典，都是O(1)。

Discuss 中使用的 count 方法居然比这种方式快...

beat 72%

测试地址：
https://leetcode.com/problems/first-unique-character-in-a-string/description/


"""
c.. Solution o..
    ___ firstUniqChar  s
        """
        :type s: str
        :rtype: int
        """
        
        x _ # dict
        
        ___ i __ s:
            try:
                x[i] += 1
            except:
                x[i] = 1
        
        ___ i __ x.keys(
            __ x[i] > 1:
                x.pop(i)
        
        ___ i __ r..(l..(s)):
            __ s[i] __ x:
                r_ i
        r_ -1
