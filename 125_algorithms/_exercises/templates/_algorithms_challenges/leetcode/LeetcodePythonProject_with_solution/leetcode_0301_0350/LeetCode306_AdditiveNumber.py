'''
Created on Mar 11, 2017

@author: MT
'''

c_ STreeNode(o..
    ___ - , left, right, sumVal=0
        start left
        end right
        sumVal sumVal
        leftChild N..
        rightChild N..

c_ NumArray(o..
    ___ - , nums
        __ n.. nums:
            root N..
        ____
            root buildTree(nums, 0, l..(nums)-1)
    
    ___ buildTree  nums, i, j
        __ n.. nums o. i > j:
            r.. N..
        __ i __ j:
            r.. STreeNode(i, j, nums[i])
        curr STreeNode(i, j)
        mid i+(j-i)//2
        curr.leftChild buildTree(nums, i, mid)
        curr.rightChild buildTree(nums, mid+1, j)
        curr.sumVal curr.leftChild.sumVal + curr.rightChild.sumVal
        r.. curr
    
    ___ update  i, val
        updateHelper(root, i, val)
    
    ___ updateHelper  root, i, val
        __ n.. root:
            r..
        mid root.start+(root.end-root.start)//2
        __ i <_ mid:
            updateHelper(root.leftChild, i, val)
        ____
            updateHelper(root.rightChild, i, val)
        __ root.start __ i a.. root.end __ i:
            root.sumVal val
            r..
        root.sumVal root.leftChild.sumVal + root.rightChild.sumVal
    
    ___ sumRange  i, j
        r.. sumRangeHelper(root, i, j)
    
    ___ sumRangeHelper  root, i, j
        __ n.. root o. i > j o. j < root.start o. i > root.end:
            r.. 0
        __ i __ root.start a.. j __ root.end:
            r.. root.sumVal
        mid root.start + (root.end-root.start)//2
        result sumRangeHelper(root.leftChild, i, m..(j, mid +\
            sumRangeHelper(root.rightChild, m..(i, mid+1), j)
        r.. result
    