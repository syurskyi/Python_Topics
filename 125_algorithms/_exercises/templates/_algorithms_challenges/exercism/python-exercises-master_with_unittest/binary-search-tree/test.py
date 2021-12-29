_______ unittest

____ binary_search_tree _______ BinarySearchTree, TreeNode


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class BinarySearchTreeTest(unittest.TestCase):

    ___ test_data_is_retained(self):
        expected = TreeNode('4', N.., N..)
        self.assertTreeEqual(BinarySearchTree(['4']).data(), expected)

    # Test inserting data at proper node
    ___ test_smaller_data_at_left_node(self):
        expected = TreeNode('4', TreeNode('2', N.., N..), N..)
        self.assertTreeEqual(BinarySearchTree(['4', '2']).data(), expected)

    ___ test_same_number_at_left_node(self):
        expected = TreeNode('4', TreeNode('4', N.., N..), N..)
        self.assertTreeEqual(BinarySearchTree(['4', '4']).data(), expected)

    ___ test_greater_number_at_right_node(self):
        expected = TreeNode('4', N.., TreeNode('5', N.., N..))
        self.assertTreeEqual(BinarySearchTree(['4', '5']).data(), expected)

    ___ test_can_create_complex_tree(self):
        expected = TreeNode(
            '4',
            TreeNode(
                '2',
                TreeNode('1', N.., N..),
                TreeNode('3', N.., N..)
            ),
            TreeNode(
                '6',
                TreeNode('5', N.., N..),
                TreeNode('7', N.., N..)
            )
        )
        self.assertTreeEqual(
            BinarySearchTree(['4', '2', '6', '1', '3', '5', '7']).data(),
            expected
        )

    # Test can sort data
    ___ test_can_sort_single_number(self):
        self.assertEqual(BinarySearchTree(['2']).sorted_data(), ['2'])

    ___ test_can_sort_if_second_number_is_smaller_than_first(self):
        self.assertEqual(
            BinarySearchTree(['2', '1']).sorted_data(), ['1', '2']
        )

    ___ test_can_sort_if_second_number_is_same_as_first(self):
        self.assertEqual(
            BinarySearchTree(['2', '2']).sorted_data(), ['2', '2']
        )

    ___ test_can_sort_if_second_number_is_greater_than_first(self):
        self.assertEqual(
            BinarySearchTree(['2', '3']).sorted_data(), ['2', '3']
        )

    ___ test_can_sort_complex_tree(self):
        self.assertEqual(
            BinarySearchTree(['2', '1', '3', '6', '7', '5']).sorted_data(),
            ['1', '2', '3', '5', '6', '7']
        )

    # Utilities
    ___ assertTreeEqual(self, tree_one, tree_two):
        try:
            self.compare_tree(tree_one, tree_two)
        except AssertionError:
            raise AssertionError("{} != {}".format(tree_one, tree_two))

    ___ compare_tree(self, tree_one, tree_two):
        self.assertEqual(tree_one.data, tree_two.data)

        # Compare left tree nodes
        __ tree_one.left and tree_two.left:
            self.compare_tree(tree_one.left, tree_two.left)
        ____ tree_one.left __ N.. and tree_two.left __ N..
            pass
        ____:
            raise AssertionError

        # Compare right tree nodes
        __ tree_one.right and tree_two.right:
            self.compare_tree(tree_one.right, tree_two.right)
        ____ tree_one.right __ N.. and tree_two.right __ N..
            pass
        ____:
            raise AssertionError


__ __name__ __ '__main__':
    unittest.main()
