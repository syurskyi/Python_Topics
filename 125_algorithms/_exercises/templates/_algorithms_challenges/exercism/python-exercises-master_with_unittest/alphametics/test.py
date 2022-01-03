_______ unittest

____ alphametics _______ solve


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ TestAlphametics(unittest.TestCase):
    ___ test_puzzle_with_three_letters
        assertEqual(solve("I + BB == ILL"), {"I": 1, "B": 9, "L": 0})

    ___ solution_must_have_unique_value_for_each_letter
        assertEqual(solve("A == B"), {})

    ___ leading_zero_solution_is_invalid
        assertEqual(solve("ACA + DD == BD"), {})

    ___ test_puzzle_with_four_letters
        assertEqual(
            solve("AS + A == MOM"), {"A": 9, "S": 2, "M": 1, "O": 0})

    ___ puzzle_with_six_letters
        assertEqual(
            solve("NO + NO + TOO == LATE"),
            {"N": 7,
             "O": 4,
             "T": 9,
             "L": 1,
             "A": 0,
             "E": 2})

    ___ test_puzzle_with_seven_letters
        assertEqual(
            solve("HE + SEES + THE == LIGHT"),
            {"E": 4,
             "G": 2,
             "H": 5,
             "I": 0,
             "L": 1,
             "S": 9,
             "T": 7})

    ___ test_puzzle_with_eight_letters
        assertEqual(
            solve("SEND + MORE == MONEY"),
            {"S": 9,
             "E": 5,
             "N": 6,
             "D": 7,
             "M": 1,
             "O": 0,
             "R": 8,
             "Y": 2})

    ___ test_puzzle_with_ten_letters
        assertEqual(
            solve("AND + A + STRONG + OFFENSE + AS + A + GOOD == DEFENSE"),
            {"A": 5,
             "D": 3,
             "E": 4,
             "F": 7,
             "G": 8,
             "N": 0,
             "O": 2,
             "R": 1,
             "S": 6,
             "T": 9})


__ __name__ __ '__main__':
    unittest.main()
