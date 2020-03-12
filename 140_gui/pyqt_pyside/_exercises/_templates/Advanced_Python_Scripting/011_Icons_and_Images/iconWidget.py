# ____ __.__ ______ _
# ____ __._ ______ _
#
# ______ iW_UIs __ ui
# ____ i__.i.. ______ i..
#
# ______ __
# ______ ra..
# ______ ct..
#
# ____ i.. ______ i_r..  # potomy shto eto paket, nado importirovat' s pomochjy fom
#
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
#
# # vse pyti k ikonkam nahodjatsja v papke icons file icons
#
# c_ iconWidgetClass QM.. __.Ui_M..
#     ___ -
#         s___ ? ? . -
#         setupUi ?
#         # ui
#         sWI.. QI.. i..|*create  # klass Icons imeet neskol'ko konstryktorov
#         f_b_.sT.. ''
#         f_b_.sFS.. QS.. 40, 40
#         f_b_.sIS.. QS.. 32, 32
#         f_b_.sF.. 1
#         f_b_.sI.. QI.. i..|*create # icons from icons.py
#         f_b_.sI.. QI.. ':/create.png'  # icons from resource file (icons_rcs)
#
#         c_b_.sT.. ''
#         c_b_.sFS.. QS.. 40, 40
#         c_b_.sIS.. QS.. 32, 32
#         c_b_.sF.. 1
#         c_b_.sI.. QI.. i..['clear
#
#         fill_act.sI.. QI.. i..|*create
#         clear_act.sI.. QI.. i..|*clear
#         open_act.sI.. QI.. i..|*open
#         save_act.sI.. QI.. i..|*save
#         exit_act.sI.. QI.. i..|*close
#
#         pix = QPixmap i..['sphere']).sc.. 40, 40,
#                                               __.KAR..
#                                               __.STr..
#         i_l_.sP.. ?      # shto bu sozdat' Pixmap nado sozdat' exampljar klasa Pixmap i podat' tyda pyt'
#                                             # eto prosto label s nej nikak nel'zja vzaimodejstvovat'
#
#         l_l_.sVM.. QLV__.IM..           # nastrojka kak otobrazajytsja kartinki
#         l_l_.sIS.. QS.. 64, 64                # yvelichivaem razmer ikonok
#         l_l_.sRM.. QLW__.RM__.Ad..  # kartinki izmenjayt razmer kogda izmenjaetsja razmer vidgeta
#         l_l_.sDDM.. QAbIV__.NDD.. # otklychaet vozmoznost'  peremechat'  kartinki
#
#         # connects
#         f_b_.c___.c__ fL..
#         c_b_.c___.c__ cL..
#         f_a__.tr__.c__ fC..
#         c_a__.tr__.c__ cC..
#
#     ___ filList
#         path _ __.pa__.j.. __.pa__.d.. -f), *textures ) # polychaem polnuj pyt' k papke
#         cL.. )
#         ___ i __ __.l..d.. pa..                               # cherez list dir polychaem spisok fajlov
#             item _ QWI.. ?                              # sozdajotsja item i v teks k nemy kidaem imja faocherednogo fajla
#             ?.sI.. QI.. __.pa__.j.. p.. ?
#             l_l_.aI.. i..
#
#     ___ clearList
#         l_l_.cl..
#
#     ___ fillCombo
#         cC..
#         __ i __ ra.. 10
#             item _ QLWI.. 'Item @'  ?
#             # item.setIcon getRandomIcon ))
#             # item.setIcon((QI.. icons['item1'])))
#             c_c__.aI.. 'Item @'  ?
#             c__c__.sII.. ? gRI..   # 1uj argyment eto index itema a 2oj ikonka
#                                                                  # 1uj index mozno ykazuvat' tol'ko posle togo kak element s etim indexom bul sozdan
#
#     ___ clearCombo
#         c_c__.c..
#
#     ___ getRandomIcon
#         r_ QI.. i___|ra__.ch.. |'item1', 'item2', 'item3'
#         # return QI..(icons[random.choice(['item1', 'item2', 'item3'])])
#
#
# __ ______ __ ______
#     app _ ?
#     w _ ?
#     ?.s..
#     ?.e..
