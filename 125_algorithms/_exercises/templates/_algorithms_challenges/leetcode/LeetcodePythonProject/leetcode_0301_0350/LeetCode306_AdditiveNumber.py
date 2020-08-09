'''
Created on Mar 11, 2017

@author: MT
'''

class STreeNode(object
    ___ __init__(self, left, right, sumVal=0
        self.start = left
        self.end = right
        self.sumVal = sumVal
        self.leftChild = None
        self.rightChild = None

class NumArray(object
    ___ __init__(self, nums
        __ not nums:
            self.root = None
        ____
            self.root = self.buildTree(nums, 0, le.(nums)-1)
    
    ___ buildTree(self, nums, i, j
        __ not nums or i > j:
            r_ None
        __ i __ j:
            r_ STreeNode(i, j, nums[i])
        curr = STreeNode(i, j)
        mid = i+(j-i)//2
        curr.leftChild = self.buildTree(nums, i, mid)
        curr.rightChild = self.buildTree(nums, mid+1, j)
        curr.sumVal = curr.leftChild.sumVal + curr.rightChild.sumVal
        r_ curr
    
    ___ update(self, i, val
        self.updateHelper(self.root, i, val)
    
    ___ updateHelper(self, root, i, val
        __ not root:
            r_
        mid = root.start+(root.end-root.start)//2
        __ i <= mid:
            self.updateHelper(root.leftChild, i, val)
        ____
            self.updateHelper(root.rightChild, i, val)
        __ root.start __ i and root.end __ i:
            root.sumVal = val
            r_
        root.sumVal = root.leftChild.sumVal + root.rightChild.sumVal
    
    ___ sumRange(self, i, j
        r_ self.sumRangeHelper(self.root, i, j)
    
    ___ sumRangeHelper(self, root, i, j
        __ not root or i > j or j < root.start or i > root.end:
            r_ 0
        __ i __ root.start and j __ root.end:
            r_ root.sumVal
        mid = root.start + (root.end-root.start)//2
        result = self.sumRangeHelper(root.leftChild, i, min(j, mid)) +\
            self.sumRangeHelper(root.rightChild, max(i, mid+1), j)
        r_ result
    