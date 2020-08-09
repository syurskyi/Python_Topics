from nose.tools ______ assert_equal


class TestBfs(object

    ___ __init__(self
        self.results = Results()

    ___ test_bfs(self
        nodes = []
        graph = GraphBfs()
        ___ id in range(0, 6
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.bfs(nodes[0], self.results.add_result)
        assert_equal(str(self.results), "[0, 1, 4, 5, 3, 2]")

        print('Success: test_bfs')


___ main(
    test = TestBfs()
    test.test_bfs()


__ __name__ __ '__main__':
    main()