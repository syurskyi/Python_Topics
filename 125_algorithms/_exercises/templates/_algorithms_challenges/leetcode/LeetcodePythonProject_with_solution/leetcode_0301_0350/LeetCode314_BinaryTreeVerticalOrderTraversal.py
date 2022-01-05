'''
Created on Mar 15, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x):
        val = x
        left = N..
        right = N..

c_ Solution(object):
    ___ verticalOrder  root):
        __ n.. root: r.. []
        hashmap    # dict
        result    # list
        queue = [(0, root)]
        minLevel, maxLevel = 0, 0
        w.... queue:
            level, node = queue.pop(0)
            maxLevel = m..(maxLevel, level)
            minLevel = m..(minLevel, level)
            __ level n.. __ hashmap:
                hashmap[level] = [node.val]
            ____:
                hashmap[level].a..(node.val)
            __ node.left:
                queue.a..((level-1, node.left))
            __ node.right:
                queue.a..((level+1, node.right))
        ___ i __ r..(minLevel, maxLevel+1):
            result.a..(hashmap[i])
        r.. result
    
    