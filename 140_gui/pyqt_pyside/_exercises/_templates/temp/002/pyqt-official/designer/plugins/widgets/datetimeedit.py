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

____ ?.?C.. ______ pyqtProperty, __
____ ?.?W.. ______ (?A.., QCalendarWidget, QDateEdit,
        QDateTimeEdit, QHBoxLayout, QWidget)


#============================================================================#
# PyDateEdit                                                                 #
#----------------------------------------------------------------------------#
c_ PyDateEdit(QDateEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    ___ __init__  *args):
        super(PyDateEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw _ N..
        self.__firstDayOfWeek _ __.Monday
        self.__gridVisible _ False
        self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible _ True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    ___ mousePressEvent  event):
        super(PyDateEdit, self).mousePressEvent(event)

        __ no. self.__cw:
            self.__cw _ self.findChild(QCalendarWidget)
            __ self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    ___ getCalendarPopup(self):
        r_ True
    calendarPopup _ pyqtProperty(bool, fget_getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    ___ getFirstDayOfWeek(self):
        r_ self.__firstDayOfWeek
    ___ setFirstDayOfWeek  dayOfWeek):
        __ dayOfWeek !_ self.__firstDayOfWeek:
            self.__firstDayOfWeek _ dayOfWeek
            __ self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    ___ resetFirstDayOfWeek(self):
        __ self.__firstDayOfWeek !_ __.Monday:
            self.__firstDayOfWeek _ __.Monday
            __ self.__cw:
                self.__cw.setFirstDayOfWeek(__.Monday)
    firstDayOfWeek _ pyqtProperty(__.DayOfWeek,
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
        r_ self.__gridVisible
    ___ setGridVisible  show):
        __ show !_ self.__gridVisible:
            self.__gridVisible _ show
            __ self.__cw:
                self.__cw.setGridVisible(show)
    ___ resetGridVisible(self):
        __ self.__gridVisible !_ False:
            self.__gridVisible _ False
            __ self.__cw:
                self.__cw.setGridVisible F..
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
        r_ self.__horizontalHeaderFormat
    ___ setHorizontalHeaderFormat  format):
        __ format !_ self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat _ format
            __ self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    ___ resetHorizontalHeaderFormat(self):
        __ self.__horizontalHeaderFormat !_ QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
            __ self.__cw:
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
        r_ self.__verticalHeaderFormat
    ___ setVerticalHeaderFormat  format):
        __ format !_ self.__verticalHeaderFormat:
            self.__verticalHeaderFormat _ format
            __ self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    ___ resetVerticalHeaderFormat(self):
        __ self.__verticalHeaderFormat !_ QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
            __ self.__cw:
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
        r_ self.__navigationBarVisible
    ___ setNavigationBarVisible  visible):
        __ visible !_ self.__navigationBarVisible:
            self.__navigationBarVisible _ visible
            __ self.__cw:
                self.__cw.setNavigationBarVisible(visible)
    ___ resetNavigationBarVisible(self):
        __ self.__navigationBarVisible !_ T..
            self.__navigationBarVisible _ True
            __ self.__cw:
                self.__cw.setNavigationBarVisible(True)
    navigationBarVisible _ pyqtProperty(bool,
                                               fget_isNavigationBarVisible,
                                               fset_setNavigationBarVisible,
                                               freset_resetNavigationBarVisible)


#============================================================================#
# PyDateTimeEdit                                                             #
#----------------------------------------------------------------------------#
c_ PyDateTimeEdit(QDateTimeEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    ___ __init__  *args):
        super(PyDateTimeEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw _ N..
        self.__firstDayOfWeek _ __.Monday
        self.__gridVisible _ False
        self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible _ True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    ___ mousePressEvent  event):
        super(PyDateTimeEdit, self).mousePressEvent(event)

        __ no. self.__cw:
            self.__cw _ self.findChild(QCalendarWidget)
            __ self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    ___ getCalendarPopup(self):
        r_ True
    calendarPopup _ pyqtProperty(bool, fget_getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    ___ getFirstDayOfWeek(self):
        r_ self.__firstDayOfWeek
    ___ setFirstDayOfWeek  dayOfWeek):
        __ dayOfWeek !_ self.__firstDayOfWeek:
            self.__firstDayOfWeek _ dayOfWeek
            __ self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    ___ resetFirstDayOfWeek(self):
        __ self.__firstDayOfWeek !_ __.Monday:
            self.__firstDayOfWeek _ __.Monday
            __ self.__cw:
                self.__cw.setFirstDayOfWeek(__.Monday)
    firstDayOfWeek _ pyqtProperty(__.DayOfWeek,
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
        r_ self.__gridVisible
    ___ setGridVisible  show):
        __ show !_ self.__gridVisible:
            self.__gridVisible _ show
            __ self.__cw:
                self.__cw.setGridVisible(show)
    ___ resetGridVisible(self):
        __ self.__gridVisible !_ False:
            self.__gridVisible _ False
            __ self.__cw:
                self.__cw.setGridVisible F..
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
        r_ self.__horizontalHeaderFormat
    ___ setHorizontalHeaderFormat  format):
        __ format !_ self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat _ format
            __ self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    ___ resetHorizontalHeaderFormat(self):
        __ self.__horizontalHeaderFormat !_ QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
            __ self.__cw:
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
        r_ self.__verticalHeaderFormat
    ___ setVerticalHeaderFormat  format):
        __ format !_ self.__verticalHeaderFormat:
            self.__verticalHeaderFormat _ format
            __ self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    ___ resetVerticalHeaderFormat(self):
        __ self.__verticalHeaderFormat !_ QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
            __ self.__cw:
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
        r_ self.__navigationBarVisible
    ___ setNavigationBarVisible  visible):
        __ visible !_ self.__navigationBarVisible:
            self.__navigationBarVisible _ visible
            __ self.__cw:
                self.__cw.setNavigationBarVisible(visible)
    ___ resetNavigationBarVisible(self):
        __ self.__navigationBarVisible !_ T..
            self.__navigationBarVisible _ True
            __ self.__cw:
                self.__cw.setNavigationBarVisible(True)
    navigationBarVisible _ pyqtProperty(bool,
                                               fget_isNavigationBarVisible,
                                               fset_setNavigationBarVisible,
                                               freset_resetNavigationBarVisible)


__ __name__ == "__main__":

    ______ sys

    app _ ?A..(sys.argv)

    w _ ?W..
    lay _ QHBoxLayout()

    lay.aW..(PyDateEdit())
    lay.aW..(PyDateTimeEdit())

    w.sL..(lay)
    w.s..

    sys.exit(app.exec_())

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
