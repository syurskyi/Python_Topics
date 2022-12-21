"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

忽略特殊字符，空白，大小写。判断是否为回文字符串，空的话也为有效的。

关键字: re.

测试地址：
https://leetcode.com/problems/valid-palindrome/description/

"""
import re

c.. Solution o..
    ___ isPalindrome  s
        """
        :type s: str
        :rtype: bool
        """
        
        __ n.. s:
            r_ True
        
        s = s.lower()
        x = ''.join(re.findall(r'[a-z0-9]{1}', s))
        
        r_ x __ x[::-1]
        