import unittest
import linkedNodes


class TestLinkedNodesListMethods(unittest.TestCase):
    def setUp(self):
        self.node_values = [3, 4, 5, 6, 7, 9, 1, 2, 3, 6, 0, 4]
        self.my_linked_list = linkedNodes.NodeList(self.node_values)

    def test_add_node(self):
        test_value = 5
        self.my_linked_list.add_node(test_value)
        self.assertEqual(test_value,
                         self.my_linked_list.get_node_value(len(self.node_values)))

    def test_remove_node(self):
        node_be_removed_index = 1
        next_in_line_value = self.my_linked_list.get_node_value(
            node_be_removed_index + 1)
        self.my_linked_list.remove_node(node_be_removed_index)
        self.assertEqual(next_in_line_value,
                         self.my_linked_list.get_node_value(node_be_removed_index))

    def test_print_list(self):
        self.my_linked_list.print()


if __name__ == 'main':
    unittest.main()
