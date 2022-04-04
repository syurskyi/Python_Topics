____ rhombus _______ gen_rhombus


___ test_rhombus_width3
    # recommended: actual before expected
    # https://twitter.com/brianokken/status/1063337328553295876
    actual = l..(gen_rhombus(3
    expected =  ' * ', '***', ' * '
    ... actual __ expected


___ test_rhombus_width5
    actual = l..(gen_rhombus(5
    expected =  '  *  ', ' *** ', '*****',
                ' *** ', '  *  '
    ... actual __ expected


___ test_rhombus_width11
    """print('\n'.join(expected)) would give (ignore indents):
         *
        ***
       *****
      *******
     *********
    ***********
     *********
      *******
       *****
        ***
         *
    """
    actual = l..(gen_rhombus(11
    expected =  '     *     ', '    ***    ', '   *****   ',
                '  *******  ', ' ********* ', '***********', ' ********* ',
                '  *******  ', '   *****   ', '    ***    ', '     *     '
    ... actual __ expected