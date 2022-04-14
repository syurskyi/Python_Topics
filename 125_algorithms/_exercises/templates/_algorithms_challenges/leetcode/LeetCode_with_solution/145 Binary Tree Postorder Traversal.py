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
__author__ 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..

c_ Solution:
    ___ postorderTraversal  root
        """
        dfs
        Recursive post-order traversal is trivial. What is the iteration version for this
        :param root: TreeNode
        :return: a list of int
        """
        lst    # list
        postTraverse_itr(root, lst)
        r.. ?



    ___ postTraverse  node, lst
        __ n.. node:
            r..
        postTraverse(node.left, lst)
        postTraverse(node.right, lst)

        lst.a..(node.val)

    ___ postTraverse_itr  root, lst
        """
        stack = [L, R, cur]

        double stacks

        :param root:
        :param lst:
        :return:
        """
        __ n.. root:
            r..
        stk [root]
        w.... stk:
            cur stk.p.. )
            ?.i.. 0, cur.val)  # reversely insert
            __ cur.left:
                stk.a..(cur.left)

            __ cur.right:
                stk.a..(cur.right)






__ _____ __ ____
    t1 TreeNode(1)
    t1.left TreeNode(2)
    print Solution().postorderTraversal(t1)