_______ __
_______ urllib
#from Bio import SeqIO
_______ r__

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)

URL "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE __.p...j..(__.g.. TMP  /tmp, "fasta_genes.fasta")

response r__.g.. URL)

w__ o.. 'test.txt','w') __ f:
    f.w.. response.text)


__ n.. __.p...i..(FASTA_FILE
    u__.r...u..(URL, FASTA_FILE)

___ fasta_to_2line_fasta(fasta_file:s..="test.txt", fasta_2line_file: s..='test_converter.txt') __ i..
    """
    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """

    sequence    # list
    lines    # list
    records 0
    w__ o.. fasta_2line_file,'w') __ f1, o.. fasta_file _ __ f2:

            ___ i,line __ e..(f2,1
                line line.s..
                line line.s..
                __ line[0] __ '>':
                    __ ?
                        sequence.a..(''.j..(lines
                        f1.w.. '\n'.j..(sequence
                        f1.w.. '\n')
                        sequence    # list
                    ____
                        sequence [line]
                    records += 1
                    lines    # list
                ____
                    lines.a..(line)
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

    r.. records



__ _______ __ _______
    fasta_to_2line_fasta()
    #fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")
