#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


c.. Solution o..
    ___ isValidSerialization  preorder
        """
        When there are two consecutive "#" characters on top of the stack,
        pop both of them and replace the top element on the remain stack with "#".
        """
        preorder = preorder.split(",")
        stack   # list
        ___ val __ preorder:
            stack.a.. val)
            _____ self.twoConsecutive(stack
                stack = stack[:-3]
                stack.a.. "#")

        r_ stack __ ["#"]

    ___ twoConsecutive  stack
        __ l..(stack) < 3:
            r_ False
        r_ stack[-1] __ stack[-2] __ "#" a.. stack[-3] != "#"


c.. Solution_2 o..
    """
    Refer to:
    https://leetcode.com/discuss/83824/7-lines-easy-java-solution
    In a binary tree, if we consider null as leaves, then
        1. all non-null node provides 2 outdegree and 1 indegree(except root).
        2. all null node provides 0 outdegree and 1 indegree.

    Record diff = outdegree - indegree. When the next node comes:
    Decrease diff by 1, because the node provides an indegree.
    If the node is not null, increase diff by 2, because it provides two out degrees.

    diff should never be negative and diff will be zero when finished.
    """
    ___ isValidSerialization  preorder
        preorder = preorder.split(",")
        diff = 1
        ___ val __ preorder:
            diff -= 1
            __ diff < 0:
                r_ False
            __ val != "#":
                diff += 2
        r_ diff __ 0

"""
""
"#,#"
"1,#"
"1,#,#"
"#,#,#"
"1,#,#,#,#"
"9,#,#,1"
"9,3,4,#,#,1,#,#,2,#,6,#,#"
"""
