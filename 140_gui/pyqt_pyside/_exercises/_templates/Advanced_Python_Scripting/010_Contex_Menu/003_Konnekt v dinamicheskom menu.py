# ____ __.__ ______ _
# ____ __.__ ______ _
#
# c_ MainWindowClass QMa..
#     ___ -
#         s___ ?  ?. -
#         # widget
#         widget _ QW.. ?
#         sCW.. ?
#         # menu bar
#         menu_bar _ QMB..
#         sMB.. ?
#         # menu
#         menu _ QMe.. File
#         ?.sTOE.. 1
#         m_b__.aM.. ?
#         # actions
#         act1 _ QAc... Open ?
#         ?.sCh.. 1
#         ?.tr__.c.. a..
#         m__.aA.. _1
#
#         m__.aAc.. QAc.. Save ? t_a..
#         # menu.actions()[1]
#
#         # submenu
#         sMenu _ QM.. Sub
#         m__.aM.. ?
#
#         for i __ ra.. 10
#             # sMenu.addAction(QAction('Item %s' % i, self, triggered_action)) # mu ne mozem zapisat' acrion(i)
#                                                                                       # potomy shto eto bydet vuzov fynkcii a ne connect na imja funkcii
#                                                                                       # poetomy zdes' nyzno ispol'zovat' lambda
#
#             # sMenu.addAction(QAction('Item %s' % i, self,
#             #                              triggered_lambda: action(i))) # v etoj versii mu vsegda bydem polychat' 9
#                                                                             # eto proishodit potomyshto v processe cukla kazdaja lambda
#                                                                             # connectjas' na 'i', konektitsja na odno i toze znachenie
#                                                                             # 'i' iteriryetsja, nabiraja kazduj raz edinicy i pod konec cykla, stanovitsja ravno 9
#                                                                             # I vse lambda fyhkcii shto y nas sozdalis', oni zakonektenu y nas na odno i toze znachenie
#                                                                             #
#             ?.aA.. QAc.. 'Item @'  ? ?
#                                          triggered _ l____ x _ i a... ?
#                                                                             # x_i, mu zastovljaem lambda prinimat' argyment, no pri etom triggered nam ego ne otpravljaet
#                                                                             # i mu pishem znachenie po ymolchanijy x_i, kotoroe ravno nashemy i, to est' nomery iteracii
#                                                                             # i v nytri mu ispol'zyem etot x
#                                                                             # KAzduj raz vnytri lambda fynkcii sozdajotsja x, kotoruj javljaetsja lokal'noj peremenoj dlja etoj fynkcuu
#                                                                             # i on yze ne izmenjaetsja, prosto znachenie dlja etogo x berjotsja  is peremennoj 'i', kotoraja
#                                                                             # v konkretnoj iteracii ravna konkretnomy znachenijy
#
#     ___ action i
#         print ?
#
#
# __ ______ __ ______
#     app _ ?
#     w _ ?
#     ?.s..
#     ?.e..