# ____ PySide ______ ?C.., ?G__
#
#
# c_ MyLabel ?G__.?L..
#     ___ -  text parent_N..
#         ?G__.?L...-  ? ?
#         sA.. ?C...__.AC.
#
#     ___ mousePressEvent  e
#         name _ n__.sN__ .k.. *n.. .gV..
#         __ e.b..  & ?C...__.LB..
#             print("Нажата левая кнопка мыши")
#         __ e.b..  & ?C...__.RB..
#             print("Нажата правая кнопка мыши")
#         __ e.b..  & ?C...__.MB..
#             print("Нажата средняя кнопка мыши")
#         __ (e.b..  & ?C...__.LB.. and
#                     e.b..  & ?C...__.RB..
#             print("Левая и правая кнопки нажаты")
#         sT..('Name of the Selected node is: ' + st. n..
#
#
# c_ MyWindow ?G__.W..
#     ___ - (self, parent=N..
#         ?G__.W...-  parent
#         sWT__("Name Window")
#
#         resize(300, 150)
#         label _ MyLabel("Click here with the mouse")
#         label.setFrameStyle(?G__.QFrame.Box | ?G__.QFrame.Plain)
#         vbox _ ?G__.?VB..
#         vbox.aW..(label)
#         sL..(vbox)
#
#
# ___ main :
#     global c
#     c _ MyWindow
#     c.raise_
#     c.show
#
# main
#
