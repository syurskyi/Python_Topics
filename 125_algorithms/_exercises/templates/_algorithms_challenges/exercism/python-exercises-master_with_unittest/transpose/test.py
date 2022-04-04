_______ unittest
____ transpose _______ transpose


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ TransposeTests(unittest.TestCase
    ___ test_empty_string
        input_line = ""
        e.. = ""
        assertEqual(
            transpose(input_line),
            e..
        )

    ___ test_two_characters_in_a_row
        assertEqual(
            transpose("A1"),
            "\n".j..(["A", "1"])
        )

    ___ test_two_characters_in_a_column
        assertEqual(
            transpose("\n".j..(["A", "1"],
            "A1"
        )

    ___ test_simple
        input_line = [
            "ABC",
            "123"
        ]
        e.. = [
            "A1",
            "B2",
            "C3"
        ]

        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_single_line
        input_line = ["Single line."]
        e.. = [
            "S",
            "i",
            "n",
            "g",
            "l",
            "e",
            " ",
            "l",
            "i",
            "n",
            "e",
            "."
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_first_line_longer_than_second_line
        input_line = [
            "The fourth line.",
            "The fifth line."
        ]
        e.. = [
            "TT",
            "hh",
            "ee",
            "  ",
            "ff",
            "oi",
            "uf",
            "rt",
            "th",
            "h ",
            " l",
            "li",
            "in",
            "ne",
            "e.",
            "."
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_second_line_longer_than_first_line
        input_line = [
            "The first line.",
            "The second line."
        ]
        e.. = [
            "TT",
            "hh",
            "ee",
            "  ",
            "fs",
            "ie",
            "rc",
            "so",
            "tn",
            " d",
            "l ",
            "il",
            "ni",
            "en",
            ".e",
            " ."
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_square
        input_line = [
            "HEART",
            "EMBER",
            "ABUSE",
            "RESIN",
            "TREND"
        ]
        e.. = [
            "HEART",
            "EMBER",
            "ABUSE",
            "RESIN",
            "TREND"
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_rectangle
        input_line = [
            "FRACTURE",
            "OUTLINED",
            "BLOOMING",
            "SEPTETTE"
        ]
        e.. = [
            "FOBS",
            "RULE",
            "ATOP",
            "CLOT",
            "TIME",
            "UNIT",
            "RENT",
            "EDGE"
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_triangle
        input_line = [
            "T",
            "EE",
            "AAA",
            "SSSS",
            "EEEEE",
            "RRRRRR"
        ]
        e.. = [
            "TEASER",
            " EASER",
            "  ASER",
            "   SER",
            "    ER",
            "     R"
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )

    ___ test_many_lines
        input_line = [
            "Chor. Two households, both alike in dignity,",
            "In fair Verona, where we lay our scene,",
            "From ancient grudge break to new mutiny,",
            "Where civil blood makes civil hands unclean.",
            "From forth the fatal loins of these two foes",
            "A pair of star-cross'd lovers take their life;",
            "Whose misadventur'd piteous overthrows",
            "Doth with their death bury their parents' strife.",
            "The fearful passage of their death-mark'd love,",
            "And the continuance of their parents' rage,",
            "Which, but their children's end, naught could remove,",
            "Is now the two hours' traffic of our stage;",
            "The which if you with patient ears attend,",
            "What here shall miss, our toil shall strive to mend."
        ]
        e.. = [
            "CIFWFAWDTAWITW",
            "hnrhr hohnhshh",
            "o oeopotedi ea",
            "rfmrmash  cn t",
            ".a e ie fthow ",
            " ia fr weh,whh",
            "Trnco miae  ie",
            "w ciroitr btcr",
            "oVivtfshfcuhhe",
            " eeih a uote  ",
            "hrnl sdtln  is",
            "oot ttvh tttfh",
            "un bhaeepihw a",
            "saglernianeoyl",
            "e,ro -trsui ol",
            "h uofcu sarhu ",
            "owddarrdan o m",
            "lhg to'egccuwi",
            "deemasdaeehris",
            "sr als t  ists",
            ",ebk 'phool'h,",
            "  reldi ffd   ",
            "bweso tb  rtpo",
            "oea ileutterau",
            "t kcnoorhhnatr",
            "hl isvuyee'fi ",
            " atv es iisfet",
            "ayoior trr ino",
            "l  lfsoh  ecti",
            "ion   vedpn  l",
            "kuehtteieadoe ",
            "erwaharrar,fas",
            "   nekt te  rh",
            "ismdsehphnnosa",
            "ncuse ra-tau l",
            " et  tormsural",
            "dniuthwea'g t ",
            "iennwesnr hsts",
            "g,ycoi tkrttet",
            "n ,l r s'a anr",
            "i  ef  'dgcgdi",
            "t  aol   eoe,v",
            "y  nei sl,u; e",
            ",  .sf to l   ",
            "     e rv d  t",
            "     ; ie    o",
            "       f, r   ",
            "       e  e  m",
            "       .  m  e",
            "          o  n",
            "          v  d",
            "          e  .",
            "          ,"
        ]
        assertEqual(
            transpose("\n".j..(input_line,
            "\n".j..(e..)
        )


__ _____ __ _____
    unittest.main()
