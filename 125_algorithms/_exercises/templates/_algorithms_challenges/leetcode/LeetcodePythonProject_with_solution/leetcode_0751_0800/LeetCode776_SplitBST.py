'''
Created on Apr 8, 2018

@author: tongq
'''
# Definition for a binary tree node.
c_ TreeNode(o..
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Solution(o..
    ___ splitBST  root, V
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
                o. (preNode a.. preNode.val <= V < node.val
                r.. getRes(root, preNode)
            ____:
                preNode = node
                node0 = node.right
                w.... node0:
                    stack.a..(node0)
                    node0 = node0.left
        r.. [root, N..]
    
    ___ getRes  root, node
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
    
    ___ test
        testCases = [
            [
                TreeNode(4,
                         TreeNode(2, TreeNode(1), TreeNode(3,
                         TreeNode(6, TreeNode(5), TreeNode(7,
                        ),
                2,
            ],
            [
                TreeNode(4,
                         TreeNode(2, TreeNode(1), TreeNode(3,
                         TreeNode(6, TreeNode(5), TreeNode(7,
                        ),
                3,
            ],
        ]
        ___ root, v __ testCases:
            result = splitBST(root, v)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
