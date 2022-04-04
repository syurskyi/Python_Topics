'''
Created on Sep 10, 2017

@author: MT
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ addOneRow  root, v, d
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        __ d __ 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            r.. newRoot
        level = 1
        queue = [root]
        w.... queue:
            num = l..(queue)
            ___ _ __ r..(num
                node = queue.p.. 0)
                __ node.left:
                    __ level __ d-1:
                        newNode = TreeNode(v)
                        node0 = node.left
                        node.left = newNode
                        newNode.left = node0
                        queue.a..(newNode)
                    ____
                        queue.a..(node.left)
                ____ level __ d-1:
                    node.left = TreeNode(v)
                    queue.a..(node.left)
                __ node.right:
                    __ level __ d-1:
                        newNode = TreeNode(v)
                        node0 = node.right
                        node.right = newNode
                        newNode.right = node0
                        queue.a..(newNode)
                    ____
                        queue.a..(node.right)
                ____ level __ d-1:
                    node.right = TreeNode(v)
                    queue.a..(node.right)
            level += 1
        r.. root
    
    ___ test
        testCases = [
            [
                TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1, TreeNode(6, TreeNode(5))),
                1,
                2
            ],
            [
                TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1))),
                1,
                3
            ],
        ]
        ___ root, v, d __ testCases:
            newRoot = addOneRow(root, v, d)
            print(newRoot.val)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
