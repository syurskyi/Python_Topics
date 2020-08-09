# Definition for a binary tree node.
# class TreeNode:
#     ___ __init__(self, x
#         self.val = x
#         self.left = None
#         self.right = None

____ co.. ______ deque

c_ Solution:
    ___ levelOrder(, root: TreeNode)  L..[L..[in.]]:
        ans _   # list

        __(root is N..
            r_ ans
        
        q _ deque([root])

        w___(q
            n _ le.(q)
            temp _   # list
            ___ i __ ra..(0,n
                f _ q.popleft()
                temp.ap..(f.val)

                __(f.left is no. N..
                    q.ap..(f.left)
                __(f.right is no. N..
                    q.ap..(f.right)

            __(le.(temp)>0
                ans.ap..(temp[:])
                temp.clear()
        r_ ans
        
