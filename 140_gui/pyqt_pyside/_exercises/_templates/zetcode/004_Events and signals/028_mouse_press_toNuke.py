____ PySide ______ ?C.., ?G__


c_ MyLabel(?G__.?L..):
    ___ - (self, text, parent=N..):
        ?G__.?L...- (self, text, parent)
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


c_ MyWindow(?G__.W..):
    ___ - (self, parent=N..):
        ?G__.W...- (self, parent)
        sWT__("Name Window")

        resize(300, 150)
        label _ MyLabel("Click here with the mouse")
        label.setFrameStyle(?G__.QFrame.Box | ?G__.QFrame.Plain)
        vbox _ ?G__.?VB..
        vbox.aW..(label)
        sL..(vbox)


___ main :
    global c
    c _ MyWindow
    c.raise_
    c.show

main

