'''
Created on Mar 15, 2017

@author: MT
'''

class TreeNode(object
    ___ __init__(self, val, num=1
        self.val = val
        self.num = num
        self.left = None
        self.right = None
    
    ___ __str__(self
        r_ '<val: %s, num: %s>' % (self.val, self.num)
    
    ___ __repr__(self
        r_ self.__str__()

class Solution(object
    ___ countSmaller(self, nums
        __ not nums: r_ []
        root = TreeNode(nums[-1])
        result = [0]
        ___ i in range(le.(nums)-2, -1, -1
            result.insert(0, self.getVal(root, nums[i], 0))
        r_ result, root
    
    ___ getVal(self, root, val, num
        __ root.val >= val:
            root.num += 1
            __ not root.left:
                root.left = TreeNode(val)
                r_ num
            ____
                r_ self.getVal(root.left, val, num)
        ____
            num += root.num
            __ not root.right:
                root.right = TreeNode(val)
                r_ num
            ____
                r_ self.getVal(root.right, val, num)
    
    ___ test(self
        testCases = [
            [5, 2, 6, 1],
            [-1, -1],
            [3, 2, 2, 6, 1],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result, root = self.countSmaller(nums)
            print('result: %s' % (result))
            print('-='*20+'-')
            
            queue= [root]
            line = []
            nextQueue = []
            w___ queue:
                node = queue.pop(0)
                line.append(node)
                __ node.left:
                    nextQueue.append(node.left)
                __ node.right:
                    nextQueue.append(node.right)
                __ not queue:
                    queue = nextQueue
                    nextQueue = []
                    print(line)
                    line = []
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

