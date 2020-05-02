____ PySide ______ ?C.., QtGui


c_ MyLabel(QtGui.?L..):
    ___ - (self, text, parent=N..):
        QtGui.?L...- (self, text, parent)
        setAlignment(?C...__.AlignCenter)

    ___ mousePressEvent(self, e):
        name _ nuke.selectedNode .knob('name').getValue
        __ e.buttons  & ?C...__.LeftButton:
            print("Нажата левая кнопка мыши")
        __ e.buttons  & ?C...__.RightButton:
            print("Нажата правая кнопка мыши")
        __ e.buttons  & ?C...__.MiddleButton:
            print("Нажата средняя кнопка мыши")
        __ (e.buttons  & ?C...__.LeftButton and
                    e.buttons  & ?C...__.RightButton):
            print("Левая и правая кнопки нажаты")
        sT..('Name of the Selected node is: ' + st.(name))


c_ MyWindow(QtGui.W..):
    ___ - (self, parent=N..):
        QtGui.W...- (self, parent)
        sWT__("Name Window")

        resize(300, 150)
        label _ MyLabel("Click here with the mouse")
        label.setFrameStyle(QtGui.QFrame.Box | QtGui.QFrame.Plain)
        vbox _ QtGui.?VB..
        vbox.aW..(label)
        sL..(vbox)


___ main :
    global c
    c _ MyWindow
    c.raise_
    c.show

main

