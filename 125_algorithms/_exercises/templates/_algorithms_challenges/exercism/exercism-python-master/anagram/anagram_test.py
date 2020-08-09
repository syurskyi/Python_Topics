______ unittest

from anagram ______ detect_anagrams


class AnagramTests(unittest.TestCase
    ___ test_no_matches(self
        self.assertEqual(
            [],
            detect_anagrams('diaper', 'hello world zombies pants'.split())
        )

    ___ test_detect_simple_anagram(self
        self.assertEqual(
            ['tan'],
            detect_anagrams('ant', 'tan stand at'.split())
        )

    ___ test_detect_multiple_anagrams(self
        self.assertEqual(
            ['stream', 'maters'],
            detect_anagrams('master', 'stream pigeon maters'.split())
        )

    ___ test_does_not_confuse_different_duplicates(self
        self.assertEqual(
            [],
            detect_anagrams('galea', ['eagle'])
        )

    ___ test_eliminate_anagram_subsets(self
        self.assertEqual(
            [],
            detect_anagrams('good', 'dog goody'.split())
        )

    ___ test_detect_anagram(self
        self.assertEqual(
            ['inlets'],
            detect_anagrams('listen', 'enlists google inlets banana'.split())
        )

    ___ test_multiple_anagrams(self
        self.assertEqual(
            'gallery regally largely'.split(),
            detect_anagrams(
                'allergy',
                'gallery ballerina regally clergy largely leading'.split()
            )
        )

    ___ test_anagrams_are_case_insensitive(self
        self.assertEqual(
            ['Carthorse'],
            detect_anagrams('Orchestra',
                            'cashregister Carthorse radishes'.split())
        )

    ___ test_same_word_isnt_anagram(self
        self.assertEqual(
            [],
            detect_anagrams('banana', ['banana'])
        )

        self.assertEqual(
            [],
            detect_anagrams('go', 'go Go GO'.split())
        )

__ __name__ __ '__main__':
    unittest.main()
