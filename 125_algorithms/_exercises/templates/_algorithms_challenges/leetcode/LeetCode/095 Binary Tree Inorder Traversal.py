"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'


class TreeNode(object
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


class Solution(object
    ___ inorderTraversal(self, root
        """
        Morris Traversal
        """
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
                    cur = cur.left
                ____
                    pre.right = None
                    ret.append(cur.val)
                    cur = cur.right

        r_ ret

    ___ inorderTraversal_memory(self, root
        """
        :type root: TreeNode
        :param root:
        :return: a list of integers
        """
        lst = []
        self.inorderTraverse_itr(root, lst)
        r_ lst

    ___ inorderTraverse(self, root, lst
        """
        In order traverse
        """
        __ not root:
            r_
        self.inorderTraverse(root.left, lst)
        lst.append(root.val)
        self.inorderTraverse(root.right, lst)

    ___ inorderTraverse_itr(self, root, lst
        """
        iterative version
        leftmost first in the lst
        double loop

        reference: http://fisherlei.blogspot.sg/2013/01/leetcode-binary-tree-inorder-traversal.html
        :type root: TreeNode
        :param root:
        :param lst:
        :return:
        """
        __ not root:
            r_

        cur = root
        stk = []
        w___ stk or cur:
            w___ cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()  # left_most
            lst.append(cur.val)
            cur = cur.right
            # if cur.right:  # should go to next iteration
            #     cur = cur.right
            #     stk.append(cur)

