c_ Solution o..
    ___ wordPattern  pattern, s..
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        __ pattern is N.. or s.. is N..:
            r_ T..
        # double map
        words_to_pattern  # dict
        pattern_to_words  # dict
        word_list = s...split(' ')
        __ l.. word_list) != l.. pattern
            r_ F..
        ___ index, word __ e.. word_list
            curr_p = pattern[index]
            __ pattern_to_words.get(curr_p, word) != word or words_to_pattern.get(word, curr_p) != curr_p:
                r_ F..
            pattern_to_words[curr_p] = pattern_to_words.get(curr_p, word)
            words_to_pattern[word] = words_to_pattern.get(word, curr_p)
        r_ T..