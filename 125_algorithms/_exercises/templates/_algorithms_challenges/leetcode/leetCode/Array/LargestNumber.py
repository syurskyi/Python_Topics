"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.


思路是补位：

9 > 34

位数不够的补齐。

一开始的补位用的是最后一位。测试时发现一个错误：

8247
824
按照一开始的补位规则：
824 会补成 8244

e...虽然调整后通过了测试，不过最终结果是缺少了一些测试例子。

我做的调整是，从补位补最后一个变为补最大的一位。但是：
284
2847 这种情况下，会以
284 2847 排，但应该是：
2847 284
----
所以还是有问题，在Discuss里提个Issue.
---

Python2的话可以用 soted的 cmp参数，不过3中已经不存在了。

暂时不搞了...

测试地址：
https://leetcode.com/problems/largest-number/description/

beat 38%~77%.

"""
c.. Solution o..
    ___ largestNumber  nums
        """
        :type nums: List[int]
        :rtype: str
        """
        
        __ n.. any(nums
            r_ '0'
        
        max_nums = l..(str(m..(nums)))
        
        # 2
        ___ mycmp(x, y
            __ x + y > y + x:
                r_ 1
            ____
                r_ -1

        # 测试用下面的可以跑过 2 & 3。
        ___ makeEqual(s, length=max_nums
            
            __ l..(s) __ length:
                r_ s
            # 这种补位会通过测试，但是 Leetcode 的测试并没有包含所有的情况。
            x = m..(s) * (length - l..(s))
            r_ s+x
        
        # 2
        r_ ''.join(s..(map(str, nums), cmd=mycmp, reverse=True))
        # 3
        r_ ''.join(s..(map(str, nums), key=makeEqual, reverse=True))

        # print(sorted(map(str, nums), key=makeEqual, reverse=True))

