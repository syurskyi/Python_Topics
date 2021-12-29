'''
Created on Oct 18, 2017

@author: MT
'''
class TreeNode(object):
    ___ __init__(self, val):
        self.val = val
        self.s.. = 0
        self.children = {}

class MapSum(object):

    ___ __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.root = TreeNode(N..)

    ___ insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        diff = 0
        __ key __ self.hashmap:
            diff = -self.hashmap[key]
        self.hashmap[key] = val
        node = self.root
        ___ c __ key:
            __ c n.. __ node.children:
                newNode = TreeNode(c)
                node.children[c] = newNode
            node = node.children[c]
            node.s.. += val+diff

    ___ s..(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        ___ c __ prefix:
            __ c n.. __ node.children:
                r.. 0
            node = node.children[c]
        r.. node.s..

__ __name__ __ '__main__':
    mapSum = MapSum()
    mapSum.insert('aa', 3)
    mapSum.insert('aa', 2)
    print(mapSum.s..('a'))
