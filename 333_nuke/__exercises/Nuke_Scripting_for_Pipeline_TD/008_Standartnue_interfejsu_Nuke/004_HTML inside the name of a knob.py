# ______ __
# node _ ?.sN__
#
# ? i.. sV..('C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png')
# k _ ?.T_K.. tutor  Tutorial
# ?.aK.. ?
# ? "tutor" .sL.. '<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>'
#
# #######################
# h _ ?.D_K..('sue', '')
# ?.sL.. '<h2>H </h2><img src="@/icons/hue.png">'  __.e.. N.._P.. .r.. '\\','/'
# ?.aK.. ?
#
# s _ ?.D_K.. 'sat', ''
# ?.sL.. '<h2>S </h2><img src="@/icons/saturation.png">'  __.en__ N_P.. .r.. '\\','/'
# ?.aK.. ?
#
# v _ ?.D_K.. 'val', ''
# ?.sL.. '<h2>V </h2><img src="@/icons/lightness.png">'  __.en__ N_P.. .r.. '\\','/'
# ?.aK.. ?
#
#
# #######################
# ?.aK.. ?.T_K.. '',''
# #######################
#
# ###### node icon
# ? i.. .sV.. 'C:/pipeline/icons/cgninjas_node.png'
#
# ###### Label HTML
# # link
#
# k _ ?.T_K.. 'tutor', 'Tutorial'
# ?.aK.. ?
# ?.sL.. '<h4><a style="color:lightgray;" href="http://cgninjas.ru">CGNINJAS<a></h4>'
#
# ###########################
# # image label
#
# h _ ?.D_K.. 'sue', ''
# h.sL..('<h2>H </h2><img src="@/icons/h.png">'  __.en__ N_P.. .r.. '\\','/'
# ?.aK..(h)
#
# s _ ?.D_K.. 'sat', ''
# ?.sL.. '<h2>S </h2><img src="@/icons/s.png">'  __.en__ N_P.. .r.. '\\','/'
# ?.aK.. ?
#
# v _ ?.D_K.. 'val', ''
# ?.sL..('<h2>V </h2><img src="@/icons/v.png">'  __.en__ N_P.. .r.. '\\','/'
# ?.aK.. ?
#
# ########################
# ?.aK.. ?.T_K.. '',''
# ##########################
#
# # interactive label
#
# power _ ?.D_K.. 'power', 'Power'
# ?.aK.. ?
#
# ___ powerKnob a
#     k _ ?.tK..
#     __ ?.n.. __ 'power' an. a__'Blur'
#         v _ ?.gV..
#         img _ in. ?*5)+1
#         ?.sL.. '<img src="@/icons/power@.png">'  __.en__ N_P.. .r.. '\\','/' ?
#
# ?.aKC.. ? 'Blur'
# ?.rKC.. ? 'Blur'
#
# ########################################################################################################################
#
# set cut_paste_input [stack 0]
# version 10.0 v4
# push $cut_paste_input
# Blur {
#  channels rgba
#  name Blur1
#  label "---------------\n\[value size]"
#  selected true
#  xpos 219
#  ypos -135
#  icon "C:/Users/serge/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/004_Pipeline/icons/cgninjas.png"
#  addUserKnob {20 User}
#  addUserKnob {26 tutor l "<h4><a style=\"color:lightgray;\" href=\"http://cgninjas.ru\">CGNINJAS<a></h4>"}
#  addUserKnob {7 hue l "<h2>H </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/hue.png\">"}
#  addUserKnob {7 sat l "<h2>S </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/saturation.png\">"}
#  addUserKnob {7 val l "<h2>V </h2><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/lightness.png\">"}
#  addUserKnob {26 "" +ST..}
#  addUserKnob {7 power l "<h3>POWER</h3><img src=\"C:/Users/syurskyi/Dropbox/nuke/.nuke/example/NUKE/Nuke Scripting for Pipeline TD/008_Standartnue_interfejsu_Nuke/icons/power/power6.png\">"}
#  power 1
# }
