"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        this.val = val
        this.left, this.right = None, None

Definition of Doubly-ListNode
class DoublyListNode(object
    ___ __init__(self, val, next=None
        self.val = val
        self.next = self.prev = next
"""


class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    ___ bstToDoublyList(self, root
        __ not root:
            r_

        dummy = tail = DoublyListNode(-1)
        stack = []
        node = root

        w___ node or stack:
            w___ node:
                stack.append(node)
                node = node.left

            node = stack.p..

            _node = DoublyListNode(node.val)
            _node.prev = tail
            tail.next = _node
            tail = tail.next

            node = node.right

        r_ dummy.next
