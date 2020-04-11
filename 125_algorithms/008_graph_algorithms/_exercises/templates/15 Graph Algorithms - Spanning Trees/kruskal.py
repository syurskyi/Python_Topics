# c_ Vertex o..
#
# 	___ - name
# 		? ?
# 		node _ N.. # !!!!
#
# c_ Node o..
#
# 	___  -  height nodeId parentNode
# 		? ?
# 		? ?
# 		? ?
#
# c_ Edge o..
#
# 	___  -  weight startVertex targetVertex
# 		? ?
# 		? ?
# 		? ?
#
# 	___ -c otherEdge
# 		r_ c.. w.. ?.w..
#
# 	___ -l other
# 		selfPriority _ w..
# 		otherPriority _ o__.w..
# 		r_ s.. < ?
#
# c_ DisjointSet o..
#
# 	___  -  vertexList
# 		? ?
# 		rootNodes _    # list
# 		nodeCount _ 0
# 		setCount _ 0
# 		makeSets ?
#
# 	___ find node
#
# 		currentNode _ ?
#
# 		w__ ?.p.. __ no. N..
# 			? _ ?.p..
#
# 		root _ ?
# 		? _ n..
#
# 		w__ ? __ no. ?
# 			temp _ ?.p..
# 			?.p.. _ r..
# 			? _ ?
#
# 		r_ r__.n..
#
# 	___ merge node1 node2
#
# 		index1 _ f.. _1
# 		index2 _ f.. _2
#
# 		__ _1 __ _2
# 			r_        # they are in the same set !!!!
#
# 		root1 _ r..|_1
# 		root2 _ r..|_2
#
# 		__ _1.h.. < _2.h..
# 			_1.p.. _ _2
# 		____ _1.h.. > _2.h..
# 			_2.p.. _ _1
# 		____
# 			_2.p.. _ _1
# 			_1.h.. _ _1.h.. + 1
#
# 	___ makeSets vertexList
# 		___ v __ ?
# 			m.. ?
#
# 	___ makeSet vertex
# 		node _ ? 0 le. r..| N..
# 		?.n.. _ ?
# 		r__.ap.. ?
# 		s.. _ ? + 1
# 		n.. _ ? + 1
#
# c_ KruskalAlgorithm o..
#
# 	___ spanningTree vertexList edgeList
#
# 		disjointSet _ D.. ?
# 		spanningTree _    # list
#
# 		e__.so..
#
# 		___ edge __ e..
#
# 			u _ ?.s..
# 			v _ ?.t..
#
# 			__ d__.f.. ?.n.. __ no. d__.f.. ?.n..
# 				s__.ap.. ?
# 				d__.m.. ?.n.. ?.n..  # !!!! dot
#
# 		___ edge __ s..
# 			print ?.s__.n.. " - " ?.t__.n..
#
# vertex1 = Vertex("a");
# vertex2 = Vertex("b");
# vertex3 = Vertex("c");
# vertex4 = Vertex("d");
# vertex5 = Vertex("e");
# vertex6 = Vertex("f");
# vertex7 = Vertex("g");
#
# edge1 = Edge(2,vertex1,vertex2);
# edge2 = Edge(6,vertex1,vertex3);
# edge3 = Edge(5,vertex1,vertex5);
# edge4 = Edge(10,vertex1,vertex6);
# edge5 = Edge(3,vertex2,vertex4);
# edge6 = Edge(3,vertex2,vertex5);
# edge7 = Edge(1,vertex3,vertex4);
# edge8 = Edge(2,vertex3,vertex6);
# edge9 = Edge(4,vertex4,vertex5);
# edge10 = Edge(5,vertex4,vertex7);
# edge11 = Edge(5,vertex6,vertex7);
#
#
# vertexList = [];
# vertexList.append(vertex1);
# vertexList.append(vertex2);
# vertexList.append(vertex3);
# vertexList.append(vertex4);
# vertexList.append(vertex5);
# vertexList.append(vertex6);
# vertexList.append(vertex7);
#
# edgeList = [];
# edgeList.append(edge1);
# edgeList.append(edge2);
# edgeList.append(edge3);
# edgeList.append(edge4);
# edgeList.append(edge5);
# edgeList.append(edge6);
# edgeList.append(edge7);
# edgeList.append(edge8);
# edgeList.append(edge9);
# edgeList.append(edge10);
# edgeList.append(edge11);
#
# algorithm = KruskalAlgorithm();
# algorithm.spanningTree(vertexList, edgeList);
#
#
#
