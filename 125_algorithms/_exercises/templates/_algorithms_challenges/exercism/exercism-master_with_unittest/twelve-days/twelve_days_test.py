_______ unittest

____ twelve_days _______ sing, verse, verses


c_ TwelveDaysTests(unittest.TestCase

    ___ test_verse1
        e.. ("On the first day of Christmas my true love gave to me, "
                    "a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(1

    ___ test_verse2
        e.. ("On the second day of Christmas my true love gave to me, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(2

    ___ test_verse3
        e.. ("On the third day of Christmas my true love gave to me, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(3

    ___ test_verse4
        e.. ("On the fourth day of Christmas my true love gave to me, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(4

    ___ test_verse5
        e.. ("On the fifth day of Christmas my true love gave to me, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(5

    ___ test_verse6
        e.. ("On the sixth day of Christmas my true love gave to me, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(6

    ___ test_verse7
        e.. ("On the seventh day of Christmas my true love gave to me, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(7

    ___ test_verse8
        e.. ("On the eighth day of Christmas my true love gave to me, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(8

    ___ test_verse9
        e.. ("On the ninth day of Christmas my true love gave to me, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        assertEqual(e.., verse(9

    ___ test_verse10
        e.. ("On the tenth day of Christmas my true love gave to me, "
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
        assertEqual(e.., verse(10

    ___ test_verse11
        e.. ("On the eleventh day of Christmas "
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
        assertEqual(e.., verse(11

    ___ test_verse12
        e.. ("On the twelfth day of Christmas my true love gave to me, "
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
        assertEqual(e.., verse(12

    ___ test_multiple_verses
        e.. ("On the first day of Christmas my true love gave to me, "
                    "a Partridge in a Pear Tree.\n\n"
                    "On the second day of Christmas my true love gave to me, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n\n"
                    "On the third day of Christmas my true love gave to me, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n\n")
        assertEqual(e.., verses(1, 3

    ___ test_the_whole_song
        assertEqual(verses(1, 12), sing


__ _____ __ _____
    unittest.main()
