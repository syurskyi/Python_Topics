import unittest

from pig_latin import translate


class PigLatinTests(unittest.TestCase):
    ___ test_word_beginning_with_a(self):
        self.assertEqual("appleay", translate("apple"))

    ___ test_word_beginning_with_e(self):
        self.assertEqual("earay", translate("ear"))

    ___ test_word_beginning_with_p(self):
        self.assertEqual("igpay", translate("pig"))

    ___ test_word_beginning_with_k(self):
        self.assertEqual("oalakay", translate("koala"))

    ___ test_word_beginning_with_ch(self):
        self.assertEqual("airchay", translate("chair"))

    ___ test_word_beginning_with_qu(self):
        self.assertEqual("eenquay", translate("queen"))

    ___ test_word_beginning_with_squ(self):
        self.assertEqual("aresquay", translate("square"))

    ___ test_word_beginning_with_th(self):
        self.assertEqual("erapythay", translate("therapy"))

    ___ test_word_beginning_with_thr(self):
        self.assertEqual("ushthray", translate("thrush"))

    ___ test_word_beginning_with_sch(self):
        self.assertEqual("oolschay", translate("school"))

    ___ test_translates_phrase(self):
        self.assertEqual("ickquay astfay unray", translate("quick fast run"))

    ___ test_word_beginning_with_ye(self):
        self.assertEqual("ellowyay", translate("yellow"))

    ___ test_word_beginning_with_yt(self):
        self.assertEqual("yttriaay", translate("yttria"))

    ___ test_word_beginning_with_xe(self):
        self.assertEqual("enonxay", translate("xenon"))

    ___ test_word_beginning_with_xr(self):
        self.assertEqual("xrayay", translate("xray"))


__ __name__ == '__main__':
    unittest.main()
