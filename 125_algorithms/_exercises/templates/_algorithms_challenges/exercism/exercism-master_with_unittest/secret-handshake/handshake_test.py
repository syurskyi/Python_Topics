_______ unittest

____ handshake _______ handshake, code


c_ HandshakeTest(unittest.TestCase):
    ___ test_shake_int
        assertEqual(['wink', 'jump'], handshake(9))

    ___ test_shake_bin1
        assertEqual(['close your eyes', 'double blink'],
                         handshake('10110'))

    ___ test_shake_bin2
        assertEqual(['wink', 'close your eyes'], handshake('101'))

    ___ test_shake_negative_int
        assertEqual([], handshake(-9))

    ___ test_shake_bin_invalid
        assertEqual([], handshake('121'))

    ___ test_unknown_action
        assertEqual('0', code(['wink', 'sneeze']))

    ___ test_code1
        assertEqual('1100', code(['close your eyes', 'jump']))

    ___ test_code2
        assertEqual('11', code(['wink', 'double blink']))

    ___ test_code3
        assertEqual('11010', code(['jump', 'double blink']))

    ___ test_composition1
        assertEqual('11011', code(handshake(27)))

    ___ test_composition2
        assertEqual('1', code(handshake(1)))

    ___ test_composition3
        assertEqual('111', code(handshake('111')))

    ___ test_composition4
        inp = ['wink', 'double blink', 'jump']
        assertEqual(inp, handshake(code(inp)))


__ _____ __ _____
    unittest.main()
