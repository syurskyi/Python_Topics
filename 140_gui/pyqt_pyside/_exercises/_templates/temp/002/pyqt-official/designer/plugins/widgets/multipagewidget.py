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

    ___  -   parent_None):
        super(PyMultiPageWidget, self). - (parent)

        comboBox _ QComboBox()
        # MAGIC
        # It is important that the combo box has an object name beginning
        # with '__qt__passive_', otherwise, it is inactive in the form editor
        # of the designer and you can't change the current page via the
        # combo box.
        # MAGIC
        comboBox.setObjectName('__qt__passive_comboBox')
        stackWidget _ QStackedWidget()
        comboBox.activated.c..(setCurrentIndex)
        layout _ ?VBL..
        layout.aW..(comboBox)
        layout.aW..(stackWidget)
        sL..(layout)

    ___ sizeHint
        r_ QSize(200, 150)

    ___ count
        r_ stackWidget.count()

    ___ widget  index):
        r_ stackWidget.widget(index)

    @pyqtSlot(QWidget)
    ___ addPage  page):
        insertPage(count(), page)

    @pyqtSlot(int, QWidget)
    ___ insertPage  index, page):
        page.setParent(stackWidget)
        stackWidget.insertWidget(index, page)
        title _ page.windowTitle()
        __ title == "":
            title _ "Page %d" % (comboBox.count() + 1)
            page.setWindowTitle(title)
        comboBox.insertItem(index, title)

    @pyqtSlot(int)
    ___ removePage  index):
        widget _ stackWidget.widget(index)
        stackWidget.removeWidget(widget)
        comboBox.removeItem(index)

    ___ getPageTitle
        cw _ stackWidget.currentWidget()
        r_ cw.windowTitle() __ cw __ no. N.. else ''
    
    @pyqtSlot(str)
    ___ setPageTitle  newTitle):
        cw _ stackWidget.currentWidget()
        __ cw __ no. N..:
            comboBox.setItemText(getCurrentIndex(), newTitle)
            cw.setWindowTitle(newTitle)
            pageTitleChanged.emit(newTitle)

    ___ getCurrentIndex
        r_ stackWidget.currentIndex()

    @pyqtSlot(int)
    ___ setCurrentIndex  index):
        __ index !_ getCurrentIndex
            stackWidget.setCurrentIndex(index)
            comboBox.setCurrentIndex(index)
            currentIndexChanged.emit(index)

    pageTitle _ pyqtProperty(str, fget_getPageTitle, fset_setPageTitle, stored_False)
    currentIndex _ pyqtProperty(int, fget_getCurrentIndex, fset_setCurrentIndex)


#============================================================================#
# Main for testing the class                                                 #
#----------------------------------------------------------------------------#
__ __name__ == "__main__":
    ______ ___
    app _ ?A..(___.a..
    widget _ PyMultiPageWidget()
    widget.addPage(QLabel('This is page #1'))
    widget.addPage(QLabel('This is page #2'))
    widget.s..
    ___.exit(app.exec_())

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
