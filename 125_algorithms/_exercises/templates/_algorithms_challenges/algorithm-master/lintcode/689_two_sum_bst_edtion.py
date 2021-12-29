"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    ___ twoSum(self, root, n):
        self.left = self.right = N..
        self.head = self.tail = root

        self.pre()
        self.nxt()

        w.... self.left != self.right:
            _sum = self.left.val + self.right.val

            __ _sum __ n:
                r.. [self.left.val, self.right.val]

            __ _sum < n:
                self.nxt()
            ____:
                self.pre()

    ___ pre(self):
        w.... self.tail:
            cur = self.tail.right

            __ cur a.. cur != self.right:
                w.... cur.left a.. cur.left != self.tail:
                    cur = cur.left

                __ cur.left __ self.tail:
                    self.right = self.tail

                    cur.left = N..
                    self.tail = self.tail.left
                    break
                ____:
                    cur.left = self.tail
                    self.tail = self.tail.right
            ____:
                self.right = self.tail
                self.tail = self.tail.left
                break

    ___ nxt(self):
        w.... self.head:
            cur = self.head.left

            __ cur a.. cur != self.left:
                w.... cur.right a.. cur.right != self.head:
                    cur = cur.right

                __ cur.right __ self.head:
                    self.left = self.head

                    cur.right = N..
                    self.head = self.head.right
                    break
                ____:
                    cur.right = self.head
                    self.head = self.head.left
            ____:
                self.left = self.head
                self.head = self.head.right
                break
