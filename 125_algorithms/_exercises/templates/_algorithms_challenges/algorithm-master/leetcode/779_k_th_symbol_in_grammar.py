class Solution:
    ___ kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        __ N == 1:
            return 0

        __ K % 2 == 0:
            __ self.kthGrammar(N - 1, K // 2) == 0:
                return 1
            else:
                return 0
        else:
            __ self.kthGrammar(N - 1, (K + 1) // 2) == 0:
                return 0
            else:
                return 1
