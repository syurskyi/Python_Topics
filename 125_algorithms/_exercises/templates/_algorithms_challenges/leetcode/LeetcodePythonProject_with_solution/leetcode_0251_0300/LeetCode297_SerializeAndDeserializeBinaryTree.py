'''
Created on Mar 9, 2017

@author: MT
'''

# Definition for a binary tree node.
c_ TreeNode(object):
    ___ - , x, left=N.., right_ N..
        val = x
        left = left
        right = right

c_ Codec:
    ___ serialize(self, root):
        stack = [root]
        result = ''
        w.... stack:
            node = stack.pop()
            __ node:
                result += '%s,' % (node.val)
                stack.a..(node.right)
                stack.a..(node.left)
            ____:
                result += '#,'
        r.. result[:-1]
    
    ___ deserialize(self, data):
        arr = data.s..(',')
        ind = [0]
        root = helper(arr, ind)
        r.. root
    
    ___ helper(self, arr, ind):
        __ arr[ind[0]] __ '#':
            r.. N..
        root = TreeNode(arr[ind[0]])
        ind[0]+=1
        root.left = helper(arr, ind)
        ind[0]+=1
        root.right = helper(arr, ind)
        r.. root

__ __name__ __ '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    s = codec.serialize(root)
    print('s: %s' % (s))
    root = codec.deserialize(s)
    
    queue = [root]
    line    # list
    nextQueue   # list
    w.... queue:
        node = queue.pop(0)
        line.a..(node.val)
        __ node.left:
            nextQueue.a..(node.left)
        __ node.right:
            nextQueue.a..(node.right)
        __ n.. queue:
            print(line)
            line    # list
            queue = nextQueue
            nextQueue    # list
        
    