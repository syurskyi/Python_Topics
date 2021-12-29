'''
Created on Apr 8, 2018

@author: tongq
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
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
        __ n.. root: r.. [N.., N..]
        stack    # list
        root0 = root
        w.... root0:
            stack.a..(root0)
            root0 = root0.left
        preNode = N..
        w.... stack:
            node = stack.pop()
            __ (n.. preNode a.. V < node.val)\
                o. (preNode a.. preNode.val <= V < node.val):
                r.. self.getRes(root, preNode)
            ____:
                preNode = node
                node0 = node.right
                w.... node0:
                    stack.a..(node0)
                    node0 = node0.left
        r.. [root, N..]
    
    ___ getRes(self, root, node):
        root0 = root
        __ n.. node:
            r.. [root0, N..]
        stack    # list
        w.... node != root0:
            stack.a..(root0)
            __ root0.val > node.val:
                root0 = root0.left
            ____:
                root0 = root0.right
        cand = node
        w.... stack a.. stack[-1].val < node.val:
            cand = stack.pop()
        __ n.. stack:
            right = node.right
            node.right = N..
            r.. [root, right]
        ____:
            right = node.right
            node.right = N..
            stack[-1].left = right
            r.. [root, cand]
    
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
        ___ root, v __ testCases:
            result = self.splitBST(root, v)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
