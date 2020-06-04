#!/usr/bin/env python

#============================================================================#
# PyQt5 port of the designer/containerextension example from Qt v5.x         #
#----------------------------------------------------------------------------#
____ ?.?C.. ______ pP.., pS.., pyqtSlot, ?S..
____ ?.?W.. ______ (?A.., ?CB, ?L.., ?SW..,
        ?VBL.., ?W..)


#============================================================================#
# Implementation of a MultiPageWidget using a QComboBox and a QStackedWidget #
#----------------------------------------------------------------------------#
c_ PyMultiPageWidget(?W..):

    currentIndexChanged _ pS..(in.)

    pageTitleChanged _ pS.. st.

    ___  -   parent_None):
        s__(PyMultiPageWidget, self). - (parent)

        comboBox _ ?CB()
        # MAGIC
        # It is important that the combo box has an object name beginning
        # with '__qt__passive_', otherwise, it is inactive in the form editor
        # of the designer and you can't change the current page via the
        # combo box.
        # MAGIC
        comboBox.setObjectName('__qt__passive_comboBox')
        stackWidget _ ?SW..()
        comboBox.activated.c..(sCI..)
        layout _ ?VBL..
        layout.aW..(comboBox)
        layout.aW..(stackWidget)
        sL..(layout)

    ___ sH..
        r_ ?S..(200, 150)

    ___ count
        r_ stackWidget.count()

    ___ widget  index):
        r_ stackWidget.widget(index)

    @pyqtSlot(?W..)
    ___ addPage  page):
        insertPage(count(), page)

    @pyqtSlot(in., ?W..)
    ___ insertPage  index, page):
        page.setParent(stackWidget)
        stackWidget.insertWidget(index, page)
        title _ page.windowTitle()
        __ title __ "":
            title _ "Page %d" % (comboBox.count() + 1)
            page.sWT..(title)
        comboBox.iI..(index, title)

    @pyqtSlot(in.)
    ___ removePage  index):
        widget _ stackWidget.widget(index)
        stackWidget.removeWidget(widget)
        comboBox.removeItem(index)

    ___ getPageTitle
        cw _ stackWidget.currentWidget()
        r_ cw.windowTitle() __ cw __ no. N.. ____ ''
    
    @pyqtSlot st.
    ___ setPageTitle  newTitle):
        cw _ stackWidget.currentWidget()
        __ cw __ no. N..:
            comboBox.setItemText(getCurrentIndex(), newTitle)
            cw.sWT..(newTitle)
            pageTitleChanged.e..(newTitle)

    ___ getCurrentIndex
        r_ stackWidget.currentIndex()

    @pyqtSlot(in.)
    ___ sCI..  index):
        __ index !_ getCurrentIndex
            stackWidget.sCI..(index)
            comboBox.sCI..(index)
            currentIndexChanged.e..(index)

    pageTitle _ pP..(st., fget_getPageTitle, fset_setPageTitle, stored_False)
    currentIndex _ pP..(in., fget_getCurrentIndex, fset_setCurrentIndex)


#============================================================================#
# Main for testing the class                                                 #
#----------------------------------------------------------------------------#
__ __name__ __ "__main__":
    ______ ___
    app _ ?A..(___.a..
    widget _ PyMultiPageWidget()
    widget.addPage(?L..('This is page #1'))
    widget.addPage(?L..('This is page #2'))
    widget.s..
    ___.e.. ?.e..

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
