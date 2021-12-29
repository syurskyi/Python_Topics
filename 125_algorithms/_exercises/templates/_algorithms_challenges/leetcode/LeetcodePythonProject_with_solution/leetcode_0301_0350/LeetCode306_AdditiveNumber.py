'''
Created on Mar 11, 2017

@author: MT
'''

class STreeNode(object):
    ___ __init__(self, left, right, sumVal=0):
        self.start = left
        self.end = right
        self.sumVal = sumVal
        self.leftChild = N..
        self.rightChild = N..

class NumArray(object):
    ___ __init__(self, nums):
        __ n.. nums:
            self.root = N..
        ____:
            self.root = self.buildTree(nums, 0, l..(nums)-1)
    
    ___ buildTree(self, nums, i, j):
        __ n.. nums o. i > j:
            r.. N..
        __ i __ j:
            r.. STreeNode(i, j, nums[i])
        curr = STreeNode(i, j)
        mid = i+(j-i)//2
        curr.leftChild = self.buildTree(nums, i, mid)
        curr.rightChild = self.buildTree(nums, mid+1, j)
        curr.sumVal = curr.leftChild.sumVal + curr.rightChild.sumVal
        r.. curr
    
    ___ update(self, i, val):
        self.updateHelper(self.root, i, val)
    
    ___ updateHelper(self, root, i, val):
        __ n.. root:
            r..
        mid = root.start+(root.end-root.start)//2
        __ i <= mid:
            self.updateHelper(root.leftChild, i, val)
        ____:
            self.updateHelper(root.rightChild, i, val)
        __ root.start __ i a.. root.end __ i:
            root.sumVal = val
            r..
        root.sumVal = root.leftChild.sumVal + root.rightChild.sumVal
    
    ___ sumRange(self, i, j):
        r.. self.sumRangeHelper(self.root, i, j)
    
    ___ sumRangeHelper(self, root, i, j):
        __ n.. root o. i > j o. j < root.start o. i > root.end:
            r.. 0
        __ i __ root.start a.. j __ root.end:
            r.. root.sumVal
        mid = root.start + (root.end-root.start)//2
        result = self.sumRangeHelper(root.leftChild, i, m..(j, mid)) +\
            self.sumRangeHelper(root.rightChild, max(i, mid+1), j)
        r.. result
    