_______ unittest

____ dot_dsl _______ Graph, Node, Edge, NODE, EDGE, ATTR


c_ DotDslTest(unittest.TestCase
    ___ test_empty_graph
        g = Graph()

        assertEqual(g.nodes, [])
        assertEqual(g.edges, [])
        assertEqual(g.attrs, {})

    ___ test_graph_with_one_node
        g = Graph([
            (NODE, "a", {})
        ])

        assertEqual(g.nodes, [Node("a")])
        assertEqual(g.edges, [])
        assertEqual(g.attrs, {})

    ___ test_graph_with_one_node_with_keywords
        g = Graph([
            (NODE, "a", {"color": "green"})
        ])

        assertEqual(g.nodes, [Node("a", {"color": "green"})])
        assertEqual(g.edges, [])
        assertEqual(g.attrs, {})

    ___ test_graph_with_one_edge
        g = Graph([
            (EDGE, "a", "b", {})
        ])

        assertEqual(g.nodes, [])
        assertEqual(g.edges, [Edge("a", "b", {})])
        assertEqual(g.attrs, {})

    ___ test_graph_with_one_attribute
        g = Graph([
            (ATTR, "foo", "1")
        ])

        assertEqual(g.nodes, [])
        assertEqual(g.edges, [])
        assertEqual(g.attrs, {"foo": "1"})

    ___ test_graph_with_attributes
        g = Graph([
            (ATTR, "foo", "1"),
            (ATTR, "title", "Testing Attrs"),
            (NODE, "a", {"color": "green"}),
            (NODE, "c", {}),
            (NODE, "b", {"label": "Beta!"}),
            (EDGE, "b", "c", {}),
            (EDGE, "a", "b", {"color": "blue"}),
            (ATTR, "bar", "true")
        ])

        assertEqual(g.nodes, [Node("a", {"color": "green"}),
                                   Node("c", {}),
                                   Node("b", {"label": "Beta!"})])
        assertEqual(g.edges, [Edge("b", "c", {}),
                                   Edge("a", "b", {"color": "blue"})])
        assertEqual(g.attrs, {
            "foo": "1",
            "title": "Testing Attrs",
            "bar": "true"
        })

    ___ test_malformed_graph
        w__ assertRaisesWithMessage T..
            Graph(1)

        w__ assertRaisesWithMessage T..
            Graph("problematic")

    ___ test_malformed_graph_item
        w__ assertRaisesWithMessage T..
            Graph([
                ()
            ])

        w__ assertRaisesWithMessage T..
            Graph([
                (ATTR, )
            ])

    ___ test_malformed_attr
        w__ assertRaisesWithMessage(V...
            Graph([
                (ATTR, 1, 2, 3)
            ])

    ___ test_malformed_node
        w__ assertRaisesWithMessage(V...
            Graph([
                (NODE, 1, 2, 3)
            ])

    ___ test_malformed_EDGE
        w__ assertRaisesWithMessage(V...
            Graph([
                (EDGE, 1, 2)
            ])

    ___ test_unknown_item
        w__ assertRaisesWithMessage(V...
            Graph([
                (99, 1, 2)
            ])

    # Utility methods
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
