# ______ ___
# ______ j___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
# ____ ? ______ ?N.. __ qtn
#
#
# c_ Poster ?.?O..
#
#     # emit body of reply
#     replyReceived _ ?.pS.. st.
#
#     ___  -
#         s_. -
#         nam _ ?.?NAM..
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
#         json_string _ ?.d.. d..
#         http_part _ ?.?HP..
#         ?.sH..
#             ?.?NR...CTH..,
#             'text/json'
#         )
#         h_p_.sB.. j_s_.e.. utf-8'
#         m_.ap.. h..
#
#         # Write the file data to the multipart
#         __ filename:
#             file_part _ ?.?HP..
#             filedata _ o.. ? __ .r..
#             f_p_.sH..
#                 ?.?NR...CDH..
#                 _*form-data; name="attachment"; filename="{filename}"'
#
#             f_p_.sB.. f..
#             m__.ap.. f_p..
#
#         # Post the request with the form data
#         n__.p.. r.. m..
#
#     ___ on_reply  reply
#         # reply.readAll() returns a QByteArray
#         reply_bytes _ ?.rA..
#         reply_string _ by.. ?.d.. utf-8
#
#         # emit reply
#         rR__.e.. ?
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
#         w__.sL.. ?.?VBL..
#         url _ ?.?LE..
#         table _ ?.?TW.. cC.._2 rC.._5
#         t__.hH.. .sSRM..
#             qtw.?HV...St..
#         t__.sHHL.. 'key', 'value'
#         fname _ ?.?PB..
#             '(No File)' c___s...o_f_b..
#         submit _ ?.?PB.. 'Submit Post' c___s__.s..
#         response _ ?.?TE..readOnly_ st.
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
#         __ ? __ '(No File)'
#             ? _ N..
#         data _   # dict
#         ___ rownum __ ra.. t__.rC..
#             key_item _ t__.i.. ? 0
#             key _ ?.t__ __ ? ____ N..
#             __ ?
#                 d..|? _ t__.i.. r.. 1 .t__
#         p__.m_r.. u.. d.. f..
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
