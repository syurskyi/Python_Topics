_______ unittest

____ pig_latin _______ translate


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ PigLatinTests(unittest.TestCase):
    ___ test_word_beginning_with_a
        assertEqual(translate("apple"), "appleay")

    ___ test_word_beginning_with_e
        assertEqual(translate("ear"), "earay")

    ___ test_word_beginning_with_i
        assertEqual(translate("igloo"), "iglooay")

    ___ test_word_beginning_with_o
        assertEqual(translate("object"), "objectay")

    ___ test_word_beginning_with_u
        assertEqual(translate("under"), "underay")

    ___ test_word_beginning_with_a_vowel_and_followed_by_a_qu
        assertEqual(translate("equal"), "equalay")

    ___ test_word_beginning_with_p
        assertEqual(translate("pig"), "igpay")

    ___ test_word_beginning_with_k
        assertEqual(translate("koala"), "oalakay")

    ___ test_word_beginning_with_y
        assertEqual(translate("yellow"), "ellowyay")

    ___ test_word_beginning_with_x
        assertEqual(translate("xenon"), "enonxay")

    ___ test_word_beginning_with_q_without_a_following_u
        assertEqual(translate("qat"), "atqay")

    ___ test_word_beginning_with_ch
        assertEqual(translate("chair"), "airchay")

    ___ test_word_beginning_with_qu
        assertEqual(translate("queen"), "eenquay")

    ___ test_word_beginning_with_qu_and_a_preceding_consonant
        assertEqual(translate("square"), "aresquay")

    ___ test_word_beginning_with_th
        assertEqual(translate("therapy"), "erapythay")

    ___ test_word_beginning_with_thr
        assertEqual(translate("thrush"), "ushthray")

    ___ test_word_beginning_with_sch
        assertEqual(translate("school"), "oolschay")

    ___ test_word_beginning_with_yt
        assertEqual(translate("yttria"), "yttriaay")

    ___ test_word_beginning_with_xr
        assertEqual(translate("xray"), "xrayay")

    ___ test_a_whole_phrase
        assertEqual(translate("quick fast run"), "ickquay astfay unray")


__ __name__ __ '__main__':
    unittest.main()
