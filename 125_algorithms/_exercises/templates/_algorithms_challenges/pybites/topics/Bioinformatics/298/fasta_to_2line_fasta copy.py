_______ __
_______ u..
____ Bio _______ SeqIO

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
URL "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE __.p...j..(__.g.. TMP  /tmp, "fasta_genes.fasta")
__ n.. __.p...i.. F..
    u__.r...u.. ? ?

___ fasta_to_2line_fasta(fasta_file: s.., fasta_2line_file: s..) __ i..
    """
    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """
    new_seq F..
    seq, info N.., N..
    w__ o.. fasta_file) __ f:
        fasta_list f.r..
    #for line in fasta_list:
    ___ line __ fasta_list:
        __ line[:1] __ '>':
            __ seq !_ N.. a.. info !_ N..
                print(seq, info)
            new_seq T..
            seq line[1:]
            print(seq)
        ____
            __ line[-1] __ '>':
                info.a..(line[:-1])
            ____
                info.a..(line)



__ _______ __ _______
    fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")