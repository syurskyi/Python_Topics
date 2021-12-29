# TODO: Add imports
from Bio.Seq import Seq
from Bio.Data.CodonTable import TranslationError

def translate_cds(cds: str, translation_table: str) -> str:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """

    # TODO: Put your code here
    clean_cds = ''.join([char for char in cds if char.isalpha()])
    return str(Seq(clean_cds)
            .upper()
            .translate(table=translation_table, to_stop=True, cds=True)
            )
