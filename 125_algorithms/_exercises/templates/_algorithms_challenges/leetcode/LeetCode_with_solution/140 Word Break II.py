"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid
dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
__author__ 'Danyang'
____ c.. _______ d..


c_ Solution:
    ___ wordBreak  s, d..
        """
        .______   .______       _______  _______  __  ___   ___  _______     _______.
        |   _  \  |   _  \     |   ____||   ____||  | \  \ /  / |   ____|   /       |
        |  |_)  | |  |_)  |    |  |__   |  |__   |  |  \  V  /  |  |__     |   (----`
        |   ___/  |      /     |   __|  |   __|  |  |   >   <   |   __|     \   \
        |  |      |  |\  \----.|  |____ |  |     |  |  /  .  \  |  |____.----)   |
        | _|      | _| `._____||_______||__|     |__| /__/ \__\ |_______|_______/

        record how to construct the sentences for a given dp

        In Word Break, we use a bool array to record whether a dp could be segmented.
        Now we should use a vector for every dp to record how to construct that dp from another dp.

        Google On Campus Presentation, demonstration questions. 4 Sep 2014, Nanyang Technological University, Singapore

                - l e e t c o d e
        prefix: d       l       c


        :param s: String
        :param dict: a set of string
        :return: a list of strings
        """
        # dp = [[]] * (len(s) + 1) # namespace reuse
        dp [[] ___ _ __ r..(l..(s) + 1)]

        dp[0].a..("dummy")

        ___ i __ r..(l..(s:
            __ n.. dp[i]:
                _____

            ___ word __ d..:
                __ s[i:i + l.. ?] __ word:
                    dp[i + l.. ?].a..(word)

        # build result
        __ n.. dp[-1]:
            r..    # list

        result    # list
        build_result(dp, l..(s), d..(), result)
        r.. result


    ___ build_result  dp, cur_index, cur_sentence, result
        """
        dfs recursive

        from right to left
        """
        # reached, build the result from cur_sentence
        __ cur_index __ 0:
            result.a..(" ".j..(cur_sentence
            r..

        # dfs
        ___ prefix __ dp[cur_index]:
            cur_sentence.appendleft(prefix)
            build_result(dp, cur_index - l..(prefix), cur_sentence, result)
            cur_sentence.popleft()


__ _____ __ ____
    ... Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])__ 'cat sand dog', 'cats and dog'
