# ____ __.__ ______ _
# ____ __.__ ______ _
#
# # ne vsegda menjy buvaet statichnoe. Sostav menju zavisit ot kakih to yslovij. Poetomy chasto menu prohoditsja generirovat'
# # v moment sozdanija
#
# c_ MainWindowClass QMa..
#     ___ -
#         s___ ?  ? -
#         # widget
#         widget _ QW.. ?
#         sCW.. ?
#         # menu bar
#         menu_bar _ QM..
#         sMB.. ?
#         # menu
#         menu _ QM.. File
#         ?.sTOE.. 1                                    # dobavljaet v menu  divide line pri nazatii na kototyjy mozno otsoedinit' menu i ono stanet otdel;num vidgetpm
#         m_b_.aM.. ?
#         # actions first version
#         act1 _ QAc.. Open ?    # objazatel'no ykazuvat' parent
#         ?.sC.. 1
#         ?.tr__.c.. a..
#         m__.aA.. ?
#
#         # actions second version                                            # raznica mezdy pervum i vtorum sposobom
#                                                                             # mu ne imeem prjmogo dostypa neposredstvenno k action (act1)
#                                                                             # potomy shto vo vtorom variante on sozdajotsja dinamicheski
#                                                                             # i y nas net peremennoj, kotoraja ssulaetsja na etot objekt
#
#         m___.aA.. QAc.. Save ? t_a..
#         # menu.actions()[1]
#
#         # submenu
#         sMenu _ QMe.. Sub
#         m___.aM.. ?
#
#         ___ i __ ra.. 10
#             sM__.aA.. QAc.. 'Item @'  ? ?
#
#     ___ action
#         __ _1.iCh..
#             print 'ACTION'
#         ____
#             print 'STOP'
#
# __ ______ __ ______
#     app _ ?
#     w _ ?
#     ?.s..
#     ?.e..