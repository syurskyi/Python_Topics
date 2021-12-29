_______ unittest

____ handshake _______ handshake, code


class HandshakeTest(unittest.TestCase):
    ___ test_shake_int(self):
        self.assertEqual(['wink', 'jump'], handshake(9))

    ___ test_shake_bin1(self):
        self.assertEqual(['close your eyes', 'double blink'],
                         handshake('10110'))

    ___ test_shake_bin2(self):
        self.assertEqual(['wink', 'close your eyes'], handshake('101'))

    ___ test_shake_negative_int(self):
        self.assertEqual([], handshake(-9))

    ___ test_shake_bin_invalid(self):
        self.assertEqual([], handshake('121'))

    ___ test_unknown_action(self):
        self.assertEqual('0', code(['wink', 'sneeze']))

    ___ test_code1(self):
        self.assertEqual('1100', code(['close your eyes', 'jump']))

    ___ test_code2(self):
        self.assertEqual('11', code(['wink', 'double blink']))

    ___ test_code3(self):
        self.assertEqual('11010', code(['jump', 'double blink']))

    ___ test_composition1(self):
        self.assertEqual('11011', code(handshake(27)))

    ___ test_composition2(self):
        self.assertEqual('1', code(handshake(1)))

    ___ test_composition3(self):
        self.assertEqual('111', code(handshake('111')))

    ___ test_composition4(self):
        inp = ['wink', 'double blink', 'jump']
        self.assertEqual(inp, handshake(code(inp)))


__ __name__ __ '__main__':
    unittest.main()
