from PySide2.QtGui _____ *
from PySide2.QtCore _____ *
from PySide2.QtWidgets _____ *
_____ __
_____ json

HOME_FOLDER = __.pa__.join(__.pa__.dirname(__file__), 'icons')


class Panel(QWidget):
    ___ __init__(self):
        super(Panel, self).__init__()
        self.resize(400, 400)
        mouse_position = QCursor().pos()
        self.move(mouse_position - QPoint(200, 200))
        self.setMouseTracking T..
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_QuitOnClose)

        self.selected_item = N..

        self.mouse_destination = QPoint(self.width()/2, self.height()/2)

        self.layout = QGridLayout()
        self.layout.addWidget(ActionLabel(1), 0, 0)
        self.layout.addWidget(ActionLabel(2), 0, 1)
        self.layout.addWidget(ActionLabel(3), 0, 2)
        self.layout.addWidget(ActionLabel(4), 1, 0)
        self.layout.addWidget(ActionLabel(5), 1, 2)
        self.layout.addWidget(ActionLabel(6), 2, 0)
        self.layout.addWidget(ActionLabel(7), 2, 1)
        self.layout.addWidget(ActionLabel(8), 2, 2)

        self.setLayout(self.layout)

        action_path = __.pa__.join(HOME_FOLDER, "actions")
        __ no. __.pa__.exists(action_path):
            __.m_d_(action_path)

    ___ keyReleaseEvent(self, event):
        __ event.isAutoRepeat
            r_
        __ event.text() __ "n":
            __ self.selected_item __ N..:
                self.close()
                r_
            exec self.selected_item.code
            self.close()

    ___ paintEvent(self, QPaintEvent):
        super(Panel, self).paintEvent(QPaintEvent)
        painter = QPainter(self)

        self.draw_line(painter)
        self.set_label_color()

        nuke_image = QPixmap("%s/nuke.png" % HOME_FOLDER)
        painter.drawPixmap(QPoint(self.width()/2-24, self.height()/2-24), nuke_image)

    ___ set_label_color(self):
        widgets = [self.layout.itemAt(i).widget() ___ i __ range(self.layout.count())]
        self.selected_item = N..
        ___ w __ widgets:
            __ self.line.intersected(w.geometry()):
                w.set_selected T..
                self.selected_item = w
            else:
                w.set_selected F..

    ___ draw_line(self,painter):
        pen = QPen(QColor(0,0,0))
        pen.setWidth(2)
        painter.setPen(pen)
        center = QPoint(self.width()/2, self.height()/2)
        destination = self.mouse_destination
        self.line = QPolygon([center, center+QPoint(1, 0), destination, destination+QPoint(-1, 0)])
        painter.drawPolygon(self.line)

    ___ mouseMoveEvent(self, event):
        self.mouse_destination = event.pos()
        self.update()

    ___ keyPressEvent(self, event):
        __ event.isAutoRepeat
            r_


class Dialog(QDialog):
    ___ __init__(self, id):
        super(Dialog, self).__init__()

        self.id = id
        self.action_path = __.pa__.join(HOME_FOLDER, "actions", "%s.txt" % self.id)
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        self.code_plain_text = QPlainTextEdit()

        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_line_edit)

        master_layout = QVBoxLayout()
        master_layout.addLayout(name_layout)
        master_layout.addWidget(self.code_plain_text)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        master_layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        self.setLayout(master_layout)
        self.load_action()

    ___ load_action(self):
        __ __.pa__.exists(self.action_path):
            doc = json.load(open(self.action_path))
            name = doc['name']
            code = doc['code']
            self.name_line_edit.setText(name)
            self.code_plain_text.setPlainText(code)

    ___ save_action(self):
        doc = dict()
        doc['name'] = self.name_line_edit.text()
        doc['code'] = self.code_plain_text.toPlainText()
        pa__ = open(self.action_path, "w")
        json.dump(doc, pa__)


class ActionLabel(QLabel):
    ___ __init__(self, id):
        super(ActionLabel, self).__init__()

        self.id = id
        self.setAlignment(Qt.AlignCenter)
        self.setMouseTracking T..
        self.setFixedWidth(100)
        self.setFixedHeight(25)
        self.setStyleSheet("""background:red;
                            color:black""")
        self.set_action()

    ___ set_action(self):

        pa__ = __.pa__.join(HOME_FOLDER, "actions", "%s.txt" % self.id)
        __ __.pa__.exists(pa__):
            doc = json.load(open(pa__))
            name = doc['name']
            code = doc['code']
        else:
            name = "Action %s" % self.id
            code = ""

        self.setText(name)
        self.code = code

    ___ mousePressEvent(self, event):
        __ event.buttons() __ Qt.RightButton:
            dialog = Dialog(self.id)
            __ dialog.exec_
                dialog.save_action()
            self.parent().close()

    ___ set_selected(self, is_selected):

        __ is_selected:
                self.setStyleSheet("""background:green;
                            color:black""")
        else:
            self.setStyleSheet("""background:red;
                            color:black""")
___ start
    start.panel = Panel()
    start.panel.show()