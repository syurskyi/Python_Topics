import unittest
from app import class_example
import array


class BoardTest(unittest.TestCase):
    def test_is_solved(self):
        inputs_and_outputs = [
            (
                [  # input
                    array.array('B', [1, 2, 3, 4]),
                    array.array('B', [5, 6, 7, 8]),
                    array.array('B', [9, 10, 11, 12]),
                    array.array('B', [13, 14, 15, 0])
                ],
                True  # output
            ),
            (
                [  # input
                    array.array('B', [2, 1, 3, 4]),
                    array.array('B', [5, 6, 7, 8]),
                    array.array('B', [9, 10, 11, 12]),
                    array.array('B', [13, 14, 15, 0])
                ],
                False  # output
            ),
        ]

        for input, expected_output in inputs_and_outputs:
            with self.subTest(input=input, expected_output=expected_output):
                board = class_example.Board(input)
                actual_output = board.is_solved()
                self.assertEqual(actual_output, expected_output)

    def test_check(self):
        missing_two = [
            array.array('B', [1, 0, 3, 4]),
            array.array('B', [5, 6, 7, 8]),
            array.array('B', [9, 10, 11, 12]),
            array.array('B', [13, 14, 15, 0])
        ]

        board = class_example.Board(missing_two, check=False)
        self.assertRaisesRegex(ValueError, 'Number 2 is missing in the input data', board.check)
