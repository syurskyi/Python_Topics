from nose.tools ______ assert_equal


class TestShortestPath(object

    ___ test_shortest_path(self
        nodes =   # list
        graph = GraphShortestPath()
        ___ id __ range(0, 6
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        assert_equal(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        assert_equal(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        assert_equal(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


___ main(
    test = TestShortestPath()
    test.test_shortest_path()


__  -n __ '__main__':
    main()