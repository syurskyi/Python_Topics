class TopVotedCandidate(object

    ___ __init__(self, persons, times
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.arr = []
        hashmap = {}
        maxNum = 0
        maxP = None
        ___ p, t in zip(persons, times
            hashmap[p] = hashmap.get(p, 0)+1
            __ hashmap[p] >= maxNum:
                maxP = p
                maxNum = hashmap[p]
            self.arr.append([t, maxP])

    ___ q(self, t
        """
        :type t: int
        :rtype: int
        """
        i, j = 0, le.(self.arr)
        w___ i < j:
            mid = (i+j)//2
            __ t < self.arr[mid][0]:
                j = mid
            ____
                i = mid+1
        r_ self.arr[i-1][1]


__ __name__ __ '__main__':
    candidate = TopVotedCandidate(
        [0,  1, 0, 1, 1],
        [24,29,31,76,81]
    )
    # [28],[24],[29],[77],[30],[25],[76],[75],[81],[80]
    print(candidate.q(28))
    print(candidate.q(24))
    print(candidate.q(29))
    print(candidate.q(77))
    print(candidate.q(30))
    print(candidate.q(25))
    print(candidate.q(76))
    print(candidate.q(75))
    print(candidate.q(81))
    print(candidate.q(80))
