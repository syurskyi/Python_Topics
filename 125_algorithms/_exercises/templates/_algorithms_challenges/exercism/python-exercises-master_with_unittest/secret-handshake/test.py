_______ unittest

____ secret_handshake _______ handshake, code


c_ HandshakeTest(unittest.TestCase):
    ___ test_shake_int
        assertEqual(handshake(9), ['wink', 'jump'])

    ___ test_shake_bin1
        assertEqual(
            handshake('10110'), ['close your eyes', 'double blink'])

    ___ test_shake_bin2
        assertEqual(handshake('101'), ['wink', 'close your eyes'])

    ___ test_shake_negative_int
        assertEqual(handshake(-9), [])

    ___ test_shake_bin_invalid
        assertEqual(handshake('121'), [])

    ___ test_unknown_action
        assertEqual(code(['wink', 'sneeze']), '0')

    ___ test_code1
        assertEqual(code(['close your eyes', 'jump']), '1100')

    ___ test_code2
        assertEqual(code(['wink', 'double blink']), '11')

    ___ test_code3
        assertEqual(code(['jump', 'double blink']), '11010')

    ___ test_composition1
        assertEqual(code(handshake(27)), '11011')

    ___ test_composition2
        assertEqual(code(handshake(1)), '1')

    ___ test_composition3
        assertEqual(code(handshake('111')), '111')

    ___ test_composition4
        inp = ['wink', 'double blink', 'jump']
        assertEqual(handshake(code(inp)), inp)


__ _____ __ _____
    unittest.main()
