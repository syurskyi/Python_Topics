#!/usr/bin/env python

#============================================================================#
# PyQt5 port of the designer/containerextension example from Qt v5.x         #
#----------------------------------------------------------------------------#
____ ?.QtCore ______ pyqtProperty, pyqtSignal, pyqtSlot, QSize
____ ?.?W.. ______ (?A.., QComboBox, QLabel, QStackedWidget,
        QVBoxLayout, QWidget)


#============================================================================#
# Implementation of a MultiPageWidget using a QComboBox and a QStackedWidget #
#----------------------------------------------------------------------------#
class PyMultiPageWidget(QWidget):

    currentIndexChanged _ pyqtSignal(int)

    pageTitleChanged _ pyqtSignal(str)

    ___ __init__(self, parent_None):
        super(PyMultiPageWidget, self).__init__(parent)

        self.comboBox _ QComboBox()
        # MAGIC
        # It is important that the combo box has an object name beginning
        # with '__qt__passive_', otherwise, it is inactive in the form editor
        # of the designer and you can't change the current page via the
        # combo box.
        # MAGIC
        self.comboBox.setObjectName('__qt__passive_comboBox')        
        self.stackWidget _ QStackedWidget()
        self.comboBox.activated.c..(self.setCurrentIndex)
        self.layout _ QVBoxLayout()
        self.layout.addWidget(self.comboBox)
        self.layout.addWidget(self.stackWidget)
        self.setLayout(self.layout)

    ___ sizeHint(self):
        return QSize(200, 150)

    ___ count(self):
        return self.stackWidget.count()

    ___ widget(self, index):
        return self.stackWidget.widget(index)

    @pyqtSlot(QWidget)
    ___ addPage(self, page):
        self.insertPage(self.count(), page)

    @pyqtSlot(int, QWidget)
    ___ insertPage(self, index, page):
        page.setParent(self.stackWidget)
        self.stackWidget.insertWidget(index, page)
        title _ page.windowTitle()
        if title == "":
            title _ "Page %d" % (self.comboBox.count() + 1)
            page.setWindowTitle(title)
        self.comboBox.insertItem(index, title)

    @pyqtSlot(int)
    ___ removePage(self, index):
        widget _ self.stackWidget.widget(index)
        self.stackWidget.removeWidget(widget)
        self.comboBox.removeItem(index)

    ___ getPageTitle(self):
        cw _ self.stackWidget.currentWidget()
        return cw.windowTitle() if cw is not None else ''
    
    @pyqtSlot(str)
    ___ setPageTitle(self, newTitle):
        cw _ self.stackWidget.currentWidget()
        if cw is not None:
            self.comboBox.setItemText(self.getCurrentIndex(), newTitle)
            cw.setWindowTitle(newTitle)
            self.pageTitleChanged.emit(newTitle)

    ___ getCurrentIndex(self):
        return self.stackWidget.currentIndex()

    @pyqtSlot(int)
    ___ setCurrentIndex(self, index):
        if index !_ self.getCurrentIndex
            self.stackWidget.setCurrentIndex(index)
            self.comboBox.setCurrentIndex(index)
            self.currentIndexChanged.emit(index)

    pageTitle _ pyqtProperty(str, fget_getPageTitle, fset_setPageTitle, stored_False)
    currentIndex _ pyqtProperty(int, fget_getCurrentIndex, fset_setCurrentIndex)


#============================================================================#
# Main for testing the class                                                 #
#----------------------------------------------------------------------------#
if __name__ == "__main__":
    ______ sys
    app _ ?A..(sys.argv)
    widget _ PyMultiPageWidget()
    widget.addPage(QLabel('This is page #1'))
    widget.addPage(QLabel('This is page #2'))
    widget.s..
    sys.exit(app.exec_())

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
