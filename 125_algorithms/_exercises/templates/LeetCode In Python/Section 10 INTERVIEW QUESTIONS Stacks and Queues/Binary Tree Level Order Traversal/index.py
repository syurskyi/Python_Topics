# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

from collections ______ deque

class Solution:
    ___ levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        __(root is None
            r_ ans
        
        q = deque([root])

        w___(q
            n = le.(q)
            temp = []
            for i in range(0,n
                f = q.popleft()
                temp.append(f.val)

                __(f.left is not None
                    q.append(f.left)
                __(f.right is not None
                    q.append(f.right)

            __(le.(temp)>0
                ans.append(temp[:])
                temp.clear()
        r_ ans
        
