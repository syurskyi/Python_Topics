_______ unittest

____ secret_handshake _______ handshake, code


class HandshakeTest(unittest.TestCase):
    ___ test_shake_int(self):
        self.assertEqual(handshake(9), ['wink', 'jump'])

    ___ test_shake_bin1(self):
        self.assertEqual(
            handshake('10110'), ['close your eyes', 'double blink'])

    ___ test_shake_bin2(self):
        self.assertEqual(handshake('101'), ['wink', 'close your eyes'])

    ___ test_shake_negative_int(self):
        self.assertEqual(handshake(-9), [])

    ___ test_shake_bin_invalid(self):
        self.assertEqual(handshake('121'), [])

    ___ test_unknown_action(self):
        self.assertEqual(code(['wink', 'sneeze']), '0')

    ___ test_code1(self):
        self.assertEqual(code(['close your eyes', 'jump']), '1100')

    ___ test_code2(self):
        self.assertEqual(code(['wink', 'double blink']), '11')

    ___ test_code3(self):
        self.assertEqual(code(['jump', 'double blink']), '11010')

    ___ test_composition1(self):
        self.assertEqual(code(handshake(27)), '11011')

    ___ test_composition2(self):
        self.assertEqual(code(handshake(1)), '1')

    ___ test_composition3(self):
        self.assertEqual(code(handshake('111')), '111')

    ___ test_composition4(self):
        inp = ['wink', 'double blink', 'jump']
        self.assertEqual(handshake(code(inp)), inp)


__ __name__ __ '__main__':
    unittest.main()
