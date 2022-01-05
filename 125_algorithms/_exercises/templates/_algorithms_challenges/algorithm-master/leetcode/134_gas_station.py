c_ Solution:
    """
    Main Concept:

    if the tank is enough, go to next, otherwise back to previous to get gas
    """
    ___ canCompleteCircuit  gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        NOT_FOUND = -1

        __ n.. gas o. n.. cost o. l..(gas) != l..(cost):
            r.. NOT_FOUND

        end, start = -1, l..(gas) - 1  # since its a circle, end start from `-1` means `n - 1`
        tank = gas[start] - cost[start]

        w.... start > end:
            __ tank >= 0:
                end += 1
                tank += gas[end] - cost[end]
            ____:
                start -= 1
                tank += gas[start] - cost[start]

        r.. start __ tank >= 0 ____ NOT_FOUND


c_ Solution:
    """
    TLE: Simulate the process
    """
    ___ canCompleteCircuit  gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        NOT_FOUND = -1

        __ n.. gas o. n.. cost o. l..(gas) != l..(cost):
            r.. NOT_FOUND

        n = l..(gas)
        RANGE = l..(r..(n))

        ___ start __ r..(n):
            tank = 0
            is_failed = F..

            ___ mid __ RANGE[start:n] + RANGE[:start]:
                tank += gas[mid]
                __ tank < cost[mid]:
                    is_failed = T..
                    break
                tank -= cost[mid]

            __ n.. is_failed:
                r.. start

        r.. NOT_FOUND
