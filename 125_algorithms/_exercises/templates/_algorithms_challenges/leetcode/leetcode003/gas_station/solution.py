c_ Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    ___ canCompleteCircuit  gas, cost
        n l..(gas)
        t [0 ___ i __ r..(n)]
        ___ i __ r..(n
            t[i] gas[i] - cost[i]
        res 0
        cs 0  # Current sum
        ts 0  # Total sum
        ___ i __ r..(n
            cs += t[i]
            ts += t[i]
            __ cs < 0:
                res i + 1
                cs 0
        __ ts < 0:
            r.. -1
        ____
            r.. res

    ___ canCompleteCircuit2  gas, cost
        # Brute-force
        n l..(gas)
        ___ i __ r..(n
            __ gas[i] - cost[i] < 0:
                _____
            carry gas[i] - cost[i]
            j (i + 1) % n
            flag T..
            w.... j !_ i % n:
                __ carry + gas[j] - cost[j] < 0:
                    flag F..
                    _____
                j (j + 1) % n
            __ flag:
                r.. i
        r.. -1


s Solution()
print s.canCompleteCircuit2([2, 4], [3, 4])
