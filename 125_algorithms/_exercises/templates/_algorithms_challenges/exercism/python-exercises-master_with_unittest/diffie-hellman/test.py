_______ unittest

_______ diffie_hellman


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

c_ DiffieHellmanTest(unittest.TestCase

    ___ test_private_key_is_in_range
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        ___ i __ primes:
            assertTrue(1 < diffie_hellman.private_key(i) < i)

    # Can fail due to randomness, but most likely will not,
    # due to pseudo-randomness and the large number chosen
    ___ test_private_key_is_random
        p = 2147483647
        private_keys    # list
        ___ i __ r..(5
            private_keys.a..(diffie_hellman.private_key(p
        assertEqual(l..(s..(private_keys, l..(private_keys

    ___ test_can_calculate_public_key_using_private_key
        p = 23
        g = 5
        private = 6
        expected = 8

        actual = diffie_hellman.public_key(p, g, private)
        assertEqual(actual, expected)

    ___ test_can_calculate_secret_using_other_party_s_public_key
        p = 23
        public = 19
        private = 6
        expected = 2

        actual = diffie_hellman.secret(p, public, private)
        assertEqual(actual, expected)

    ___ test_key_exchange
        p = 23
        g = 5
        alice_private_key = diffie_hellman.private_key(p)
        bob_private_key = diffie_hellman.private_key(p)
        alice_public_key = diffie_hellman.public_key(p, g, alice_private_key)
        bob_public_key = diffie_hellman.public_key(p, g, bob_private_key)
        secret_a = diffie_hellman.secret(p, bob_public_key, alice_private_key)
        secret_b = diffie_hellman.secret(p, alice_public_key, bob_private_key)

        assertEqual(secret_a, secret_b)


__ _____ __ _____
    unittest.main()
