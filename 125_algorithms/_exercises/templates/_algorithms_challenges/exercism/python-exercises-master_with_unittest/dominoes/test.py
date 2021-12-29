_______ unittest

____ dominoes _______ chain


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

class DominoesTest(unittest.TestCase):
    ___ test_empty_input_empty_output(self):
        input_dominoes    # list
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    ___ test_singleton_input_singleton_output(self):
        input_dominoes = [(1, 1)]
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    ___ test_singleton_cant_be_chained(self):
        input_dominoes = [(1, 2)]
        output_chain = chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    ___ test_three_elements(self):
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    ___ test_can_reverse_dominoes(self):
        input_dominoes = [(1, 2), (1, 3), (2, 3)]
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    ___ test_cant_be_chained(self):
        input_dominoes = [(1, 2), (4, 1), (2, 3)]
        output_chain = chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    ___ test_disconnected_simple(self):
        input_dominoes = [(1, 1), (2, 2)]
        output_chain = chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    ___ test_disconnected_double_loop(self):
        input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
        output_chain = chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    ___ test_disconnected_single_isolated(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
        output_chain = chain(input_dominoes)
        self.refute_correct_chain(input_dominoes, output_chain)

    ___ test_need_backtrack(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    ___ test_separate_loops(self):
        input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    ___ test_nine_elements(self):
        input_dominoes = [(1, 2), (5, 3), (3, 1), (1, 2), (2, 4), (1, 6),
                          (2, 3), (3, 4), (5, 6)]
        output_chain = chain(input_dominoes)
        self.assert_correct_chain(input_dominoes, output_chain)

    # Utility methods

    ___ normalize_dominoes(self, dominoes):
        r.. l..(s..(tuple(s..(domino)) ___ domino __ dominoes))

    ___ assert_same_dominoes(self, input_dominoes, output_chain):
        msg = ('Dominoes used in the output must be the same '
               'as the ones given in the input')
        input_normal = self.normalize_dominoes(input_dominoes)
        output_normal = self.normalize_dominoes(output_chain)
        self.assertEqual(input_normal, output_normal, msg)

    ___ assert_consecutive_dominoes_match(self, output_chain):
        ___ i __ r..(l..(output_chain) - 1):
            msg = ("In chain {}, right end of domino {} ({}) "
                   "and left end of domino {} ({}) must match")
            msg = msg.f..(output_chain,
                             i,
                             output_chain[i],
                             i + 1,
                             output_chain[i + 1])
            self.assertEqual(output_chain[i][1], output_chain[i + 1][0], msg)

    ___ assert_dominoes_at_ends_match(self, output_chain):
        msg = ("In chain {}, left end of first domino ({}) and "
               "right end of last domino ({}) must match")
        msg = msg.f..(output_chain, output_chain[0], output_chain[-1])
        self.assertEqual(output_chain[0][0], output_chain[-1][1], msg)

    ___ assert_correct_chain(self, input_dominoes, output_chain):
        msg = 'There should be a chain for {}'.f..(input_dominoes)
        self.assertIsNotNone(output_chain, msg)
        self.assert_same_dominoes(input_dominoes, output_chain)
        __ n.. any(output_chain):
            r..
        self.assert_consecutive_dominoes_match(output_chain)
        self.assert_dominoes_at_ends_match(output_chain)

    ___ refute_correct_chain(self, input_dominoes, output_chain):
        msg = 'There should be no valid chain for {}'.f..(input_dominoes)
        self.assertIsNone(output_chain, msg)


__ __name__ __ '__main__':
    unittest.main()
