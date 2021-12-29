"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""


class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    ___ bstToDoublyList(self, root):
        __ n.. root:
            r..

        dummy = tail = DoublyListNode(-1)
        stack    # list
        node = root

        w.... node o. stack:
            w.... node:
                stack.a..(node)
                node = node.left

            node = stack.pop()

            _node = DoublyListNode(node.val)
            _node.prev = tail
            tail.next = _node
            tail = tail.next

            node = node.right

        r.. dummy.next
