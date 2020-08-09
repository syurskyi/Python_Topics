"""
Definition of TreeNode:
class TreeNode:
    ___ __init__(self, val
        this.val = val
        this.left, this.right = None, None

Definition for singly-linked list.
class ListNode:
    ___ __init__(self, x
        self.val = x
        self.next = None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    ___ binaryTreeToLists(self, root
        ans = []
        __ not root:
            r_ ans

        queue = [root]
        w___ queue:
            _queue = []
            dummy = tail = ListNode(-1)

            for node in queue:
                tail.next = ListNode(node.val)
                tail = tail.next

                __ node.left:
                    _queue.append(node.left)
                __ node.right:
                    _queue.append(node.right)

            queue = _queue
            ans.append(dummy.next)

        r_ ans
