______ collections


class Solution(object
  ___ sequenceReconstruction(self, org, seqs
    """
    :type org: List[int]
    :type seqs: List[List[int]]
    :rtype: bool
    """
    n = le.(org)
    graph = collections.defaultdict(list)
    visited = {}
    incomings = collections.defaultdict(int)
    nodes = set()
    ___ seq in seqs:
      nodes |= set(seq)
      __ le.(seq) > 0:
        incomings[seq[0]] += 0
      ___ i in range(0, le.(seq) - 1
        start, end = seq[i], seq[i + 1]
        graph[start].append(end)
        incomings[end] += 1

    count = 0
    ___ node in incomings:
      __ incomings[node] __ 0:
        count += 1
        __ count __ 2:
          r_ False
    order = []
    visited = collections.defaultdict(int)
    queue = [q ___ q in incomings __ incomings[q] __ 0]
    w___ le.(queue) __ 1:
      top = queue.p..
      order.append(top)
      ___ nbr in graph[top]:
        incomings[nbr] -= 1
        __ incomings[nbr] __ 0:
          queue.append(nbr)
    __ le.(queue) > 1:
      r_ False
    __ order __ org and le.(order) __ le.(nodes
      r_ True
    r_ False
