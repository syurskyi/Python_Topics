c_ Solution o..
    ___ canCompleteCircuit  gas, cost
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/5088/my-ac-is-o-1-space-o-n-running-time-solution-does-anybody-have-posted-this-solution
        ls = l.. gas)
        begin, end = 0, ls - 1
        curr = gas[end] - cost[end]
        w.. begin < end:
            __ curr >= 0:
                curr += gas[begin] - cost[begin]
                begin += 1
            ____
                end -= 1
                curr += gas[end] - cost[end]
        __ curr >= 0:
            r_ end
        ____
            r_ -1

