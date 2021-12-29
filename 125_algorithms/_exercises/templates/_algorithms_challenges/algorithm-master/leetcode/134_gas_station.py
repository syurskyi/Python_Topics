class Solution:
    """
    Main Concept:

    if the tank is enough, go to next, otherwise back to previous to get gas
    """
    ___ canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        NOT_FOUND = -1

        __ not gas or not cost or len(gas) != len(cost):
            return NOT_FOUND

        end, start = -1, len(gas) - 1  # since its a circle, end start from `-1` means `n - 1`
        tank = gas[start] - cost[start]

        while start > end:
            __ tank >= 0:
                end += 1
                tank += gas[end] - cost[end]
            else:
                start -= 1
                tank += gas[start] - cost[start]

        return start __ tank >= 0 else NOT_FOUND


class Solution:
    """
    TLE: Simulate the process
    """
    ___ canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        NOT_FOUND = -1

        __ not gas or not cost or len(gas) != len(cost):
            return NOT_FOUND

        n = len(gas)
        RANGE = list(range(n))

        for start in range(n):
            tank = 0
            is_failed = False

            for mid in RANGE[start:n] + RANGE[:start]:
                tank += gas[mid]
                __ tank < cost[mid]:
                    is_failed = True
                    break
                tank -= cost[mid]

            __ not is_failed:
                return start

        return NOT_FOUND
