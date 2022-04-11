_______ unittest

____ tree_building _______ Record, BuildTree


c_ TreeBuildingTest(unittest.TestCase
    """
        Record(record_id, parent_id): records given to be processed
        Node(node_id): Node in tree
        BuildTree(records): records as argument and returns tree
        BuildTree should raise ValueError if given records are invalid
    """

    ___ test_empty_list_input
        records    # list
        root BuildTree(records)
        assertIsNone(root)

    ___ test_one_node
        records [
            Record(0, 0)
        ]
        root BuildTree(records)

        assert_node_is_leaf(root, node_id=0)

    ___ test_three_nodes_in_order
        records [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0)
        ]
        root BuildTree(records)

        assert_node_is_branch(root, node_id=0, children_count=2)
        assert_node_is_leaf(root.children[0], node_id=1)
        assert_node_is_leaf(root.children[1], node_id=2)

    ___ test_three_nodes_in_reverse_order
        records [
            Record(2, 0),
            Record(1, 0),
            Record(0, 0)
        ]
        root BuildTree(records)

        assert_node_is_branch(root, node_id=0, children_count=2)
        assert_node_is_leaf(root.children[0], node_id=1)
        assert_node_is_leaf(root.children[1], node_id=2)

    ___ test_more_than_two_children
        records [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 0)
        ]
        root BuildTree(records)

        assert_node_is_branch(root, node_id=0, children_count=3)
        assert_node_is_leaf(root.children[0], node_id=1)
        assert_node_is_leaf(root.children[1], node_id=2)
        assert_node_is_leaf(root.children[2], node_id=3)

    ___ test_binary_tree
        records [
            Record(6, 2),
            Record(0, 0),
            Record(3, 1),
            Record(2, 0),
            Record(4, 1),
            Record(5, 2),
            Record(1, 0)
        ]
        root BuildTree(records)

        assert_node_is_branch(root, 0, 2)
        assert_node_is_branch(root.children[0], 1, 2)
        assert_node_is_branch(root.children[1], 2, 2)
        assert_node_is_leaf(root.children[0].children[0], 3)
        assert_node_is_leaf(root.children[0].children[1], 4)
        assert_node_is_leaf(root.children[1].children[0], 5)
        assert_node_is_leaf(root.children[1].children[1], 6)

    ___ test_unbalanced_tree
        records [
            Record(0, 0),
            Record(1, 0),
            Record(2, 0),
            Record(3, 1),
            Record(4, 1),
            Record(5, 1),
            Record(6, 2),
        ]
        root BuildTree(records)

        assert_node_is_branch(root, 0, 2)
        assert_node_is_branch(root.children[0], 1, 3)
        assert_node_is_branch(root.children[1], 2, 1)
        assert_node_is_leaf(root.children[0].children[0], 3)
        assert_node_is_leaf(root.children[0].children[1], 4)
        assert_node_is_leaf(root.children[0].children[2], 5)
        assert_node_is_leaf(root.children[1].children[0], 6)

    ___ test_root_node_has_parent
        records [
            Record(0, 1),
            Record(1, 0)
        ]
        # Root parent_id should be equal to record_id(0)
        w__ assertRaisesWithMessage(V...
            BuildTree(records)

    ___ test_no_root_node
        records [
            Record(1, 0),
            Record(2, 0)
        ]
        # Record with record_id 0 (root) is missing
        w__ assertRaisesWithMessage(V...
            BuildTree(records)

    ___ test_non_continuous
        records [
            Record(2, 0),
            Record(4, 2),
            Record(1, 0),
            Record(0, 0)
        ]
        # Record with record_id 3 is missing
        w__ assertRaisesWithMessage(V...
            BuildTree(records)

    ___ test_cycle_directly
        records [
            Record(5, 2),
            Record(3, 2),
            Record(2, 2),
            Record(4, 1),
            Record(1, 0),
            Record(0, 0),
            Record(6, 3)
        ]
        # Cycle caused by Record 2 with parent_id pointing to itself
        w__ assertRaisesWithMessage(V...
            BuildTree(records)

    ___ test_cycle_indirectly
        records [
            Record(5, 2),
            Record(3, 2),
            Record(2, 6),
            Record(4, 1),
            Record(1, 0),
            Record(0, 0),
            Record(6, 3)
        ]
        # Cycle caused by Record 2 with parent_id(6) greater than record_id(2)
        w__ assertRaisesWithMessage(V...
            BuildTree(records)

    ___ test_higher_id_parent_of_lower_id
        records [
            Record(0, 0),
            Record(2, 0),
            Record(1, 2)
        ]
        # Record 1 have parent_id(2) greater than record_id(1)
        w__ assertRaisesWithMessage(V...
            BuildTree(records)

    ___ assert_node_is_branch  node, node_id, children_count
        assertEqual(node.node_id, node_id)
        assertNotEqual(l..(node.children), 0)
        assertEqual(l..(node.children), children_count)

    ___ assert_node_is_leaf  node, node_id
        assertEqual(node.node_id, node_id)
        assertEqual(l..(node.children), 0)

    # Utility functions
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
