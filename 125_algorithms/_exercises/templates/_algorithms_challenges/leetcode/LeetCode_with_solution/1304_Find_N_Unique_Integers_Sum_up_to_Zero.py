c_ Solution:
    ___ sumZero  n: i..   List[i..]:
        prefix_sum = 0
        res =    # list
        # 1, n-1
        ___ i __ r.. 1, n
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        r_ res
    
    # def sumZero(self, n: int) -> List[int]:
    #     # 1,n-1
    #     prefix = list(range(1, n))
    #     # sum(from 1 to n-1)
    #     return prefix + [-sum(prefix)]
