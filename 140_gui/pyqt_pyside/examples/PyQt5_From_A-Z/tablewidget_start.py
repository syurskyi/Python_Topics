import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Object Hierarchy")
        self.resize(1300, 700)

#########   Set up widgets

        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(1)
        self.trwQt.setHeaderLabels(["Qt Class"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQt_dblClicked)

        twi = self.populateTree()

        self.trwQt.sortItems(0, Qt.AscendingOrder)
        self.trwQt.expandItem(self.twiQWidget)
        self.trwQt.expandItem(twi)
        self.trwQt.setColumnWidth(0, 200)

        self.ledClassName = QLineEdit()
        self.ledClassName.setPlaceholderText("Enter class name to add")

        self.cmbParentClass = QComboBox()
        lstClasses = get_all_items(self.trwQt)
        lstClasses.sort()
        for cls in lstClasses:
            self.cmbParentClass.addItem(cls.text(0))
        self.cmbParentClass.setCurrentText("QLineEdit")

        self.btnAddClass = QPushButton("Add Class")
        self.btnAddClass.clicked.connect(self.evt_btnAddClass_clicked)

        self.wevWindow = QWebEngineView()
        self.wevWindow.setUrl(QUrl().fromUserInput("doc.qt.io/qt-5/qlineedit.html"))

        self.btnForward = QPushButton(">")
        self.btnForward.clicked.connect(self.wevWindow.forward)

        self.btnBack = QPushButton("<")
        self.btnBack.clicked.connect(self.wevWindow.back)

        self.btnHistory = QPushButton("Show History")
        self.btnHistory.clicked.connect(self.evt_btnHistory_clicked)

        self.tblHistory = QTableWidget()
        self.tblHistory.setColumnCount(4)
        self.tblHistory.hide()

        self.setupLayout()

    def setupLayout(self):
        self.lytMain = QHBoxLayout()

        self.lytTree = QVBoxLayout()
        self.lytTree.addWidget(self.trwQt)
        self.lytTree.addWidget(self.cmbParentClass)
        self.lytTree.addWidget(self.ledClassName)
        self.lytTree.addWidget(self.btnAddClass)

        self.lytButtons = QHBoxLayout()
        self.lytButtons.addStretch()
        self.lytButtons.addWidget(self.btnBack)
        self.lytButtons.addWidget(self.btnHistory)
        self.lytButtons.addWidget(self.btnForward)
        self.lytButtons.addStretch()

        self.lytBrowser = QVBoxLayout()
        self.lytBrowser.addWidget(self.wevWindow)
        self.lytBrowser.addLayout(self.lytButtons)
        self.lytBrowser.addWidget(self.tblHistory)

        self.lytMain.addLayout(self.lytTree, 2)
        self.lytMain.addLayout(self.lytBrowser, 8)

        self.setLayout(self.lytMain)

    def populateTree(self):
        ####### Create top level items
        self.twiQWidget = QTreeWidgetItem(self.trwQt, ["QWidget Module"])
        self.twiQGui = QTreeWidgetItem(self.trwQt, ["QGui Module"])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ["QCore Module"])

        ###### add subitems to top level items
        ###### QWidget
        lstQtWidget = ["QDialog", "QLabel", "QLineEdit", "QTextEdit", "QGroupBox", "QFrame"]
        for cls in lstQtWidget:
            self.twiQWidget.addChild(QTreeWidgetItem([cls]))

        lstQtGui = ["QBitmap", "QColor", "QFont", "QIcon", "QImage"]
        for cls in lstQtGui:
            self.twiQGui.addChild(QTreeWidgetItem([cls]))

        lstQtCore = ["QThread", "QDateTime", "QPixmap", "QUrl", "QFile"]
        for cls in lstQtCore:
            self.twiQCore.addChild(QTreeWidgetItem([cls]))

        ###### add subitems to QDialog
        twi = self.trwQt.findItems("QDialog", Qt.MatchRecursive)[0]
        lstQDialog = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls]))

        ###### add subitems to QFrame
        twi = self.trwQt.findItems("QFrame", Qt.MatchRecursive)[0]
        lstQFrame = ["QLabel", "QLCDNumber", "QStackedWidget", "QToolBox"]
        for cls in lstQFrame:
            twi.addChild(QTreeWidgetItem([cls]))

        return twi

####### Event handlers
    def evt_trwQt_dblClicked(self, twi, col):
        #QMessageBox.information(self, "Qt Classes", "You chose the {} class".format(twi.text(0)))
        self.cmbParentClass.setCurrentText(twi.text(0))
        url = "doc.qt.io/qt-5/{}.html".format(twi.text(0).lower())
        self.wevWindow.setUrl(QUrl().fromUserInput(url))
        self.wevWindow.repaint()

    def evt_btnAddClass_clicked(self):
        res = QMessageBox.question(self, "Add Class", "Are you sure you want to add {} to {}?".format(self.ledClassName.text(), self.cmbParentClass.currentText()))
        if res == QMessageBox.Yes:
            twi = self.trwQt.findItems(self.cmbParentClass.currentText(), Qt.MatchRecursive)[0]
            twi.addChild(QTreeWidgetItem([self.ledClassName.text()]))
            self.trwQt.sortItems(0, Qt.AscendingOrder)
            self.cmbParentClass.addItem(self.ledClassName.text())
            self.ledClassName.setText("")

    def evt_btnHistory_clicked(self):
        if self.tblHistory.isHidden():
            history = self.wevWindow.history()
            QMessageBox.information(self, "History", "There are {} elements in the browser history".format(history.count()))
            self.tblHistory.clear()
            self.tblHistory.setRowCount(len(history))
            for idx in range(history.count()):
                print(history.itemAt(idx).title())
            self.tblHistory.show()
            self.btnHistory.setText("Hide History")
        else:
            self.tblHistory.hide()
            self.btnHistory.setText("Show History")


#######  TWO FUNCTIONS REQUIRED TO RECURSIVELY RETURN ALL ITEMS

def get_subtree_nodes(tree_widget_item):
    """Returns all QTreeWidgetItems in the subtree rooted at the given node."""
    nodes = []
    nodes.append(tree_widget_item)
    for i in range(tree_widget_item.childCount()):
        nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
    return nodes

def get_all_items(tree_widget):
    """Returns all QTreeWidgetItems in the given QTreeWidget."""
    all_items = []
    for i in range(tree_widget.topLevelItemCount()):
        top_item = tree_widget.topLevelItem(i)
        all_items.extend(get_subtree_nodes(top_item))
    return all_items


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())