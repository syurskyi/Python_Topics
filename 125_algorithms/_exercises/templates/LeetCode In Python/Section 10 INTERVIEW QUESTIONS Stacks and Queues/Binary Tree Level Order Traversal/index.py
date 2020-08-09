# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

from collections ______ deque

c_ Solution:
    ___ levelOrder(, root: TreeNode) -> L..[L..[int]]:
        ans _ []

        __(root is None
            r_ ans
        
        q _ deque([root])

        w___(q
            n _ le.(q)
            temp _ []
            ___ i __ ra..(0,n
                f _ q.popleft()
                temp.append(f.val)

                __(f.left is no. None
                    q.append(f.left)
                __(f.right is no. None
                    q.append(f.right)

            __(le.(temp)>0
                ans.append(temp[:])
                temp.clear()
        r_ ans
        
