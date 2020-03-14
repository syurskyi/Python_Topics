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
#     ___ - ____
#         s.. ? ____ . -
#         ____.sU. ____
#         ____.sWT..('ITEM LIST')
#         ____.co.. _ 1                                 # shobu dobavit nymeracijy. Zavodim atribyt klassa
#         ____.a_b__.cl__.co.. ____.aI..
#         ____.name_le.returnPressed.co.. ____.aI.. # signal vuzuvaetsja kogda nazimaetsja Enter
#
#     ___ addItem ____
#         text = ____.n_l_.t..    # vo pervuh nado polychit test s lineedit. On vozvrachaet nam tekst s lineedit
#         # print text, type(text)
#         __ t..                                   # esli teks est' on ne pystoj,
#             # lb = QLabel(text)
#             lb = QL.. '@: @'  ____.c.. t..  # mu sozdajom novuj label
#             ____.i_l_.aW.. ?                # dobavljaem v svoj layout novuj vidget
#             ____.co.. +_ 1
#
# __ _______ __ _____
#     app = QA..
#     w = ?
#     ?.s..
#     ?.e..
