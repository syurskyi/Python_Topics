# ## Default Nuke pipelinefunctions
#
# ______ ?
# ______ __
#
#
# ___ nkPath
#     nkPath _ __.pa__.d_n_(?.r.. .n..
#     nkPath _ __.pa__.n_p_  ?
#     r_ ?
#
#
# ___ nkScriptName
#     nkScriptName _ __.pa__.b_n_(?.r.. .n..
#     r_ ?
#
#
# ___ showPath
#     showPath _ __.pa__.s_d_ nP.. 1
#     r_ ?
#
#
# ___ show
#     ___
#         nkPath _ __.pa__.d_n_ ?.r.. .n..
#         nkPath _ __.pa__.n_p_ ?
#         showPath _ __.pa__.s_d_ ?
#         show _ ? 1
#         show _ st..s.. ? "\\" 1
#         r_ ?
#     ______
#         print "Error: show not found in nkPath..."
#
#
# ___ sequence
#     ___
#         nkScriptName _ __.pa__.b_n_ ?.r.. .n..
#         sequence _ st..s.. ? "_" 0
#         r_ ?
#     ______
#         print "Error: sequence not found in nk script name..."
#
#
# ___ shot
#     ___
#         nkScriptName _ __.pa__.b_n_ ?.r.. .n..
#         shot _ st..s.. ? "_" 1
#         r_ ?
#     ______
#         print "Error: shot not found in nk script name..."
#
#
# ___ assetName
#     ___
#         scriptInfo _ __.pa__.b_n_ ?.r.. .n..
#         scriptInfo _ st..s.. ? "_"
#         assetName _ ? 2
#         r_ ?
#     ______
#         print "Error: couldn't find assetName in nk script name..."
#
#
# ___ taskName
#     ___
#         scriptInfo _ __.pa__.b_n_ ?.r.. .n..
#         scriptInfo _ st..s.. ? "_"
#         taskName _ ? 3
#         r_ ?
#     ______
#         print "Error: taskName not found in nk script name..."
#
#
# ___ nkScriptVersion
#     ___
#         nkScriptVersion _ ?.r.. .n..
#         nkScriptVersion _ st..s.. ? "_"
#         nkScriptVersion _ ? -1
#         nkScriptVersion _ st..s.. ? "."
#         nkScriptVersion _ ? 0
#         r_ ?
#     ______:
#         print "Error: nkScriptVersion not found in nk script name..."