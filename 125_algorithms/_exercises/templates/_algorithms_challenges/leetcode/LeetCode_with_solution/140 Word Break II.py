"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid
dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
__author__ = 'Danyang'
from collections import deque


class Solution:
    ___ wordBreak(self, s, dict):
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
        dp = [[] for _ in range(len(s) + 1)]

        dp[0].append("dummy")

        for i in range(len(s)):
            __ not dp[i]:
                continue

            for word in dict:
                __ s[i:i + len(word)] == word:
                    dp[i + len(word)].append(word)

        # build result
        __ not dp[-1]:
            return []

        result = []
        self.build_result(dp, len(s), deque(), result)
        return result


    ___ build_result(self, dp, cur_index, cur_sentence, result):
        """
        dfs recursive

        from right to left
        """
        # reached, build the result from cur_sentence
        __ cur_index == 0:
            result.append(" ".join(cur_sentence))
            return

        # dfs
        for prefix in dp[cur_index]:
            cur_sentence.appendleft(prefix)
            self.build_result(dp, cur_index - len(prefix), cur_sentence, result)
            cur_sentence.popleft()


__ __name__=="__main__":
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])==['cat sand dog', 'cats and dog']
