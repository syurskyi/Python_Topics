'''
Created on Feb 1, 2017

@author: MT
'''

c_ Solution(object):
    ___ levelOrder  root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result    # list
        __ n.. root: r.. result
        queue    # list
        nextQueue    # list
        elem    # list
        queue.a..(root)
        w.... queue:
            first = queue[0]
            elem.a..(first.val)
            del queue[0]
            __ first.left:
                nextQueue.a..(first.left)
            __ first.right:
                nextQueue.a..(first.right)
            __ n.. queue:
                result.a..(elem)
                elem    # list
                queue = nextQueue
                nextQueue    # list
        r.. result
