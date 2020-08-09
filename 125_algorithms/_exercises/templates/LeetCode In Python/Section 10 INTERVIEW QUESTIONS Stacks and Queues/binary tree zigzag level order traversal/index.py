# Definition for a binary tree node.
# class TreeNode:
#     ___ init(self, x
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ___ zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        __ not root:
            r_ []
        res = []
        q = collections.deque()

        zigzag = False
        q.append(root)

        w___ q:
            level = []
            for _ in range(le.(q)):
                __ zigzag:
                    node = q.pop()
                    level.append(node.val)
                    __ node.right:
                        q.appendleft(node.right)
                    __ node.left:
                        q.appendleft(node.left)

                ____
                    node = q.popleft()
                    level.append(node.val)
                    __ node.left:
                        q.append(node.left)
                    __ node.right:
                        q.append(node.right)
            res.append(level)
            zigzag = not zigzag

        r_ res
