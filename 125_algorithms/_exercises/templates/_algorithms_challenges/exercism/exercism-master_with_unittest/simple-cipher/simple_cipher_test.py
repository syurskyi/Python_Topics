_______ unittest

____ cipher _______ Caesar, Cipher


c_ CipherTest(unittest.TestCase

    ___ test_caesar_encode1
        assertEqual('lwlvdzhvrphsurjudpplqjlqsbwkrq',
                         Caesar().e.. 'itisawesomeprogramminginpython'

    ___ test_caesar_encode2
        assertEqual('yhqlylglylfl', Caesar().e.. 'venividivici'

    ___ test_caesar_encode3
        assertEqual('wzdvwkhqljkwehiruhfkulvwpdv',
                         Caesar().e.. '\'Twas the night before Christmas'

    ___ test_caesar_encode_with_numbers
        assertEqual('jr', Caesar().e.. '1, 2, 3, Go!'

    ___ test_caesar_decode
        assertEqual('venividivici', Caesar().d.. 'yhqlylglylfl'

    ___ test_cipher_encode1
        c Cipher('a')
        assertEqual('itisawesomeprogramminginpython',
                         c.e.. 'itisawesomeprogramminginpython'

    ___ test_cipher_encode2
        c Cipher('aaaaaaaaaaaaaaaaaaaaaa')
        assertEqual('itisawesomeprogramminginpython',
                         c.e.. 'itisawesomeprogramminginpython'

    ___ test_cipher_encode3
        c Cipher('dddddddddddddddddddddd')
        assertEqual('yhqlylglylfl', c.e.. 'venividivici'

    ___ test_cipher_encode4
        key ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        c Cipher(key)
        assertEqual('gccwkixcltycv', c.e.. 'diffiehellman'

    ___ test_cipher_encode_short_key
        c Cipher('abcd')
        assertEqual('abcdabcd', c.e.. 'aaaaaaaa'

    ___ test_cipher_compositiion1
        key ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        plaintext 'adaywithoutlaughterisadaywasted'
        c Cipher(key)
        assertEqual(plaintext, c.d.. c.e.. plaintext)))

    ___ test_cipher_compositiion2
        plaintext 'adaywithoutlaughterisadaywasted'
        c Cipher()
        assertEqual(plaintext, c.d.. c.e.. plaintext)))

    ___ test_cipher_random_key
        c Cipher()
        assertTrue(l..(c.key) >_ 100,
                        'A random key must be generated when no key is given!')
        assertTrue(c.key.islower() a.. c.key.i..,
                        'All items in the key must be chars and lowercase!')

    ___ test_cipher_wrong_key
        assertRaises(V..., Cipher, 'a1cde')
        assertRaises(V..., Cipher, 'aBcde')


__ _____ __ _____
    unittest.main()
