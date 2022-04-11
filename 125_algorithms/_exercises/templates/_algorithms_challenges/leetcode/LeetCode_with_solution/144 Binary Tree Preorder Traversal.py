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
__author__ 'Danyang'


# Definition for a  binary tree node
c_ TreeNode(o..
    ___ - , x
        val x
        left N..
        right N..


c_ Solution(o..
    ___ preorderTraversal  root
        """Morris"""
        ret    # list
        cur root
        w.... cur:
            __ n.. cur.left:
                ret.a..(cur.val)
                cur cur.right
            ____
                pre cur.left
                w.... pre.right a.. pre.right != cur:
                    pre pre.right

                __ n.. pre.right:
                    pre.right cur
                    ret.a..(cur.val)
                    cur cur.left
                ____
                    pre.right N..
                    cur cur.right

        r.. ret

    ___ preorderTraversal_memory  root
        """
        dfs
        :param root:
        :return:
        """
        lst    # list
        preTraverse_itr(root, lst)
        r.. lst


    ___ preTraverse  node, lst
        __ n.. node:
            r..
        lst.a..(node.val)

        preTraverse(node.left, lst)
        preTraverse(node.right, lst)

    ___ preTraverse_itr  root, lst
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
        stk [root]
        w.... stk:
            node stk.p.. )
            lst.a..(node.val)
            __ node.right:  # right first
                stk.a..(node.right)

            __ node.left:
                stk.a..(node.left)



__ _____ __ ____
    t1 TreeNode(1)
    t1.left TreeNode(2)
    print Solution().preorderTraversal(t1)