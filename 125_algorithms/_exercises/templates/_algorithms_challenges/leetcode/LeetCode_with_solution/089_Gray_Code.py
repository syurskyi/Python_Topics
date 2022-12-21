c_ Solution o..
    ___ grayCode  n
        """
        :type n: int
        :rtype: List[int]
        """
        # https://leetcode.com/discuss/86617/6-line-java-solution-very-concise
        res = [0]
        ___ i __ r.. n
            ___ j __ reversed(r.. l.. res))):
                res.append(res[j] + (1 << i))
        r_ res


    # def count_one(self, num):
    #     count = 0
    #     while num:
    #         num &= (num - 1)
    #         count += 1
    #     return count

__ __name__ __ "__main__":
    s  ?
    print s.grayCode(2)

