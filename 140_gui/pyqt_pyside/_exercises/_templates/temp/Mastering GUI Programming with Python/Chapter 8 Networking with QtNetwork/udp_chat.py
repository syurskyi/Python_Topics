# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?N.. __ qtn
# ____ ? ______ ?C.. __ qtc
#
#
# c_ UdpChatInterface ? .?O..
#     """Network interface for chat messages."""
#
#     port _ 7777
#     delimiter _ '||'
#     received _ ? .pS.. st. st.
#     error _ ? .pS.. st.
#
#     ___  -   username
#         s_. -
#         ? ?
#
#         socket _ ? .?US..
#         ? .b.. ? .?HA...A.. p..
#         ? .rR__.c.. p_d..
#         ? .e_.c.. o_e..
#
#     ___ process_datagrams
#         w__ ? .hPD..
#             datagram _ ? .rD..
#             # to convert QByteArray to a string,
#             # cast it to bytes then decode
#             raw_message _ by.. d__.d.. .d.. utf-8
#
#             __ delimiter no. __ r_m..
#                 # invalid message, ignore
#                 c___
#             username, message _ r_m_.sp.. d.. 1
#             r__.e.. ? ?
#
#     ___ on_error  socket_error
#         # Magic to get the enum name
#         error_index _ ? .?AS..
#                        .sMO..
#                        .iOE.. SocketError
#         error _ ? .?AS..
#                  .sMO..
#                  .en.. e_i..
#                  .vTK.. s_e..
#         message _ _* There was a network error: |?
#         e__.e.. ?
#
#     ___ send_message  message
#         """Prepare and send a message"""
#         msg_bytes _
#             _*|u.. |d.. |m..
#             .e.. utf-8
#         s__.wD..
#             ? .?BA.. m_b..
#             ? .?HA...Br..
#             p..
#
#
#
# c_ ChatWindow ?.?W..
#     """The form to show and enter chats"""
#
#     submitted _ ? .pS.. st.
#
#     ___  -
#         s_. -
#
#         sL.. ?.?GL..
#         message_view _ ?.?TE..rO.._ st.
#         la__ .aW.. m_v.. 1, 1, 1, 2
#         message_entry _ ?.?LE..
#         la__ .aW.. m_e.. 2, 1
#         send_btn _ ?.?PB.. 'Send', c___.s..
#         la__ .aW.. send_btn, 2, 2
#
#     ___ write_message  username, message
#         message_view.ap.. _* _b_|u.. : _/b_ |m.. _br__
#
#     ___ send
#         message _ m_e_.t__ .s..
#         __ ?
#             s__.e.. ?
#             m_e_.c..
#
#
# c_ MainWindow ?.?MW..
#
#     ___  -
#         """MainWindow constructor."""
#         s_. -
#         # Code starts here
#
#         cw _ ?
#         sCW.. ?
#
#         username _ ? .?D...h.. .dN..
#         interface _ ? ?
#         c_.s_.c.. i__.s_m..
#         ?.r__.c.. c_.w_m..
#         ?.e__.c..
#             l___ x ?.?MB...c.. N.. 'Error' x
#         # Code ends here
#         s..
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
