c_ Solution(o..
  ___ canCompleteCircuit  gas, cost
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """

    totalgas = 0
    totalcost = 0
    start = 0
    balance = 0
    ___ i __ r..(0, l..(gas)):
      totalgas += gas[i]
      totalcost += cost[i]

    ___ i __ r..(0, l..(gas)):
      balance += gas[i] - cost[i]
      __ balance < 0:
        start = i + 1
        balance = 0

    __ totalcost <= totalgas:
      r.. start
    r.. -1
