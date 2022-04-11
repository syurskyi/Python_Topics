# TODO: Add imports
____ Bio.Seq _______ Seq
____ Bio.Data.CodonTable _______ TranslationError

___ translate_cds(cds: s.., translation_table: s..) __ s..:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """

    # TODO: Put your code here
    #print(f'{cds}\n{translation_table}')
    ___
        clean_cds ''.j..([char ___ char __ cds __ char.i..])
        r.. s..(Seq(clean_cds)
                .u..
                .translate(table=translation_table, to_stop=T.., cds=T..)
                )
    ______ TranslationError:
        r.. TranslationError

#print(translate_cds("ATGTAATAA", "Standard"))