# Definition for a binary tree node.
# class TreeNode:
#     ___ init(self, x
#         self.val = x
#         self.left = None
#         self.right = None


c_ Solution:
    ___ zigzagLevelOrder(, root: TreeNode) -> L..[L..[int]]:
        __ no. root:
            r_ []
        res _ []
        q _ collections.deque()

        zigzag _ F..
        q.append(root)

        w___ q:
            level _ []
            ___ _ __ ra..(le.(q)):
                __ zigzag:
                    node _ q.pop()
                    level.append(node.val)
                    __ node.right:
                        q.appendleft(node.right)
                    __ node.left:
                        q.appendleft(node.left)

                ____
                    node _ q.popleft()
                    level.append(node.val)
                    __ node.left:
                        q.append(node.left)
                    __ node.right:
                        q.append(node.right)
            res.append(level)
            zigzag _ no. zigzag

        r_ res
