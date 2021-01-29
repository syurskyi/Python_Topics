import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lytMain = QVBoxLayout()
        self.setLayout(self.lytMain)

        self.ted = QTextEdit()
        self.ted.setText("012345678901234567890123456789012345678901234567890123456789012345678901234567890")
        self.lytMain.addWidget(self.ted)

        self.btnBackground = QPushButton("Set Background Color")
        self.lytMain.addWidget(self.btnBackground)
        self.btnBackground.clicked.connect(self.evt_btnBackground_clicked)

        self.btnHtml = QPushButton("Add HTML")
        self.lytMain.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btnHTML_clicked)

        curText = self.ted.textCursor()
        curText.setPosition(15, QTextCursor.MoveAnchor)
        curText.setPosition(25, QTextCursor.KeepAnchor)
        self.ted.setTextCursor(curText)
        self.ted.setTextColor(QColor('red'))

    def evt_btnBackground_clicked(self):
        clr = QColorDialog.getColor(QColor('black'))
        self.ted.setTextBackgroundColor(clr)
        self.ted.setFontPointSize(16)
        self.ted.repaint()

    def evt_btnHTML_clicked(self):
        html = """
            <h1>My header</h1>
            <p>This is <b>BOLD</b> and <i>italic</i> type</p>
            <ul>
                <li>List item A</li>
                <li>List item B</li>
                <li>List item C</li>
                <li>List item D</li>
            </ul>
        """
        self.ted.setText(html)
        self.ted.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
