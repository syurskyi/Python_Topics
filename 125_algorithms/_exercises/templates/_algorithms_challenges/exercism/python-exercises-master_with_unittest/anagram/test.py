_______ unittest

____ anagram _______ detect_anagrams


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.1

class AnagramTests(unittest.TestCase):
    ___ test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        self.assertEqual(detect_anagrams("diaper", candidates), [])

    ___ test_detects_simple_anagram(self):
        candidates = ["tan", "stand", "at"]
        self.assertEqual(detect_anagrams("ant", candidates), ["tan"])

    ___ test_does_not_detect_false_positives(self):
        self.assertEqual(detect_anagrams("galea", ["eagle"]), [])

    ___ test_detects_two_anagrams(self):
        candidates = ["stream", "pigeon", "maters"]
        self.assertEqual(
            detect_anagrams("master", candidates), ["stream", "maters"])

    ___ test_does_not_detect_anagram_subsets(self):
        self.assertEqual(detect_anagrams("good", ["dog", "goody"]), [])

    ___ test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        self.assertEqual(detect_anagrams("listen", candidates), ["inlets"])

    ___ test_detects_three_anagrams(self):
        candidates = [
            "gallery", "ballerina", "regally", "clergy", "largely", "leading"
        ]
        self.assertEqual(
            detect_anagrams("allergy", candidates),
            ["gallery", "regally", "largely"])

    ___ test_does_not_detect_identical_words(self):
        candidates = ["corn", "dark", "Corn", "rank", "CORN", "cron", "park"]
        self.assertEqual(detect_anagrams("corn", candidates), ["cron"])

    ___ test_does_not_detect_non_anagrams_with_identical_checksum(self):
        self.assertEqual(detect_anagrams("mass", ["last"]), [])

    ___ test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        self.assertEqual(
            detect_anagrams("Orchestra", candidates), ["Carthorse"])

    ___ test_detects_anagrams_using_case_insensitive_subjec(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        self.assertEqual(
            detect_anagrams("Orchestra", candidates), ["carthorse"])

    ___ test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        self.assertEqual(
            detect_anagrams("orchestra", candidates), ["Carthorse"])

    ___ test_does_not_detect_a_word_as_its_own_anagram(self):
        self.assertEqual(detect_anagrams("banana", ["Banana"]), [])

    ___ test_does_not_detect_a_anagram_if_the_original_word_is_repeated(self):
        self.assertEqual(detect_anagrams("go", ["go Go GO"]), [])

    ___ test_anagrams_must_use_all_letters_exactly_once(self):
        self.assertEqual(detect_anagrams("tapper", ["patter"]), [])

    ___ test_capital_word_is_not_own_anagram(self):
        self.assertEqual(detect_anagrams("BANANA", ["Banana"]), [])


__ __name__ __ '__main__':
    unittest.main()
