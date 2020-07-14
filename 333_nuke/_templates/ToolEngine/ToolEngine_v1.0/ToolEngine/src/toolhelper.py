# ########################################################################################################################
# #
# # helper module
# # this module provides important functionality for the main module
# #
# ########################################################################################################################
#
#
# ______ __
# ______ j___
# ______ ?
# ______ c..
#
#
# ___ reload_tools_menu notify_T..
#     """
#     advanced load_tools function
#     reload tools directory and scan for new toolsets
#     If something is found display a message
#     @param notify: Bool if True show message when found new tool
#     :return: None
#     """
#
#     # save existing tools in list
#     all_tools_before _ g..
#
#     # reload tools dir
#     l..
#
#     # save tools in list after scanning
#     all_tools_after _ g..
#
#     # check for difference
#     dif_list _ tool ___ ? __ a.. __ ? no. __ a..
#     dif_msg _ "@".j.. ?
#
#     # show message of new tools
#     __ notify an. dif_msg !_ "":
#         ?.m..("@ new tools found:@@@".f.. le. ? ?
#
#
# ___ get_all_tools
#     """
#     scan tools dir and get a list of all tools
#     assert that all tools menus are uppercase
#     :return: list list of all tools
#     """
#
#     all_tools _ || list
#
#     ___ item __ ?.m.. "Nodes" .fI.. "ToolEngine" .i..
#         # check only for tools menus which are uppercase
#         __ ?.n.. .isu..
#
#             # iterate through each tool menu and save all its tools
#             tool_menu _ ?... "Nodes" .fI.. "@/@".f.. "ToolEngine" ?.n..
#             ___
#                 ___ tool __ ?.i..
#                     a_t_.ap..("@/@".f.. ?.n.. ?.n..
#             ______
#                 c___
#
#     r_ ?
#
#
# ___ load_tools no.._F..
#     """
#     load tools from tools root directory
#     :return: None
#     """
#
#     settings _ load_settings
#     build_tools_menu ? "tools_root"
#
#
# ___ load_settings
#     """
#     load settings file and return values
#     if settings file / folder doesn't exist then create it
#     :return: dict settings_data
#     """
#
#     # settings file
#     settings_file _ c__.P..
#
#     # make sure the settings directory exists
#     __ no. __.pa__.isd.. __.pa__.d_n_ ?
#         __.m_d_ __.pa__.d_n_ ?
#
#     # if the settings file doesn't exist then create it
#     __ no. __.pa__.isf.. ?
#         w__ o.. ? _ __ f
#             ?.w.. '{"tools_root": ""}'
#
#     # load the settings file
#     w__ o.. ? _ __ f
#         settings_data _ j___.l.. ?
#
#     r_ ?
#
#
# ___ get_tools_categories tools_root
#     """
#     get a list of all tool categories
#     scan the tools_root for dirs and skip tool categories that mustn't
#     be loaded regarding to the config's TOOLSDIR_IGNORE and TOOLS_TEMP values
#     :param tools_root: String full path of tools root
#     :return: list list of all categories
#     """
#
#     __ no. __.pa__.isd.. ?
#         r_ # list
#
#     tools_categories _ # list
#
#     ___ item __ __.l_d_ ?
#         item_full_path _ __.pa__.j.. ? ?
#         __ __.pa__.isd.. ? an. item !_ c__.T.. an. i.. no. __ c__.T..
#             ?.ap.. i..
#
#     r_ ?
#
#
# ___ build_tools_menu tools_root
#     """
#     scan tools_dir and dynamically build tools structure
#     :param tools_root: String full path of tools root
#     :return: None
#     """
#
#     __ no. __.pa__.isd..
#         __ ? __ ""
#             print "ToolEngine: tools_root not set. You can set it via 'ToolEngine->settings'"
#         ____
#             print "ToolEngine: tools_root '@' doesn't exist".f.. ?
#
#     te_menu _ ?.m.. "Nodes" .fI.. "ToolEngine"
#
#     # scan for tools dirs
#     tool_categories _ g_t_c.. ?
#     ___ category __ ?
#
#         category_menu _ te_.aM.. ?.u..
#
#         # create toolsets
#         item_full_path _ __.pa__.j.. t_r.. c..
#         ___ tool __ __.l_d_ ?
#
#             __ __.pa__.s_t_ ? 1 __ ".nk"
#                 toolset_path _ __.pa__.j.. ? ?
#                 c_m_.aC.. t__.r.. ".nk" ""  l___ toolset_path_toolset_path i_t.. t_p.. de.._F.. ic.._""
#
#     # temp tools
#     t_m_.aS..
#     temp_menu _ t_m_.aM.. c__.T__.u..
#
#     # create temp toolsets
#     temp_dir _ __.pa__.j.. t_r.. c__.T..
#     __ no. __.pa__.isd.. ?
#         __.m_d_ ?
#
#     ___ tool __ __.l_d_ ?
#         __ __.pa__.s_t_ ? 1 __ ".nk"
#             toolset_path _ __.pa__.j.. t_r.. c__.T.. ?
#             t_m_.aC.. __.pa__.s_t_ ? 0 l___ toolset_path_toolset_path i_t.. ? delete_T..
#
#
# ___ insert_toolset toolpath delete_F..
#     """
#     insert toolset
#     if it is a temp tool then the delete flag is set to True thus it will be removed after inserting
#     :param path: String full path of toolset
#     :param delete: if True delete the toolset after importing; default: False
#     :return: None
#     """
#
#     __ no. __.pa__.isf.. ?
#         ?.m.. "The tool cannot be found"
#         r_
#
#     ?.nP.. ?
#
#     __ delete
#         # physically delete the toolset
#         __.re.. ?
#
#         # remove command from menu bar
#         toolset_name _ __.pa__.s_t_ __.pa__.b_n_ ? 0
#         ?.m.. *Nodes* .fI.. *@/@*.f.. *ToolEngine* c__.T__.u.. .rI.. t_n..
#
#
#
