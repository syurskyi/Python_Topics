_______ unittest

_______ hamming


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class HammingTest(unittest.TestCase):

    ___ test_identical_strands(self):
        self.assertEqual(hamming.distance("A", "A"), 0)

    ___ test_long_identical_strands(self):
        self.assertEqual(hamming.distance("GGACTGA", "GGACTGA"), 0)

    ___ test_complete_distance_in_single_nucleotide_strands(self):
        self.assertEqual(hamming.distance("A", "G"), 1)

    ___ test_complete_distance_in_small_strands(self):
        self.assertEqual(hamming.distance("AG", "CT"), 2)

    ___ test_small_distance_in_small_strands(self):
        self.assertEqual(hamming.distance("AT", "CT"), 1)

    ___ test_small_distance(self):
        self.assertEqual(hamming.distance("GGACG", "GGTCG"), 1)

    ___ test_small_distance_in_long_strands(self):
        self.assertEqual(hamming.distance("ACCAGGG", "ACTATGG"), 2)

    ___ test_non_unique_character_in_first_strand(self):
        self.assertEqual(hamming.distance("AGA", "AGG"), 1)

    ___ test_non_unique_character_in_second_strand(self):
        self.assertEqual(hamming.distance("AGG", "AGA"), 1)

    ___ test_same_nucleotides_in_different_positions(self):
        self.assertEqual(hamming.distance("TAG", "GAT"), 2)

    ___ test_large_distance(self):
        self.assertEqual(hamming.distance("GATACA", "GCATAA"), 4)

    ___ test_large_distance_in_off_by_one_strand(self):
        self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    ___ test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

    ___ test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.distance("AATG", "AAA")

    ___ test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.distance("ATA", "AGTG")


__ __name__ __ '__main__':
    unittest.main()
