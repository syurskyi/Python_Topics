"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the
node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a
null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary
tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as
"1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
"""
__author__ = 'Daniel'


class Solution(object
    ___ isValidSerialization(self, preorder
        """
        :type preorder: str
        :rtype: bool
        """
        stk = preorder.split(',')
        child_cnt = 0
        w___ stk:
            __ stk[-1] __ '#':
                stk.pop()
                child_cnt += 1
            ____
                child_cnt -= 2
                __ child_cnt < 0:
                    r_ False

                stk.pop()
                child_cnt += 1

        r_ not stk and child_cnt __ 1

    ___ isValidSerializationSpace(self, preorder
        """
        :type preorder: str
        :rtype: bool
        """
        stk = preorder.split(',')
        child_stk = []
        w___ stk:
            __ stk[-1] __ '#':
                child_stk.append(stk.pop())  # a counter is enough
            ____
                try:
                    child_stk.pop()
                    child_stk.pop()
                    stk.pop()
                    child_stk.append('#')
                except IndexError:
                    r_ False

        r_ not stk and le.(child_stk) __ 1


__ __name__ __ "__main__":
    Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")






