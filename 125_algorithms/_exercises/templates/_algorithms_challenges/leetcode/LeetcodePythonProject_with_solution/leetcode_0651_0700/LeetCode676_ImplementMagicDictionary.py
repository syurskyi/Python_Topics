'''
Created on Oct 18, 2017

@author: MT
'''
class TreeNode(object):
    ___ __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False

class MagicDictionary(object):

    ___ __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(N..)

    ___ buildDict(self, d..):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.root = TreeNode(N..)
        ___ word __ d..:
            node = self.root
            ___ c __ word:
                __ c n.. __ node.children:
                    newNode = TreeNode(c)
                    node.children[c] = newNode
                node = node.children[c]
            node.isLeaf = True

    ___ search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        r.. self.helper(self.root, word, 0, False)
    
    ___ helper(self, node, word, ind, diffFlag):
        __ n.. node: r.. False
        __ ind __ l..(word):
            __ node.isLeaf and diffFlag:
                r.. True
            r.. False
        c = word[ind]
        ___ c0 __ node.children:
            __ c0 != c and diffFlag:
                continue
            __ self.helper(node.children.get(c, N..), word, ind+1, diffFlag) o.\
                (c0 != c and self.helper(node.children[c0], word, ind+1, True)):
                r.. True
        r.. False

__ __name__ __ '__main__':
    magicDict = MagicDictionary()
    magicDict.buildDict(['hello', 'leetcode', 'hallo'])
    print(magicDict.search('hello'))
    print(magicDict.search('hhllo'))
    print(magicDict.search('hell'))
    print(magicDict.search('leetcoded'))
