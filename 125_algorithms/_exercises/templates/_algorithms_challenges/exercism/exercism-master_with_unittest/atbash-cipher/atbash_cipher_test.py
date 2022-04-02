_______ unittest

____ atbash_cipher _______ decode, encode


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

c_ AtbashCipherTest(unittest.TestCase
    ___ test_encode_no
        assertMultiLineEqual(encode("no"), "ml")

    ___ test_encode_yes
        assertMultiLineEqual(encode("yes"), "bvh")

    ___ test_encode_OMG
        assertMultiLineEqual(encode("OMG"), "lnt")

    ___ test_encode_O_M_G
        assertMultiLineEqual(encode("O M G"), "lnt")

    ___ test_encode_long_word
        assertMultiLineEqual(encode("mindblowingly"), "nrmwy oldrm tob")

    ___ test_encode_numbers
        assertMultiLineEqual(
            encode("Testing, 1 2 3, testing."), "gvhgr mt123 gvhgr mt")

    ___ test_encode_sentence
        assertMultiLineEqual(
            encode("Truth is fiction."), "gifgs rhurx grlm")

    ___ test_encode_all_things
        plaintext = "The quick brown fox jumps over the lazy dog."
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        assertMultiLineEqual(encode(plaintext), ciphertext)

    ___ test_decode_word
        assertMultiLineEqual(d.. "vcvix rhn"), "exercism")

    ___ test_decode_sentence
        assertMultiLineEqual(
            d.. "zmlyh gzxov rhlug vmzhg vkkrm thglm v"),
            "anobstacleisoftenasteppingstone")

    ___ test_decode_numbers
        assertMultiLineEqual(
            d.. "gvhgr mt123 gvhgr mt"), "testing123testing")

    ___ test_decode_all_the_letters
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        plaintext = "thequickbrownfoxjumpsoverthelazydog"
        assertMultiLineEqual(d.. ciphertext), plaintext)

    ___ test_decode_with_too_many_spaces
        assertMultiLineEqual(d.. "vc vix    r hn"), "exercism")

    ___ test_decode_with_no_spaces
        ciphertext = "zmlyhgzxovrhlugvmzhgvkkrmthglmv"
        plaintext = "anobstacleisoftenasteppingstone"
        assertMultiLineEqual(d.. ciphertext), plaintext)

    # additional track specific test
    ___ test_encode_decode
        assertMultiLineEqual(
            d.. encode("Testing, 1 2 3, testing.")), "testing123testing")


__ _____ __ _____
    unittest.main()
