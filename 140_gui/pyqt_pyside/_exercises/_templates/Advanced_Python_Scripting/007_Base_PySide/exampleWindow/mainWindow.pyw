# ____ ?.? ____ _
# ____ ?.? ____ _

#
# ____ window_UIs
#
# # v perekompilirovanom fajle window_Uis y nas est' fynkcija setupUi, kotoraj polychaet v vide argymenta nekij objekt,
# # v dannom slychae 'example' i potom k nemy prikleivaet vse nashi widgetu ili otpravljet ego kak parent
# # example.setObjectName("example")
# # self.verticalLayout_2 = QtGui.QVBoxLayout(example) - otpravljet kak parent
# # eto znachit nam nado vuzvat' fynkcijy setupUi i peredat' nyznuj widget v kachestve argymenta.
# # potomy shto mu nasledyemsja ot klas Ui_example i teper' vse metodu etogo klassa javljaytsja metodami etogo klassa.
# # ochen' vazno connektit' knopky posle vuzova fynkcii setupUi, potomyshto do etogo etoj knopki ne sychestvyet
#
# c_ exampleWindowClass QW.. ?.Ui_ex..
#     ___ -
#         s.. ? ?. -
#         sU.?
#         sWT.. *ITEM LIST
#         co.. _ 1                                 # shobu dobavit nymeracijy. Zavodim atribyt klassa
#         a_b__.cl__.co.. ____.aI..
#         n_l_.rP___.co.. ____.aI.. # signal vuzuvaetsja kogda nazimaetsja Enter
#
#     ___ addItem
#         text _ n_l_.t..    # vo pervuh nado polychit test s lineedit. On vozvrachaet nam tekst s lineedit
#         # print text, type(text)
#         __ t..                                   # esli teks est' on ne pystoj,
#             # lb _ QLabel(text)
#             lb _ QL.. '@: @'  c.. t..  # mu sozdajom novuj label
#             i_l_.aW.. ?                # dobavljaem v svoj layout novuj vidget
#             co.. +_ 1
#
# __ _______ __ _____
#     app _ QA..
#     w _ ?
#     ?.s..
#     ?.e..
