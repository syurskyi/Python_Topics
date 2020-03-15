# ____ ?.? _____ _
# ____ ?.? _____ _
#
# # Kogda prilozenie zapyskaetsja to ono vstraivaetsja v EventLoop, to est' cykl sobutij. Eto beskonechnuj cikl sobutij
# # kotorue proishodjat y nas na kompjytere ili y nas v operacionnoj sisteme
# # Kogda srabatuvaet signal on vuzuvaet slot.
# # Slotov mozet but' neskol'ko na odnom signale a takze signal mozet vuzuvat' neskol'ko slotov.
# # KOgda rabotaet prilozenie, postojanno generiryjytsja kakieto signalu, bydto sozdanue pol'zovatelem
# # ili operacionoj sistemoj. Etim signalam sootvestvyjyt opredeljonue slotu, slotu eto fynkcii, kotorue bydyt
# # vuzuvatsja kogda signal srabotaet
#
# c_ myWidget QW..
#     ___ - ____
#         s.. ? ____ . -
#         layout _ QVBL.. ?
#         button _ QPB.. *Print
#         l__.aW.. ?
#         line _ QLE..
#         l__.aW.. ?
#         l__.tC__.co.. ?.t..
#         # first version
#         # b___.cl__.co.. ?.a..
#         # second version
#         # ?.co.. b.. S.. 'cl.. ' ? S.. 'ac.. '
#         # third version
#         # Zapis cheres dekorator rabotaet tochno takze kak pervuj variant, potomyshto decorator eto funkcija,
#         # kotoraja polychaet v vide argumenta drygyjy fynkcijy. V pervom variante mu peredajom  prosto funcijy,
#         # na kotoryjy bydet zakonekchen eto signal a v slychae s dekoratorom ja mogy proizvesti
#         # echjo kakie to dejstvija.
#         #
#
#         ?b__.cl__.c..
#         ___ click
#             a..
#
#     # @SLOT()
#     ___ action
#         print 'ACTION'
#
#     ___ text arg
#         print ?
#
#
# app = QA..
# window = ?
# ?.s..
# ?.e..
