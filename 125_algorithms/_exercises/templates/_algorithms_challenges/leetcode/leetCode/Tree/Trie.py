"""
前缀树又叫字典树，该树会覆盖多个相同的字符以形成空间上的优势。

如：
rat 与 rain
  r
  a
t  i
   n
最终会形成这样的树。

字典树有多种实现方式，下面直接用了列表（数组）来实现。
测试用例：
https://leetcode.com/problems/implement-trie-prefix-tree/description/

使用Python 中的字典可以直接形成这种树，所以弃用这种方式，用类的思路实现了一下。

"""

c.. TrieNode o..
    # __slots__ 考虑到TrieNode会大量创建，使用 __slot__来减少内存的占用。
    # 在测试的15个例子中：
    # 使用 __slots__会加快创建，平均的耗时为290ms-320ms。
    # 而不使用则在 340ms-360ms之间。
    # 创建的越多效果越明显。
    # 当然，使用字典而不是类的方式会更加更加更加高效。
    __slots__ = {'value', 'nextNodes', 'breakable'}

    ___ __init__  value, nextNode=None
        self.value = value
        __ nextNode:
            self.nextNodes = [nextNode]
        ____
            self.nextNodes   # list
        self.breakable = F..
    
    ___ addNext  nextNode
        self.nextNodes.a.. nextNode)
    
    ___ setBreakable  enable
        self.breakable = enable
    
    ___ __eq__  other
        r_ self.value __ other

    
        
c.. Trie o..

    ___ __init__(self
        """
        Initialize your data structure here.
        """
        self.root   # list
        

    ___ insert  word
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.makeATrieNodes(word)

    ___ search  word
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ___ i __ self.root:
            __ i __ word[0]:
            
                r_ self._search(i, word[1:])
        r_ F..
    
    ___ _search  root, word
        __ n.. word:
            __ root.breakable:
                r_ True
            r_ F..
        __ n.. root.nextNodes:
            r_ F..
        
        ___ i __ root.nextNodes:
            __ i __ word[0]:
                r_ self._search(i, word[1:])
        
        r_ F..

    ___ startsWith  prefix
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ___ i __ self.root:
            __ i __ prefix[0]:
                r_ self._startWith(i, prefix[1:])
        r_ F..
    
    ___ _startWith  root, prefix
        __ n.. prefix:
            r_ True
        
        __ n.. root.nextNodes:
            r_ F..
        
        ___ i __ root.nextNodes:
            __ i __ prefix[0]:
                r_ self._startWith(i, prefix[1:])
        
        r_ F..
        
    ___ makeATrieNodes  word
        ___ j __ self.root:
            __ word[0] __ j:
                rootWord = j
                ______
        ____

            rootWord = TrieNode(word[0])
            self.root.a.. rootWord)
            ___ i __ word[1:]:
                nextNode = TrieNode(i)
                rootWord.addNext(nextNode)
                rootWord = nextNode
            rootWord.setBreakable(True)
            r_
        
        # has the letter. 
        word = word[1:]
        _____ 1:
            __ n.. word:
                rootWord.setBreakable(True)
                ______
                
            ___ i __ rootWord.nextNodes:
                __ i __ word[0]:
                    rootWord = i
                    word = word[1:]
                    ______
            ____
                ___ i __ word:
                    nextNode = TrieNode(i)
                    rootWord.addNext(nextNode)
                    rootWord = nextNode
                rootWord.setBreakable(True)
                ______