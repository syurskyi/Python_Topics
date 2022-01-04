____ arithmetic _______ calc_sums, VALUES


EXPECTED = (
    ("0.1", "0.2", "0.30"),
    ("0.2", "0.3", "0.50"),
    ("0.3", "0.005", "0.31"),
    ("0.005", "0.005", "0.01"),
    ("0.005", "2.67", "2.68"),
)


___ test_calc_sums
    i = 0
    ___ i, line __ e..(calc_sums(VALUES)):
        n1, n2, sum_ = EXPECTED[i]
        ... (
            line __ f"The sum of {n1} and {n2}, rounded to two decimal places, is {sum_}."
        )

    # Confirm all output was generated
    ... i __ l..(EXPECTED) - 1, "Not all output was generated!"