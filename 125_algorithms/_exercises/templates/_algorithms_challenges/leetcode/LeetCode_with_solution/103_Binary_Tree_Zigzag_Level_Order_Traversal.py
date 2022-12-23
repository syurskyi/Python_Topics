# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c_ Solution o..
    ___ zigzagLevelOrder  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # level order
        __ root is N..:
            r_    # list
        q = [[root]]
        ___ level __ q:
            record =    # list
            ___ node __ level:
                __ node.left:
                    record.a.. node.left)
                __ node.right:
                    record.a.. node.right)
            __ record:
                q.a.. record)
        # zigzag order
        res =    # list
        ___ index, level __ e.. q
            temp = [x.val ___ x __ level]
            __ index % 2 __ 0:
                res.a.. temp)
            ____
                res.a.. temp||-1])
        r_ res
