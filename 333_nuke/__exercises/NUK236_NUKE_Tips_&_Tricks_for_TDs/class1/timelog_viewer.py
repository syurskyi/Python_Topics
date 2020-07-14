# ______ ?
# ______ __
# ______ getpass
# ______ shutil
# ______ j___
# ______ ?
#
# CURRENT_USER _ getpass.getuser()
# LOG_DIR _ "/Users/hugoleveille/Desktop/logs"
#
#
# c_ Panel ?.PP..
#     ___  -  name
#         s_ ? ?. - ?
#
#         sMS.. 500,500
#
#         date_combo_box _ ?.E_K.. "date", "Date" ||
#         delete_push_button _ ?.PS_K.. "delete", "Delete", ""
#         log_knob _ ?.M_E_S_K.. "text","Log",""
#
#         aK.. ?
#         aK.. ?
#         aK.. ?
#
#         ?
#
#     ___ delete_log
#         m.. _ ?.a.. "Are you sure you want to delete this log?"
#         __ no. m..
#             r_
#
#         date _ da__.v..
#         path _ "@/@/@"  L.. C.. ?
#         sh__.rmt.. ?
#         l_k_.sV..("")
#         ?
#
#     ___ build_date_combo_box
#         log_dir _ "@/@" L.. C..
#         da__.sV.. __.w.. ? .ne.. 1
#
#         __ da__.value
#             da__.sV.. da__.v.. 0
#             b.. g_l..
#
#     ___ get_log
#
#         date _ da__.v..
#         json_path _ "@/@/@/log.json"  L.. C.. ?
#         log _ j___.lo.. o.. ?
#         r_ ?
#
#     ___ build_log_text log
#         txt _ ""
#         ___ i __ log
#             ti__ _ ? ?
#             ? +_ "@\n@\n\n"  ? s_t_s.. ti__
#         l_k_.sV.. ?
#
#     ___ knobChanged knob
#
#         __ ?.n.. __ "date"
#             bu.. g_l..
#
#         __ ?.n.. __ "delete"
#             ?
#
#     ___ delete_log
#
#         m.. _ ?.a.. "Are you sure you want to delete this log?"
#         __ no. m..
#             r_
#
#         date _ da__.v..
#         path _ "@/@/@"  L.. C.. ?
#         sh__.rmt.. ?
#         l_k_.sV.. ""
#         bu..
#
#     ___ seconds_to_str sec
#
#         m.. s.. _ d_m_ s.. 60
#         h.. m.. _ d_m_ m.. 60
#         r_ "@02d:@02d"  h.. m..