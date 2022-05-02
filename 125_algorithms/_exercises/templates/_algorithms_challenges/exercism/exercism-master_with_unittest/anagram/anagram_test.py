_______ unittest

____ anagram _______ find_anagrams


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

c_ AnagramTest(unittest.TestCase
    ___ test_no_matches
        candidates ["hello", "world", "zombies", "pants"]
        assertEqual(find_anagrams("diaper", candidates),    # list)

    ___ test_detects_two_anagrams
        candidates ["stream", "pigeon", "maters"]
        assertEqual(
            find_anagrams("master", candidates), ["stream", "maters"])

    ___ test_does_not_detect_anagram_subsets
        assertEqual(find_anagrams("good", ["dog", "goody"]),    # list)

    ___ test_detects_anagram
        candidates ["enlists", "google", "inlets", "banana"]
        assertEqual(find_anagrams("listen", candidates), ["inlets"])

    ___ test_detects_three_anagrams
        candidates [
            "gallery", "ballerina", "regally", "clergy", "largely", "leading"
        ]
        assertEqual(
            find_anagrams("allergy", candidates),
            ["gallery", "regally", "largely"])

    ___ test_does_not_detect_non_anagrams_with_identical_checksum
        assertEqual(find_anagrams("mass", ["last"]),    # list)

    ___ test_detects_anagrams_case_insensitively
        candidates ["cashregister", "Carthorse", "radishes"]
        assertEqual(
            find_anagrams("Orchestra", candidates), ["Carthorse"])

    ___ test_detects_anagrams_using_case_insensitive_subject
        candidates ["cashregister", "carthorse", "radishes"]
        assertEqual(
            find_anagrams("Orchestra", candidates), ["carthorse"])

    ___ test_detects_anagrams_using_case_insensitive_possible_matches
        candidates ["cashregister", "Carthorse", "radishes"]
        assertEqual(
            find_anagrams("orchestra", candidates), ["Carthorse"])

    ___ test_does_not_detect_a_anagram_if_the_original_word_is_repeated
        assertEqual(find_anagrams("go", ["go Go GO"]),    # list)

    ___ test_anagrams_must_use_all_letters_exactly_once
        assertEqual(find_anagrams("tapper", ["patter"]),    # list)

    ___ test_words_are_not_anagrams_of_themselves_case_insensitive
        candidates ["BANANA", "Banana", "banana"]
        assertEqual(find_anagrams("BANANA", candidates),    # list)


__ _____ __ _____
    unittest.main()
