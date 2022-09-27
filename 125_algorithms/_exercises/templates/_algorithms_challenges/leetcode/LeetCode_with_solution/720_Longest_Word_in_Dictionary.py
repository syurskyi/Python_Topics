c_ Solution o..
    # def longestWord(self, words):
    #     words.sort()
    #     words_set, longest_word = set(['']), ''
    #     for word in words:
    #         if word[:-1] in words_set:
    #             words_set.add(word)
    #             if len(word) > len(longest_word):
    #                 longest_word = word
    #     return longest_word

    # def longestWord(self, words):
    #     ans = ""
    #     wordset = set(words)
    #     for word in words:
    #         if len(word) > len(ans) or len(word) == len(ans) and word < ans:
    #             if all(word[:k] in wordset for k in xrange(1, len(word))):
    #                 ans = word
    #     return ans

    ___ longestWord  words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = T..
        ___ i, word __ e.. words):
            reduce(dict.-g, word, trie)[END] = i
        stack = trie.values()
        ans = ""
        w.. stack:
            cur = stack.pop()
            __ END __ cur:
                word = words[cur[END]]
                __ l.. word) > l.. ans) or l.. word) __ l.. ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] ___ letter __ cur __ letter != END])
        r_ ans
