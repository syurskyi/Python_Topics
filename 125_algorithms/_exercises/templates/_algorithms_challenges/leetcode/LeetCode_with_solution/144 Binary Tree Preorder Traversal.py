"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively? - see preTraverse_itr
"""
__author__ = 'Danyang'


# Definition for a  binary tree node
class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ preorderTraversal(self, root):
        """Morris"""
        ret    # list
        cur = root
        w.... cur:
            __ n.. cur.left:
                ret.a..(cur.val)
                cur = cur.right
            ____:
                pre = cur.left
                w.... pre.right a.. pre.right != cur:
                    pre = pre.right

                __ n.. pre.right:
                    pre.right = cur
                    ret.a..(cur.val)
                    cur = cur.left
                ____:
                    pre.right = N..
                    cur = cur.right

        r.. ret

    ___ preorderTraversal_memory(self, root):
        """
        dfs
        :param root:
        :return:
        """
        lst    # list
        self.preTraverse_itr(root, lst)
        r.. lst


    ___ preTraverse(self, node, lst):
        __ n.. node:
            r..
        lst.a..(node.val)

        self.preTraverse(node.left, lst)
        self.preTraverse(node.right, lst)

    ___ preTraverse_itr(self, root, lst):
        """
        stack = [R, L, cur]

        Pretty simple using stack
        double stacks

        :param root:
        :param lst:
        :return:
        """
        __ n.. root:
            r..
        stk = [root]
        w.... stk:
            node = stk.pop()
            lst.a..(node.val)
            __ node.right:  # right first
                stk.a..(node.right)

            __ node.left:
                stk.a..(node.left)



__ __name____"__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().preorderTraversal(t1)