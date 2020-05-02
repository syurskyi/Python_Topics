# ____ PySide ______ ?C.., ?G__
#
#
# c_ MyLabel ?G__.?L..
#     ___ -  text parent_N..
#         ?G__.?L...-  ? ?
#         sA.. ?C...__.AC.
#
#     ___ mousePressEvent  e
#         name _ nuke.selectedNode .knob('name').getValue
#         __ e.b..  & ?C...__.LeftButton:
#             print("Нажата левая кнопка мыши")
#         __ e.b..  & ?C...__.RightButton:
#             print("Нажата правая кнопка мыши")
#         __ e.b..  & ?C...__.MiddleButton:
#             print("Нажата средняя кнопка мыши")
#         __ (e.b..  & ?C...__.LeftButton and
#                     e.b..  & ?C...__.RightButton):
#             print("Левая и правая кнопки нажаты")
#         sT..('Name of the Selected node is: ' + st.(name))
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
