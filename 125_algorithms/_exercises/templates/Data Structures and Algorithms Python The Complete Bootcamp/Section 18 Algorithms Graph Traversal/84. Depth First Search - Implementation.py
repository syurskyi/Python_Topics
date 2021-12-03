c_ Node():

    ___  -   value):
        value = value
        adjacentlist = []
        visited = False


c_ Graph():

    ___ DFS  node, traversal):
        node.visited = True
        traversal.append(node.value)

        ___ element __ node.adjacentlist:
            __ element.visited __ False:
                DFS(element, traversal)

        r_ traversal


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

node1.adjacentlist.append(node2)
node1.adjacentlist.append(node3)
node1.adjacentlist.append(node4)
node2.adjacentlist.append(node5)
node2.adjacentlist.append(node6)
node4.adjacentlist.append(node7)
node6.adjacentlist.append(node8)

graph = Graph()
print(graph.DFS(node1, []))