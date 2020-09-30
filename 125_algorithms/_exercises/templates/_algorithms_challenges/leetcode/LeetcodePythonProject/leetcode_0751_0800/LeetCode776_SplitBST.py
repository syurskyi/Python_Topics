'''
Created on Apr 8, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ splitBST(self, root, V
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        __ not root: r_ [None, None]
        stack =   # list
        root0 = root
        w___ root0:
            stack.append(root0)
            root0 = root0.left
        preNode = None
        w___ stack:
            node = stack.p..
            __ (not preNode and V < node.val)\
                or (preNode and preNode.val <= V < node.val
                r_ self.getRes(root, preNode)
            ____
                preNode = node
                node0 = node.right
                w___ node0:
                    stack.append(node0)
                    node0 = node0.left
        r_ [root, None]
    
    ___ getRes(self, root, node
        root0 = root
        __ not node:
            r_ [root0, None]
        stack =   # list
        w___ node != root0:
            stack.append(root0)
            __ root0.val > node.val:
                root0 = root0.left
            ____
                root0 = root0.right
        cand = node
        w___ stack and stack[-1].val < node.val:
            cand = stack.p..
        __ not stack:
            right = node.right
            node.right = None
            r_ [root, right]
        ____
            right = node.right
            node.right = None
            stack[-1].left = right
            r_ [root, cand]
    
    ___ test(self
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
        ___ root, v __ testCases:
            result = self.splitBST(root, v)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
