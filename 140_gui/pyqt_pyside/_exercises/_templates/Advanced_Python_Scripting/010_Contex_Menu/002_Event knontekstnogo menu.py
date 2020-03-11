# ____ __.__ ______ _
# ____ __.__ ______ _
#
# textArray _ 'Click', 'Press', 'Enter'
#
#
# c_ WidgetMenuClass QW..
#     ___ -
#         s____ ?  ?. -
#         ly _ QVBL.. ?
#        btn _ QPB.. *Cl..
#         ?.aW.. ?
#        line _ QE..
#         l_.aW.. ?
#
#        ?.sCMP.. __.CCM..       # shto bu contekstnoe menu pojavilos', nado etoj knopke skazat' shto bu ona reagirovala na etot signal
#        ?.cCMR__.c.. o.. # etot signal generitsja kogda mu zaprashuvaem
#                                                                    #  konteksnoe menu a eto y nas nazatie pravoj knopkoj mushi
#
#     ___ openMenu pos
#         pos _b__.mTG.. ?                        # y lybogo widgeta est' metodu kotorue delajyt remap koordinat
#         menu _ QM..                                           # esli net pozicii gde bul proizvedjon klik mozno ykazat' koordinatu kyrsora
#
#         ___ i __ tA..
#             m__.aA.. QA.. ? ?
#         # menu.exec_(pos)                                         # lokalnue koordinatu klika na preobrazovat' v global'nue koordinatu ekrana
#         a _ m__.ex.._ QCu...p..                         # funkcija obrachaetsja k tekychemy kyrsory i vozvrachaet ego global'nue koordinatu
#         # print a                                                 # menu.exec_ vozvrachaet nam action, kotoruj bul vubran i mu mozem ego zabrat'
#         # print a.text()
#         __ a
#            b__.sT.. ?.t..
#
#
# __ ______ __ ______
#     app _ ?
#     w _ ?
#     ?.s..
#     ?.e..