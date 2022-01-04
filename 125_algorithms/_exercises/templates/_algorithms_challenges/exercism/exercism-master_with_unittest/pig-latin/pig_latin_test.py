_______ unittest

____ pig_latin _______ translate


c_ PigLatinTests(unittest.TestCase):
    ___ test_word_beginning_with_a
        assertEqual("appleay", translate("apple"))

    ___ test_word_beginning_with_e
        assertEqual("earay", translate("ear"))

    ___ test_word_beginning_with_p
        assertEqual("igpay", translate("pig"))

    ___ test_word_beginning_with_k
        assertEqual("oalakay", translate("koala"))

    ___ test_word_beginning_with_ch
        assertEqual("airchay", translate("chair"))

    ___ test_word_beginning_with_qu
        assertEqual("eenquay", translate("queen"))

    ___ test_word_beginning_with_squ
        assertEqual("aresquay", translate("square"))

    ___ test_word_beginning_with_th
        assertEqual("erapythay", translate("therapy"))

    ___ test_word_beginning_with_thr
        assertEqual("ushthray", translate("thrush"))

    ___ test_word_beginning_with_sch
        assertEqual("oolschay", translate("school"))

    ___ test_translates_phrase
        assertEqual("ickquay astfay unray", translate("quick fast run"))

    ___ test_word_beginning_with_ye
        assertEqual("ellowyay", translate("yellow"))

    ___ test_word_beginning_with_yt
        assertEqual("yttriaay", translate("yttria"))

    ___ test_word_beginning_with_xe
        assertEqual("enonxay", translate("xenon"))

    ___ test_word_beginning_with_xr
        assertEqual("xrayay", translate("xray"))


__ _____ __ _____
    unittest.main()
