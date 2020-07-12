# # Na samoj node nigde nezapisana informacija, shto nyzno dobavljat' vkladki
# # Kak nam sdelat'  ak shto bu vsjo vostanavlivalos' pri otkrutii nodu
# # Delaetsja eto opjat' ze s pomochjy PySide, s pomochjy sredstv etogo Framework
# # v teorii vugljadit sledyjychim obrazom, vsjakij raz, kogda v Nuke otkruvaetsja novoe okno mu dolznu proverit'
# # javljaetsja eto okno interfejsom nodu i esli da,  vjzat'  ego i obrabotat'  kak trebyetsja,
# # to est'  dobavit' nyznue elementu interfejsa
# # Dlja realizacii nam potrebyetsja specialnuj fynkcional QT framework, kotoruj nazuvaetsja eventFilter.
# # v prilozenii vsegda proishodja kakie to eventu i otkrutie okna eto odin iz etih eventov
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# c_ eventFilterClass ?O..
#     ___ eventFilter  obj ev
#         print e_.ty..
#         r_ F..
#
# f _ ?
# qn__.iEF.. ?
# qn__.rEF.. ?
#
# # ne rabotaet na rabote, proverit'  doma
#
# ########################################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# c_ eventFilterClass ?O..
#     ___ eventFilter obj ev
#         __ e_.ty.. __ ?E__.CP..
#             w _ e_.ch..
#             ?.sQT.. 'NUKE
#         r_ F..
#
# f _ ?
# ?.iEF.. ?
# ?.rEF.. ?