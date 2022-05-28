"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..

c_ Solution:
    ___ levelOrder  root
        """
        Queue
        BFS
        :param root: Tree node
        :return: a list of lists of integers
        """
        result    # list
        q    # list
        __ root:
            q.a..(root)

        w.... q:
            length l..(q)
            # cur_level = []
            ___ i __ r..(length
                cur q[i]
                __ cur.left:
                    q.a..(cur.left)
                __ cur.right:
                    q.a..(cur.right)
            result.a.. m..(l.... x: x.val, q[:length]  # no need to create a new list
            q q[length:]  # no need to create a new list
        r.. ?

__ _____ __ ____
    nodes [TreeNode(i) ___ i __ r..(3)]
    nodes[0].left nodes[1]
    nodes[1].left nodes[2]
    print Solution().levelOrder(nodes 0


