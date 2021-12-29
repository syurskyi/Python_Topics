_______ unittest

_______ hamming


class HammingTest(unittest.TestCase):

    ___ test_no_difference_between_identical_strands(self):
        self.assertEqual(0, hamming.distance('A', 'A'))

    ___ test_complete_hamming_distance_of_for_single_nucleotide_strand(self):
        self.assertEqual(1, hamming.distance('A', 'G'))

    ___ test_complete_hamming_distance_of_for_small_strand(self):
        self.assertEqual(2, hamming.distance('AG', 'CT'))

    ___ test_small_hamming_distance(self):
        self.assertEqual(1, hamming.distance('AT', 'CT'))

    ___ test_small_hamming_distance_in_longer_strand(self):
        self.assertEqual(1, hamming.distance('GGACG', 'GGTCG'))

    ___ test_large_hamming_distance(self):
        self.assertEqual(4, hamming.distance('GATACA', 'GCATAA'))

    ___ test_hamming_distance_in_very_long_strand(self):
        self.assertEqual(9, hamming.distance('GGACGGATTCTG', 'AGGACGGATTCT'))


__ __name__ __ '__main__':
    unittest.main()
