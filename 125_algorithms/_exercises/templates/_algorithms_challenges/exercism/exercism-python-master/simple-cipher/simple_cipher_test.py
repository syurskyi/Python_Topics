______ unittest

from cipher ______ Caesar, Cipher


class CipherTest(unittest.TestCase

    ___ test_caesar_encode1(self
        self.assertEqual('lwlvdzhvrphsurjudpplqjlqsbwkrq',
                         Caesar().encode('itisawesomeprogramminginpython'))

    ___ test_caesar_encode2(self
        self.assertEqual('yhqlylglylfl', Caesar().encode('venividivici'))

    ___ test_caesar_encode3(self
        self.assertEqual('wzdvwkhqljkwehiruhfkulvwpdv',
                         Caesar().encode('\'Twas the night before Christmas'))

    ___ test_caesar_encode_with_numbers(self
        self.assertEqual('jr', Caesar().encode('1, 2, 3, Go!'))

    ___ test_caesar_decode(self
        self.assertEqual('venividivici', Caesar().decode('yhqlylglylfl'))

    ___ test_cipher_encode1(self
        c = Cipher('a')
        self.assertEqual('itisawesomeprogramminginpython',
                         c.encode('itisawesomeprogramminginpython'))

    ___ test_cipher_encode2(self
        c = Cipher('aaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual('itisawesomeprogramminginpython',
                         c.encode('itisawesomeprogramminginpython'))

    ___ test_cipher_encode3(self
        c = Cipher('dddddddddddddddddddddd')
        self.assertEqual('yhqlylglylfl', c.encode('venividivici'))

    ___ test_cipher_encode4(self
        key = ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        c = Cipher(key)
        self.assertEqual('gccwkixcltycv', c.encode('diffiehellman'))

    ___ test_cipher_encode_short_key(self
        c = Cipher('abcd')
        self.assertEqual('abcdabcd', c.encode('aaaaaaaa'))

    ___ test_cipher_compositiion1(self
        key = ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher(key)
        self.assertEqual(plaintext, c.decode(c.encode(plaintext)))

    ___ test_cipher_compositiion2(self
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher()
        self.assertEqual(plaintext, c.decode(c.encode(plaintext)))

    ___ test_cipher_random_key(self
        c = Cipher()
        self.assertTrue(le.(c.key) >= 100,
                        'A random key must be generated when no key is given!')
        self.assertTrue(c.key.islower() and c.key.isalpha(),
                        'All items in the key must be chars and lowercase!')

    ___ test_cipher_wrong_key(self
        self.assertRaises(ValueError, Cipher, 'a1cde')
        self.assertRaises(ValueError, Cipher, 'aBcde')


__ __name__ __ '__main__':
    unittest.main()
