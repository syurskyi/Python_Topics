'''
Created on Oct 4, 2017

@author: MT
'''
# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Solution(object
    ___ findTarget(self, root, k
        r_ self.dfs(root, set(), k)
    
    ___ dfs(self, root, hashset, k
        __ not root:
            r_ False
        __ k-root.val in hashset:
            r_ True
        hashset.add(root.val)
        r_ self.dfs(root.left, hashset, k) or\
            self.dfs(root.right, hashset, k)
    
    ___ findTargetSpace(self, root, k
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        __ not root: r_ False
        arr = []
        stack = []
        node = root
        w___ node:
            stack.append(node)
            node = node.left
        w___ stack:
            node = stack.pop()
            arr.append(node.val)
            node0 = node.right
            w___ node0:
                stack.append(node0)
                node0 = node0.left
        i, j = 0, le.(arr)-1
        w___ i < j:
            __ k __ arr[i]+arr[j]:
                r_ True
            ____ k > arr[i]+arr[j]:
                i += 1
            ____
                j -= 1
        r_ False
    
    ___ test(self
        testCases = [
            [
                TreeNode(2, TreeNode(1), TreeNode(3)),
                4,
            ],
            [
                TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))),
                9
            ],
            [
                TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))),
                28,
            ],
        ]
        for root, k in testCases:
            result = self.findTarget(root, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
