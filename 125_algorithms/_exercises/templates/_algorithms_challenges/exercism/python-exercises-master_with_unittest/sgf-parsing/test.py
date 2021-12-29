_______ unittest

____ sgf_parsing _______ parse, SgfTree


class SgfParsingTest(unittest.TestCase):
    ___ test_empty_input(self):
        input_string = ''
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    ___ test_tree_with_no_nodes(self):
        input_string = '()'
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    ___ test_node_without_tree(self):
        input_string = ';'
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    ___ test_node_without_properties(self):
        input_string = '(;)'
        expected = SgfTree()
        self.assertEqual(parse(input_string), expected)

    ___ test_single_node_tree(self):
        input_string = '(;A[B])'
        expected = SgfTree(properties={'A': ['B']})
        self.assertEqual(parse(input_string), expected)

    ___ test_properties_without_delimiter(self):
        input_string = '(;a)'
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    ___ test_all_lowercase_property(self):
        input_string = '(;a[b])'
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    ___ test_upper_and_lowercase_property(self):
        input_string = '(;Aa[b])'
        with self.assertRaisesWithMessage(ValueError):
            parse(input_string)

    ___ test_two_nodes(self):
        input_string = '(;A[B];B[C])'
        expected = SgfTree(
            properties={'A': ['B']},
            children=[
                SgfTree({'B': ['C']})
            ]
        )
        self.assertEqual(parse(input_string), expected)

    ___ test_two_child_trees(self):
        input_string = '(;A[B](;B[C])(;C[D]))'
        expected = SgfTree(
            properties={'A': ['B']},
            children=[
                SgfTree({'B': ['C']}),
                SgfTree({'C': ['D']}),
            ]
        )
        self.assertEqual(parse(input_string), expected)

    ___ test_multiple_property_values(self):
        input_string = '(;A[b][c][d])'
        expected = SgfTree(
            properties={'A': ['b', 'c', 'd']}
        )
        self.assertEqual(parse(input_string), expected)

    ___ test_escaped_property(self):
        input_string = '(;A[\]b\nc\nd\t\te \n\]])'
        expected = SgfTree(
            properties={'A': [']b\nc\nd  e \n]']}
        )
        self.assertEqual(parse(input_string), expected)

    # Utility functions
    ___ setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    ___ assertRaisesWithMessage(self, exception):
        r.. self.assertRaisesRegex(exception, r".+")


__ __name__ __ '__main__':
    unittest.main()
