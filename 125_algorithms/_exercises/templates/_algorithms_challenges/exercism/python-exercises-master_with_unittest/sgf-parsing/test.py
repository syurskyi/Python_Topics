_______ unittest

____ sgf_parsing _______ p.., SgfTree


c_ SgfParsingTest(unittest.TestCase
    ___ test_empty_input
        input_string = ''
        w__ assertRaisesWithMessage(ValueError
            p..(input_string)

    ___ test_tree_with_no_nodes
        input_string = '()'
        w__ assertRaisesWithMessage(ValueError
            p..(input_string)

    ___ test_node_without_tree
        input_string = ';'
        w__ assertRaisesWithMessage(ValueError
            p..(input_string)

    ___ test_node_without_properties
        input_string = '(;)'
        expected = SgfTree()
        assertEqual(p..(input_string), expected)

    ___ test_single_node_tree
        input_string = '(;A[B])'
        expected = SgfTree(properties={'A':  'B' })
        assertEqual(p..(input_string), expected)

    ___ test_properties_without_delimiter
        input_string = '(;a)'
        w__ assertRaisesWithMessage(ValueError
            p..(input_string)

    ___ test_all_lowercase_property
        input_string = '(;a[b])'
        w__ assertRaisesWithMessage(ValueError
            p..(input_string)

    ___ test_upper_and_lowercase_property
        input_string = '(;Aa[b])'
        w__ assertRaisesWithMessage(ValueError
            p..(input_string)

    ___ test_two_nodes
        input_string = '(;A[B];B[C])'
        expected = SgfTree(
            properties={'A':  'B' },
            children=[
                SgfTree({'B':  'C' })
            ]
        )
        assertEqual(p..(input_string), expected)

    ___ test_two_child_trees
        input_string = '(;A[B](;B[C])(;C[D]))'
        expected = SgfTree(
            properties={'A':  'B' },
            children=[
                SgfTree({'B':  'C' }),
                SgfTree({'C':  'D' }),
            ]
        )
        assertEqual(p..(input_string), expected)

    ___ test_multiple_property_values
        input_string = '(;A[b][c][d])'
        expected = SgfTree(
            properties={'A':  'b', 'c', 'd' }
        )
        assertEqual(p..(input_string), expected)

    ___ test_escaped_property
        input_string = '(;A[\]b\nc\nd\t\te \n\]])'
        expected = SgfTree(
            properties={'A':  ' b\nc\nd  e \n]' }
        )
        assertEqual(p..(input_string), expected)

    # Utility functions
    ___ setUp
        ___
            assertRaisesRegex
        ______ AttributeError:
            assertRaisesRegex = assertRaisesRegexp

    ___ assertRaisesWithMessage  exception
        r.. assertRaisesRegex(exception, r".+")


__ _____ __ _____
    unittest.main()
