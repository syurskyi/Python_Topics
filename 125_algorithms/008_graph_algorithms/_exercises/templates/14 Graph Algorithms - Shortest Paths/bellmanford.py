# ________ ___
#
# c_ Node o..
#
# 	___ - name
# 		? ?
# 		visited _ F..
# 		predecessor _ N..
# 		adjacenciesList _   # list
# 		minDistance _ ___.m_s..
#
# c_ Edge o..
#
# 	___ _ weight startVertex targetVertex
# 		? ?
# 		? ?
# 		? ?
#
# c_ BellmanFord o..
#
# 	HAS_CYCLE _ F..
#
# 	___ calculateShortestPath vertexList edgeList startVertex
#
# 		s__.m.. _ 0
#
# 		___ i __ ra.. 0 le. ?|-1
# 			___ edge __ ?
#
# 				u _ ?.s__
# 				v _ ?.t..
#
# 				newDistance _ u.m.. + ?.w..
#
# 				__ newDistance < v.m..
# 					v.m.. _ n..
# 					v.p.. _ u
#
# 		___ edge __ ?
# 			__ h.. ?
# 				print("Negative cycle detected...");
# 				?.H.. _ T..
# 				r_
#
# 	___ hasCycle edge
# 		__  ?.s__.m.. + ?.w..| < ?.t__.m..
# 			r_ T..
# 		____
# 			r_ F..
#
# 	___ getShortestPathTo targetVertex
#
# 		__ no. ?.H..
# 			print("Shortest path exists with value: " t__.m..
#
# 			node _ t..
#
# 			w__ node __ no. N..
# 				print("@ " ?.n..    # string
# 				? _ ?.p..
# 		____
# 			print("Negative cycle detected...");
#
#
# node1 _ Node("A");
# node2 _ Node("B");
# node3 _ Node("C");
# node4 _ Node("D");
# node5 _ Node("E");
# node6 _ Node("F");
# node7 _ Node("G");
# node8 _ Node("H");
#
# edge1 _ Edge(5,node1,node2);
# edge2 _ Edge(8,node1,node8);
# edge3 _ Edge(9,node1,node5);
# edge4 _ Edge(15,node2,node4);
# edge5 _ Edge(12,node2,node3);
# edge6 _ Edge(4,node2,node8);
# edge7 _ Edge(7,node8,node3);
# edge8 _ Edge(6,node8,node6);
# edge9 _ Edge(5,node5,node8);
# edge10 _ Edge(4,node5,node6);
# edge11 _ Edge(20,node5,node7);
# edge12 _ Edge(1,node6,node3);
# edge13 _ Edge(13,node6,node7);
# edge14 _ Edge(3,node3,node4);
# edge15 _ Edge(11,node3,node7);
# edge16 _ Edge(9,node4,node7);
#
# edge17 _ Edge(1,node1,node2);
# edge18 _ Edge(1,node2,node3);
# edge19 _ Edge(-3,node3,node1);
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
# vertexList _ (node1,node2,node3, node4, node5, node6, node7, node8);
# #edgeList _ (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14,edge15,edge16);
# edgeList _ (edge17, edge18, edge19);
#
# algorithm _ BellmanFord();
# algorithm.calculateShortestPath(vertexList, edgeList, node1);
# algorithm.getShortestPathTo(node7);