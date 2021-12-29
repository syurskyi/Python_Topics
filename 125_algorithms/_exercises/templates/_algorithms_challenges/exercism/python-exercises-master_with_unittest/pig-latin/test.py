import unittest

from pig_latin import translate


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class PigLatinTests(unittest.TestCase):
    ___ test_word_beginning_with_a(self):
        self.assertEqual(translate("apple"), "appleay")

    ___ test_word_beginning_with_e(self):
        self.assertEqual(translate("ear"), "earay")

    ___ test_word_beginning_with_i(self):
        self.assertEqual(translate("igloo"), "iglooay")

    ___ test_word_beginning_with_o(self):
        self.assertEqual(translate("object"), "objectay")

    ___ test_word_beginning_with_u(self):
        self.assertEqual(translate("under"), "underay")

    ___ test_word_beginning_with_a_vowel_and_followed_by_a_qu(self):
        self.assertEqual(translate("equal"), "equalay")

    ___ test_word_beginning_with_p(self):
        self.assertEqual(translate("pig"), "igpay")

    ___ test_word_beginning_with_k(self):
        self.assertEqual(translate("koala"), "oalakay")

    ___ test_word_beginning_with_y(self):
        self.assertEqual(translate("yellow"), "ellowyay")

    ___ test_word_beginning_with_x(self):
        self.assertEqual(translate("xenon"), "enonxay")

    ___ test_word_beginning_with_q_without_a_following_u(self):
        self.assertEqual(translate("qat"), "atqay")

    ___ test_word_beginning_with_ch(self):
        self.assertEqual(translate("chair"), "airchay")

    ___ test_word_beginning_with_qu(self):
        self.assertEqual(translate("queen"), "eenquay")

    ___ test_word_beginning_with_qu_and_a_preceding_consonant(self):
        self.assertEqual(translate("square"), "aresquay")

    ___ test_word_beginning_with_th(self):
        self.assertEqual(translate("therapy"), "erapythay")

    ___ test_word_beginning_with_thr(self):
        self.assertEqual(translate("thrush"), "ushthray")

    ___ test_word_beginning_with_sch(self):
        self.assertEqual(translate("school"), "oolschay")

    ___ test_word_beginning_with_yt(self):
        self.assertEqual(translate("yttria"), "yttriaay")

    ___ test_word_beginning_with_xr(self):
        self.assertEqual(translate("xray"), "xrayay")

    ___ test_a_whole_phrase(self):
        self.assertEqual(translate("quick fast run"), "ickquay astfay unray")


__ __name__ == '__main__':
    unittest.main()
