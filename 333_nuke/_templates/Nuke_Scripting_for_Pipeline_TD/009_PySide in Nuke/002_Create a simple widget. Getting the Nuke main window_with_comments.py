# """
# Nyzno polychit' tekychee aktivnoe okno Nuke, dlja togo shto bu ispol'zovat' ego kak parent dlja widgeta
# """
#
# ##### Extrimely nessacery to know how to found out what classes and function has class #######
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# qnuke _ ?A...aW..
# w _ ?W..
# ?.s__
#
# print qnuke
# ############################################################################################################
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# qnuke _ ?A...aW..
# w _ ?W.. ?
# ?.s__
#
# """
# nichego ne proishodit. Na samom dele widget otkrulsja. No tak kak on preparencen k aktivnomy okny to on pojavilsja vnytri etogo okna.
# No tak kak tam nichego nety on nahoditsja gde to vnytri etogo okna kak prozrachnuj prjamoygol'nik
# """
# ############################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# qnuke _ ?A...aW..
# w _ ?W.. ? __.T..
# ?.s__
#
# """
# Takoj poisk parenta on ne sovsem odnoznachnuj
# """
#
# ############################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# qnuke _ ?A...aW..
# w _ ?W.. ? __.T..
# ?.s__
#
# ___ active
#     print ?A...aW..
#
# ?T...sS.. 2000 ?
#
# """
# Pochemy to ne rabotaet na rabote. Posmotret' doma.
# Polychenie parenta takim obrazomsrabotaet tol'ko esli y nas Nuke aktiven. Esli Nuke ne aktiven, to parenta y nas ne bydet a znachit widget prosto ne priparentitsja
# Esli okno otkruvaetsja ne pol'zovatelem cherez menjy, a skazem po kakomy to sobutijy ili cherz vremja i v etot moment Nuke bydet ne aktiven,
# to mu ne polychim glavnogo okna Nuke
# """
#
# ############################################################################################################
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# app _ ?A...ins.. # vozvrachaet tekychee aktivnoe prilozenie
# # app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne
#
# ___ w __ app.tLW..
#     print ?.wT..
# ############################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# app _ ?A...ins.. # vozvrachaet tekychee aktivnoe prilozenie
# # app.topLevelWidgets() # mu polychaem spisok vseh widzetov. kotorue est'  na samom verhnem yrovne
#
# ___ w __ assert.tLW..
#     print ?.mO.. .cN.. # method metaObject vernjot specialnuj klass s informaciej ob objekte. Y etogo klassa est' edinstvenuj method vozvrachajychij stroky
#
# """
# Like exersice made that print only Foundry classes
# """
#
#
# ############################################################################################################
#
# """
# Kogda sozdajy novuj widget, ja pomechajy fynkcijy getNukeWindow(), kotoraja vernjot mne glavnoe okno v lybom slychae
#
# """
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# ___ getNukeWindow
#     app _ ?A...ins..
#
#     ___ w __ app.tLW..
#         __ ?.mO.. .cN.. __ 'F...||U.||DMW..'
#             r_ w
#
# qnuke _ g..
# ?.sQT.. Nuke
#
# ############################################################################################################
#
# w _ ?W.. ? __.T..
# ?.s__
# ############################################################################################################
#
# ____ ?.?C.. ______ _
# ____ ?.?G.. ______ _
#
# ___ getNukeWindow
#     app _ ?A...ins..
#
#     ___ w __ ?.tLW..
#         __ ?.mO.. .cN.. __ 'F..||U.||DMW..'
#             r_ w
#
# qnuke _ g..
# ?.sQT.. Nuke
#
# w _ ?W..(g.. __.T..
# ?.sWF.. ?C...__.W.. |
#                       ?C...__.FWH..
# ?.s__
# ?.c__