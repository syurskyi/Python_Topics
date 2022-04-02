_______ unittest

____ protein_translation _______ proteins


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1

c_ ProteinTranslationTest(unittest.TestCase

    ___ test_AUG_translates_to_methionine
        assertEqual(proteins('AUG'),  'Methionine' )

    ___ test_identifies_Phenylalanine_codons
        ___ codon __  'UUU', 'UUC' :
            assertEqual(proteins(codon),  'Phenylalanine' )

    ___ test_identifies_Leucine_codons
        ___ codon __  'UUA', 'UUG' :
            assertEqual(proteins(codon),  'Leucine' )

    ___ test_identifies_Serine_codons
        ___ codon __  'UCU', 'UCC', 'UCA', 'UCG' :
            assertEqual(proteins(codon),  'Serine' )

    ___ test_identifies_Tyrosine_codons
        ___ codon __  'UAU', 'UAC' :
            assertEqual(proteins(codon),  'Tyrosine' )

    ___ test_identifies_Cysteine_codons
        ___ codon __  'UGU', 'UGC' :
            assertEqual(proteins(codon),  'Cysteine' )

    ___ test_identifies_Tryptophan_codons
        assertEqual(proteins('UGG'),  'Tryptophan' )

    ___ test_identifies_stop_codons
        ___ codon __  'UAA', 'UAG', 'UGA' :
            assertEqual(proteins(codon), [])

    ___ test_translates_rna_strand_into_correct_protein_list
        strand = 'AUGUUUUGG'
        expected =  'Methionine', 'Phenylalanine', 'Tryptophan'
        assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_at_beginning_of_sequence
        strand = 'UAGUGG'
        expected    # list
        assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_at_end_of_two_codon_sequence(
            self
        strand = 'UGGUAG'
        expected =  'Tryptophan'
        assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_at_end_of_three_codon_sequence(
            self
        strand = 'AUGUUUUAA'
        expected =  'Methionine', 'Phenylalanine'
        assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_in_middle_of_three_codon_sequence(
            self
        strand = 'UGGUAGUGG'
        expected =  'Tryptophan'
        assertEqual(proteins(strand), expected)

    ___ test_stops_translation_if_stop_codon_in_middle_of_six_codon_sequence(
            self
        strand = 'UGGUGUUAUUAAUGGUUU'
        expected =  'Tryptophan', 'Cysteine', 'Tyrosine'
        assertEqual(proteins(strand), expected)


__ _____ __ _____
    unittest.main()
