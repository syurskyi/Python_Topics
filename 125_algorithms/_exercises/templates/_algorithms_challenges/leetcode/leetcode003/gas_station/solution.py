class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    ___ canCompleteCircuit(self, gas, cost):
        n = len(gas)
        t = [0 for i in range(n)]
        for i in range(n):
            t[i] = gas[i] - cost[i]
        res = 0
        cs = 0  # Current sum
        ts = 0  # Total sum
        for i in range(n):
            cs += t[i]
            ts += t[i]
            __ cs < 0:
                res = i + 1
                cs = 0
        __ ts < 0:
            return -1
        else:
            return res

    ___ canCompleteCircuit2(self, gas, cost):
        # Brute-force
        n = len(gas)
        for i in range(n):
            __ gas[i] - cost[i] < 0:
                continue
            carry = gas[i] - cost[i]
            j = (i + 1) % n
            flag = True
            while j != i % n:
                __ carry + gas[j] - cost[j] < 0:
                    flag = False
                    break
                j = (j + 1) % n
            __ flag:
                return i
        return -1


s = Solution()
print s.canCompleteCircuit2([2, 4], [3, 4])
