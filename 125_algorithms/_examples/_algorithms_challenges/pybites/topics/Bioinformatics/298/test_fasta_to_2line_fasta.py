from fasta_to_2line_fasta import fasta_to_2line_fasta, FASTA_FILE

EXPECTED_RECORDS = 59


def test_well_formed_fasta():
    """
    Test if output is correct with well-formed input.
    """

    CONVERTED_FASTA = f"{FASTA_FILE}-test.fasta"

    assert fasta_to_2line_fasta(FASTA_FILE, CONVERTED_FASTA) == EXPECTED_RECORDS
    with open(FASTA_FILE, "r") as f:
        f.readline()
        assert (
            f.readline().strip()
            == "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
        )

    with open(CONVERTED_FASTA, "r") as f_conv:
        f_conv.readline()
        assert (
            f_conv.readline().strip()
            == "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
            "LPISILSARIYYVLFEWAYYKNHLNEIFAIWNGGIAIHGGLIGAIVTTIVFTKKRNISF"
            "WKLADIAAPSLILGQAIGRWGNFMNQEAHGGPVSRTFLESLRLPDIIINQMYINGSYYH"
            "PTFLYESIWNIIGFVTLLILRKGSLKRGEIFLSYLIWYSIGRFFVEGLRTDSLMLTSSL"
            "RMAQVMSISLIIISLLLMIYRRRKGLATTRYNELNNNALE"
        )

