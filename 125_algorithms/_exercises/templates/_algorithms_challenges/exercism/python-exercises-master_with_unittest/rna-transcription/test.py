_______ unittest

____ rna_transcription _______ to_rna


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

c_ DNATests(unittest.TestCase
    ___ test_transcribes_guanine_to_cytosine
        assertEqual(to_rna('G'), 'C')

    ___ test_transcribes_cytosine_to_guanine
        assertEqual(to_rna('C'), 'G')

    ___ test_transcribes_thymine_to_adenine
        assertEqual(to_rna('T'), 'A')

    ___ test_transcribes_adenine_to_uracil
        assertEqual(to_rna('A'), 'U')

    ___ test_transcribes_all_occurences
        assertMultiLineEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')

    ___ test_correctly_handles_single_invalid_input
        assertEqual(to_rna('U'), '')

    ___ test_correctly_handles_completely_invalid_input
        assertMultiLineEqual(to_rna('XXX'), '')

    ___ test_correctly_handles_partially_invalid_input
        assertMultiLineEqual(to_rna('ACGTXXXCTTAA'), '')


__ _____ __ _____
    unittest.main()
