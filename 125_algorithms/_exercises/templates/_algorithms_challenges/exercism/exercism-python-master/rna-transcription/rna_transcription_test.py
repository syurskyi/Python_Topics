______ unittest

from dna ______ to_rna


class DNATests(unittest.TestCase

    ___ test_transcribes_guanine_to_cytosine(self
        self.assertEqual('C', to_rna('G'))

    ___ test_transcribes_cytosine_to_guanine(self
        self.assertEqual('G', to_rna('C'))

    ___ test_transcribes_thymine_to_adenine(self
        self.assertEqual('A', to_rna('T'))

    ___ test_transcribes_adenine_to_uracil(self
        self.assertEqual('U', to_rna('A'))

    ___ test_transcribes_all_occurences(self
        self.assertMultiLineEqual('UGCACCAGAAUU', to_rna('ACGTGGTCTTAA'))


__ __name__ __ '__main__':
    unittest.main()
