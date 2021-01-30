# _____ ?
# _____ __
# _____ ti__
# _____ h__
#
#
# """
# This module contains functionality to make an automatic backup of your current nuke script whenever you save it.
# """
#
#
# # autoBackup setting
# #############################################################################
# #
# # backup_dir
# # here you can set the root backup directory in which all backups are saved
# backup_dir _ "@/nuke_backups".f.. __.pa__.e__"~"
#
# # number_of_backups
# # here you can decide how many latest backups to have per script
# number_of_backups _ 5
# #
# #############################################################################
#
#
# ___ get_script_name
#     """
#     get the name of the current nuke script
#     :return: String name of the current nuke script
#     """
#
#     script _ ?.r__ .name()
#     script_name _ __.pa__.b__ ?
#     script_name _ __.pa__.s__ ? 0
#
#     r_ ?
#
#
# ___ open_backup_dir
#     """
#     open backup directory in explorer
#     :return: None
#     """
#
#     script_name _ g..
#     script_backup_dir _ "@/@".f.. ? ?
#     h_.o_f.. ?
#
#
# ___ make_backup
#     """
#     make backup of script
#     :return: None
#     """
#
#     script_name _ g__
#     script_backup_dir _ "@/@".f.. .. s...
#     current_time _ ti__.s_t_("%y%m%d-%H%M")
#
#     __ no. __.pa__.i_d_ s..
#         __.m_d_ s..
#
#     ___
#         # remove callback, make backup, add callback
#         # this is a special case because we do a save operation inside the save callback itself.
#         # the callback needs to be removed and added afterwards, otherwise it would end up in an infinite loop
#         ?.rOSS m..
#         ?.sS_("@/bckp_@_@.nk".f.. s_ c_ s_
#         ?.aOSS.. m_
#     ______
#         ?.m__("Couldn't write a backup file")
#
#     d__ s..
#
#
# ___ delete_older_backup_versions pa__
#     """
#     keep only the last backups of a script
#     The number of backup scripts to keep is determined by 'number_of_backups'
#     :param path: String full path of the script backup directory
#     :return: None
#     """
#
#     files_list _  # list
#     keep_list _   # list
#
#     ___ filename __ __.l_d_ pa__
#         __ __.pa__.s__ ? 1 __ ".nk"
#             f__.a__ ?
#
#     __ le. f.. > n..
#         keep_list _ f.. -n...
#
#         # sorry, i forgot to indent this code here
#         # it *must* be indented so it gets only executed
#         # when our if statement above is True
#         ___ filename __ f..
#             __ ? no. __ k..
#                 file_to_delete _ "@/@".f.. pa__ ?
#                 __ __.pa__.i_f.. f..
#                     __.r__ f..
