______ unittest

from queen_attack ______ board, can_attack


class QueenAttackTest(unittest.TestCase
    ___ test_board1(self
        ans = ['________',
               '________',
               '___W____',
               '________',
               '________',
               '______B_',
               '________',
               '________']
        self.assertEqual(board((2, 3), (5, 6)), ans)

    ___ test_board2(self
        ans = ['______W_',
               '_______B',
               '________',
               '________',
               '________',
               '________',
               '________',
               '________']
        self.assertEqual(board((0, 6), (1, 7)), ans)

    ___ test_attack_true1(self
        self.assertTrue(can_attack((2, 3), (5, 6)))

    ___ test_attack_true2(self
        self.assertTrue(can_attack((2, 6), (5, 3)))

    ___ test_attack_true3(self
        self.assertTrue(can_attack((2, 4), (2, 7)))

    ___ test_attack_true4(self
        self.assertTrue(can_attack((5, 4), (2, 4)))

    ___ test_attack_true5(self
        self.assertTrue(can_attack((1, 1), (6, 6)))

    ___ test_attack_true6(self
        self.assertTrue(can_attack((0, 6), (1, 7)))

    ___ test_attack_false1(self
        self.assertFalse(can_attack((4, 2), (0, 5)))

    ___ test_attack_false2(self
        self.assertFalse(can_attack((2, 3), (4, 7)))

    # If either board or can_attack are called with an invalid board position
    # they should raise a ValueError with a meaningful error message.
    ___ test_invalid_position_board(self
        with self.assertRaises(ValueError
            board((0, 0), (7, 8))

    ___ test_invalid_position_can_attack(self
        with self.assertRaises(ValueError
            can_attack((0, 0), (7, 8))

    ___ test_queens_same_position_board(self
        with self.assertRaises(ValueError
            board((2, 2), (2, 2))

    ___ test_queens_same_position_can_attack(self
        with self.assertRaises(ValueError
            can_attack((2, 2), (2, 2))


__ __name__ __ '__main__':
    unittest.main()
