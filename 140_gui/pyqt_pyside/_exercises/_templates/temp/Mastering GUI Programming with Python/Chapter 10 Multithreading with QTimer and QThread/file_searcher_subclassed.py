# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
#
#
# c_ SlowSearcherThread ?.?T..
#     """A somewhat deliberately slow searcher."""
#
#     match_found _ ?.pS.. st.
#     directory_changed _ ?.pS.. st.
#     finished _ ?.pS..
#
#     ___  -
#         s_. -
#         term _ N..
#
#     ??.? st.
#     ___ set_term  term
#         ? ?
#
#     ??.?
#     ___ run
#         #print(f'Beginning search for: {self.term}')
#         root _ ?.?D...rP..
#         _s.. t.. r..
#         f__.e..
#
#     ___ _search  term pa__
#         d_c_.e.. ?
#         directory _ ?.?D.. ?
#         ?.sF..
#             ?.f.. _
#             ?.?D...NDADD.. _
#             ?.?D...NSL..
#
#         ___ entry __ d__.eIL..
#             __ term __ ?.fP..
#                 print ?.fP..
#                 m_f__.e.. ?.fP..
#             __ ?.iD..
#                 _s.. t.. ?.fP..
#
#
# c_ SearchForm ?.?W..
#
#     tC.. _ ?.pS.. st.
#     rP__ _ ?.pS..
#
#     ___  -
#         s_. -
#         sL.. ?.?VBL..
#         search_term_inp _ ?.?LE..
#             pT.._'Search Term'
#             tC.._.tC..
#             rP.._.rP__
#         la__ .aW.. s_t_i..
#         results _ ?.?LW..
#         la__ .aW.. ?
#         rP__.c.. ?.c..
#
#     ___ addResult  result
#         r__.aI.. ?
#
#
#
# c_ MainWindow ?.?MW..
#
#     ___  -
#         """MainWindow constructor.
#
#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         s_. -
#         # Main UI code goes here
#
#         form _ ?
#         sCW.. ?
#         ss _ ?
#
#         # Connect to search engine
#         f__.tC...c.. s_.s_t..
#         f__.rP__.c.. s_.s..
#         s_.match_found.c.. f__.aR..
#         s_.f__.c.. o_f..
#         s_.d_c_.c.. o_d_c..
#
#         # End main UI code
#         s..
#
#     ___ o_f..
#         sB.. .sM.. Search Finished
#
#     ___ on_directory_changed  pa__
#         sB.. .sM.. _*Searching in: ?
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
