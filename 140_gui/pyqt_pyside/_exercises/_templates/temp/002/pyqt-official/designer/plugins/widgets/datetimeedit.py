#!/usr/bin/env python

#============================================================================#
# (Re)Implementation of QDateEdit and QDateTimeEdit. These classes force the #
# use of the calendar popup.                                                 #
#----------------------------------------------------------------------------#
# Copyright (c) 2008 by Denviso GmbH, <ulrich.berning@denviso.de>            #
#                                                                            #
# All Rights Reserved                                                        #
#                                                                            #
# Permission to use, copy, modify, and distribute this software and its      #
# documentation for any purpose and without fee is hereby granted,           #
# provided that the above copyright notice appear in all copies and that     #
# both that copyright notice and this permission notice appear in            #
# supporting documentation.                                                  #
#                                                                            #
# DENVISO DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS                       #
# SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY              #
# AND FITNESS, IN NO EVENT SHALL DENVISO BE LIABLE FOR ANY                   #
# SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES                  #
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,                    #
# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER                      #
# TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE              #
# OR PERFORMANCE OF THIS SOFTWARE.                                           #
#----------------------------------------------------------------------------#

____ ?.QtCore ______ pyqtProperty, Qt
____ ?.?W.. ______ (?A.., QCalendarWidget, QDateEdit,
        QDateTimeEdit, QHBoxLayout, QWidget)


