import os
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
    new_seq = False
    seq, info = None, None
    with open(fasta_file) as f:
        fasta_list = f.readlines()
    #for line in fasta_list:
    for line in fasta_list:
        if line[:1] == '>':
            if seq != None and info != None:
                print(seq, info)
            new_seq = True
            seq = line[1:]
            print(seq)
        else:
            if line[-1] == '>':
                info.append(line[:-1])
            else:
                info.append(line)



if __name__ == "__main__":
    fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")