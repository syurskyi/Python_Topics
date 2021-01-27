# testing code for module (including project)

from apsp import *
from project_apsp import *

a__(89 == fibonacci(10))

dist,pred = allPairsShortestPath(graph)
a__(7 == dist[0][3])

a__([0,4,3] == constructShortestPath(0,3,pred))

a__(15 == dist[1][0])
a__([1, 2, 4, 3, 0] == constructShortestPath(1,0,pred))

a__([2] == constructShortestPath(2,2,pred))
       
a__(0 == minEditDistance('test', 'test'))
a__(4 == minEditDistance('test', ''))
a__(4 == minEditDistance('', 'test'))

a__(3 == minEditDistance('Grates', 'Create'))
a__(3 == minEditDistance('Create', 'Grates'))
a__(1 == minEditDistance('walk', 'talk'))

# simply replace each letter one at a time
a__(4 == minEditDistance('walk', 'pore'))

# remove first and last letter
a__(2 == minEditDistance('waltz', 'malt'))