#============================================================================#
# PyDateEdit                                                                 #
#----------------------------------------------------------------------------#
class PyDateEdit(QDateEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    ___ __init__(self, *args):
        super(PyDateEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw _ None
        self.__firstDayOfWeek _ Qt.Monday
        self.__gridVisible _ False
        self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible _ True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    ___ mousePressEvent(self, event):
        super(PyDateEdit, self).mousePressEvent(event)

        if not self.__cw:
            self.__cw _ self.findChild(QCalendarWidget)
            if self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    ___ getCalendarPopup(self):
        return True
    calendarPopup _ pyqtProperty(bool, fget_getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    ___ getFirstDayOfWeek(self):
        return self.__firstDayOfWeek
    ___ setFirstDayOfWeek(self, dayOfWeek):
        if dayOfWeek !_ self.__firstDayOfWeek:
            self.__firstDayOfWeek _ dayOfWeek
            if self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    ___ resetFirstDayOfWeek(self):
        if self.__firstDayOfWeek !_ Qt.Monday:
            self.__firstDayOfWeek _ Qt.Monday
            if self.__cw:
                self.__cw.setFirstDayOfWeek(Qt.Monday)
    firstDayOfWeek _ pyqtProperty(Qt.DayOfWeek,
                                         fget_getFirstDayOfWeek,
                                         fset_setFirstDayOfWeek,
                                         freset_resetFirstDayOfWeek)

    #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    ___ isGridVisible(self):
        return self.__gridVisible
    ___ setGridVisible(self, show):
        if show !_ self.__gridVisible:
            self.__gridVisible _ show
            if self.__cw:
                self.__cw.setGridVisible(show)
    ___ resetGridVisible(self):
        if self.__gridVisible !_ False:
            self.__gridVisible _ False
            if self.__cw:
                self.__cw.setGridVisible(False)
    gridVisible _ pyqtProperty(bool,
                                      fget_isGridVisible,
                                      fset_setGridVisible,
                                      freset_resetGridVisible)

    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    ___ getHorizontalHeaderFormat(self):
        return self.__horizontalHeaderFormat
    ___ setHorizontalHeaderFormat(self, format):
        if format !_ self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat _ format
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    ___ resetHorizontalHeaderFormat(self):
        if self.__horizontalHeaderFormat !_ QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
    horizontalHeaderFormat _ pyqtProperty(QCalendarWidget.HorizontalHeaderFormat,
                                                 fget_getHorizontalHeaderFormat,
                                                 fset_setHorizontalHeaderFormat,
                                                 freset_resetHorizontalHeaderFormat)

    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    ___ getVerticalHeaderFormat(self):
        return self.__verticalHeaderFormat
    ___ setVerticalHeaderFormat(self, format):
        if format !_ self.__verticalHeaderFormat:
            self.__verticalHeaderFormat _ format
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    ___ resetVerticalHeaderFormat(self):
        if self.__verticalHeaderFormat !_ QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
    verticalHeaderFormat _ pyqtProperty(QCalendarWidget.VerticalHeaderFormat,
                                               fget_getVerticalHeaderFormat,
                                               fset_setVerticalHeaderFormat,
                                               freset_resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    ___ isNavigationBarVisible(self):
        return self.__navigationBarVisible
    ___ setNavigationBarVisible(self, visible):
        if visible !_ self.__navigationBarVisible:
            self.__navigationBarVisible _ visible
            if self.__cw:
                self.__cw.setNavigationBarVisible(visible)
    ___ resetNavigationBarVisible(self):
        if self.__navigationBarVisible !_ True:
            self.__navigationBarVisible _ True
            if self.__cw:
                self.__cw.setNavigationBarVisible(True)
    navigationBarVisible _ pyqtProperty(bool,
                                               fget_isNavigationBarVisible,
                                               fset_setNavigationBarVisible,
                                               freset_resetNavigationBarVisible)


#============================================================================#
# PyDateTimeEdit                                                             #
#----------------------------------------------------------------------------#
class PyDateTimeEdit(QDateTimeEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    ___ __init__(self, *args):
        super(PyDateTimeEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw _ None
        self.__firstDayOfWeek _ Qt.Monday
        self.__gridVisible _ False
        self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible _ True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    ___ mousePressEvent(self, event):
        super(PyDateTimeEdit, self).mousePressEvent(event)

        if not self.__cw:
            self.__cw _ self.findChild(QCalendarWidget)
            if self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    ___ getCalendarPopup(self):
        return True
    calendarPopup _ pyqtProperty(bool, fget_getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    ___ getFirstDayOfWeek(self):
        return self.__firstDayOfWeek
    ___ setFirstDayOfWeek(self, dayOfWeek):
        if dayOfWeek !_ self.__firstDayOfWeek:
            self.__firstDayOfWeek _ dayOfWeek
            if self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    ___ resetFirstDayOfWeek(self):
        if self.__firstDayOfWeek !_ Qt.Monday:
            self.__firstDayOfWeek _ Qt.Monday
            if self.__cw:
                self.__cw.setFirstDayOfWeek(Qt.Monday)
    firstDayOfWeek _ pyqtProperty(Qt.DayOfWeek,
                                         fget_getFirstDayOfWeek,
                                         fset_setFirstDayOfWeek,
                                         freset_resetFirstDayOfWeek)

    #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    ___ isGridVisible(self):
        return self.__gridVisible
    ___ setGridVisible(self, show):
        if show !_ self.__gridVisible:
            self.__gridVisible _ show
            if self.__cw:
                self.__cw.setGridVisible(show)
    ___ resetGridVisible(self):
        if self.__gridVisible !_ False:
            self.__gridVisible _ False
            if self.__cw:
                self.__cw.setGridVisible(False)
    gridVisible _ pyqtProperty(bool,
                                      fget_isGridVisible,
                                      fset_setGridVisible,
                                      freset_resetGridVisible)

    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    ___ getHorizontalHeaderFormat(self):
        return self.__horizontalHeaderFormat
    ___ setHorizontalHeaderFormat(self, format):
        if format !_ self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat _ format
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    ___ resetHorizontalHeaderFormat(self):
        if self.__horizontalHeaderFormat !_ QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
    horizontalHeaderFormat _ pyqtProperty(QCalendarWidget.HorizontalHeaderFormat,
                                                 fget_getHorizontalHeaderFormat,
                                                 fset_setHorizontalHeaderFormat,
                                                 freset_resetHorizontalHeaderFormat)

    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    ___ getVerticalHeaderFormat(self):
        return self.__verticalHeaderFormat
    ___ setVerticalHeaderFormat(self, format):
        if format !_ self.__verticalHeaderFormat:
            self.__verticalHeaderFormat _ format
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    ___ resetVerticalHeaderFormat(self):
        if self.__verticalHeaderFormat !_ QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
    verticalHeaderFormat _ pyqtProperty(QCalendarWidget.VerticalHeaderFormat,
                                               fget_getVerticalHeaderFormat,
                                               fset_setVerticalHeaderFormat,
                                               freset_resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    ___ isNavigationBarVisible(self):
        return self.__navigationBarVisible
    ___ setNavigationBarVisible(self, visible):
        if visible !_ self.__navigationBarVisible:
            self.__navigationBarVisible _ visible
            if self.__cw:
                self.__cw.setNavigationBarVisible(visible)
    ___ resetNavigationBarVisible(self):
        if self.__navigationBarVisible !_ True:
            self.__navigationBarVisible _ True
            if self.__cw:
                self.__cw.setNavigationBarVisible(True)
    navigationBarVisible _ pyqtProperty(bool,
                                               fget_isNavigationBarVisible,
                                               fset_setNavigationBarVisible,
                                               freset_resetNavigationBarVisible)


if __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)

    w _ QWidget()
    lay _ QHBoxLayout()

    lay.addWidget(PyDateEdit())
    lay.addWidget(PyDateTimeEdit())

    w.setLayout(lay)
    w.s..

    sys.exit(app.exec_())

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
