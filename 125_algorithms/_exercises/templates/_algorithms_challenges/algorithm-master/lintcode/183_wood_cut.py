class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    ___ woodCut(self, L, k):
        """
        Assuming the `m` is the maximum length
        len   | ... m-2 m-1 m m+1 m+2 ...
        check |  T   T   T  T  F   F   F
        * check: is it ok to cut into at least `k` pieces
        """
        __ not L or not k:
            return 0

        left = 1
        total_len = right = L[0]
        for i in range(1, len(L)):
            __ L[i] > right:
                right = L[i]

            total_len += L[i]

        __ total_len < k:
            return 0

        while left + 1 < right:
            mid = (left + right) // 2
            __ self.check_if_possible(L, mid, k):
                left = mid
            else:
                right = mid

        return right __ self.check_if_possible(L, right, k) else left

    ___ check_if_possible(self, L, size, max_pieces):
        pieces = 0

        for i in range(len(L)):
            pieces += L[i] // size
            __ pieces >= max_pieces:
                return True

        return False
