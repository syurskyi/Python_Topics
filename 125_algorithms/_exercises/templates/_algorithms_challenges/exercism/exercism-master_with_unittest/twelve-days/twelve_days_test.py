_______ unittest

____ twelve_days _______ sing, verse, verses


class TwelveDaysTests(unittest.TestCase):

    ___ test_verse1(self):
        expected = ("On the first day of Christmas my true love gave to me, "
                    "a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(1))

    ___ test_verse2(self):
        expected = ("On the second day of Christmas my true love gave to me, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(2))

    ___ test_verse3(self):
        expected = ("On the third day of Christmas my true love gave to me, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(3))

    ___ test_verse4(self):
        expected = ("On the fourth day of Christmas my true love gave to me, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(4))

    ___ test_verse5(self):
        expected = ("On the fifth day of Christmas my true love gave to me, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(5))

    ___ test_verse6(self):
        expected = ("On the sixth day of Christmas my true love gave to me, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(6))

    ___ test_verse7(self):
        expected = ("On the seventh day of Christmas my true love gave to me, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(7))

    ___ test_verse8(self):
        expected = ("On the eighth day of Christmas my true love gave to me, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(8))

    ___ test_verse9(self):
        expected = ("On the ninth day of Christmas my true love gave to me, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(9))

    ___ test_verse10(self):
        expected = ("On the tenth day of Christmas my true love gave to me, "
                    "ten Lords-a-Leaping, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(10))

    ___ test_verse11(self):
        expected = ("On the eleventh day of Christmas "
                    "my true love gave to me, "
                    "eleven Pipers Piping, "
                    "ten Lords-a-Leaping, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(11))

    ___ test_verse12(self):
        expected = ("On the twelfth day of Christmas my true love gave to me, "
                    "twelve Drummers Drumming, "
                    "eleven Pipers Piping, "
                    "ten Lords-a-Leaping, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(expected, verse(12))

    ___ test_multiple_verses(self):
        expected = ("On the first day of Christmas my true love gave to me, "
                    "a Partridge in a Pear Tree.\n\n"
                    "On the second day of Christmas my true love gave to me, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n\n"
                    "On the third day of Christmas my true love gave to me, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n\n")
        self.assertEqual(expected, verses(1, 3))

    ___ test_the_whole_song(self):
        self.assertEqual(verses(1, 12), sing())


__ __name__ __ '__main__':
    unittest.main()
