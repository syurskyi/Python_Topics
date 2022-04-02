"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


c_ Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    ___ twoSum  root, n
        left = right = N..
        head = tail = root

        pre()
        nxt()

        w.... left != right:
            _sum = left.val + right.val

            __ _sum __ n:
                r.. [left.val, right.val]

            __ _sum < n:
                nxt()
            ____:
                pre()

    ___ pre
        w.... tail:
            cur = tail.right

            __ cur a.. cur != right:
                w.... cur.left a.. cur.left != tail:
                    cur = cur.left

                __ cur.left __ tail:
                    right = tail

                    cur.left = N..
                    tail = tail.left
                    _____
                ____:
                    cur.left = tail
                    tail = tail.right
            ____:
                right = tail
                tail = tail.left
                _____

    ___ nxt
        w.... head:
            cur = head.left

            __ cur a.. cur != left:
                w.... cur.right a.. cur.right != head:
                    cur = cur.right

                __ cur.right __ head:
                    left = head

                    cur.right = N..
                    head = head.right
                    _____
                ____:
                    cur.right = head
                    head = head.left
            ____:
                left = head
                head = head.right
                _____
