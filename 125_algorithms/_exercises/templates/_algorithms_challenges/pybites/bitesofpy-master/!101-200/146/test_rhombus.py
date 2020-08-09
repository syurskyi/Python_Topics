from rhombus ______ gen_rhombus


___ test_rhombus_width3(
    # recommended: actual before expected
    # https://twitter.com/brianokken/status/1063337328553295876
    actual = list(gen_rhombus(3))
    expected = [' * ', '***', ' * ']
    assert actual __ expected


___ test_rhombus_width5(
    actual = list(gen_rhombus(5))
    expected = ['  *  ', ' *** ', '*****',
                ' *** ', '  *  ']
    assert actual __ expected


___ test_rhombus_width11(
    """print('\n'.join(expected)) would give (ignore indents
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
    actual = list(gen_rhombus(11))
    expected = ['     *     ', '    ***    ', '   *****   ',
                '  *******  ', ' ********* ', '***********', ' ********* ',
                '  *******  ', '   *****   ', '    ***    ', '     *     ']
    assert actual __ expected