_______ unittest

____ dominoes _______ c__


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

c_ DominoesTest(unittest.TestCase):
    ___ test_empty_input_empty_output
        input_dominoes    # list
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    ___ test_singleton_input_singleton_output
        input_dominoes = [(1, 1)]
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    ___ test_singleton_cant_be_chained
        input_dominoes = [(1, 2)]
        output_chain = c__(input_dominoes)
        refute_correct_chain(input_dominoes, output_chain)

    ___ test_three_elements
        input_dominoes = [(1, 2), (3, 1), (2, 3)]
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    ___ test_can_reverse_dominoes
        input_dominoes = [(1, 2), (1, 3), (2, 3)]
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    ___ test_cant_be_chained
        input_dominoes = [(1, 2), (4, 1), (2, 3)]
        output_chain = c__(input_dominoes)
        refute_correct_chain(input_dominoes, output_chain)

    ___ test_disconnected_simple
        input_dominoes = [(1, 1), (2, 2)]
        output_chain = c__(input_dominoes)
        refute_correct_chain(input_dominoes, output_chain)

    ___ test_disconnected_double_loop
        input_dominoes = [(1, 2), (2, 1), (3, 4), (4, 3)]
        output_chain = c__(input_dominoes)
        refute_correct_chain(input_dominoes, output_chain)

    ___ test_disconnected_single_isolated
        input_dominoes = [(1, 2), (2, 3), (3, 1), (4, 4)]
        output_chain = c__(input_dominoes)
        refute_correct_chain(input_dominoes, output_chain)

    ___ test_need_backtrack
        input_dominoes = [(1, 2), (2, 3), (3, 1), (2, 4), (2, 4)]
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    ___ test_separate_loops
        input_dominoes = [(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    ___ test_nine_elements
        input_dominoes = [(1, 2), (5, 3), (3, 1), (1, 2), (2, 4), (1, 6),
                          (2, 3), (3, 4), (5, 6)]
        output_chain = c__(input_dominoes)
        assert_correct_chain(input_dominoes, output_chain)

    # Utility methods

    ___ normalize_dominoes  dominoes):
        r.. l..(s..(t..(s..(domino)) ___ domino __ dominoes))

    ___ assert_same_dominoes  input_dominoes, output_chain):
        msg = ('Dominoes used in the output must be the same '
               'as the ones given in the input')
        input_normal = normalize_dominoes(input_dominoes)
        output_normal = normalize_dominoes(output_chain)
        assertEqual(input_normal, output_normal, msg)

    ___ assert_consecutive_dominoes_match  output_chain):
        ___ i __ r..(l..(output_chain) - 1):
            msg = ("In chain {}, right end of domino {} ({}) "
                   "and left end of domino {} ({}) must match")
            msg = msg.f..(output_chain,
                             i,
                             output_chain[i],
                             i + 1,
                             output_chain[i + 1])
            assertEqual(output_chain[i][1], output_chain[i + 1][0], msg)

    ___ assert_dominoes_at_ends_match  output_chain):
        msg = ("In chain {}, left end of first domino ({}) and "
               "right end of last domino ({}) must match")
        msg = msg.f..(output_chain, output_chain[0], output_chain[-1])
        assertEqual(output_chain[0][0], output_chain[-1][1], msg)

    ___ assert_correct_chain  input_dominoes, output_chain):
        msg = 'There should be a chain for {}'.f..(input_dominoes)
        assertIsNotNone(output_chain, msg)
        assert_same_dominoes(input_dominoes, output_chain)
        __ n.. any(output_chain):
            r..
        assert_consecutive_dominoes_match(output_chain)
        assert_dominoes_at_ends_match(output_chain)

    ___ refute_correct_chain  input_dominoes, output_chain):
        msg = 'There should be no valid chain for {}'.f..(input_dominoes)
        assertIsNone(output_chain, msg)


__ _____ __ _____
    unittest.main()
