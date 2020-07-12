# # Esli mu vstavljaem widget v nodu s pompocjiy PyQt, to on ne ostavljaet nikakih sledov na samoj node
# # To est'  nam ne nyzno sozdavat' knob, mu prosto sozdajom widget i vstavljaem ego v imejychijsja interfais
# # Esli vu sozdajote knob  Tab to pri pereotkrutii Nuke etot knob"Tab" tak ze bydet nahoditsja na node, no esli vu delaete eto skriptom
# # To esli vash skript ne zagryzen to vasha taba prosto ne bydyt pojavitsja
# # Nachat' nado s polychenija widgeta okna ili nodu kak QT  objekta. Y lybogo okna, lyboj nodu on prisytstvyet i on ravnjaetsja imeni etoj nodu
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# ___ getMainWindow
#     app _ ?A...ins..
#     ___ widget __ ?.tLW..
#         __ ?.mO.. .cN.. __ 'F..||U.||DMW..'
#             r_ ?
#
# qnuke _ ?
# ?.fC.. ?W.., 'Transform1'
#
# #####################################################################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# ___ getMainWindow
#     app _ ?A...ins..
#     ___ widget __ ?.tLW..
#         __ ?.mO.. .cN.. __ 'F..||U.||DMW..'
#             r_ ?
#
# qnuke _ ?
# w _ ?.fC.. ?W.. 'Transform1'
# ?.sQT.. 'Transform11'
#
#
# #####################################################################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# ___ getMainWindow
#     app _ ?A...ins..
#     ___ widget __ ?.tLW..
#         __ ?.mO.. .cN.. __ 'F..||U.||DMW..'
#             r_ ?
#
# qnuke _ getMainWindow
# w _ ?.fC.. ?W.. 'Transform1'
# ?.sQT.. 'Transform11'
# t _ ?.fC.. ?TW..
# ?.co..
# nw _ ?W..
# ly _ ?VB..
# ?.sL.. ?
# ___ i __ ra.. 5
#     ly.aW.. ?PB..
# t.aT.. n. 'My Tab'
# c _ ?CW..
# ?.iT.. 0, c, 'Calendar'
# ?.sCI.. 0