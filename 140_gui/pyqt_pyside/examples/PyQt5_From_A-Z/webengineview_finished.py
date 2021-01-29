import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")

        self.lytMain = QVBoxLayout()
        self.setLayout(self.lytMain)

        self.wev = QWebEngineView()
        self.wev.resize(1000, 700)
        self.lytMain.addWidget(self.wev)

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
        self.wev.setHtml(html)
        self.wev.repaint()

        self.ledClass = QLineEdit("QWebEngineView")
        self.lytMain.addWidget(self.ledClass)

        self.btnHtml = QPushButton("Load HTML")
        self.lytMain.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btnHtml_clicked)

        self.btnPlot = QPushButton("Plot")
        self.lytMain.addWidget(self.btnPlot)
        self.btnPlot.clicked.connect(self.evt_btnPlot_clicked)

    def evt_btnHtml_clicked(self):
        url = "https://doc.qt.io/qt-5/{}.html".format(self.ledClass.text().lower())
        self.wev.setUrl(QUrl.fromUserInput(url))
        self.wev.repaint()

    def evt_btnPlot_clicked(self):
        url = "/Users/lstomsl/PyCharmProjects/PyQt5_course/html/plotly.html"
        self.wev.setUrl(QUrl.fromLocalFile(url))
        self.wev.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
