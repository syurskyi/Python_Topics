'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object):
    ___ __init__(self, x, left=N.., right_ N..
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    ___ findTarget(self, root, k):
        r.. self.dfs(root, set(), k)
    
    ___ dfs(self, root, hashset, k):
        __ n.. root:
            r.. False
        __ k-root.val __ hashset:
            r.. True
        hashset.add(root.val)
        r.. self.dfs(root.left, hashset, k) o.\
            self.dfs(root.right, hashset, k)
    
    ___ findTargetSpace(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        __ n.. root: r.. False
        arr    # list
        stack    # list
        node = root
        while node:
            stack.a..(node)
            node = node.left
        while stack:
            node = stack.pop()
            arr.a..(node.val)
            node0 = node.right
            while node0:
                stack.a..(node0)
                node0 = node0.left
        i, j = 0, l..(arr)-1
        while i < j:
            __ k __ arr[i]+arr[j]:
                r.. True
            ____ k > arr[i]+arr[j]:
                i += 1
            ____:
                j -= 1
        r.. False
    
    ___ test(self):
        testCases = [
            [
                TreeNode(2, TreeNode(1), TreeNode(3)),
                4,
            ],
            [
                TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, N.., TreeNode(7))),
                9
            ],
            [
                TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, N.., TreeNode(7))),
                28,
            ],
        ]
        ___ root, k __ testCases:
            result = self.findTarget(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
