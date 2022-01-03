_______ unittest

____ diamond _______ make_diamond


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ DiamondTests(unittest.TestCase):
    ___ test_degenerate_case_with_a_single_row
        assertMultiLineEqual(make_diamond('A'), 'A\n')

    ___ test_degenerate_case_with_two_rows
        result = [' A ',
                  'B B',
                  ' A ']
        assertMultiLineEqual(make_diamond('B'), '\n'.j..(result) + '\n')

    ___ test_smallest_non_degenerate_case_with_odd_diamond_side_length
        result = ['  A  ',
                  ' B B ',
                  'C   C',
                  ' B B ',
                  '  A  ']
        assertMultiLineEqual(make_diamond('C'), '\n'.j..(result) + '\n')

    ___ test_smallest_non_degenerate_case_with_even_diamond_side_length
        result = ['   A   ',
                  '  B B  ',
                  ' C   C ',
                  'D     D',
                  ' C   C ',
                  '  B B  ',
                  '   A   ']
        assertMultiLineEqual(make_diamond('D'), '\n'.j..(result) + '\n')

    ___ test_largest_possible_diamond
        result = ['                         A                         ',
                  '                        B B                        ',
                  '                       C   C                       ',
                  '                      D     D                      ',
                  '                     E       E                     ',
                  '                    F         F                    ',
                  '                   G           G                   ',
                  '                  H             H                  ',
                  '                 I               I                 ',
                  '                J                 J                ',
                  '               K                   K               ',
                  '              L                     L              ',
                  '             M                       M             ',
                  '            N                         N            ',
                  '           O                           O           ',
                  '          P                             P          ',
                  '         Q                               Q         ',
                  '        R                                 R        ',
                  '       S                                   S       ',
                  '      T                                     T      ',
                  '     U                                       U     ',
                  '    V                                         V    ',
                  '   W                                           W   ',
                  '  X                                             X  ',
                  ' Y                                               Y ',
                  'Z                                                 Z',
                  ' Y                                               Y ',
                  '  X                                             X  ',
                  '   W                                           W   ',
                  '    V                                         V    ',
                  '     U                                       U     ',
                  '      T                                     T      ',
                  '       S                                   S       ',
                  '        R                                 R        ',
                  '         Q                               Q         ',
                  '          P                             P          ',
                  '           O                           O           ',
                  '            N                         N            ',
                  '             M                       M             ',
                  '              L                     L              ',
                  '               K                   K               ',
                  '                J                 J                ',
                  '                 I               I                 ',
                  '                  H             H                  ',
                  '                   G           G                   ',
                  '                    F         F                    ',
                  '                     E       E                     ',
                  '                      D     D                      ',
                  '                       C   C                       ',
                  '                        B B                        ',
                  '                         A                         ']
        assertMultiLineEqual(make_diamond('Z'), '\n'.j..(result) + '\n')


__ __name__ __ '__main__':
    unittest.main()
