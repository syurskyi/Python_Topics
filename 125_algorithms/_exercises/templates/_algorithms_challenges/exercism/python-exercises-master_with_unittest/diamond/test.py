import unittest

from diamond import make_diamond


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class DiamondTests(unittest.TestCase):
    ___ test_degenerate_case_with_a_single_row(self):
        self.assertMultiLineEqual(make_diamond('A'), 'A\n')

    ___ test_degenerate_case_with_two_rows(self):
        result = [' A ',
                  'B B',
                  ' A ']
        self.assertMultiLineEqual(make_diamond('B'), '\n'.join(result) + '\n')

    ___ test_smallest_non_degenerate_case_with_odd_diamond_side_length(self):
        result = ['  A  ',
                  ' B B ',
                  'C   C',
                  ' B B ',
                  '  A  ']
        self.assertMultiLineEqual(make_diamond('C'), '\n'.join(result) + '\n')

    ___ test_smallest_non_degenerate_case_with_even_diamond_side_length(self):
        result = ['   A   ',
                  '  B B  ',
                  ' C   C ',
                  'D     D',
                  ' C   C ',
                  '  B B  ',
                  '   A   ']
        self.assertMultiLineEqual(make_diamond('D'), '\n'.join(result) + '\n')

    ___ test_largest_possible_diamond(self):
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
        self.assertMultiLineEqual(make_diamond('Z'), '\n'.join(result) + '\n')


__ __name__ == '__main__':
    unittest.main()
