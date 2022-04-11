_______ unittest

____ simple_cipher _______ Caesar, Cipher


c_ CipherTest(unittest.TestCase
    ___ test_caesar_encode1
        assertEqual(Caesar().encode('itisawesomeprogramminginpython'),
                         'lwlvdzhvrphsurjudpplqjlqsbwkrq')

    ___ test_caesar_encode2
        assertEqual(Caesar().encode('venividivici'), 'yhqlylglylfl')

    ___ test_caesar_encode3
        assertEqual(Caesar().encode('\'Twas the night before Christmas'),
                         'wzdvwkhqljkwehiruhfkulvwpdv')

    ___ test_caesar_encode_with_numbers
        assertEqual(Caesar().encode('1, 2, 3, Go!'), 'jr')

    ___ test_caesar_decode
        assertEqual(Caesar().d.. 'yhqlylglylfl'), 'venividivici')

    ___ test_cipher_encode1
        c Cipher('a')
        assertEqual(
            c.encode('itisawesomeprogramminginpython'),
            'itisawesomeprogramminginpython')

    ___ test_cipher_encode2
        c Cipher('aaaaaaaaaaaaaaaaaaaaaa')
        assertEqual(
            c.encode('itisawesomeprogramminginpython'),
            'itisawesomeprogramminginpython')

    ___ test_cipher_encode3
        c Cipher('dddddddddddddddddddddd')
        assertEqual(c.encode('venividivici'), 'yhqlylglylfl')

    ___ test_cipher_encode4
        key ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        c Cipher(key)
        assertEqual(c.encode('diffiehellman'), 'gccwkixcltycv')

    ___ test_cipher_encode_short_key
        c Cipher('abcd')
        assertEqual(c.encode('aaaaaaaa'), 'abcdabcd')

    ___ test_cipher_compositiion1
        key ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        plaintext 'adaywithoutlaughterisadaywasted'
        c Cipher(key)
        assertEqual(c.d.. c.encode(plaintext, plaintext)

    ___ test_cipher_compositiion2
        plaintext 'adaywithoutlaughterisadaywasted'
        c Cipher()
        assertEqual(c.d.. c.encode(plaintext, plaintext)

    ___ test_cipher_random_key
        c Cipher()
        assertTrue(
            l..(c.key) >_ 100,
            'A random key must be generated when no key is given!')
        assertTrue(c.key.islower() a.. c.key.i..,
                        'All items in the key must be chars and lowercase!')

    ___ test_cipher_wrong_key
        assertRaises(V..., Cipher, 'a1cde')
        assertRaises(V..., Cipher, 'aBcde')


__ _____ __ _____
    unittest.main()
