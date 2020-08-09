______ unittest

from raindrops ______ raindrops


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class RaindropsTest(unittest.TestCase
    ___ test_the_sound_for_1_is_1(self
        self.assertEqual(raindrops(1), "1")

    ___ test_the_sound_for_3_is_pling(self
        self.assertEqual(raindrops(3), "Pling")

    ___ test_the_sound_for_5_is_plang(self
        self.assertEqual(raindrops(5), "Plang")

    ___ test_the_sound_for_7_is_plong(self
        self.assertEqual(raindrops(7), "Plong")

    ___ test_the_sound_for_6_is_pling(self
        self.assertEqual(raindrops(6), "Pling")

    ___ test_2_to_the_power_3_does_not_make_sound(self
        self.assertEqual(raindrops(8), "8")

    ___ test_the_sound_for_9_is_pling(self
        self.assertEqual(raindrops(9), "Pling")

    ___ test_the_sound_for_10_is_plang(self
        self.assertEqual(raindrops(10), "Plang")

    ___ test_the_sound_for_14_is_plong(self
        self.assertEqual(raindrops(14), "Plong")

    ___ test_the_sound_for_15_is_plingplang(self
        self.assertEqual(raindrops(15), "PlingPlang")

    ___ test_the_sound_for_21_is_plingplong(self
        self.assertEqual(raindrops(21), "PlingPlong")

    ___ test_the_sound_for_25_is_plang(self
        self.assertEqual(raindrops(25), "Plang")

    ___ test_the_sound_for_27_is_pling(self
        self.assertEqual(raindrops(27), "Pling")

    ___ test_the_sound_for_35_is_plangplong(self
        self.assertEqual(raindrops(35), "PlangPlong")

    ___ test_the_sound_for_49_is_plong(self
        self.assertEqual(raindrops(49), "Plong")

    ___ test_the_sound_for_52_is_52(self
        self.assertEqual(raindrops(52), "52")

    ___ test_the_sound_for_105_is_plingplangplong(self
        self.assertEqual(raindrops(105), "PlingPlangPlong")

    ___ test_the_sound_for_12121_is_12121(self
        self.assertEqual(raindrops(12121), "12121")


__ __name__ __ '__main__':
    unittest.main()
