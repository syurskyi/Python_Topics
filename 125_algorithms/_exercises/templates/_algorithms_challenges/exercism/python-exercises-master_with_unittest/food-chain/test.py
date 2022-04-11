_______ unittest

____ food_chain _______ recite


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

c_ FoodChainTest(unittest.TestCase

    ___ test_fly
        e.. [
            "I know an old lady who swallowed a fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(1, 1), e..)

    ___ test_spider
        e.. [
            "I know an old lady who swallowed a spider.",
            "It wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(2, 2), e..)

    ___ test_bird
        e.. [
            "I know an old lady who swallowed a bird.",
            "How absurd to swallow a bird!",
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(3, 3), e..)

    ___ test_cat
        e.. [
            "I know an old lady who swallowed a cat.",
            "Imagine that, to swallow a cat!",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(4, 4), e..)

    ___ test_dog
        e.. [
            "I know an old lady who swallowed a dog.",
            "What a hog, to swallow a dog!",
            "She swallowed the dog to catch the cat.",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that wriggled "
            "and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(5, 5), e..)

    ___ test_goat
        e.. [
            "I know an old lady who swallowed a goat.",
            "Just opened her throat and swallowed a goat!",
            "She swallowed the goat to catch the dog.",
            "She swallowed the dog to catch the cat.",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(6, 6), e..)

    ___ test_cow
        e.. [
            "I know an old lady who swallowed a cow.",
            "I don't know how she swallowed a cow!",
            "She swallowed the cow to catch the goat.",
            "She swallowed the goat to catch the dog.",
            "She swallowed the dog to catch the cat.",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
        assertEqual(recite(7, 7), e..)

    ___ test_horse
        e.. [
            "I know an old lady who swallowed a horse.",
            "She's dead, of course!",
        ]
        assertEqual(recite(8, 8), e..)

    ___ test_multiple_verses
        e.. recite(1, 1) + [""] + recite(2, 2) + [""] + recite(3, 3)
        assertEqual(recite(1, 3), e..)

    ___ test_full_song
        e..    # list
        ___ n __ r..(1, 9
            e.. += recite(n, n) + [""]
        e...p.. )
        assertEqual(recite(1, 8), e..)


__ _____ __ _____
    unittest.main()
