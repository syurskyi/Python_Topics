______ unittest
______ linkedNodes


c_ TestLinkedNodesListMethods(unittest.TestCase):
    ___ setUp
        node_values _ [3, 4, 5, 6, 7, 9, 1, 2, 3, 6, 0, 4]
        my_linked_list _ linkedNodes.NodeList(node_values)

    ___ test_add_node
        test_value _ 5
        my_linked_list.add_node(test_value)
        assertEqual(test_value,
                         my_linked_list.get_node_value(len(node_values)))

    ___ test_remove_node
        node_be_removed_index _ 1
        next_in_line_value _ my_linked_list.get_node_value(
            node_be_removed_index + 1)
        my_linked_list.remove_node(node_be_removed_index)
        assertEqual(next_in_line_value,
                         my_linked_list.get_node_value(node_be_removed_index))

    ___ test_print_list
        my_linked_list.print()


if __name__ == 'main':
    unittest.main()
