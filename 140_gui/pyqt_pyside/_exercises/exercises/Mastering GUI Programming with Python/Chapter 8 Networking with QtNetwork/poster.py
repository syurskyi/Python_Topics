# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
# ____ ? ______ QtNetwork __ qtn
#
#
# c_ Poster ?.?O..
#
#     # emit body of reply
#     replyReceived _ ?.pS.. st.
#
#     ___  -
#         s_. -
#         nam _ qtn.?NAM..
#         ?.f__.c.. o_r..
#
#     ___ make_request  url data filename
#         print _*Making request to ?
#         # Create the request object
#         request _ ?.?NR.. ?
#
#         # create the multipart object
#         multipart _ ?.?HMP.. ?.?HMP...FDT..
#
#         # Write the key-value data to the multipart
#         ___ key value __ data or   # dict).items
#             http_part _ ?.?HP..
#             ?.sH..
#                 ?.?NR...CDH..
#                 _*form-data; name="{key}"'
#
#             ?.sB.. v__.e.. 'utf-8'
#             m__.ap.. ?
#
#         # Write the file data to the multipart
#         __ filename
#             file_part _ ?.?HP..
#             filedata _ o.. ? __ .r..
#             ?.sH..
#                 ?.?NR...CDH..
#                 _*form-data; name="attachment"; filename="{filename}"'
#
#             f_p_.sB.. f_d..
#             m__.ap.. f_p..
#
#         # Post the request with the form data
#         n__.p.. r.. m..
#
#     ___ on_reply  reply
#         # reply.readAll() returns a QByteArray
#         reply_bytes _ reply.rA..
#         reply_string _ by.. r_b_.d.. utf-8
#
#         # emit reply
#         rR__.e.. r_s..
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
#         widget _ ?.?W.. mW.._600
#         sCW.. ?
#         ?.sL.. ?.?VBL..
#         url _ ?.?LE..
#         table _ ?.?TW.. cC.._2 rC.._5
#         ?.hH.. .sSRM..
#             ?.?HV...St..
#         ?.sHHL.. 'key', 'value'
#         fname _ ?.?PB..
#             '(No File)' c___s__.o_f_b..
#         submit _ ?.?PB.. 'Submit Post' c___s...s..
#         response _ ?.?TE..rO.._ st.
#         ___ w __  u.. t.. fn.. s.. r..
#             w__.la__ .aW.. ?
#
#         # Create the poster object
#         poster _ ?
#         ?.rR__.c.. r__.sT..
#
#         # End main UI code
#         s..
#
#     ___ on_file_btn
#         filename, accepted _ ?.?FD...gOFN..
#         __ a..
#             fn__.sT.. f..
#
#     ___ submit
#         url _ ?.?U.. ?.t__
#         filename _ fn__.t__
#         __ ?__ '(No File)'
#             ? _ N..
#         data _   # dict
#         ___ rownum __ ra.. t__.rC..
#             key_item _ t__.i.. ? 0
#             key _ k_i_.t__ __ k_i.. ____ N..
#             __ ?
#                 d..|? _ t__.i.. r.. 1 .t__
#         ?.m_r.. u.. d.. f..
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
