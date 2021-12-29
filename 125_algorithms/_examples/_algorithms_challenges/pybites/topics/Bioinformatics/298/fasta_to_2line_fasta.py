import os
from typing import Sequence
import urllib
from Bio import SeqIO

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE = os.path.join(os.getenv("TMP", "/tmp"), "fasta_genes.fasta")
if not os.path.isfile(FASTA_FILE):
    urllib.request.urlretrieve(URL, FASTA_FILE)

def fasta_to_2line_fasta(fasta_file: str, fasta_2line_file: str) -> int:
    """
    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """
    with open(fasta_2line_file, 'w') as f:
        sequence = list(SeqIO.parse(fasta_file, "fasta"))
        for record in sequence:
            #print(f'>{record.description}\n{record.seq}')
            f.write(f'>{record.description}\n{record.seq}\n')
        f.close()
    print(FASTA_FILE)
    return len(sequence)


if __name__ == "__main__":
    fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")