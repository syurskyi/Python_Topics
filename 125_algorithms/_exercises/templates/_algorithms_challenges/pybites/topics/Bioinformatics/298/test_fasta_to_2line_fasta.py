____ fasta_to_2line_fasta _______ fasta_to_2line_fasta, FASTA_FILE

EXPECTED_RECORDS 59


___ test_well_formed_fasta
    """
    Test if output is correct with well-formed input.
    """

    CONVERTED_FASTA f"{FASTA_FILE}-test.fasta"

    ... fasta_to_2line_fasta(FASTA_FILE, CONVERTED_FASTA) __ EXPECTED_RECORDS
    w__ o.. FASTA_FILE, "r") __ f:
        f.readline()
        ... (
            f.readline().s..
            __ "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
        )

    w__ o.. CONVERTED_FASTA, "r") __ f_conv:
        f_conv.readline()
        ... (
            f_conv.readline().s..
            __ "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
            "LPISILSARIYYVLFEWAYYKNHLNEIFAIWNGGIAIHGGLIGAIVTTIVFTKKRNISF"
            "WKLADIAAPSLILGQAIGRWGNFMNQEAHGGPVSRTFLESLRLPDIIINQMYINGSYYH"
            "PTFLYESIWNIIGFVTLLILRKGSLKRGEIFLSYLIWYSIGRFFVEGLRTDSLMLTSSL"
            "RMAQVMSISLIIISLLLMIYRRRKGLATTRYNELNNNALE"
        )

