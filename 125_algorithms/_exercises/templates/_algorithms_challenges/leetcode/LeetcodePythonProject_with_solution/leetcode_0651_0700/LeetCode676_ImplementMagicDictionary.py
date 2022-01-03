'''
Created on Oct 18, 2017

@author: MT
'''
c_ TreeNode(object):
    ___ - , val):
        val = val
        children    # dict
        isLeaf = F..

c_ MagicDictionary(object):

    ___ - ):
        """
        Initialize your data structure here.
        """
        root = TreeNode(N..)

    ___ buildDict(self, d..):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        root = TreeNode(N..)
        ___ word __ d..:
            node = root
            ___ c __ word:
                __ c n.. __ node.children:
                    newNode = TreeNode(c)
                    node.children[c] = newNode
                node = node.children[c]
            node.isLeaf = T..

    ___ s..(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        r.. helper(root, word, 0, F..)
    
    ___ helper(self, node, word, ind, diffFlag):
        __ n.. node: r.. F..
        __ ind __ l..(word):
            __ node.isLeaf a.. diffFlag:
                r.. T..
            r.. F..
        c = word[ind]
        ___ c0 __ node.children:
            __ c0 != c a.. diffFlag:
                continue
            __ helper(node.children.get(c, N..), word, ind+1, diffFlag) o.\
                (c0 != c a.. helper(node.children[c0], word, ind+1, T..)):
                r.. T..
        r.. F..

__ __name__ __ '__main__':
    magicDict = MagicDictionary()
    magicDict.buildDict(['hello', 'leetcode', 'hallo'])
    print(magicDict.s..('hello'))
    print(magicDict.s..('hhllo'))
    print(magicDict.s..('hell'))
    print(magicDict.s..('leetcoded'))
