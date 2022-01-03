"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the
"root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that
"all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses
were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
__author__ = 'Daniel'


# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..


c_ Solution(object):
    ___ - ):
        cache_rob    # dict
        cache_notrob    # dict

    ___ rob(self, root):
        """
        possible rob at root
        :type root: TreeNode
        :rtype: int
        """
        __ root __ N..
            r.. 0

        __ root n.. __ cache_rob:
            val = max(
                notrob(root),
                root.val + notrob(root.left) + notrob(root.right)
            )
            cache_rob[root] = val

        r.. cache_rob[root]

    ___ notrob(self, root):
        """
        not rob at the root
        :param root: TreeNode
        :return: int
        """
        __ root __ N..
            r.. 0

        __ root n.. __ cache_notrob:
            val = (
                rob(root.left) +
                rob(root.right)
            )

            cache_notrob[root] = val

        r.. cache_notrob[root]


c_ SolutionTLE(object):
    ___ rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        __ root __ N..
            r.. 0

        r.. max(
            dorob(root),
            notrob(root)
        )

    ___ dorob(self, root):
        __ root __ N..
            r.. 0

        r.. (
            root.val +
            notrob(root.left) +
            notrob(root.right)
        )

    ___ notrob(self, root):
        __ root __ N..
            r.. 0

        r.. (max(notrob(root.left), rob(root.left)) +
                    max(notrob(root.right), rob(root.right)))
