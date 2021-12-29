"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively? - see postTraverse_itr
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..

class Solution:
    ___ postorderTraversal(self, root):
        """
        dfs
        Recursive post-order traversal is trivial. What is the iteration version for this
        :param root: TreeNode
        :return: a list of int
        """
        lst    # list
        self.postTraverse_itr(root, lst)
        r.. lst



    ___ postTraverse(self, node, lst):
        __ n.. node:
            r..
        self.postTraverse(node.left, lst)
        self.postTraverse(node.right, lst)

        lst.a..(node.val)

    ___ postTraverse_itr(self, root, lst):
        """
        stack = [L, R, cur]

        double stacks

        :param root:
        :param lst:
        :return:
        """
        __ n.. root:
            r..
        stk = [root]
        w.... stk:
            cur = stk.pop()
            lst.insert(0, cur.val)  # reversely insert
            __ cur.left:
                stk.a..(cur.left)

            __ cur.right:
                stk.a..(cur.right)






__ __name____"__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().postorderTraversal(t1)