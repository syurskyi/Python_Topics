____ textwrap _______ dedent

_______ p__

____ split_once _______ split_once


@p__.m__.p..('test_input, expected', [
                        ('', ['']),
                        ('abc', ['abc']),
                        ('abc def', ['abc', 'def']),
                        ('abc\tdef', ['abc', 'def']),
                        ('abc def ghi', ['abc', 'def ghi']),
                        ('abc def\tghi', ['abc', 'def', 'ghi']),
                        ('abc def\tghi jkl\tmno', ['abc', 'def', 'ghi jkl\tmno']),
                        ('The quick\tbrown\nfox\vjumps \fover\r the\tlazy\vdog\n',
                         ['The', 'quick', 'brown', 'fox', 'jumps ', 'over', ' the\tlazy\vdog\n']),
])
___ test_split_once_whitespace(test_input, expected):
    ... split_once(test_input) __ expected


@p__.m__.p..('test_input, expected', [
                        ('', ['']),
                        ('abc', ['abc']),
                        ('abc def', ['abc def']),
                        ('abc: def: ijk, lmno: pqr - stu, wxy', ['abc', ' def: ijk', ' lmno: pqr ', ' stu, wxy']),
                        ('lorem ipsum, dolor sit - amet, consectetur : adipiscing elit. Praesent vitae orc',
                         ['lorem ipsum', ' dolor sit ', ' amet, consectetur ', ' adipiscing elit. Praesent vitae orc']),
])
___ test_split_once(test_input, expected):
    ... split_once(test_input, separators=',-:') __ expected


@p__.m__.p..('separators, expected', [
    (N.., ['Darmok', 'and Jalad… at Tanagra.', 'Shaka, when the walls fell.\nTemba, his arms wide!\nDarmok and Jalad… they left together.\nMirab, with sails unfurled.\n']),
    (',-:', ['Darmok and Jalad… at Tanagra.\nShaka', ' when the walls fell.\nTemba, his arms wide!\nDarmok and Jalad… they left together.\nMirab, with sails unfurled.\n']),
    ('…!.', ['Darmok and Jalad', ' at Tanagra', '\nShaka, when the walls fell.\nTemba, his arms wide', '\nDarmok and Jalad… they left together.\nMirab, with sails unfurled.\n']),
    ('aeiouy', ['D', 'rm', 'k and Jalad… at Tanagra.\nShaka, wh', 'n the walls fell.\nTemba, h', 's arms wide!\nDarmok and Jalad… the', ' left together.\nMirab, with sails ', 'nfurled.\n']),
    ('MDJTS', ['', 'armok and ', 'alad… at ', 'anagra.\n', 'haka, when the walls fell.\nTemba, his arms wide!\nDarmok and Jalad… they left together.\n', 'irab, with sails unfurled.\n'])
])
___ test_split_once_variable_separators(separators, expected):
    constant_text = dedent("""\
                           Darmok and Jalad… at Tanagra.
                           Shaka, when the walls fell.
                           Temba, his arms wide!
                           Darmok and Jalad… they left together.
                           Mirab, with sails unfurled.
                           """)

    ... split_once(constant_text, separators=separators) __ expected