"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


c_ Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    ___ binaryTreeToLists  root
        ans    # list
        __ n.. root:
            r.. ans

        queue = [root]
        w.... queue:
            _queue    # list
            dummy = tail = ListNode(-1)

            ___ node __ queue:
                tail.next = ListNode(node.val)
                tail = tail.next

                __ node.left:
                    _queue.a..(node.left)
                __ node.right:
                    _queue.a..(node.right)

            queue = _queue
            ans.a..(dummy.next)

        r.. ans
