"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

类似于 Find All Anagrams in a String 难度应该颠倒过来。

这个的测试用例更丰富，发现了没想到的一个盲点。

思路请看 https://github.com/HuberTRoy/leetCode/blob/master/DP/FindAllAnagramsInAString.py


beat 79%

测试地址：
https://leetcode.com/problems/permutation-in-string/description/


"""
c.. Solution o..
    ___ checkInclusion  s1, s2
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        __ l..(s1) > l..(s2
            r_ False
        
        counts _ # dict
        
        ___ i __ s1:
            try:
                counts[i] += 1
            except:
                counts[i] = 1
        
        pre = counts.copy()
        
        ___ c __ r..(l..(s2)):
            i = s2[c]
            __ i __ pre:
                pre[i] -= 1
                __ n.. pre[i]:
                    pre.pop(i)
                
                __ n.. pre:
                    r_ True
            ____
                __ i __ counts:
                    __ i != s2[c-l..(s1)+s..(pre.values())]:
                        ___ t __ s2[c-l..(s1)+s..(pre.values()):c]:
                            __ t __ i:
                                break
                            try:
                                pre[t] += 1
                            except:
                                pre[t] = 1
                    c_
                pre = counts.copy()
                __ i __ pre:
                    pre[i] -= 1
                    __ n.. pre[i]:
                        pre.pop(i)
        
        r_ False
