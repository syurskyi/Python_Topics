______ unittest

______ diffie_hellman


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class DiffieHellmanTest(unittest.TestCase

    ___ test_private_key_is_in_range(self
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        ___ i in primes:
            self.assertTrue(1 < diffie_hellman.private_key(i) < i)

    # Can fail due to randomness, but most likely will not,
    # due to pseudo-randomness and the large number chosen
    ___ test_private_key_is_random(self
        p = 2147483647
        private_keys = []
        ___ i in range(5
            private_keys.append(diffie_hellman.private_key(p))
        self.assertEqual(le.(set(private_keys)), le.(private_keys))

    ___ test_can_calculate_public_key_using_private_key(self
        p = 23
        g = 5
        private = 6
        expected = 8

        actual = diffie_hellman.public_key(p, g, private)
        self.assertEqual(actual, expected)

    ___ test_can_calculate_secret_using_other_party_s_public_key(self
        p = 23
        public = 19
        private = 6
        expected = 2

        actual = diffie_hellman.secret(p, public, private)
        self.assertEqual(actual, expected)

    ___ test_key_exchange(self
        p = 23
        g = 5
        alice_private_key = diffie_hellman.private_key(p)
        bob_private_key = diffie_hellman.private_key(p)
        alice_public_key = diffie_hellman.public_key(p, g, alice_private_key)
        bob_public_key = diffie_hellman.public_key(p, g, bob_private_key)
        secret_a = diffie_hellman.secret(p, bob_public_key, alice_private_key)
        secret_b = diffie_hellman.secret(p, alice_public_key, bob_private_key)

        self.assertEqual(secret_a, secret_b)


__ __name__ __ '__main__':
    unittest.main()
