# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

c_ Solution:
    # @param root, a tree node
    # @return nothing
    ___ connect(self, root):
        head = N..  # Head node of the next level
        prev = N..
        w.... root __ n.. N..
            # Build the next level of root
            w.... root __ n.. N..
                __ root.left __ n.. N..
                    __ prev __ N..
                        head = root.left
                        prev = head
                    ____:
                        prev.next = root.left
                        prev = prev.next
                __ root.right __ n.. N..
                    __ prev __ N..
                        head = root.right
                        prev = head
                    ____:
                        prev.next = root.right
                        prev = prev.next
                root = root.next
            root = head
            head = N..
            prev = N..
