# test module and project
from bheap import *
from project_bheap import *

bh = BHeap(10)
a__(bh.isEmpty())

bh.insert(2,90)
a__(2 == bh.smallest())
a__(bh.isEmpty())

bh.insert(3,40)
bh.insert(5,30)

a__(5 == bh.smallest())
bh.decreaseKey(3,20)
a__(3 == bh.smallest())
a__(bh.isEmpty())

bh.insert(1,70)
bh.insert(2,50)
bh.decreaseKey(1,30)
a__(1 == bh.smallest())
bh.insert(3,20)
bh.decreaseKey(2,10)
a__(2 == bh.smallest())
a__(3 == bh.smallest())

a__(bh.isEmpty())

for i in range(10):
    bh.insert(i, i + 100)

for i in range(9,-1,-1):
    bh.decreaseKey(i, i+ 10)

for i in range(10):
    m = bh.smallest()
    a__(i == m)

a__(bh.isEmpty())

# MST algorithm
solved = computeMST(graph)
edges = solution(solved)
total = 0
for e in edges:
    total += graph[e[0]][e[1]]
a__(11 == total)


[(1, 0), (2, 1), (4, 2), (2, 3)]
