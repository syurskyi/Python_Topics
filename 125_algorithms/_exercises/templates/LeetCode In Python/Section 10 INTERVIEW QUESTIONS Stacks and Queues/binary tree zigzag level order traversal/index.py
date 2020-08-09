# Definition for a binary tree node.
# class TreeNode:
#     ___ init(self, x
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ___ zigzagLevelOrder(, root: TreeNode) -> L..[L..[in.]]:
        __ no. root:
            r_ []
        res _ []
        q _ collections.deque()

        zigzag _ F..
        q.ap..(root)

        w___ q:
            level _ []
            ___ _ __ ra..(le.(q)):
                __ zigzag:
                    node _ q.pop()
                    level.ap..(node.val)
                    __ node.right:
                        q.appendleft(node.right)
                    __ node.left:
                        q.appendleft(node.left)

                ____
                    node _ q.popleft()
                    level.ap..(node.val)
                    __ node.left:
                        q.ap..(node.left)
                    __ node.right:
                        q.ap..(node.right)
            res.ap..(level)
            zigzag _ no. zigzag

        r_ res
