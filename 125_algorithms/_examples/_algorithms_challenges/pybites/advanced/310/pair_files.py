import re
from collections import defaultdict
def pair_files(filenames):
    """
    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    # TODO: You code

    mapping = defaultdict(list)


    for file in filenames:
        

        match = re.search(r'(\S+?_S[1-9][0-9]?_L\d{3})_R[12]_([0-9]{2}[1-9]).fastq.gz$',file,flags=re.I)

        if match:
            first_part = match.group(1).lower()
            second_part = match.group(2).lower()

            combined = first_part + second_part

            mapping[combined].append(file)

    
    result = []
    for value in mapping.values():
        if len(value) == 2:

            if '_R1_' in value[1]:
                value.reverse()
            result.append(tuple(value))


    return result





















# Set up for your convenience during testing
if __name__ == "__main__":
    filenames = [
        "Sample1_S1_L001_R1_001.FASTQ.GZ",
        "Sample1_S1_L001_R2_001.fastq.gz",
        "Sample2_S2_L001_R1_001.fastq.gz",
        "sample2_s2_l001_r2_001.fastq.gz",
    ]
    print(pair_files(filenames))
    # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    for pair in pair_files(filenames):
        print(pair)
