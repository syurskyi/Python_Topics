"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False


题目中将三种情况定义为 capitals：
1. 全是大写。（"USA"）
2. 全是小写。("leetcode")
3. 多于1个字符只在第一位用了大写。("Google")

思路O(n)的遍历和内置。

遍历的判断：
ASCII码中：
65-90 是 A-Z.
97-122 是 a-z.

若第一个字符是大写，则判断：
剩下的是否全是大写，剩下的是否全是小写。

若第一个字符是小写，则判断：
剩下的是否全是小写。

只有一个字符时，无论如何都是capital.

测试用例：
https://leetcode.com/problems/detect-capital/description/

内置最快，自写慢个4ms，考虑到内置是c写的。4ms完全可以接受。


"""

c.. Solution o..
    ___ detectCapitalUse  word
        """
        :type word: str
        :rtype: bool
        """
        __ l..(word) < 2:
            r_ True
        
        letter_one = ord(word[0])
        # letter_two = word[1]
        __ 65 <= letter_one <= 90:
            r_ self.letter_all_capital_or_lower(word[1:])
        
        r_ self.letter_all_lower(word[1:])
        # for i in word:
    
    ___ letter_all_capital_or_lower  word
        #
        lower = F..
        capital = F..
        
        # A-Z
        left = 65
        right = 90
        
        __ 97 <= ord(word[0]) <= 122:
            left = 97
            right = 122
            
        ___ i __ word:
            __ n.. left <= ord(i) <= right:
                r_ F..
        r_ True
    
    ___ letter_all_lower  word
        ___ i __ word:
            __ n.. 97 <= ord(i) <= 122:
                r_ F..
        r_ True

