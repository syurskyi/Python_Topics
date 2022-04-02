_______ unittest

_______ hamming


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ HammingTest(unittest.TestCase

    ___ test_identical_strands
        assertEqual(hamming.distance("A", "A"), 0)

    ___ test_long_identical_strands
        assertEqual(hamming.distance("GGACTGA", "GGACTGA"), 0)

    ___ test_complete_distance_in_single_nucleotide_strands
        assertEqual(hamming.distance("A", "G"), 1)

    ___ test_complete_distance_in_small_strands
        assertEqual(hamming.distance("AG", "CT"), 2)

    ___ test_small_distance_in_small_strands
        assertEqual(hamming.distance("AT", "CT"), 1)

    ___ test_small_distance
        assertEqual(hamming.distance("GGACG", "GGTCG"), 1)

    ___ test_small_distance_in_long_strands
        assertEqual(hamming.distance("ACCAGGG", "ACTATGG"), 2)

    ___ test_non_unique_character_in_first_strand
        assertEqual(hamming.distance("AGA", "AGG"), 1)

    ___ test_non_unique_character_in_second_strand
        assertEqual(hamming.distance("AGG", "AGA"), 1)

    ___ test_same_nucleotides_in_different_positions
        assertEqual(hamming.distance("TAG", "GAT"), 2)

    ___ test_large_distance
        assertEqual(hamming.distance("GATACA", "GCATAA"), 4)

    ___ test_large_distance_in_off_by_one_strand
        assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    ___ test_empty_strands
        assertEqual(hamming.distance("", ""), 0)

    ___ test_disallow_first_strand_longer
        w__ assertRaises(ValueError
            hamming.distance("AATG", "AAA")

    ___ test_disallow_second_strand_longer
        w__ assertRaises(ValueError
            hamming.distance("ATA", "AGTG")


__ _____ __ _____
    unittest.main()
