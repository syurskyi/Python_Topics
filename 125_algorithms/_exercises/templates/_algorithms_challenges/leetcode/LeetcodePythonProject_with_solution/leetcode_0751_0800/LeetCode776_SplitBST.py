'''
Created on Apr 8, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=None, right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        __ not root: return [None, None]
        stack = []
        root0 = root
        while root0:
            stack.append(root0)
            root0 = root0.left
        preNode = None
        while stack:
            node = stack.pop()
            __ (not preNode and V < node.val)\
                or (preNode and preNode.val <= V < node.val):
                return self.getRes(root, preNode)
            else:
                preNode = node
                node0 = node.right
                while node0:
                    stack.append(node0)
                    node0 = node0.left
        return [root, None]
    
    ___ getRes(self, root, node):
        root0 = root
        __ not node:
            return [root0, None]
        stack = []
        while node != root0:
            stack.append(root0)
            __ root0.val > node.val:
                root0 = root0.left
            else:
                root0 = root0.right
        cand = node
        while stack and stack[-1].val < node.val:
            cand = stack.pop()
        __ not stack:
            right = node.right
            node.right = None
            return [root, right]
        else:
            right = node.right
            node.right = None
            stack[-1].left = right
            return [root, cand]
    
    ___ test(self):
        testCases = [
            [
                TreeNode(4,
                         TreeNode(2, TreeNode(1), TreeNode(3)),
                         TreeNode(6, TreeNode(5), TreeNode(7)),
                        ),
                2,
            ],
            [
                TreeNode(4,
                         TreeNode(2, TreeNode(1), TreeNode(3)),
                         TreeNode(6, TreeNode(5), TreeNode(7)),
                        ),
                3,
            ],
        ]
        for root, v in testCases:
            result = self.splitBST(root, v)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
