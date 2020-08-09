'''
Created on Sep 10, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ addOneRow(self, root, v, d
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        __ d __ 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            r_ newRoot
        level = 1
        queue = [root]
        w___ queue:
            num = le.(queue)
            ___ _ in range(num
                node = queue.pop(0)
                __ node.left:
                    __ level __ d-1:
                        newNode = TreeNode(v)
                        node0 = node.left
                        node.left = newNode
                        newNode.left = node0
                        queue.append(newNode)
                    ____
                        queue.append(node.left)
                ____ level __ d-1:
                    node.left = TreeNode(v)
                    queue.append(node.left)
                __ node.right:
                    __ level __ d-1:
                        newNode = TreeNode(v)
                        node0 = node.right
                        node.right = newNode
                        newNode.right = node0
                        queue.append(newNode)
                    ____
                        queue.append(node.right)
                ____ level __ d-1:
                    node.right = TreeNode(v)
                    queue.append(node.right)
            level += 1
        r_ root
    
    ___ test(self
        testCases = [
            [
                TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5))),
                1,
                2
            ],
            [
                TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1))),
                1,
                3
            ],
        ]
        ___ root, v, d in testCases:
            newRoot = self.addOneRow(root, v, d)
            print(newRoot.val)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
