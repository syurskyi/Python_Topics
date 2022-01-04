"""Tests for the nucleotide-count exercise

Implementation note:
The count function must raise a ValueError with a meaningful error message
in case of a bad argument.
"""
_______ unittest

____ nucleotide_count _______ count, nucleotide_counts


c_ DNATest(unittest.TestCase):
    ___ test_empty_dna_string_has_no_adenosine
        assertEqual(c.. '', 'A'), 0)

    ___ test_empty_dna_string_has_no_nucleotides
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        assertEqual(nucleotide_counts(""), expected)

    ___ test_repetitive_cytidine_gets_counted
        assertEqual(c.. 'CCCCC', 'C'), 5)

    ___ test_repetitive_sequence_has_only_guanosine
        expected = {'A': 0, 'T': 0, 'C': 0, 'G': 8}
        assertEqual(nucleotide_counts('GGGGGGGG'), expected)

    ___ test_counts_only_thymidine
        assertEqual(c.. 'GGGGGTAACCCGG', 'T'), 1)

    ___ test_validates_nucleotides
        w__ assertRaises(ValueError):
            c.. "GACT", 'X')

    ___ test_counts_all_nucleotides
        dna = ('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT'
               'CTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        expected = {'A': 20, 'T': 21, 'G': 17, 'C': 12}
        assertEqual(nucleotide_counts(dna), expected)


__ __name__ __ '__main__':
    unittest.main()
