c_ Solution o..
    ___ findSubstring  s, words
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ls = l.. s)
        word_ls = l.. words[0])
        target_dict  # dict
        # create a targe dict for match
        ___ word __ words:
            try:
                target_dict[word] += 1
            except KeyError:
                target_dict[word] = 1
        res =    # list
        ___ start __ r.. ls - word_ls * l.. words) + 1
            curr_dict = target_dict.copy()
            ___ pos __ r.. start, start + word_ls * l.. words), word_ls
                curr = s[pos:pos + word_ls]
                try:
                    curr_dict[curr] -= 1
                    # word appears more than target
                    __ curr_dict[curr] < 0:
                        ______
                except KeyError:
                    # word not in words
                    ______
            ____
                # all word in target dict
                res.append(start)
        r_ res

    # def findSubstring(self, s, words):
    #     # https://leetcode.com/discuss/87745/3-line-python-solution-sorted-hash-112ms
    #     wLen, wtLen, wSet, sortHash, sLen = len(words[0]), len(words[0]) * len(words), set(words), sorted(
    #         [hash(w) for w in words]), len(s)
    #     h = [hash(s[i:i + wLen]) if s[i:i + wLen] in wSet else None for i in xrange(sLen - wLen + 1)]
    #     return [i for i in xrange(sLen - wtLen + 1) if h[i] and sorted(h[i: i + wtLen: wLen]) == sortHash]

__ ____ __ ____
    s  ?
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "good"])

    # [6,9,12]




