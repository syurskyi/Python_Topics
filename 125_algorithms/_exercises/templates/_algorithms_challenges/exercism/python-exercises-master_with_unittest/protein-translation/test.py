_______ unittest

____ protein_translation _______ of_codon, of_rna


c_ ProteinTranslationTests(unittest.TestCase

    ___ test_AUG_translates_to_methionine
        assertEqual('Methionine', of_codon('AUG'))

    ___ test_identifies_Phenylalanine_codons
        ___ codon __  'UUU', 'UUC' :
            assertEqual('Phenylalanine', of_codon(codon))

    ___ test_identifies_Leucine_codons
        ___ codon __  'UUA', 'UUG' :
            assertEqual('Leucine', of_codon(codon))

    ___ test_identifies_Serine_codons
        ___ codon __  'UCU', 'UCC', 'UCA', 'UCG' :
            assertEqual('Serine', of_codon(codon))

    ___ test_identifies_Tyrosine_codons
        ___ codon __  'UAU', 'UAC' :
            assertEqual('Tyrosine', of_codon(codon))

    ___ test_identifies_Cysteine_codons
        ___ codon __  'UGU', 'UGC' :
            assertEqual('Cysteine', of_codon(codon))

    ___ test_identifies_Tryptophan_codons
        assertEqual('Tryptophan', of_codon('UGG'))

    ___ test_identifies_stop_codons
        ___ codon __  'UAA', 'UAG', 'UGA' :
            assertEqual('STOP', of_codon(codon))

    ___ test_translates_rna_strand_into_correct_protein
        strand = 'AUGUUUUGG'
        expected =  'Methionine', 'Phenylalanine', 'Tryptophan'
        assertEqual(expected, of_rna(strand))

    ___ test_stops_translation_if_stop_codon_present
        strand = 'AUGUUUUAA'
        expected =  'Methionine', 'Phenylalanine'
        assertEqual(expected, of_rna(strand))

    ___ test_stops_translation_of_longer_strand
        strand = 'UGGUGUUAUUAAUGGUUU'
        expected =  'Tryptophan', 'Cysteine', 'Tyrosine'
        assertEqual(expected, of_rna(strand))

    ___ test_invalid_codons
        w__ assertRaises(ValueError
            of_rna('CARROT')


__ _____ __ _____
    unittest.main()
