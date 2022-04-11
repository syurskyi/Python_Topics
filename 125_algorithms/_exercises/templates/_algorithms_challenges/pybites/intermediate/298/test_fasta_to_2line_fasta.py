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


___ test_malformed_fasta
    """
    Test if output is correct with mal-formed input.
    """
    MALFORMED_FASTA f"{FASTA_FILE}.malformed.fasta"
    CONVERTED_FASTA f"{FASTA_FILE}.malformed-test.fasta"

    w__ o.. FASTA_FILE, "r") __ f_in, o.. MALFORMED_FASTA, "w") __ f_out:
        f_out.w.. f_in.r..[1:])

    ... (
        fasta_to_2line_fasta(MALFORMED_FASTA, CONVERTED_FASTA) __ EXPECTED_RECORDS - 1
    )

    w__ o.. CONVERTED_FASTA, "r") __ f_conv:
        ... (
            f_conv.readline().s..
            __ ">sp|Q74NT6|ARSC1_BACC1 Arsenate reductase 1 OS=Bacillus cereu"
            "s (strain ATCC 10987 / NRS 248) OX=222523 GN=arsC1 PE=3 SV=1"
        )
        ... (
            f_conv.readline().s..
            __ "MENKKTIYFLCTGNSCRSQMAEAWGKKYLGDKWNVLSAGIEAHGVNPNAIKAMKEVDIDIT"
            "DQTSDIIDRDILDKADLVVTLCGHANDVCPTTPPHVKRVHWGFDDPAGQEWSVFQRVRDE"
            "IGARIKKYAETGE"
        )
