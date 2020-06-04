# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?N.. __ qtn
# ____ ? ______ ?C.. __ qtc
#
#
# c_ TcpChatInterface(? .?O..
#     """Network interface for chat messages."""
#
#     port _ 7777
#     delimiter _ '||'
#     received _ ? .pS.. st. st.
#     error _ ? .pS.. st.
#
#     ___  -   username, recipient
#         s_. -
#         ? ?
#         ? ?
#
#         listener _ ? .?TS..
#         ?.l.. ? .?HA...A.. p..
#         ?.nC__.c.. o_c..
#         ?.aE__.c.. o_e..
#         connections _   # list
#
#         client_socket _ ? .?TS..
#         ?.e__.c.. o_e..
#
#     ___ on_connection
#         connection _ l__.nPC..
#         c__.ap.. ?
#         ?.rR__.c.. p_d..
#
#     ___ process_datastream
#         ___ socket __ c..
#             datastream _ ? .?DS.. ?
#             __ no. ?.bA..
#                 c___
#             #message_length = self.datastream.readUInt32()
#             raw_message _ d__.rQS..
#             __ ? an. de.. __ ?
#                 username message _ ?.sp.. de.. 1
#                 r__.e.. ? ?
#
#     ___ send_message  message
#         """Prepare and send a message"""
#         raw_message _ _*|u.. |d.. |m..
#         __ c_s__.s.. !_ ? .?AS...CS..
#             c_s_.cTH.. r.. p..
#         datastream _ ? .?DS.. c_s..
#         #self.datastream.writeUInt32()
#         ?.wQS.. ?
#
#         # Echo locally
#         r__.e.. u.. m..
#
#     ___ on_error  socket_error
#         # Magic to get the enum name
#         error_index _ ? .?AS..
#                        .sMO..
#                        .iOE.. SocketError
#         error _ ? .?AS..
#                  .sMO..
#                  .e.. e_i..
#                  .vTK.. s_e..
#         message _ _*There was a network error: |?
#         e__.e.. ?
#
#
# c_ ChatWindow ?.?W..
#     """The form to show and enter chats"""
#
#     submitted _ ? .pS.. st.
#
#     ___  -
#         s_. -
#         sL.. ?.?GL..
#         message_view _ ?.?TE..rO.. st.
#         la__ .aW.. m_v.. 1, 1, 1, 2
#         message_entry _ ?.?LE.. rP.._.s..
#         la__ .aW.. ? 2, 1
#         send_btn _ ?.?PB.. 'Send' c___.s..
#         la__ .aW.. ? 2, 2
#
#     ___ write_message  username, message
#         message_view.ap.. _*_b_|u.. : _/b_ |m.. _br_
#
#     ___ send
#         message _ m_e__.t__ .s..
#         __ ?
#             s__.e.. ?
#             m_e_.c..
#
#
# c_ MainWindow ?.?MW..
#
#     ___  -
#         """MainWindow constructor.
#
#         Code in this method should define window properties,
#         create backend resources, etc.
#         """
#         s_. -
#         # Code starts here
#         username _ ? .?D...h.. .dN..
#         cw _ ?
#         sCW.. ?
#         recipient _ _ ?.?ID__.gT..
#             N.. 'Recipient'
#             'Specify of the IP or hostname of the remote host.'
#         __ no. ?
#             ___.e..
#
#         interface _ ? u.. r..
#         c_.s__.c.. i__.s_m..
#         i__.r__.c.. c_.w_m..
#         i__.e__.c..
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
