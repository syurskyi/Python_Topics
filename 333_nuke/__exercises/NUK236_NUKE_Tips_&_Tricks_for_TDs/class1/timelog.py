# ______ __
# ______ th..
# ______ ge..
# ______ d_t_
# ______ j___
# ______ __
# ______ ?
# ______ ti__
#
# CURRENT_USER _ g_.g_u..
# LOG_DIR _ */Users/hugoleveille/Desktop/logs
# TIMER _ 5
# IDLE_TIME _ 30
#
#
# c_ Timelog
#
#     ___ start_thread
#
#         ?.t.. _ t__.T.. T.. w..
#         ?.t....sD.. T..
#         ?.t__.st..
#
#     ___ get_json
#         date _ d_t_.d_t_.to__ .s_t.. *%Y-%m-%d
#         json_dir _ *@/@/@  L.. C.. d..
#         __ no. __.p__.e.. j..
#             __.m_d.. ?
#
#         json_path _ @/log.json  j_d..
#         __ no. __.p__.e.. ?
#             data _  # dict
#         ____
#             _file _ o.. ? _
#             data _ j___.l.. ?
#
#         r_ ?
#
#     ___ write_json
#
#         script_path _ ?.r.. *name .v..
#
#         regex _ __.s.. _*projects/(\w+)/shots/(\w+) ?
#         __ ?
#             shot _ *@_@*  ?.g.. 1 ?.g.. 2
#         ____
#             print *Invalid Path
#             s_t..
#             r_
#
#         __ i_t.. > I..
#             print "Script is idle"
#             s_t..
#             r_
#
#
#         data _ g_j..
#
#         __ ?.h_k.. s..
#             ? s.. +_ T..
#         ____
#             ? s.. _ T..
#
#         _file _ o.. j_p_ _
#         j___.d.. d.. _..
#         print d..
#         s_t..
#
#     ___ idle_time
#
#         now _ ti__.ti__
#         autosave_path _ *@.autosave  s_p..
#
#         #1)  If there is an autosave file, we compare it's last modified time to the local time
#
#         __ __.pa__.i_f.. ?
#             modification_time _ in. __.st.. assert .s._mt..
#             _idle_time _ n.. - ?
#
#         #2) If nuke is modified and there is no autosave file, it means the user has modified he's script just after
#         #saving it. So we consider the script not idle
#
#         ____ ?.m..
#             __ no. __.p__.i_f.. a..
#                 _i_t.. _ 0
#
#         #3) If there is no autosave file and nuke is not modified, we compare current time to the modification time of
#         # the nuke script
#
#         ____ no. ?.m..
#             modification_time _ in. __.st..  s_p.. .s._mt..
#             _idle_time _ n.. - ?
#
#         print _i_t..
#         r_ ?