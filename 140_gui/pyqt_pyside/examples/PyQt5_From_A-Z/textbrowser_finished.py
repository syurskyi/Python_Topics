import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lytMain = QVBoxLayout()
        self.setLayout(self.lytMain)

        self.tbr = QTextBrowser()
        self.lytMain.addWidget(self.tbr)

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
        self.tbr.setHtml(html)
        self.tbr.repaint()

        self.btnHtml = QPushButton("Load HTML")
        self.lytMain.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btnHtml_clicked)

    def evt_btnHtml_clicked(self):
        url = "html/test.html"
        self.tbr.setSource(QUrl.fromLocalFile(url))
        self.tbr.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
