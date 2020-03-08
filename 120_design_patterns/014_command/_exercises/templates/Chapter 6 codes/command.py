# ______ a..
# ______ __
#
# history _    # list
#
# c_ Command o..
#     """The command interface."""
#
#     -m
#
#     ??.?
#     ___ execute
#         """Method to execute the command."""
#         pass
#
#     ??.?
#     ___ undo
#         """A method to undo the command."""
#         pass
#
# c_ LsCommand C..
#     """Concrete command that emulates ls unix command behavior."""
#
#     ___ - receiver
#         ?  ?
#
#     ___ execute
#         """The command delegates the call to its receiver."""
#         r___.s_c_d..
#
#     ___ undo
#         """Can not undo ls command."""
#         p..
#
# c_ LsReceiver o..
#     ___ show_current_dir
#         """The receiver knows how to execute the command."""
#
#         cur_dir _ './'
#
#         filenames _   # list
#         ____ filename __ __.listdir c_d..
#             __ __.pa__.isf.. __.pa__.jo.. c_d.. ?
#                 f___.ap.. ?
#
#         print 'Content of dir: ', ' '.jo.. f..
#
# c_ TouchCommand C..
#     """Concrete command that emulates touch unix command behavior."""
#
#     ___ - receiver
#         ?  ?
#
#     ___ execute
#         r___.c_f..
#
#     ___ undo
#         r___.d_f..
#
# c_ TouchReceiver o..
#
#     ___ -  filename
#         ?  ?
#
#     ___ create_file
#         """Actual implementation of unix touch command."""
#         w__ fi.. ? _
#             __.uti.. ? N..
#
#     ___ delete_file
#         """Undo unix touch command. Here we simply delete the file."""
#         __.r... f...
#
# c_ RmCommand C..
#     """Concrete command that emulates rm unix command behavior."""
#     ___ - receiver
#         ?  ?
#
#     ___ execute
#         r___.d_f..
#
#     ___ undo
#         r___.un..
#
# c_ RmReceiver o..
#
#     ___ - filename
#         ?  ?
#         b_n.. _ N..
#
#     ___ delete_file
#         """Deletes file with creating backup to restore it in undo method."""
#         backup_name _ '.' + f...
#         __.re.. f.. ?
#
#     ___ undo
#         """Restores the deleted file."""
#         original_name _ b_n..|1;
#         __.re.. b_n.. o_n..
#         b_n.. _ N..
#
# c_ Invoker o..
#     ___ -  create_file_commands delete_file_commands
#         ?  ?
#         ?  ?
#         history _    # list
#
#     ___ create_file
#         print 'Creating file...'
#
#         ___ command __ c_f_c...
#             ?.ex..
#             h___.ap.. ?
#
#         print 'File created.\n'
#
#     ___ delete_file
#         print 'Deleting file...'
#         ___ command __ d_f_c..
#             ?.ex..
#             h__.ap.. ?
#         print 'File deleted.\n'
#
#     ___ undo_all
#         print 'Undo all...'
#
#         ___ command __ re.. h..
#             ?.u..
#
#         print 'Undo all finished.'
#
# __ _______ __ ______
#     # Client
#
#     # List files in current directory
#     ls_receiver _ LsR..
#     ls_command _ LsC.. ?
#
#     # Create a file
#     touch_receiver _ TR.. 'test_file')
#     touch_command _ TC.. t_r..
#
#     # Delete created file
#     rm_receiver _ RR..('test_file')
#     rm_command _ RC.. ?
#
#     create_file_commands _ l_c.. t_c.. ls_c..
#     delete_file_commands _ l_c.. r_c.. l_c..
#
#     invoker _ I.. c_f_c.. d_f_c..
#
#     ?.c_f..
#     ?.d_f..
#     ?.u_a..
