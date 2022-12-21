c_ Solution o..
    # def kClosest(self, points, K):
    #     """
    #     :type points: List[List[int]]
    #     :type K: int
    #     :rtype: List[List[int]]
    #     """
    #     # Sort
    #     return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]
    
    ___ kClosest  points, K
        # K smallest heaq
        r_ heapq.nsmallest(K, points, k.._l... x: x[0] ** 2 + x[1] ** 2)
