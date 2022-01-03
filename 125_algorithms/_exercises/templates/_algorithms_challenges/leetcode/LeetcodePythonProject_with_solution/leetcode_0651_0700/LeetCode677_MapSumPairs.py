'''
Created on Oct 18, 2017

@author: MT
'''
c_ TreeNode(object):
    ___ - , val):
        val = val
        s.. = 0
        children    # dict

c_ MapSum(object):

    ___ - ):
        """
        Initialize your data structure here.
        """
        hashmap    # dict
        root = TreeNode(N..)

    ___ insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        diff = 0
        __ key __ hashmap:
            diff = -hashmap[key]
        hashmap[key] = val
        node = root
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
        node = root
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
