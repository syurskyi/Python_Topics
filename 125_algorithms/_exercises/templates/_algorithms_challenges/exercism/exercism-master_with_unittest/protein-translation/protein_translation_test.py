_______ unittest

____ protein_translation _______ proteins


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1

class ProteinTranslationTest(unittest.TestCase):

    ___ test_AUG_translates_to_methionine(self):
        self.assertEqual(proteins('AUG'), ['Methionine'])

    ___ test_identifies_Phenylalanine_codons(self):
        ___ codon __ ['UUU', 'UUC']:
            self.assertEqual(proteins(codon), ['Phenylalanine'])

    ___ test_identifies_Leucine_codons(self):
        ___ codon __ ['UUA', 'UUG']:
            self.assertEqual(proteins(codon), ['Leucine'])

    ___ test_identifies_Serine_codons(self):
        ___ codon __ ['UCU', 'UCC', 'UCA', 'UCG']:
            self.assertEqual(proteins(codon), ['Serine'])

    ___ test_identifies_Tyrosine_codons(self):
        ___ codon __ ['UAU', 'UAC']:
            self.assertEqual(proteins(codon), ['Tyrosine'])

    ___ test_identifies_Cysteine_codons(self):
        ___ codon __ ['UGU', 'UGC']:
            self.assertEqual(proteins(codon), ['Cysteine'])

    ___ test_identifies_Tryptophan_codons(self):
        self.assertEqual(proteins('UGG'), ['Tryptophan'])

    ___ test_identifies_stop_codons(self):
        ___ codon __ ['UAA', 'UAG', 'UGA']:
            self.assertEqual(proteins(codon), [])

    ___ test_translates_rna_strand_into_correct_protein_list(self):
        strand = 'AUGUUUUGG'
        expected = ['Methionine', 'Phenylalanine', 'Tryptophan']
        self.assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_at_beginning_of_sequence(self):
        strand = 'UAGUGG'
        expected    # list
        self.assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_at_end_of_two_codon_sequence(
            self):
        strand = 'UGGUAG'
        expected = ['Tryptophan']
        self.assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_at_end_of_three_codon_sequence(
            self):
        strand = 'AUGUUUUAA'
        expected = ['Methionine', 'Phenylalanine']
        self.assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_in_middle_of_three_codon_sequence(
            self):
        strand = 'UGGUAGUGG'
        expected = ['Tryptophan']
        self.assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_in_middle_of_six_codon_sequence(
            self):
        strand = 'UGGUGUUAUUAAUGGUUU'
        expected = ['Tryptophan', 'Cysteine', 'Tyrosine']
        self.assertEqual(proteins(strand), expected)


__ __name__ __ '__main__':
    unittest.main()
