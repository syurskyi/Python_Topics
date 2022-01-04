_______ __
____ c.. _______ defaultdict
___ pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    # TODO: You code

    mapping = defaultdict(l..)


    ___ file __ filenames:
        

        m.. = __.s..(r'(\S+?_S[1-9][0-9]?_L\d{3})_R[12]_([0-9]{2}[1-9]).fastq.gz$',file,flags=__.I)

        __ m..:
            first_part = m...group(1).l..
            second_part = m...group(2).l..

            combined = first_part + second_part

            mapping[combined].a..(file)

    
    result    # list
    ___ value __ mapping.v..
        __ l..(value) __ 2:

            __ '_R1_' __ value[1]:
                value.reverse()
            result.a..(t..(value))


    r.. result





















# Set up for your convenience during testing
__ _______ __ _______
    filenames = [
        "Sample1_S1_L001_R1_001.FASTQ.GZ",
        "Sample1_S1_L001_R2_001.fastq.gz",
        "Sample2_S2_L001_R1_001.fastq.gz",
        "sample2_s2_l001_r2_001.fastq.gz",
    ]
    print(pair_files(filenames))
    # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    ___ pair __ pair_files(filenames):
        print(pair)
