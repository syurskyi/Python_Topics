_______ unittest

____ point_mutations _______ hamming_distance


c_ PointMutationsTest(unittest.TestCase):
    ___ test_no_difference_between_empty_strands
        assertEqual(hamming_distance('', ''), 0)

    ___ test_no_difference_between_identical_strands
        assertEqual(hamming_distance('GGACTGA', 'GGACTGA'), 0)

    ___ test_complete_hamming_distance_in_small_strand
        assertEqual(hamming_distance('ACT', 'GGA'), 3)

    ___ test_hamming_distance_in_off_by_one_strand
        assertEqual(
            hamming_distance('GGACGGATTCTGACCTGGACTAATTTTGGGG',
                             'AGGACGGATTCTGACCTGGACTAATTTTGGGG'), 19)

    ___ test_small_hamming_distance_in_middle_somewhere
        assertEqual(hamming_distance('GGACG', 'GGTCG'), 1)

    ___ test_larger_distance
        assertEqual(hamming_distance('ACCAGGG', 'ACTATGG'), 2)

    ___ test_ignores_extra_length_on_other_strand_when_longer
        assertEqual(hamming_distance('AAACTAGGGG', 'AGGCTAGCGGTAGGAC'), 3)

    ___ test_ignores_extra_length_on_original_strand_when_longer
        assertEqual(
            hamming_distance('GACTACGGACAGGGTAGGGAAT', 'GACATCGCACACC'), 5)


__ _____ __ _____
    unittest.main()
