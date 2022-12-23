"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
Note:
You may assume that all inputs are consist of lowercase letters a-z.

I 的升级版。
I 中只需要找一个单词是否存在。

II 中升级为找很多单词。


直接扩展 I 的话对重复比较多的单词会TLE，
比如 aaaa,aaaab,aaaac,aaaae ...

这样的都有共同的前缀，aaaa，基于这个条件，可以用前缀树来将它们整合在一起，省去重复搜索 aaaa 的步骤。

前缀树可以用字典（哈希表）来模拟。
```
trie = {}

for w in words:
    # 从根字典开始。
    t = trie

    # leetcode
    for l in w:
        # 若当前前缀不在这个前缀树字典中，则创建为一个新的前缀树字典。
        # 'l' not in t
        # t -> {'l': {}
        # }
        if l not in t:
            t[l] = {}
        # 下一次循环的为 'l' 下的 'e'
        # 所以替换为 t['l']
        t = t[l]
    # 这里添加一个标记，表示当前前缀树可以是末尾。
    # 如 leet 和 leetcode 可以在 leet 处结束。
    t['mark'] = 'mark'

```
之后的操作基本一样，只是把字符串换成了字典。

这里有个有趣的点，下面的写法会有重复的数据进去，
如果结果一开始用 set，添加时可以直接去重，效率是比不过先用 list 再用 set 去重的。

beat:
46%

测试地址：
https://leetcode.com/problems/word-search-ii/description/

前面的思路都是同一种思路，也就是可以优化。

"""
c.. Solution o..
    ___ findWords  board, words
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        result   # list
        words = s..(words)
        
        trie _ # dict
        ___ i __ words:
            t = trie
            ___ x __ i:
                __ x n.. __ t:
                    t[x] _ # dict
                t = t[x]
            t['!'] = '!'
            
        ___ find(board, x, y, word, pre
            # print(word)
            __ '!' __ word:
                result.a.. pre)

            ___ w __ word:
                raw = board[y][x]
                board[y][x] = 0

                # up
                __ y-1 >= 0 a.. board[y-1][x] __ w:
                    find(board, x, y-1, word[w], pre+w)
                # down
                __ y+1 < l..(board) a.. board[y+1][x] __ w:
                    find(board, x, y+1, word[w], pre+w)

                # left
                __ x-1 >= 0 a.. board[y][x-1] __ w:
                    find(board, x-1, y, word[w], pre+w)

                # right
                __ x+1 < l..(board[0]) a.. board[y][x+1] __ w:
                    find(board, x+1, y, word[w], pre+w)

                board[y][x] = raw      

        maps _ # dict
        
        ___ i __ r..(l..(board)):
            ___ j __ r..(l..(board[0])):
                try:
                    maps[board[i][j]].append((i,j))
                except:
                    maps[board[i][j]] = [(i,j)]

        ___ i __ trie:
            __ maps.get(i
                xy = maps.get(i)
                ___ j __ xy:
                    find(board, j[1], j[0], trie[i], i)
        r_ list(s..(result))
