____ ______._G.. _____ _
____ ______._C.. _____ _
____ ______._W.. _____ _
_____ __
_____ j..

HOME_FOLDER _ __.pa__.join __.pa__.d..  -f 'icons'


c_ Panel _W..
    ___  - 
        s__ P..  . - 
        r.. 400 400
        mouse_position _ _C.. .p..
        m.. ? - _P.. 200 200
        sMT.. T..
        sWF.. __.FWH.. | __.P..
        sA.. __.WA_QOC..

        selected_item _ N..

        mouse_destination _ _P.. w.. /2 h.. /2

        layout _ _GL..
        ?.addWidget(ActionLabel(1), 0, 0)
        ?.addWidget(ActionLabel(2), 0, 1)
        ?.addWidget(ActionLabel(3), 0, 2)
        ?.addWidget(ActionLabel(4), 1, 0)
        ?.addWidget(ActionLabel(5), 1, 2)
        ?.addWidget(ActionLabel(6), 2, 0)
        ?.addWidget(ActionLabel(7), 2, 1)
        ?.addWidget(ActionLabel(8), 2, 2)

        setLayout(?)

        action_path _ __.pa__.join(HOME_FOLDER, "actions")
        __ no. __.pa__.exists(action_path):
            __.m_d_(action_path)

    ___ keyReleaseEvent(, event):
        __ event.isAutoRepeat
            r_
        __ event.text() __ "n":
            __ selected_item __ N..:
                close()
                r_
            exec selected_item.code
            close()

    ___ paintEvent(, QPaintEvent):
        s__(Panel, ).paintEvent(QPaintEvent)
        painter _ QPainter()

        draw_line(painter)
        set_label_color()

        nuke_image _ QPixmap("%s/nuke.png" % HOME_FOLDER)
        painter.drawPixmap(_P..(width()/2-24, height()/2-24), nuke_image)

    ___ set_label_color
        widgets _ [layout.itemAt(i).widget() ___ i __ range(layout.count())]
        selected_item _ N..
        ___ w __ widgets:
            __ line.intersected(w.geometry()):
                w.set_selected T..
                selected_item _ w
            ____
                w.set_selected F..

    ___ draw_line(,painter):
        pen _ QPen(QColor(0,0,0))
        pen.setWidth(2)
        painter.setPen(pen)
        center _ _P..(width()/2, height()/2)
        destination _ mouse_destination
        line _ QPolygon([center, center+_P..(1, 0), destination, destination+_P..(-1, 0)])
        painter.drawPolygon(line)

    ___ mouseMoveEvent(, event):
        mouse_destination _ event.p..
        update()

    ___ keyPressEvent(, event):
        __ event.isAutoRepeat
            r_


c_ Dialog(QDialog):
    ___  - (, id):
        s__(Dialog, ). - ()

        id _ id
        action_path _ __.pa__.join(HOME_FOLDER, "actions", "%s.txt" % id)
        name_label _ QLabel("Name:")
        name_line_edit _ QLineEdit()
        code_plain_text _ QPlainTextEdit()

        name_layout _ QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(name_line_edit)

        master_layout _ QVBoxLayout()
        master_layout.addLayout(name_layout)
        master_layout.addWidget(code_plain_text)

        buttons _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, __.Horizontal, )
        master_layout.addWidget(buttons)

        buttons.accepted.connect(accept)
        buttons.rejected.connect(reject)

        setLayout(master_layout)
        load_action()

    ___ load_action
        __ __.pa__.exists(action_path):
            doc _ j...load(open(action_path))
            name _ doc['name']
            code _ doc['code']
            name_line_edit.setText(name)
            code_plain_text.setPlainText(code)

    ___ save_action
        doc _ dict()
        doc['name'] _ name_line_edit.text()
        doc['code'] _ code_plain_text.toPlainText()
        pa__ _ open(action_path, "w")
        j...dump(doc, pa__)


c_ ActionLabel(QLabel):
    ___  - (, id):
        s__(ActionLabel, ). - ()

        id _ id
        setAlignment(__.AlignCenter)
        sMT.. T..
        setFixedWidth(100)
        setFixedHeight(25)
        setStyleSheet("""background:red;
                            color:black""")
        set_action()

    ___ set_action

        pa__ _ __.pa__.join(HOME_FOLDER, "actions", "%s.txt" % id)
        __ __.pa__.exists(pa__):
            doc _ j...load(open(pa__))
            name _ doc['name']
            code _ doc['code']
        ____
            name _ "Action %s" % id
            code _ ""

        setText(name)
        code _ code

    ___ mousePressEvent(, event):
        __ event.buttons() __ __.RightButton:
            dialog _ Dialog(id)
            __ dialog.exec_
                dialog.save_action()
            parent().close()

    ___ set_selected(, is_selected):

        __ is_selected:
                setStyleSheet("""background:green;
                            color:black""")
        ____
            setStyleSheet("""background:red;
                            color:black""")
___ start
    start.panel _ Panel()
    start.panel.show()