_______ p__

____ taxes _______ Bracket, Taxed, Taxes

bracket_2020 [
    Bracket(9_875, 0.1),
    Bracket(40_125, 0.12),
    Bracket(85_525, 0.22),
    Bracket(163_300, 0.24),
    Bracket(207_350, 0.32),
    Bracket(518_400, 0.35),
    Bracket(518_401, 0.37),
]


?p__.f..(scope="module")
___ taxes_2019
    income 40_000
    r.. Taxes(income)


?p__.f..(scope="module")
___ taxes_2020_low
    income 8_000
    r.. Taxes(income, bracket_2020)


?p__.f..(scope="module")
___ taxes_2020_over
    income 1_000_000
    r.. Taxes(income, bracket_2020)


___ test_values(taxes_2019
    ... taxes_2019.income __ 40_000
    ... taxes_2019.total __ 4_658.50
    ... taxes_2019.tax_rate __ 11.65
    ... isi..(taxes_2019.bracket, l..)
    ... isi..(taxes_2019.bracket[0], Bracket)


___ test_taxes(taxes_2019
    ... l..(taxes_2019.tax_amounts) __ 3
    ... isi..(taxes_2019.tax_amounts[0], Taxed)
    ... taxes_2019.tax_amounts[2].tax __ 115.50


___ test_summary(taxes_2019
    output s..(taxes_2019).s..
    ... l.. ?  __ 5
    ... "Summary Report" __ output[0]


___ test_low_income(taxes_2020_low
    ... taxes_2020_low.taxes __ 800.00


___ test_report(taxes_2020_over, capfd
    taxes_2020_over.report()
    output ?.r .. 0].s...s..
    ... l.. ?  __ 17
    ... "Summary Report" __ output[0]
    ... "Taxes Breakdown" __ output[6]
    ... "=" __ output[1]
    ... l.. ? [1]) __ 34
    ... "-" __ output[-2]
    ... "14,096.00" __ output[-5]
    ... "0.24" __ output[-6]
