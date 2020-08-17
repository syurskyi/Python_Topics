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
class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution(object
    ___ preorderTraversal(self, root
        """Morris"""
        ret = []
        cur = root
        w___ cur:
            __ not cur.left:
                ret.append(cur.val)
                cur = cur.right
            ____
                pre = cur.left
                w___ pre.right and pre.right != cur:
                    pre = pre.right

                __ not pre.right:
                    pre.right = cur
                    ret.append(cur.val)
                    cur = cur.left
                ____
                    pre.right = None
                    cur = cur.right

        r_ ret

    ___ preorderTraversal_memory(self, root
        """
        dfs
        :param root:
        :return:
        """
        lst = []
        self.preTraverse_itr(root, lst)
        r_ lst


    ___ preTraverse(self, node, lst
        __ not node:
            r_
        lst.append(node.val)

        self.preTraverse(node.left, lst)
        self.preTraverse(node.right, lst)

    ___ preTraverse_itr(self, root, lst
        """
        stack = [R, L, cur]

        Pretty simple using stack
        double stacks

        :param root:
        :param lst:
        :return:
        """
        __ not root:
            r_
        stk = [root]
        w___ stk:
            node = stk.p..
            lst.append(node.val)
            __ node.right:  # right first
                stk.append(node.right)

            __ node.left:
                stk.append(node.left)



__ __name____"__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    print Solution().preorderTraversal(t1)