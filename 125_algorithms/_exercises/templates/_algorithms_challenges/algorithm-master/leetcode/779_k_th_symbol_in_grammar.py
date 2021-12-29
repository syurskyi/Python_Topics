class Solution:
    ___ kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        __ N __ 1:
            r.. 0

        __ K % 2 __ 0:
            __ self.kthGrammar(N - 1, K // 2) __ 0:
                r.. 1
            ____:
                r.. 0
        ____:
            __ self.kthGrammar(N - 1, (K + 1) // 2) __ 0:
                r.. 0
            ____:
                r.. 1
