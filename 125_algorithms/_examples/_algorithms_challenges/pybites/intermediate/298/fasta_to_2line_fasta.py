import os
import urllib
#from Bio import SeqIO
import requests

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE = os.path.join(os.getenv("TMP", "/tmp"), "fasta_genes.fasta")

response = requests.get(URL)

with open('test.txt','w') as f:
    f.write(response.text)


if not os.path.isfile(FASTA_FILE):
    u__.r...u..(URL, FASTA_FILE)

def fasta_to_2line_fasta(fasta_file:str="test.txt", fasta_2line_file: str='test_converter.txt') -> int:
    """
    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """

    sequence = []
    lines = []
    records = 0
    with open(fasta_2line_file,'w') as f1, open(fasta_file,'r') as f2:

            for i,line in enumerate(f2,1):
                line = line.strip()
                line = line.strip()
                if line[0] == '>':
                    if sequence:
                        sequence.append(''.join(lines))
                        f1.write('\n'.join(sequence))
                        f1.write('\n')
                        sequence = []
                    else:
                        sequence = [line]
                    records += 1
                    lines = []
                else:
                    lines.append(line)
    '''    
    records *= 2
    
    records  += 1
    if sequence:
        sequence.append(''.join(lines))
        f1.write('\n'.join(sequence))
    i = 10
    with open(fasta_2line_file,'r') as f:
            for line in f:
                print(line.strip())

                i -= 1
                if i == 0:
                    break
    '''

    return records



if __name__ == "__main__":
    fasta_to_2line_fasta()
    #fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")
