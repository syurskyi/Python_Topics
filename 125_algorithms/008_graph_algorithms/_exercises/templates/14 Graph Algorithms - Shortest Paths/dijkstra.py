# ______ ___
# ______ heapq
#
# c_ Edge o..
#
# 	___ -  weight startVertex targetVertex
# 		? ?
# 		? ?
# 		? ?
#
# c_ Node o..
#
# 	___ - name
# 		? ?
# 		visited _ F..
# 		predecessor _ N..
# 		adjacenciesList _    # list
# 		minDistance _ ___.m_s..
#
# 	___ -c otherVertex
# 		r_ c.. m.. ?.m..
#
# 	___ -l other
# 		selfPriority _ m..
# 		otherPriority _ o__.m..
# 		r_ ? < o..
#
# c_ Algorithm o..
#
# 	___ calculateShortestPath vertexList startVertex
#
# 		q _   # list
# 		s__.m.. _ 0
# 		h__.h_p.. ? s..
#
# 		w__ q
#
# 			actualVertex _ h__.h_p.. ?
#
# 			___ edge __ ?.a..
# 				u _ ?.s..
# 				v _ ?.t..
# 				newDistance _ u.m.. + ?.w..
#
# 				__ ? < v.m..
# 					?.p.. _ u
# 					?.m.. _ n..
# 					h__.h_p.. q, v
#
# 	___ getShortestPathTo targetVertex
# 		print("Shortest path to vertex is: " ?.m..
#
# 		node _ ?
#
# 		w__ node __ no. N..
# 			print("@ "  ?.n..    # list
# 			node _ ?.p..
#
# node1 = Node("A");
# node2 = Node("B");
# node3 = Node("C");
# node4 = Node("D");
# node5 = Node("E");
# node6 = Node("F");
# node7 = Node("G");
# node8 = Node("H");
#
# edge1 = Edge(5,node1,node2);
# edge2 = Edge(8,node1,node8);
# edge3 = Edge(9,node1,node5);
# edge4 = Edge(15,node2,node4);
# edge5 = Edge(12,node2,node3);
# edge6 = Edge(4,node2,node8);
# edge7 = Edge(7,node8,node3);
# edge8 = Edge(6,node8,node6);
# edge9 = Edge(5,node5,node8);
# edge10 = Edge(4,node5,node6);
# edge11 = Edge(20,node5,node7);
# edge12 = Edge(1,node6,node3);
# edge13 = Edge(13,node6,node7);
# edge14 = Edge(3,node3,node4);
# edge15 = Edge(11,node3,node7);
# edge16 = Edge(9,node4,node7);
#
# node1.adjacenciesList.append(edge1);
# node1.adjacenciesList.append(edge2);
# node1.adjacenciesList.append(edge3);
# node2.adjacenciesList.append(edge4);
# node2.adjacenciesList.append(edge5);
# node2.adjacenciesList.append(edge6);
# node8.adjacenciesList.append(edge7);
# node8.adjacenciesList.append(edge8);
# node5.adjacenciesList.append(edge9);
# node5.adjacenciesList.append(edge10);
# node5.adjacenciesList.append(edge11);
# node6.adjacenciesList.append(edge12);
# node6.adjacenciesList.append(edge13);
# node3.adjacenciesList.append(edge14);
# node3.adjacenciesList.append(edge15);
# node4.adjacenciesList.append(edge16);
#
#
# vertexList = (node1,node2,node3, node4, node5, node6, node7, node8);
#
# algorithm = Algorithm();
# algorithm.calculateShortestPath(vertexList, node1);
# algorithm.getShortestPathTo(node4);