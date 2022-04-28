c_ Solution o..
    ___ getRow  rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last = [1]
        res = [1]
        ___ r __ r.. 1, rowIndex + 1):
            res = [1]
            ___ index __ r.. l.. last) - 1):
                res.append(last[index] + last[index + 1])
            res.append(1)
            last = res
        r_ res

__ __name__ __ "__main__":
    s  ?
    print s.getRow(3)