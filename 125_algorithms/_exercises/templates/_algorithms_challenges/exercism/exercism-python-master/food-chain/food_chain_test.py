______ unittest

from food_chain ______ recite


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.1.0

class FoodChainTest(unittest.TestCase

    ___ test_fly(self
        expected = [
            "I know an old lady who swallowed a fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(1, 1), expected)

    ___ test_spider(self
        expected = [
            "I know an old lady who swallowed a spider."
            "It wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(2, 2), expected)

    ___ test_bird(self
        expected = [
            "I know an old lady who swallowed a bird."
            "How absurd to swallow a bird!"
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(3, 3), expected)

    ___ test_cat(self
        expected = [
            "I know an old lady who swallowed a cat."
            "Imagine that, to swallow a cat!"
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(4, 4), expected)

    ___ test_dog(self
        expected = [
            "I know an old lady who swallowed a dog."
            "What a hog, to swallow a dog!"
            "She swallowed the dog to catch the cat."
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that wriggled "
            "and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(5, 5), expected)

    ___ test_goat(self
        expected = [
            "I know an old lady who swallowed a goat."
            "Just opened her throat and swallowed a goat!"
            "She swallowed the goat to catch the dog."
            "She swallowed the dog to catch the cat."
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(6, 6), expected)

    ___ test_cow(self
        expected = [
            "I know an old lady who swallowed a cow."
            "I don't know how she swallowed a cow!"
            "She swallowed the cow to catch the goat."
            "She swallowed the goat to catch the dog."
            "She swallowed the dog to catch the cat."
            "She swallowed the cat to catch the bird."
            "She swallowed the bird to catch the spider that "
            "wriggled and jiggled and tickled inside her."
            "She swallowed the spider to catch the fly."
            "I don't know why she swallowed the fly. Perhaps she'll die."
        ]
        self.assertEqual(recite(7, 7), expected)

    ___ test_horse(self
        expected = [
            "I know an old lady who swallowed a horse."
            "She's dead, of course!"
        ]
        self.assertEqual(recite(8, 8), expected)

    ___ test_multiple_verses(self
        expected = [recite(n, n)[0] ___ n in range(1, 4)]
        self.assertEqual(recite(1, 3), expected)

    ___ test_full_song(self
        expected = [recite(n, n)[0] ___ n in range(1, 9)]
        self.assertEqual(recite(1, 8), expected)


__ __name__ __ '__main__':
    unittest.main()
