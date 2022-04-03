import os
from u__.r.. import u..
import requests
from collections import defaultdict
from itertools import combinations

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
    #x = requests.get(url)
    #return x.text.splitlines()
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        u..(url, filename)
    with open(filename, "r") as f:
        return f.r..


def get_translation_table(TRANSL_TABLE_11):
    

    table = TRANSL_TABLE_11.replace('T','U')
    lines = table.lstrip().splitlines()

    lines = lines[0:1] + lines[2:]

    for i,line in enumerate(lines):
        lines[i] = line.split('=')[1].strip()
    
    mapping = {}
    for aa,b1,b2,b3 in zip(*lines):
        if aa == 'U':
            aa = 'T'
        mapping[b1 + b2 + b3] = aa


    return mapping






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
    
    amino_acid_mapping = get_translation_table(translation_table_str)
    total = 0
    codon_to_count = defaultdict(int)
    
    for sequence in sequences:
        sequence = sequence.strip()
        for i in range(0,len(sequence),3):
            codon = sequence[i:i +3]
            codon_to_count[codon] += 1

    
    


    total = sum(codon_to_count.values())


    for codon,count in codon_to_count.items():
        amino_acid = amino_acid_mapping[codon]
        frequency_per_1000 = round((count/total) * 1000,1)
        codon_to_count[codon] = [amino_acid,frequency_per_1000,count]



    lines = []
    heading =  '|  Codon AA  Freq  Count  ' * 4  + '|'
    lines.append(heading)
    #print(heading)
    lines.append('-' * len(heading))
    #print('-' * len(heading))
    

    for codon_1 in BASE_ORDER:
        for codon_3 in BASE_ORDER:
            row = []
            for codon_2 in BASE_ORDER:
                codon = codon_1 + codon_2 + codon_3

                aa,freq,count = codon_to_count[codon]
                codon_text = codon + ':'
                data = f"|  {codon_text:<5} {aa:<2}  {freq:>4}  {count:>5}  "
                row.append(data)
            row.append('|')
            lines.append(''.join(row))
            #print(''.join(row))
        

        lines.append('-' * len(heading))
        #print('-' * len(heading))




    return '\n'.join(lines)








    


    













if __name__ == "__main__":
    print(return_codon_usage_table())

    #print(get_translation_table())
