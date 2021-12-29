# TODO: Add imports
____ Bio.Seq _______ Seq
____ Bio.Data.CodonTable _______ TranslationError

___ translate_cds(cds: s.., translation_table: s..) -> s..:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """

    # TODO: Put your code here
    clean_cds = ''.join([char ___ char __ cds __ char.isalpha()])
    r.. s..(Seq(clean_cds)
            .upper()
            .translate(table=translation_table, to_stop=True, cds=True)
            )
