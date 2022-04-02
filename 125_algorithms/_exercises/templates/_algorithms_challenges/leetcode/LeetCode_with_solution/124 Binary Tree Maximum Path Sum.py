"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..

c_ Solution:
    global_max = -1<<31
    ___ maxPathSum  root
        """
        :param root: TreeNode
        :return: integer
        """
        get_max_component(root)
        # global_max can in ANY path in the tree
        r.. global_max

    ___ get_max_component  root
        """
        Algorithm:
        dfs
        The path may start and end at any node in the tree.

           parent
           /
          cur
         /  \
         L  R

        at current: the candidate max (final result) is cur+L+R
        at current: the max component (intermediate result) is cur or cur+L or cur+R

        Reference: http://fisherlei.blogspot.sg/2013/01/leetcode-binary-tree-maximum-path-sum.html

        :param root:
        :return:
        """
        __ n.. root:
            r.. 0

        left_max_component = get_max_component(root.left)
        right_max_component = get_max_component(root.right)

        # update global max
        current_max_sum = m..(root.val, root.val+left_max_component, root.val+right_max_component, root.val+left_max_component+right_max_component)  # four situations
        global_max = m..(global_max, current_max_sum)

        # return value for upper layer to calculate the current_max_sum
        r.. m..(root.val, root.val+left_max_component, root.val+right_max_component)  # excluding arch (i.e. root.val+left_max_component+right_max_component)




