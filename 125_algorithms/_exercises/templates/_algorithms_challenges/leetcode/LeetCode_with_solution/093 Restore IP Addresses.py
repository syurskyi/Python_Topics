"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
__author__ = 'Danyang'


class Solution:
    ___ restoreIpAddresses(self, s):
        """
        dfs, branch factor 3, depth 4
        complexity: 3^4 = 81
        :param s: String
        :return: list of strings
        """
        result    # list
        self.dfs(s, [], result)
        r.. result

    ___ dfs_complicated(self, seq, cur, result):
        """
        checking done by the children
        :param seq:
        :param cur:
        :param result:
        :return:
        """
        __ l..(cur) > 4:
            r..

        __ n.. cur o. self.is_valid(cur[-1]):
            __ l..(cur) __ 4 a.. n.. seq:  # check the last one first
                result.a..(".".join(cur))
                r..

            ___ i __ xrange(1, m..(3, l..(seq))+1):
                self.dfs(seq[i:], cur+[seq[:i]], result)

    ___ dfs(self, seq, cur, result):
        """
        checking done by the parent (making debug much easier by preventing going one more step)
        structure of dfs
        1. terminal condition
        2. for loop for dfs candidates
        3. condition check for candidates
        :param seq:
        :param cur:
        :param result:
        :return:
        """
        # terminal condition
        __ n.. seq a.. l..(cur)__4:
            result.a..(".".join(cur))
            r..

        # for i in xrange(1, 3+1):
        # for loop
        ___ i __ xrange(1, m..(3, l..(seq)) + 1):
            new_seg = seq[:i]
            # condition check
            __ l..(cur) < 4 a.. self.is_valid(new_seg):
                self.dfs(seq[i:], cur + [new_seg], result)
            ____:
                r..

    ___ is_valid(self, s):
        __ n.. s:
            r.. False
        r.. s __ "0" o. s[0]!="0" a.. 0<= int(s) <256  # ["0.0.0.0"]

__ __name____"__main__":
    IP = "25525511135"
    print Solution().restoreIpAddresses(IP)
