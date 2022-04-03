'''
Created on Oct 18, 2017

@author: MT
'''
c_ TreeNode(o..
    ___ - , val
        val = val
        children    # dict
        isLeaf = F..

c_ MagicDictionary(o..

    ___ -
        """
        Initialize your data structure here.
        """
        root = TreeNode(N..)

    ___ buildDict  d..
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

    ___ s..  word
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        r.. helper(root, word, 0, F..)
    
    ___ helper  node, word, ind, diffFlag
        __ n.. node: r.. F..
        __ ind __ l..(word
            __ node.isLeaf a.. diffFlag:
                r.. T..
            r.. F..
        c = word[ind]
        ___ c0 __ node.children:
            __ c0 != c a.. diffFlag:
                _____
            __ helper(node.children.g.. c, N..), word, ind+1, diffFlag) o.\
                (c0 != c a.. helper(node.children[c0], word, ind+1, T..)):
                r.. T..
        r.. F..

__ _____ __ _____
    magicDict = MagicDictionary()
    magicDict.buildDict( 'hello', 'leetcode', 'hallo' )
    print(magicDict.s..('hello'))
    print(magicDict.s..('hhllo'))
    print(magicDict.s..('hell'))
    print(magicDict.s..('leetcoded'))
