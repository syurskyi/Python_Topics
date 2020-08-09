'''
Created on Mar 9, 2017

@author: MT
'''

# Definition for a binary tree node.
class TreeNode(object
    ___ __init__(self, x, left=None, right=None
        self.val = x
        self.left = left
        self.right = right

class Codec:
    ___ serialize(self, root
        stack = [root]
        result = ''
        w___ stack:
            node = stack.pop()
            __ node:
                result += '%s,' % (node.val)
                stack.append(node.right)
                stack.append(node.left)
            ____
                result += '#,'
        r_ result[:-1]
    
    ___ deserialize(self, data
        arr = data.split(',')
        ind = [0]
        root = self.helper(arr, ind)
        r_ root
    
    ___ helper(self, arr, ind
        __ arr[ind[0]] __ '#':
            r_ None
        root = TreeNode(arr[ind[0]])
        ind[0]+=1
        root.left = self.helper(arr, ind)
        ind[0]+=1
        root.right = self.helper(arr, ind)
        r_ root

__ __name__ __ '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    s = codec.serialize(root)
    print('s: %s' % (s))
    root = codec.deserialize(s)
    
    queue = [root]
    line = []
    nextQueue= []
    w___ queue:
        node = queue.pop(0)
        line.append(node.val)
        __ node.left:
            nextQueue.append(node.left)
        __ node.right:
            nextQueue.append(node.right)
        __ not queue:
            print(line)
            line = []
            queue = nextQueue
            nextQueue = []
        
    