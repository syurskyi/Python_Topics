"""
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

查找J中的每个字符在 S 出现的次数的总和。

改进：
J有可能有重复的数。

测试数据：
https://leetcode.com/problems/jewels-and-stones/description/

"""

c.. Solution o..
    ___ numJewelsInStones  J, S
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        S_dict = {i:S.c..(i) ___ i __ s..(S)}
        
        r_ s..((S_dict.get(i, 0) ___ i __ J))
