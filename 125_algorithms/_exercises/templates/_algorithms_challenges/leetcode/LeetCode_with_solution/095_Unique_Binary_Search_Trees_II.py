# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ generateTrees  n
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        __ n __ 0:
            r_    # list
        r_ get_trees(1, n)

    ___ get_trees  start, end
        # recursive solve this problem
        res =    # list
        __ start > end:
            res.a.. N..)
            r_ res
        ___ i __ r.. start, end + 1
            lefts = get_trees(start, i - 1)
            rights = get_trees(i + 1, end)
            ___ j __ r.. l.. lefts)):
                ___ k __ r.. l.. rights)):
                    # root point
                    root = TreeNode(i)
                    root.left = lefts[j]
                    root.right = rights[k]
                    res.a.. root)
        r_ res


