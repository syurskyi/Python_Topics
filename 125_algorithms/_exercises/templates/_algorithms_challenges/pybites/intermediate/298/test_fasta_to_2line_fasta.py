# ____ ? _______ ? ?
#
# EXPECTED_RECORDS 59
#
#
# ___ test_well_formed_fasta
#     """
#     Test if output is correct with well-formed input.
#     """
#
#     CONVERTED_FASTA _*F.. -test.fasta
#
#     ...? ? ? __ ?
#     w__ o.. F.. _ __ f
#         ?.r..
#         ...
#             ?.r...s..
#             __ "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
#
#
#     w__ o.. C.. _ __ f_conv
#         ?.r..
#         ...
#             ?.r...s..
#             __ "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
#             "LPISILSARIYYVLFEWAYYKNHLNEIFAIWNGGIAIHGGLIGAIVTTIVFTKKRNISF"
#             "WKLADIAAPSLILGQAIGRWGNFMNQEAHGGPVSRTFLESLRLPDIIINQMYINGSYYH"
#             "PTFLYESIWNIIGFVTLLILRKGSLKRGEIFLSYLIWYSIGRFFVEGLRTDSLMLTSSL"
#             "RMAQVMSISLIIISLLLMIYRRRKGLATTRYNELNNNALE"
#
#
#
# ___ test_malformed_fasta
#     """
#     Test if output is correct with mal-formed input.
#     """
#     MALFORMED_FASTA _*F__.malformed.fasta"
#     CONVERTED_FASTA _*F__.malformed-test.fasta"
#
#     w__ o.. F.. _ __ f_in o.. M.. _ __ f_out
#         ?.w.. ?.r.. 1|
#
#     ...
#         ? ? ? __ ? - 1
#
#
#     w__ o.. C.. _ __ f_conv
#         ...
#             ?.r...s..
#             __ ">sp|Q74NT6|ARSC1_BACC1 Arsenate reductase 1 OS=Bacillus cereu"
#             "s (strain ATCC 10987 / NRS 248) OX=222523 GN=arsC1 PE=3 SV=1"
#
#         ...
#             ?.r...s..
#             __ "MENKKTIYFLCTGNSCRSQMAEAWGKKYLGDKWNVLSAGIEAHGVNPNAIKAMKEVDIDIT"
#             "DQTSDIIDRDILDKADLVVTLCGHANDVCPTTPPHVKRVHWGFDDPAGQEWSVFQRVRDE"
#             "IGARIKKYAETGE"
#
