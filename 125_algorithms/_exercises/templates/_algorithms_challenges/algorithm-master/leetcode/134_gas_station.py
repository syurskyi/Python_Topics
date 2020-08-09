class Solution:
    """
    Main Concept:

    if the tank is enough, go to next, otherwise back to previous to get gas
    """
    ___ canCompleteCircuit(self, gas, cost
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        NOT_FOUND = -1

        __ not gas or not cost or le.(gas) != le.(cost
            r_ NOT_FOUND

        end, start = -1, le.(gas) - 1  # since its a circle, end start from `-1` means `n - 1`
        tank = gas[start] - cost[start]

        w___ start > end:
            __ tank >= 0:
                end += 1
                tank += gas[end] - cost[end]
            ____
                start -= 1
                tank += gas[start] - cost[start]

        r_ start __ tank >= 0 else NOT_FOUND


class Solution:
    """
    TLE: Simulate the process
    """
    ___ canCompleteCircuit(self, gas, cost
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        NOT_FOUND = -1

        __ not gas or not cost or le.(gas) != le.(cost
            r_ NOT_FOUND

        n = le.(gas)
        RANGE = list(range(n))

        for start in range(n
            tank = 0
            is_failed = False

            for mid in RANGE[start:n] + RANGE[:start]:
                tank += gas[mid]
                __ tank < cost[mid]:
                    is_failed = True
                    break
                tank -= cost[mid]

            __ not is_failed:
                r_ start

        r_ NOT_FOUND
