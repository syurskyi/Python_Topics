# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?C.. __ qtc
#
#
# c_ HashForm ?.?W..
#
#     submitted _ ?.pS.. st. st. in.
#
#     ___  -
#         s_. -
#         sL.. ?.?FL..
#         source_path _ ?.?PB..
#             'Click to select…', c___.o_s_c..
#         la__ .aR.. 'Source Path' ?
#         destination_file _ ?.?PB..
#             'Click to select…', c___.o_d_c..
#         la__ .aR.. 'Destination File' ?
#         threads _ ?.SB.. mi.._1, ma.._7, va.._2
#         la__ .aR.. 'Threads' ?
#         submit _ ?.?PB.. 'Go', c___s.o_s..
#         la__ .aR.. ?
#
#     ___ on_source_click
#         dirname _ ?.?FD...gED..
#         __ ?
#             s_p_.sT.. ?
#
#     ___ on_dest_click
#         filename, _ _ ?.?FD...gSFN..
#         __ ?
#             d_f_.sT.. ?
#
#     ___ on_submit
#         submitted.e..
#             s_p_.t__
#             d_f_.t__
#             t__.v..
#
#
#
# c_ HashRunner ?.?R..
#
#     file_lock _ ?.?M..
#
#     ___  -   infile outfile
#         s_. -
#         ? ?
#         ? ?
#         hasher _ ?.?CH..
#             ?.?CH_.Md5
#         sAD.. st.
#
#     ___ run
#         print _*hashing {infile}')
#         h__.r..
#         w__ o.. i.. __  __ fh
#             h__.aD.. fh.r..
#         hash_string _ by.. h__.r.. .tH.. .d.. UTF-8
#         # Traditional method:
#         #try:
#         #    self.file_lock.lock()
#         #    with open(self.outfile, 'a', encoding='utf-8') as out:
#         #        out.write(f'{self.infile}\t{hash_string}\n')
#         #finally:
#         #    self.file_lock.unlock()
#
#         # Better method:
#         w__ ?.?ML.. f_l..
#             w__ o.. o.. _ en.._ utf-8  __ out
#                 ou_.w.. _*{infile}\t{hash_string}\n')
#
#
# c_ HashManager ?.?O..
#
#     finished _ ?.pS..
#
#     ___  -
#         s_. -
#         pool _ ?.?TP...gI..
#
#     ??.? st. st. in.
#     ___ do_hashing  source destination threads
#         p__.sMTC.. th..
#         qdir _ ?.?D.. s..
#         ___ filename __ ?.eL.. ?.?D...Fi..
#             filepath _ ?.aFP.. ?
#             runner _ ? f.. d..
#             p__.s.. ?
#
#         # This call is why we put HashManager in its own thread.
#         # If we don't care about being notified when the process is done,
#         # we could leave this out and run HashManager in the main thread.
#         p__.wFD..
#         f__.e..
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
#         form _ ?
#         sCW.. ?
#         manager _ ?
#
#         # Move it to another thread so we can notify the user when things
#         # are finished
#         manager_thread _ ?.?
#         m__.mTT.. ?
#         ?.s..
#
#         f__.s__.c.. m__.d_h..
#         f__.s__.c..
#             l___ x, y, z: sB.. .sM..
#                 _*Processing files in ? into ? with ? threads.'))
#         m__.f__.c..
#             l___ sB.. .sM.. 'Finished'
#         # End main UI code
#         s..
#
#
# __ ______ __ ______
#     app _ ?.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
