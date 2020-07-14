# ########################################################################################################################
# #
# # ToolEngine main module
# # this main module provides functions to create the main panels
# #
# ########################################################################################################################
#
#
# ______ ?
# ______ j___
# ______ __
#
# ______ t__h..
# ______ c..
#
#
# ___ show_settings
#     """
#     show settings window
#     :return: None
#     """
#
#     settings _ t_h_.l_s..
#
#     # create settings panel
#     p _ ?.P.. *ToolEngine settings
#     ?.sW.. 600
#     ?.aFS.. *tools root:  ? *tools_root
#
#     __ ?.s__
#
#         ? *tools_root _ ?.v.. *tools root
#
#         w__ o.. c__.P.. _ __ sf
#             j___.d.. s.. ?
#
#         # load toolsets
#         t_h_.r_t_m.. no.._F..
#
#
# ___ show_info
#     """
#     show settings window
#     :return: None
#     """
#
#     info_file _ __.p__.n.. __.p__.j.. __.p__.d.. -f *../ *data *info.json
#
#     __ no. __.p__.i_f.. ?
#         print "ToolEngine: info file doesn't exist"
#         r_
#
#     w__ o.. ? __ f
#         info_data _ j___.l.. ?
#
#     logo _ __.p__.n_p_b__.p__.j.. __.p__.d..   -f *../ *img *logo.png
#     ?.m.. *<img src_*@* style_*float: right;* /><h1>ToolEngine v@</h1>\n\n@ .f.. l.. i_d.. *version i_d.. *info
#
#
# ___ add_toolset
#     """
#     create new toolset by selected nodes
#     :return: None
#     """
#
#     sel _ ?.sN..
#
#     # return if nothing is selected
#     __ le. ? __ 0
#         ?.m.. *Please select some nodes to proceed.
#         r_
#
#     # create add panel
#     p _ ?.P.. *Add toolset
#     ?.sW.. 400
#     ?.aSLI.. *Name:  ""
#     category_default _ *---please_choose---
#     categories _ t_h_.g_t_c... t_h_.l_s.. *tools_root
#     ?.i.. 0 c_d..
#     ?.ap.. c__T___T__.u..
#     ?.aEP.. *Category: ", " ".j.. ?
#
#     __ ?.s__
#         __ ?.v.. *Name:  !_ ""
#             __ ?.v.. *Category:  !_ c_d..
#                 toolset_full_path _ __.p__.j.. t_h_.l.._s.. *tools_root ?.v.. *Category:  *@.nk .f.. ?.v.. *Name:
#
#                 # if toolset already exists ask for overwriting
#                 __ __.p__.i_f.. t_f_p..
#                     __ no. ?.a.. *The toolset *@* already exists. Do you want to overwrite it? .f.. t_f_p..
#                         r_
#
#                 # write toolset
#                 ?.nC.. t_f_p..
#                 ?.m.. *Succeessfully added toolset *@/@ .f.. ?.v.. *Category:  ?.v.. *Name:
#                 t_h_.r_t_m.. no.._F..
#
#             ____
#                 ?.m.. *Please choose a category
#         ____
#             ?.m.. *Please enter a toolset name