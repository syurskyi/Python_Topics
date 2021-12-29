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
        result = []
        self.dfs(s, [], result)
        return result

    ___ dfs_complicated(self, seq, cur, result):
        """
        checking done by the children
        :param seq:
        :param cur:
        :param result:
        :return:
        """
        __ len(cur) > 4:
            return

        __ not cur or self.is_valid(cur[-1]):
            __ len(cur) == 4 and not seq:  # check the last one first
                result.append(".".join(cur))
                return

            for i in xrange(1, min(3, len(seq))+1):
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
        __ not seq and len(cur)==4:
            result.append(".".join(cur))
            return

        # for i in xrange(1, 3+1):
        # for loop
        for i in xrange(1, min(3, len(seq)) + 1):
            new_seg = seq[:i]
            # condition check
            __ len(cur) < 4 and self.is_valid(new_seg):
                self.dfs(seq[i:], cur + [new_seg], result)
            else:
                return

    ___ is_valid(self, s):
        __ not s:
            return False
        return s == "0" or s[0]!="0" and 0<= int(s) <256  # ["0.0.0.0"]

__ __name__=="__main__":
    IP = "25525511135"
    print Solution().restoreIpAddresses(IP)
