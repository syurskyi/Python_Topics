_______ unittest

____ simple_cipher _______ Caesar, Cipher


class CipherTest(unittest.TestCase):
    ___ test_caesar_encode1(self):
        self.assertEqual(Caesar().encode('itisawesomeprogramminginpython'),
                         'lwlvdzhvrphsurjudpplqjlqsbwkrq')

    ___ test_caesar_encode2(self):
        self.assertEqual(Caesar().encode('venividivici'), 'yhqlylglylfl')

    ___ test_caesar_encode3(self):
        self.assertEqual(Caesar().encode('\'Twas the night before Christmas'),
                         'wzdvwkhqljkwehiruhfkulvwpdv')

    ___ test_caesar_encode_with_numbers(self):
        self.assertEqual(Caesar().encode('1, 2, 3, Go!'), 'jr')

    ___ test_caesar_decode(self):
        self.assertEqual(Caesar().decode('yhqlylglylfl'), 'venividivici')

    ___ test_cipher_encode1(self):
        c = Cipher('a')
        self.assertEqual(
            c.encode('itisawesomeprogramminginpython'),
            'itisawesomeprogramminginpython')

    ___ test_cipher_encode2(self):
        c = Cipher('aaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(
            c.encode('itisawesomeprogramminginpython'),
            'itisawesomeprogramminginpython')

    ___ test_cipher_encode3(self):
        c = Cipher('dddddddddddddddddddddd')
        self.assertEqual(c.encode('venividivici'), 'yhqlylglylfl')

    ___ test_cipher_encode4(self):
        key = ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        c = Cipher(key)
        self.assertEqual(c.encode('diffiehellman'), 'gccwkixcltycv')

    ___ test_cipher_encode_short_key(self):
        c = Cipher('abcd')
        self.assertEqual(c.encode('aaaaaaaa'), 'abcdabcd')

    ___ test_cipher_compositiion1(self):
        key = ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher(key)
        self.assertEqual(c.decode(c.encode(plaintext)), plaintext)

    ___ test_cipher_compositiion2(self):
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher()
        self.assertEqual(c.decode(c.encode(plaintext)), plaintext)

    ___ test_cipher_random_key(self):
        c = Cipher()
        self.assertTrue(
            l..(c.key) >= 100,
            'A random key must be generated when no key is given!')
        self.assertTrue(c.key.islower() a.. c.key.isalpha(),
                        'All items in the key must be chars and lowercase!')

    ___ test_cipher_wrong_key(self):
        self.assertRaises(ValueError, Cipher, 'a1cde')
        self.assertRaises(ValueError, Cipher, 'aBcde')


__ __name__ __ '__main__':
    unittest.main()
