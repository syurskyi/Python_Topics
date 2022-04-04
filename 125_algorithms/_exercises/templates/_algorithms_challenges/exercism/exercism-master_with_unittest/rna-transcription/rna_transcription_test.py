_______ unittest

____ dna _______ to_rna


c_ DNATests(unittest.TestCase

    ___ test_transcribes_guanine_to_cytosine
        assertEqual('C', to_rna('G'

    ___ test_transcribes_cytosine_to_guanine
        assertEqual('G', to_rna('C'

    ___ test_transcribes_thymine_to_adenine
        assertEqual('A', to_rna('T'

    ___ test_transcribes_adenine_to_uracil
        assertEqual('U', to_rna('A'

    ___ test_transcribes_all_occurences
        assertEqual('UGCACCAGAAUU', to_rna('ACGTGGTCTTAA'


__ _____ __ _____
    unittest.main()
