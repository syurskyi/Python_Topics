# tests for graph

from graph import *

g = loadGraph(simple)

a__(g.isEdge(1,2))
a__(not g.isEdge(1,4))

dd = DepthFirstTraversal(g, 2)
a__([2,1,5] == dd.solution(5))

g = Graph()
g.addVertex(10)
g.addVertex(20)
g.addEdge(10,20)
a__(g.isEdge(20,10))
a__(not g.isEdge(10,99))
a__(not g.isEdge(99,10))

# disconnected graph
g = Graph()
g.addEdge(1,2)
g.addEdge(7,8)

dfs1 = DepthFirstTraversal(g,1)
a__([1,2] == dfs1.solution(2))
dfs2 = DepthFirstTraversal(g,7)
a__([7,8] == dfs2.solution(8))
