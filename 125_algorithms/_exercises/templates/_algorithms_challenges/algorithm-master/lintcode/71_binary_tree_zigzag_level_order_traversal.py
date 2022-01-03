"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    ___ zigzagLevelOrder(self, root):
        ans    # list
        __ n.. root:
            r.. ans

        queue = [root]
        w.... queue:
            _queue    # list
            ans.a..([])

            ___ node __ queue:
                __ node.left:
                    _queue.a..(node.left)
                __ node.right:
                    _queue.a..(node.right)

                ans[-1].a..(node.val)

            __ l..(ans) % 2 __ 0:
                ans[-1].reverse()

            queue = _queue

        r.. ans
