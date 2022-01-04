c_ Node

    ___  -   value):
        value  value
        adjacentlist  []
        visited  F..


c_ Graph

    ___ BFS  node):

        queue  []
        queue.a..(node)
        node.visited  T..

        traversal  []

        w__ queue:
            actualNode  queue.pop(0)
            traversal.a..(actualNode.value)

            ___ element __ actualNode.adjacentlist:
                __ element.visited __ F..:
                    queue.a..(element)
                    element.visited  T..

        r_ traversal


node1  Node("A")
node2  Node("B")
node3  Node("C")
node4  Node("D")
node5  Node("E")
node6  Node("F")
node7  Node("G")

node1.adjacentlist.a..(node2)
node1.adjacentlist.a..(node3)
node1.adjacentlist.a..(node4)
node2.adjacentlist.a..(node5)
node2.adjacentlist.a..(node6)
node4.adjacentlist.a..(node7)

graph  Graph()
print(graph.BFS(node1))