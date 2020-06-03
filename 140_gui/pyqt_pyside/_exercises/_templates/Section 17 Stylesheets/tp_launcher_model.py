# #!/usr/bin/env python
#
# '''
# Data holding (model) class for TP Launcher.
# Stores data in the following way:
#     Workspaces Ordered Dict {
#         WorkspaceName {
#             AppName : (App_file_path, Icon_file_path)
#             }
#         }
#
# has basic accessors and mutators, run and reorder.
# Also includes YouTube opening function, hardcoded url though.
# '''
#
# ____ collections _____ OD.. d_d..
# _____ j..
# _____ __
# _____ pla..
# _____ sub..
# _____ webbrowser
#
#
# c_ TP_Launcher_Model object
#     ''' Data holding (model) class for TP Launcher.
#     Stores data in the following way:
#         Workspaces Ordered Dict {
#             WorkspaceName {
#                 AppName : (App_file_path, Icon_file_path)
#                 }
#             }
#
#     has basic accessors and mutators, run and reorder.
#     Also includes YouTube opening function, hardcoded url though.
#     '''
#     ___  -
#         _workspaces _ OD..
#         _open_doc _ d_d_ l___ open
#         _?| Windows _ start
#         _platform _ pla__.sy..
#
#     # ======== WORKSPACES ============
#
#     ___ add_workspace  ws_name
#         ''' Add a new workspace, creating ordered dict'''
#         _?|? _ OD..
#
#     ___ get_workspaces
#         ''' returns a list of workspace names '''
#         r_ li.. _?.k.. # Python 3.0+ conversion
#
#     ___ delete_workspace  ws_name
#         ''' delete workspace by workspace name '''
#         de. _?|?
#
#     # ======== APPS ============
#
#     ___ get_app_names  ws_name
#         ''' returns list of application or file names, no ext'''
#         r_ _?|? .k..
#
#     ___ get_app_icon  ws_name app_name
#         ''' return filepath to icon image'''
#         r_ _?|? |? 1
#
#     ___ add_app  ws_name app_path icon_path
#         ''' add an application and icon file path to the workspace
#         dictionary designated
#         '''
#         app_name _ __.pa__.s_t.. __.pa__.b.. a_p.. 0
#         _?|? |a_n.. _ |a_p.. i_p..
#
#     ___ delete_app  ws_name app_name
#         ''' delete app from workspace dict'''
#         de. _?|? |?
#
#     ___ reorder_apps  ws_name app_list
#         ''' if app/file order has changed, reorder dict'''
#         __ _?|? .k.. !_ a_l..
#             temp _ OD..
#             ___ name __ a_l..
#                 ?|? _ _?|? |?
#             _?|? _ t..
#
#     ___ run_app  ws_name app_name
#         ''' attempt to run application/file at path if still exists'''
#         _file _ _?|? |? 0
#         __ __.pa__.e.. _?
#             ___
#                 su__.Po.. _f..
#             _____
#                 __.sy.. _o_d..|_p.. + _f..
#         ____
#             r_ V.. Exe file no longer exists
#
#     ___ run_youtube
#         ''' Open my favorite youtube channel! '''
#         w___.o..('http://www.youtube.com/TPayneExperience')
#
#     # ======== JSON ============
#
#     ___ write_json_file  pa__
#         ''' write data from ordered dict to json file'''
#         w__ o.. pa__ _ __ js_file
#             ___.d.. _? ?
#
#     ___ read_json_file  pa__
#         ''' read data from ordered dict to json file'''
#         w__ o.. pa__ _ __ js_file
#             _? _ OD.. ____.l.. ?
