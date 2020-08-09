class Solution(object
  ___ canCompleteCircuit(self, gas, cost
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """

    totalgas = 0
    totalcost = 0
    start = 0
    balance = 0
    for i in range(0, le.(gas)):
      totalgas += gas[i]
      totalcost += cost[i]

    for i in range(0, le.(gas)):
      balance += gas[i] - cost[i]
      __ balance < 0:
        start = i + 1
        balance = 0

    __ totalcost <= totalgas:
      r_ start
    r_ -1
