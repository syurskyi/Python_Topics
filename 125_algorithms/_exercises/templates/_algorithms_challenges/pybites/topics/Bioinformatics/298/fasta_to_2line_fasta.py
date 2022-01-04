_______ os
____ typing _______ Sequence
_______ urllib
____ Bio _______ SeqIO

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE = os.path.j..(os.getenv("TMP", "/tmp"), "fasta_genes.fasta")
__ n.. os.path.isfile(FASTA_FILE):
    urllib.request.urlretrieve(URL, FASTA_FILE)

___ fasta_to_2line_fasta(fasta_file: s.., fasta_2line_file: s..) __ i..:
    """
    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """
    w__ open(fasta_2line_file, 'w') __ f:
        sequence = l..(SeqIO.p..(fasta_file, "fasta"))
        ___ record __ sequence:
            #print(f'>{record.description}\n{record.seq}')
            f.write _*>{record.description}\n{record.seq}\n')
        f.close()
    print(FASTA_FILE)
    r.. l..(sequence)


__ _______ __ _______
    fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")