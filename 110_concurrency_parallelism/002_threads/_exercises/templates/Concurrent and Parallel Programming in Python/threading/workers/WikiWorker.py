# _______ _______
#
# _______ r..
# from bs4 _______ B...
#
#
# c_ WikiWorkerMasterScheduler _______.T...
#     ___  -  output_queue $$
#         __ 'input_queue' __ $$
#             ?.p.. 'input_queue'
#
#         _input_values = k__.p.. 'input_values'
#
#         temp_queue = o..
#         __ ty.. ? != list
#             t.. = t..
#         _o.. = t..
#         s__ ?   - $$
#         s..
#
#     ___ run
#         ___ entry __ _i..
#             wikiWorker = WikiWorker ?
#             symbol_counter = 0
#             ___ symbol __ ?.g..
#                 ___ o... __ _o..
#                     o....p.. ?
#                 s.. += 1
#                 __ s.. >= 5
#                     ______
#
#
# c_ WikiWorker
#     ___  -  url
#         _? = ?
#
#     $s..
#     ___ _extract_company_symbols page_html
#         soup = B... p.. 'lxml'
#         table = ?.f.. id='constituents'
#         table_rows = ?.f.. 'tr'
#         ___ table_row __ ? 1|
#             symbol = ?.f.. 'td' .t__.s... '\n'
#             _____ ?
#
#     ___ get_sp_500_companies
#         response = r...get(_url)
#         __ ?.s.. != 200
#             print("Couldn't get entries")
#             r_   # list
#
#         _____ f.. _extract_company_symbols r__.t..
#
