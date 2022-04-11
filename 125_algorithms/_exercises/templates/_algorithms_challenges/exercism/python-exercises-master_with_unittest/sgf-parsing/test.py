_______ unittest

____ sgf_parsing _______ p.., SgfTree


c_ SgfParsingTest(unittest.TestCase
    ___ test_empty_input
        input_string ''
        w__ assertRaisesWithMessage(V...
            p..(input_string)

    ___ test_tree_with_no_nodes
        input_string '()'
        w__ assertRaisesWithMessage(V...
            p..(input_string)

    ___ test_node_without_tree
        input_string ';'
        w__ assertRaisesWithMessage(V...
            p..(input_string)

    ___ test_node_without_properties
        input_string '(;)'
        e.. SgfTree()
        assertEqual(p..(input_string), e..)

    ___ test_single_node_tree
        input_string '(;A[B])'
        e.. SgfTree(properties={'A':  'B' })
        assertEqual(p..(input_string), e..)

    ___ test_properties_without_delimiter
        input_string '(;a)'
        w__ assertRaisesWithMessage(V...
            p..(input_string)

    ___ test_all_lowercase_property
        input_string '(;a[b])'
        w__ assertRaisesWithMessage(V...
            p..(input_string)

    ___ test_upper_and_lowercase_property
        input_string '(;Aa[b])'
        w__ assertRaisesWithMessage(V...
            p..(input_string)

    ___ test_two_nodes
        input_string '(;A[B];B[C])'
        e.. SgfTree(
            properties={'A':  'B' },
            children=[
                SgfTree({'B':  'C' })
            ]
        )
        assertEqual(p..(input_string), e..)

    ___ test_two_child_trees
        input_string '(;A[B](;B[C])(;C[D]))'
        e.. SgfTree(
            properties={'A':  'B' },
            children=[
                SgfTree({'B':  'C' }),
                SgfTree({'C':  'D' }),
            ]
        )
        assertEqual(p..(input_string), e..)

    ___ test_multiple_property_values
        input_string '(;A[b][c][d])'
        e.. SgfTree(
            properties={'A':  'b', 'c', 'd' }
        )
        assertEqual(p..(input_string), e..)

    ___ test_escaped_property
        input_string '(;A[\]b\nc\nd\t\te \n\]])'
        e.. SgfTree(
            properties={'A':  ' b\nc\nd  e \n]' }
        )
        assertEqual(p..(input_string), e..)

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
