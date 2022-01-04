_______ unittest

____ zipper _______ Zipper


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

c_ ZipperTest(unittest.TestCase):
    ___ bt(self, value, left, right):
        r.. {
            'value': value,
            'left': left,
            'right': right
        }

    ___ leaf(self, value):
        r.. bt(value, N.., N..)

    ___ create_trees
        t1 = bt(1, bt(2, N.., leaf(3)), leaf(4))
        t2 = bt(1, bt(5, N.., leaf(3)), leaf(4))
        t3 = bt(1, bt(2, leaf(5), leaf(3)), leaf(4))
        t4 = bt(1, leaf(2), leaf(4))
        r.. (t1, t2, t3, t4)

    ___ test_data_is_retained
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        tree = zipper.to_tree()
        assertEqual(tree, t1)

    ___ test_left_and_right_value
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        assertEqual(zipper.left().right().value(), 3)

    ___ test_dead_end
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        assertIsNone(zipper.left().left())

    ___ test_tree_from_deep_focus
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        assertEqual(zipper.left().right().to_tree(), t1)

    ___ test_set_value
        t1, t2, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_value(5)
        tree = updatedZipper.to_tree()
        assertEqual(tree, t2)

    ___ test_set_left_with_value
        t1, _, t3, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_left(leaf(5))
        tree = updatedZipper.to_tree()
        assertEqual(tree, t3)

    ___ test_set_right_to_none
        t1, _, _, t4 = create_trees()
        zipper = Zipper.from_tree(t1)
        updatedZipper = zipper.left().set_right(N..)
        tree = updatedZipper.to_tree()
        assertEqual(tree, t4)

    ___ test_different_paths_to_same_zipper
        t1, _, _, _ = create_trees()
        zipper = Zipper.from_tree(t1)
        assertEqual(zipper.left().up().right().to_tree(),
                         zipper.right().to_tree())


__ _____ __ _____
    unittest.main()
