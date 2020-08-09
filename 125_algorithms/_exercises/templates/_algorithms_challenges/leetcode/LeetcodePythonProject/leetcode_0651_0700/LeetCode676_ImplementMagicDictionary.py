'''
Created on Oct 18, 2017

@author: MT
'''
class TreeNode(object
    ___ __init__(self, val
        self.val = val
        self.children = {}
        self.isLeaf = False

class MagicDictionary(object

    ___ __init__(self
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    ___ buildDict(self, dict
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.root = TreeNode(None)
        for word in dict:
            node = self.root
            for c in word:
                __ c not in node.children:
                    newNode = TreeNode(c)
                    node.children[c] = newNode
                node = node.children[c]
            node.isLeaf = True

    ___ search(self, word
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        r_ self.helper(self.root, word, 0, False)
    
    ___ helper(self, node, word, ind, diffFlag
        __ not node: r_ False
        __ ind __ le.(word
            __ node.isLeaf and diffFlag:
                r_ True
            r_ False
        c = word[ind]
        for c0 in node.children:
            __ c0 != c and diffFlag:
                continue
            __ self.helper(node.children.get(c, None), word, ind+1, diffFlag) or\
                (c0 != c and self.helper(node.children[c0], word, ind+1, True)):
                r_ True
        r_ False

__ __name__ __ '__main__':
    magicDict = MagicDictionary()
    magicDict.buildDict(['hello', 'leetcode', 'hallo'])
    print(magicDict.search('hello'))
    print(magicDict.search('hhllo'))
    print(magicDict.search('hell'))
    print(magicDict.search('leetcoded'))
