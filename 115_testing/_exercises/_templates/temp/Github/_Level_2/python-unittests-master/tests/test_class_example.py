______ u__
____ app ______ class_example
______ array


c_ BoardTest?.?
    ___ test_is_solved
        inputs_and_outputs _ [
            (
                [  # input
                    array.array('B', [1, 2, 3, 4]),
                    array.array('B', [5, 6, 7, 8]),
                    array.array('B', [9, 10, 11, 12]),
                    array.array('B', [13, 14, 15, 0])
                ],
                T..  # output
            ),
            (
                [  # input
                    array.array('B', [2, 1, 3, 4]),
                    array.array('B', [5, 6, 7, 8]),
                    array.array('B', [9, 10, 11, 12]),
                    array.array('B', [13, 14, 15, 0])
                ],
                F..  # output
            ),
        ]

        ___ __.., expected_output __ inputs_and_outputs:
            w__ subTest(input_input, expected_output_expected_output
                board _ class_example.Board(__..)
                actual_output _ board.is_solved()
                aE..(actual_output, expected_output)

    ___ test_check
        missing_two _ [
            array.array('B', [1, 0, 3, 4]),
            array.array('B', [5, 6, 7, 8]),
            array.array('B', [9, 10, 11, 12]),
            array.array('B', [13, 14, 15, 0])
        ]

        board _ class_example.Board(missing_two, check_False)
        assertRaisesRegex(V.., 'Number 2 is missing in the input data', board.check)
