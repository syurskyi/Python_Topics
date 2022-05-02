____ ? _______ ? ?

EXPECTED_RECORDS 59


___ test_well_formed_fasta
    """
    Test if output is correct with well-formed input.
    """

    CONVERTED_FASTA f"{FASTA_FILE}-test.fasta"

    ...? ? ? __ ?
    w__ o.. F.. _ __ f
        ?.r..
        ... (
            ?.r...s..
            __ "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
        )

    w__ o.. C.. _ __ f_conv
        ?.r..
        ... (
            ?.r...s..
            __ "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
            "LPISILSARIYYVLFEWAYYKNHLNEIFAIWNGGIAIHGGLIGAIVTTIVFTKKRNISF"
            "WKLADIAAPSLILGQAIGRWGNFMNQEAHGGPVSRTFLESLRLPDIIINQMYINGSYYH"
            "PTFLYESIWNIIGFVTLLILRKGSLKRGEIFLSYLIWYSIGRFFVEGLRTDSLMLTSSL"
            "RMAQVMSISLIIISLLLMIYRRRKGLATTRYNELNNNALE"
        )

