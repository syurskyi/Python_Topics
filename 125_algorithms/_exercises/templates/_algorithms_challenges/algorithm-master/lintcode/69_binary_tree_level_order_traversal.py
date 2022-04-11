"""
Main Concept:
1. Use `_queue` to collect node in current level
2. Use `level_values` to collect the val of node in current level
3. After traverse the current level,
   append `level_values` to answer
   and reset `queue` as `_queue`

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    ___ levelOrder  root
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans    # list

        __ n.. root:
            r.. ans

        queue, _queue [root], []

        w.... queue:
            ans.a..([])

            ___ node __ queue:
                __ node.left:
                    _queue.a..(node.left)
                __ node.right:
                    _queue.a..(node.right)
                ans[-1].a..(node.val)

            queue, _queue _queue, []

        r.. ans
