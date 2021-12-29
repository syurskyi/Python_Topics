import os
#from typing import Counter
from urllib.request import urlretrieve
from collections import Counter


# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()

def codon_info(codons, count, total, translation):
    return_str = '|'
    for codon in codons:
        freq = round(count[codon]/(total/1000), 1)
        temp_str = f'  {codon}:  {translation[codon]}   {freq:4}  {count[codon]:5}  |'
        return_str = return_str + temp_str
    return return_str

def return_codon_usage_table(
    sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    first_line = "|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |"
    seperator = "---------------------------------------------------------------------------------------------------------"
    whole_table = []
    whole_table.append(first_line)
    whole_table.append(seperator)
    condon_count = Counter()
    for seq in sequences:
        codons = [seq[index:index+3] for index in range(0, len(seq.strip()), 3)]
        condon_count.update(codons)
    translation_table_line = [line for line in translation_table_str.split('\n') if line]
    _, AAs = translation_table_line[0].split('  = ')
    _, Starts = translation_table_line[1].split(' = ')
    _, Base1 = translation_table_line[2].split('  = ')
    _, Base2 = translation_table_line[3].split('  = ')
    _, Base3 = translation_table_line[4].split('  = ')
    translation = {''.join(z[0:3]): z[3] for z in 
        zip(Base1.replace('T', 'U'), Base2.replace('T', 'U'), Base3.replace('T', 'U'), AAs)}
    translation_list = list(translation.keys())
    for i in range(0, len(translation_list), 16):
        for j in range(i, i+4):
            whole_table.append(codon_info([translation_list[j], translation_list[j+4], translation_list[j+8], translation_list[j+12]], 
                            condon_count,
                            sum(condon_count.values()), 
                            translation
                            ))
        whole_table.append(seperator)
    return '\n'.join(whole_table)




if __name__ == "__main__":
    print(return_codon_usage_table())