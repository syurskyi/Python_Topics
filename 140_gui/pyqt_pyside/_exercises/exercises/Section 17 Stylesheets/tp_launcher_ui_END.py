# #!/usr/bin/env python
#
# -a _ 'Trevor Payne'
# -v _ '1.0'
#
# ____ collections _____ defaultdict
# _____ __
# _____ ___
#
# _____ __
# ____ __ _____ ?W.., ?C.., ?G..
# _____ tp_launcher_model
#
# QT_VER _ __. -b
# PY_VER _ ___.v.. ;3
#
# _STYLE_MAIN _ '''
#     QWidget{
#         color: white;
#         background-color: qlineargradient(
#             x1: 0, y1: 0, x2: 1, y2: 1,
#             stop: 0 #052e32, stop: 0.25 #030f00,
#             stop: 0.75 #030f00, stop: 1 #382213);
#         alternate-background-color: #072100;
#     }
#     QComboBox{
#         color: white;
#         background: black;
#         border: 1px inset gray;
#         border-radius: 2px;
#     }
#     QGroupBox{ background-color: rgba(0,0,0,0)}
#     QLineEdit{ color: white;  background-color: rgb(0,0,0); }
#     '''
# _STYLE_BTN _ '''
#     QPushButton{
#         border: 1px outset gray;
#         border-radius: 2px;
#         background-color: #00351d;
#         min-width: 40px;
#     }
#     QPushButton:checked {
#         border: 1px outset gray;
#         border-radius: 2px;
#         background-color: #701200;
#         min-width: 40px;
#     }
#     '''
#
# c_ Delete_Btn ?W...?PB..
#     ''' Custom button that Triggers parent's 'delete_item' function. '''
#     ___  -  p_N..
#         s__ ? ?. - ?
#         _my_parent _ ?
#         _type _ 'application/x-qabstractitemmodeldatalist'
#
#     ___ dragEnterEvent  event
#         __ ?.mD...hF.. _t..
#             ?.a..
#         ____
#             ?.i..
#
#     ___ dropEvent event
#         __ ?.mD...hF.. _t..
#             _m...d_i..
#             ?.a..
#         ____
#             ?.i..
#
# c_ TP_Launcher_GUI ?W...?W..
#     '''The goal of this tool is to create a GUI that
#         allows the user to quickly create, select and
#         delete workspaces and add, remove and launch
#         applications within those workspaces.
#     '''
#     ___  -   p.._N..
#         s__ ? ?. - ?
#
#         # System and tool icons
#         _icons _ ?W...?FIP..
#         _my_path _ __.pa__.d_n.. __.pa__.r_p.. -f
#         images_path _ __.pa__.j.. _? 'images'
#         full_path _ __.pa__.j.. ? 'TPayne_Launcher.png'
#         _tpl_icon _ ?G...?I.. ?
#
#         # Data holding instance
#         _tp_launcher _ t_l_m_.T..
#
#         # Toggle dictionary to replace 'if/else' statements
#         _edit_op _
#             T.. _e_o.
#             F.. _e_
#
#         _app_instruction _ T..
#
#         # Handle version specific file dialog box issues
#         _file_dialogs _ d_d.. l___ _f_d..
#         _?|'PyQt4' _ _f_d_pyqt4
#         _dragging _ N..
#         _delete_op _
#             'workspace' _d_w..
#             'application'_d_a..
#
#
#         # Settings and json file read/write stuff
#         txt _ 'TPayne_Experience'+Q..
#         _settings _ ?C...?S.. ? 'TPayne\'s_Launcher'
#         name _ '@_@_data.json'.f.. P.. Q..
#         pa__ _ __.pa__.j.. _m_p.. 'data'
#         _json_file _ __.pa__.j.. pa__ n00
#
#         # Handle version specific reading/writing settings
#         d _ d_d.. l___ _g_s..
#         _settings_op _ d_d.. l___ ?
#         _?|'2.7' |'PyQt4' _ _g_s_27_pyqt4
#
#         # Setup GUI, then load settings, then display editmode properly
#         _setup
#         _load_settings
#         _edit_toggle
#
#     #======= SETUP UI =================================
#
#     ___ _setup
#         ''' Create tool GUI, set title, icon, remove
#         minimize / maximize buttons, resize and style.
#         '''
#         v_layout _ ?W...?VBL..
#
#         ?.aL.. _s_h..
#         ?.aL.. _s_e_o..
#         ?.aW.. _s_a..
#
#         _s_t_i..
#         _s_c..
#
#         sWT..('TPayne\'s Launcher ' + -v
#         sWI.. _t_i..
#         flag _ ?C...__.WCBH..
#         sWF.. ?C...__.W.. _ ?
#         r.. 190 200
#         sSS.. _S_M..
#
#     ___ _setup_header
#         ''' Create combobox for workspace and edit button '''
#         h_layout _ ?W...?HBL..
#         workspace_gb _ ?W...?GB.. 'Workspaces'
#         v_layout _ ?W...?VBL.. ?
#
#         _workspace_cb _ ?W...?CB
#         ?.v__.sDDM..
#             ?W...?AIV...DO..
#             )
#
#         _edit_btn _ ?W...?PB.. 'Edit'
#         _?.sMS..(?C...?S.. 40, 23
#         _?.setCheckable T..
#         _?.sSS.. _S_B..
#
#         v_l_.aW.. _w_c.
#         h_l_.aW.. w_g.
#         h_l_.aS..
#         h_l_.aW.. _e_b..
#         r_ h_l..
#
#     ___ _setup_edit_options
#         ''' Create add / delete buttons with menus
#         and overrides
#         '''
#         add_del_l _ ?W...?HBL..
#
#         _add_btn _ ?W...?PB.. 'Add'
#         _?.sMS.. ?C...?S.. 60, 23
#         add_menu _ ?W...?M..
#         ?.aA.. 'Workspace' _a_w..
#         ?.aA.. 'App or File' _a_a..
#         _a_b_.sM.. ?
#
#         _del_btn _ ?
#         _?.sT.. 'Delete'
#         _?.sAD.. T..
#         _?.sI.. _i__.i.. _i__.Tr..
#         _?.sIS.. ?C...?S.. 32, 32
#         _?.sF.. T..
#
#         a_d_l.aW.. _a_b..
#         a_d_l.aW.. _d_b..
#         r_ a_d_l
#
#     ___ _setup_apps
#         ''' Create apps list widget with drag/drop, and stuff'''
#         _app_lw _ ?W...?LW..
#         _?.sARC.. T..
#         _?.sDDM..
#             ?W...?AIV...IM..
#
#         r_ _a_l..
#
#     ___ _setup_tray_icon
#         ''' Create icon for system tray and actions menu '''
#         tray_icon _ ?W...?STI..
#         ?.sI.. _t_i..
#         ?.sTT.. 'Launches other apps!'
#
#         tray_menu _ ?W...?M..
#         ?.aA.. 'Open' s..
#         ?.aA.. 'YouTube' _t_l_.r_y..
#         ?.aS..
#         ?.aA..
#             ?W...?A__ 'Quit' ? triggered__c..
#
#         t_i_.sCM.. ?
#         t__i_.s..
#
#     ___ _setup_connections
#         ''' Create connections between combobox, apps,
#         edit to do stuff
#         '''
#         _w_c...cIC...c..
#             _w_ch..
#
#         _edit_btn.c___.c.. _e_t..
#         _w_c...v__.p__.c..
#             _d_w..
#             )
#         _a_l_.iP__.c.. _d_a..
#
#     #======= DISPLAY =================================
#
#     ___ _populate_workspaces
#         ''' Clear and Populate the workspace combobox,
#         disconnect and reconnect signal to avoid unintended refresh
#         of populate apps.
#         '''
#         _w_c...cIC...d..
#             _w_ch..
#
#         _w_c...c..
#         _w_c...aI.. _t_l__.g_w..
#         _w_c...cIC...c..
#             _w_ch..
#
#         _p_a..
#
#     ___ _populate_apps
#         ''' Clear and Populate the apps list widget,
#         set each application icon and name.
#         '''
#         _a_l_.c..
#         workspace _ g_w..
#         ___ app_name __ _t_l__.g_a_n.. ?
#             item _ ?W...?LWI.. _a_l_
#             icon _ _t_l__.g_t_a_i.. w.. a_n..
#             __ ?
#                 ?.sI.. ?G...?I.. ?
#             ____
#                 ?.sI.. _i__.i.. _i__.F..
#             i_.sT.. a_n..
#
#     ___ closeEvent  e
#         ''' Override Qt close event to instead hide tool '''
#         h..
#         e.i..
#
#     ___ _close
#         ''' Save settings and Quit tool'''
#         _save_settings
#         ?W...?A...i__.q..
#
#     #======= WORKSPACE + APP =================================
#
#     ___ get_workspace
#         ''' Returns the currently selection workspace from combobox. '''
#         r_ st. _w_c...cT..
#
#     ___ _w_ch..
#         _p_a..
#         _s_s.
#
#     ___ _run_app  item
#         i__.sS.. F..
#         _t_l__.r_a.. g_w.. st. ?.t..
#
#     #======= EDIT MODE =================================
#
#     ___ _edit_toggle
#         ''' Whenever button is clicked, set add/del button vis,
#         set drag drop and connect/disconnect run apps signal
#         '''
#         _edit_op|_e_b__.iC..
#         _a_l_.sDE.. _e_b_.iC..
#         _a_b_.sV.. _e_b_.iC..
#         _d_b.sV.. _e_b_.iC..
#         _s_s..
#
#     ___ _edit_on
#         _a_l_.iC__.d.. _r_a..
#         _e_b_.sT.. 'Done'
#
#     ___ _edit_off
#         _a_l_.iC__.c.. _r_a_
#         _e_b_.sT.. 'Edit'
#
#     #======= ADD =================================
#
#     ___ _add_workspace
#         ''' Prompt user with line edit input dialog for new name,
#         store if valid, populate, then select it.'''
#         t.. _ ?W...?ID...gT..
#
#             'New WORKSPACE',
#             'What would you like to title the new WORKSPACE?'
#              0
#         __ t..
#             _t_l__._a_w_ st. t..
#             _populate_workspaces
#             index _ _w_c...fT.. t..
#             _w_c...sCI.. ?
#             _s_s..
#
#     ___ _add_app
#         ''' Present user with instructions ONCE, then manditory
#         file dialog for app, optional dialog for icon,
#         store, populate, and save settings'''
#         __ _app_instruction
#             msg _ '1) Select the application file\n'
#             ? +_ '2) Select a app icon image (Optional)'
#             ?W...?MB...information , 'Add App' ?
#             _a_i.. _ F..
#         sel _ 'Select APP file'
#         app _ _f_d..|Q.. s.. _m_p..
#         __ ?
#             pa__ _ __.pa__.sp.. ? 0
#             msg _ 'Select ICON file (optional)'
#             icon _ _f_d..|Q.. ? pa__
#             _t_l__.a_a.. g_w.. a.. i..
#             _p_a..
#             _s_s..
#
#     ___ _file_dialog  msg pa__
#         ''' Default File dialog for Pyside, Pyside2, PyQt5 return file path
#         and filter for the dialog. Only need the path.'''
#         r_ ?W...?FD__.gOFN.. , m.. pa__ 0
#
#     ___ _file_dialog_pyqt4 msg pa__
#         ''' File dialog for PyQt4 only returns file path as QString,
#         must be converted to a string'''
#         fd _ ?W...?FD__.gOFN..  msg pa__
#         r_ st. ?
#
#     #======= DELETE =================================
#
#     ___ _dragging_workspace index
#         ''' When the user begins dragging a workspace,
#         store the index of the item being dragged and
#         note that it is a workspace.'''
#         ws _ st. _w_c...iT.. ?.r..
#         _dragging _ 'workspace' ?
#
#     ___ _dragging_app  item
#         ''' When the user begins dragging a application,
#         store the item text and note it's an app
#         '''
#         _dragging _ 'application', st. i__.t..
#
#     ___ _delete_app  app_name
#         _t_l__.d_a.. g_w.. a_n..
#         _p_a..
#
#     ___ _delete_workspace  ws_name
#         _t_l__.d_w.. ?
#         _p_w..
#
#     ___ delete_item
#         ''' Delete the item dragged onto Delete button '''
#         typ _ _dr.. 0
#         name _ _dr.. 1
#         title _ 'Delete @?'.f.. t..
#         msg _ 'Are you sure you want to delete @ "@"'.f.. t.. n..
#         no _ ?W...?MB...No
#         yes _ ?W...?MB...Yes
#         btn _ ?W...?MB...w.. t.. m.. y.. n.
#         __ ? __ y..
#             _d_o.|t.. n..
#             _s_s..
#
#     #======= SETTINGS =================================
#
#     ___ _save_settings
#         ''' Reorder the apps if necessary, then save the user settings
#         to QSettings, and store the tool data to json file.
#         '''
#         count _ _a_l_.c..
#         names _  _a_l_.i.. i .t.. ___ ? __ ra.. c..
#         workspace _ g_w..
#         _t_l__.r_a.. w.. n..
#         _s__.sV.. 'CurrentWorkspace' ?
#         _t_l__.w_j_f _j..
#         _s__.sV.. 'PosX', in. x
#         _s__.sV.. 'PosY', in. y
#
#     ___ _load_settings
#         ''' If there is a QSettings file and the json file exists,
#         read in the json file, then make selections based on the
#         qsettings.
#         '''
#         __ 'CurrentWorkspace' __ _s__.aK.. an. \
#               __.pa__.e.. _j..
#             x, y, cws _ _s___op|P.. |Q..
#             _t_l__.r_j_f.. _j..
#             _p_w..
#             index _ _w_c...fT.. cw..
#             _w_c...sCI.. ?
#             m.. x y
#         ____
#             _t_l__._a_w_ 'Default_WS'
#             _p_w..
#
#     ___ _get_settings
#         ''' Default get settings for x, y position for,
#         tool and current workspace
#         '''
#         x _ in. _s__.v.. 'PosX' #PyQt5 conversion
#         y _ in. _s__.v.. 'PosY'
#         cws _ st. _s__.v.. 'CurrentWorkspace'
#         r_ ? ? ?
#
#     ___ _get_settings_27_pyqt4
#         ''' This specific version of PyQt and python needed to be
#         handled differently. '''
#         x _ _s__.v.. 'PosX' .tI.. 0
#         y _ _s__.v.. 'PosY' .tI.. 0
#         cws _ st. _s__.v.. 'CurrentWorkspace'
#         r_ ? ? ?
#
#
# __ _____ __ ______
#     # for debugging
#     print P..
#     print Q
#     app _ ?W...?A..
#
#     # if os doesn't support Tray, quit
#     __ no. ?W...?STI__.iSTA..
#         ?W...?MB...c..
#             N..,'Error!'
#             'No system tray available for this system! Exiting...'
#
#         ___.e.. 1
#
#     # do not close if tool is hidden
#     ?W...?A...sQOLWC.. F..
#
#     # Create an instance of tool and run it
#     ex _ ?
#     ?.s..
#     ___.e.. ?.e
#
