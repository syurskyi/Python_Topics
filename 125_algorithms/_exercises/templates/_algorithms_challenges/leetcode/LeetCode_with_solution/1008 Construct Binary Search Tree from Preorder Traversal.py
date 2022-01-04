#!/usr/bin/python3
"""
Return the root node of a binary search tree that matches the given preorder
traversal.

(Recall that a binary search tree is a binary tree where for every node, any
descendant of node.left has a value < node.val, and any descendant of node.right
has a value > node.val.  Also recall that a preorder traversal displays the
value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note:
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
____ typing _______ List


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ bstFromPreorder2(self, preorder: List[i..]) __ TreeNode:
        """
        need to be BST

        scan the list to break left and right part
        F(n) = 2 F(n/2) + O(n), then it is O(n log n)

        Make it O(n)
        maintain a stack
        After walking through example, left child can be determined quickly
        since it is pre-order. Left comes first.

        Stack maintain a node that is missing right child
        decreasing stack
        """
        root = TreeNode(preorder[0])
        stk = [root]
        ___ a __ preorder[1:]:
            node = TreeNode(a)
            __ a < stk[-1].val:  # len(stk) always >= 1
                stk[-1].left = node
            ____:
                w.... l..(stk) >= 2 a.. stk[-2].val < a:
                    stk.pop()

                stk[-1].right = node
                stk.pop()

            stk.a..(node)

        r.. root

    ___ bstFromPreorder(self, preorder: List[i..]) __ TreeNode:
        """
        If a node is a right child (larger), find the proper parent
        The proper parent should the deepest in the stack that its val < current val
        """
        root = TreeNode(preorder[0])
        stk = [root]
        ___ a __ preorder[1:]:
            node = TreeNode(a)
            __ a < stk[-1].val:
                stk[-1].left = node
            ____:
                w.... stk a.. stk[-1].val < a:
                    pi = stk.pop()
                pi.right = node
            stk.a..(node)
            
        r.. root
