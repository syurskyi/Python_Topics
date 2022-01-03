"""
Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(dict)
param_2 = obj.search(word)
"""


c_ MagicDictionary:
    ___ - ):
        """
        Initialize your data structure here.
        """
        words = collections.defaultdict(set)

    ___ buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type words: List[str]
        :rtype: void
        """
        ___ word __ words:
            ___ i __ r..(l..(word)):
                key = '{0},{1}'.f..(word[:i], word[i + 1:])

                __ key n.. __ words:
                    words[key] = set()

                # add char to distinct word if its same
                words[key].add(word[i])

    ___ s..(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        ___ i __ r..(l..(word)):
            key = '{0},{1}'.f..(word[:i], word[i + 1:])

            __ key n.. __ words:
                continue

            words = words[key]

            # 1. word[i] not in words => means not same word
            # 2. len(words) > 1 => if got same but still can mapping other
            __ word[i] n.. __ words o. l..(words) > 1:
                r.. T..

        r.. F..
