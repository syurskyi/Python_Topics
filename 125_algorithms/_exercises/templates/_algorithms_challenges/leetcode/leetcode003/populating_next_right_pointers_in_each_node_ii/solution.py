# Definition for a  binary tree node
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    ___ connect(self, root
        head = None  # Head node of the next level
        prev = None
        w___ root is not None:
            # Build the next level of root
            w___ root is not None:
                __ root.left is not None:
                    __ prev is None:
                        head = root.left
                        prev = head
                    ____
                        prev.next = root.left
                        prev = prev.next
                __ root.right is not None:
                    __ prev is None:
                        head = root.right
                        prev = head
                    ____
                        prev.next = root.right
                        prev = prev.next
                root = root.next
            root = head
            head = None
            prev = None
