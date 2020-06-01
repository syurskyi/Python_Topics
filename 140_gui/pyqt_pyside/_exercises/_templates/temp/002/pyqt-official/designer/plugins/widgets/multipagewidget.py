#!/usr/bin/env python

#============================================================================#
# PyQt5 port of the designer/containerextension example from Qt v5.x         #
#----------------------------------------------------------------------------#
____ ?.?C.. ______ pyqtProperty, pyqtSignal, pyqtSlot, QSize
____ ?.?W.. ______ (?A.., QComboBox, QLabel, QStackedWidget,
        QVBoxLayout, QWidget)


#============================================================================#
# Implementation of a MultiPageWidget using a QComboBox and a QStackedWidget #
#----------------------------------------------------------------------------#
c_ PyMultiPageWidget(QWidget):

    currentIndexChanged _ pyqtSignal(int)

    pageTitleChanged _ pyqtSignal(str)

    ___ __init__  parent_None):
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
        self.layout _ ?VBL..
        self.layout.aW..(self.comboBox)
        self.layout.aW..(self.stackWidget)
        self.sL..(self.layout)

    ___ sizeHint(self):
        r_ QSize(200, 150)

    ___ count(self):
        r_ self.stackWidget.count()

    ___ widget  index):
        r_ self.stackWidget.widget(index)

    @pyqtSlot(QWidget)
    ___ addPage  page):
        self.insertPage(self.count(), page)

    @pyqtSlot(int, QWidget)
    ___ insertPage  index, page):
        page.setParent(self.stackWidget)
        self.stackWidget.insertWidget(index, page)
        title _ page.windowTitle()
        __ title == "":
            title _ "Page %d" % (self.comboBox.count() + 1)
            page.setWindowTitle(title)
        self.comboBox.insertItem(index, title)

    @pyqtSlot(int)
    ___ removePage  index):
        widget _ self.stackWidget.widget(index)
        self.stackWidget.removeWidget(widget)
        self.comboBox.removeItem(index)

    ___ getPageTitle(self):
        cw _ self.stackWidget.currentWidget()
        r_ cw.windowTitle() __ cw __ no. N.. else ''
    
    @pyqtSlot(str)
    ___ setPageTitle  newTitle):
        cw _ self.stackWidget.currentWidget()
        __ cw __ no. N..:
            self.comboBox.setItemText(self.getCurrentIndex(), newTitle)
            cw.setWindowTitle(newTitle)
            self.pageTitleChanged.emit(newTitle)

    ___ getCurrentIndex(self):
        r_ self.stackWidget.currentIndex()

    @pyqtSlot(int)
    ___ setCurrentIndex  index):
        __ index !_ self.getCurrentIndex
            self.stackWidget.setCurrentIndex(index)
            self.comboBox.setCurrentIndex(index)
            self.currentIndexChanged.emit(index)

    pageTitle _ pyqtProperty(str, fget_getPageTitle, fset_setPageTitle, stored_False)
    currentIndex _ pyqtProperty(int, fget_getCurrentIndex, fset_setCurrentIndex)


#============================================================================#
# Main for testing the class                                                 #
#----------------------------------------------------------------------------#
__ __name__ == "__main__":
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
