_______ c..


c_ Solution(object):
  ___ sequenceReconstruction(self, org, seqs):
    """
    :type org: List[int]
    :type seqs: List[List[int]]
    :rtype: bool
    """
    n = l..(org)
    graph = c...defaultdict(l..)
    visited    # dict
    incomings = c...defaultdict(i..)
    nodes = set()
    ___ seq __ seqs:
      nodes |= set(seq)
      __ l..(seq) > 0:
        incomings[seq[0]] += 0
      ___ i __ r..(0, l..(seq) - 1):
        start, end = seq[i], seq[i + 1]
        graph[start].a..(end)
        incomings[end] += 1

    count = 0
    ___ node __ incomings:
      __ incomings[node] __ 0:
        count += 1
        __ count __ 2:
          r.. F..
    order    # list
    visited = c...defaultdict(i..)
    queue = [q ___ q __ incomings __ incomings[q] __ 0]
    w.... l..(queue) __ 1:
      top = queue.pop()
      order.a..(top)
      ___ nbr __ graph[top]:
        incomings[nbr] -= 1
        __ incomings[nbr] __ 0:
          queue.a..(nbr)
    __ l..(queue) > 1:
      r.. F..
    __ order __ org a.. l..(order) __ l..(nodes):
      r.. T..
    r.. F..
