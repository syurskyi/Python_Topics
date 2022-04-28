c_ Solution o..
    ___ wordPattern  pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        __ pattern is N.. or str is N..:
            r_ True
        # double map
        words_to_pattern  # dict
        pattern_to_words  # dict
        word_list = str.split(' ')
        __ l.. word_list) != l.. pattern):
            r_ False
        ___ index, word __ e.. word_list):
            curr_p = pattern[index]
            __ pattern_to_words.get(curr_p, word) != word or words_to_pattern.get(word, curr_p) != curr_p:
                r_ False
            pattern_to_words[curr_p] = pattern_to_words.get(curr_p, word)
            words_to_pattern[word] = words_to_pattern.get(word, curr_p)
        r_ True