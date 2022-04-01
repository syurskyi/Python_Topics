'''
Created on Apr 15, 2017

@author: MT
'''
____ lib2to3.pytree _______ Node

c_ TrieNode(o..):
    ___ - , val):
        val = val
        children    # dict
        candidates = s..()

c_ Solution(o..):
    ___ wordSquares  words):
        __ n.. words: r.. []
        root = TrieNode(-1)
        buildTrie(words)
        res    # list
        dfs(words, [], res, words)
        r.. res
    
    ___ dfs  words, elems, result, nextWords):
        __ l..(elems) __ l..(words[0]):
            result.a..(l..(elems))
            r..
        ___ word __ nextWords:
            elems.a..(word)
            __ l..(elems) < l..(words[0]):
                prefix = ''
                ___ i __ r..(l..(elems)):
                    prefix += elems[i][l..(elems)]
                candidates = wordsWithPrefix(prefix)
            ____:
                candidates    # list
            dfs(words, elems, result, candidates)
            elems.pop()
    
    ___ buildTrie  words):
        root.candidates = words
        ___ word __ words:
            children = root.children
            ___ c __ word:
                __ c __ children:
                    node = children[c]
                ____:
                    node = TrieNode(c)
                    children[c] = node
                node.candidates.add(word)
                children = node.children
    
    ___ wordsWithPrefix  prefix):
        __ n.. prefix: r.. []
        children = root.children
        ___ i, c __ e..(prefix):
            __ c __ children:
                node = children[c]
                __ i __ l..(prefix)-1:
                    r.. l..(node.candidates)
                ____:
                    children = node.children
            ____:
                r.. []
        r.. []
    
    ___ test
        testCases = [
            ["area","lead","wall","lady","ball"],
            ["abat","baba","atan","atal"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = wordSquares(words)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
