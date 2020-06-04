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

____ ?.?C.. ______ pP.., __
____ ?.?W.. ______ (?A.., QCalendarWidget, ?DE..,
        ?DTE.., ?HBL.., ?W..)


#============================================================================#
# PyDateEdit                                                                 #
#----------------------------------------------------------------------------#
c_ PyDateEdit(?DE..):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    ___  -   *args):
        s__(PyDateEdit, self). - (*args)

        setCalendarPopup( st.
        __cw _ N..
        __firstDayOfWeek _ __.Monday
        __gridVisible _ F..
        __horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
        __verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
        __navigationBarVisible _ T..

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    ___ mousePressEvent  event):
        s__(PyDateEdit, self).mousePressEvent(event)

        __ no. __cw:
            __cw _ findChild(QCalendarWidget)
            __ __cw:
                __cw.setFirstDayOfWeek(__firstDayOfWeek)
                __cw.setGridVisible(__gridVisible)
                __cw.setHorizontalHeaderFormat(__horizontalHeaderFormat)
                __cw.setVerticalHeaderFormat(__verticalHeaderFormat)
                __cw.setNavigationBarVisible(__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    ___ getCalendarPopup
        r_ T..
    calendarPopup _ pP..(bool, fget_getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    ___ getFirstDayOfWeek
        r_ __firstDayOfWeek
    ___ setFirstDayOfWeek  dayOfWeek):
        __ dayOfWeek !_ __firstDayOfWeek:
            __firstDayOfWeek _ dayOfWeek
            __ __cw:
                __cw.setFirstDayOfWeek(dayOfWeek)
    ___ resetFirstDayOfWeek
        __ __firstDayOfWeek !_ __.Monday:
            __firstDayOfWeek _ __.Monday
            __ __cw:
                __cw.setFirstDayOfWeek(__.Monday)
    firstDayOfWeek _ pP..(__.DayOfWeek,
                                         fget_getFirstDayOfWeek,
                                         fset_setFirstDayOfWeek,
                                         freset_resetFirstDayOfWeek)

    #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    ___ isGridVisible
        r_ __gridVisible
    ___ setGridVisible  show):
        __ show !_ __gridVisible:
            __gridVisible _ show
            __ __cw:
                __cw.setGridVisible(show)
    ___ resetGridVisible
        __ __gridVisible !_ F..:
            __gridVisible _ F..
            __ __cw:
                __cw.setGridVisible F..
    gridVisible _ pP..(bool,
                                      fget_isGridVisible,
                                      fset_setGridVisible,
                                      freset_resetGridVisible)

    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    ___ getHorizontalHeaderFormat
        r_ __horizontalHeaderFormat
    ___ setHorizontalHeaderFormat  f..):
        __ f.. !_ __horizontalHeaderFormat:
            __horizontalHeaderFormat _ f..
            __ __cw:
                __cw.setHorizontalHeaderFormat(f..)
    ___ resetHorizontalHeaderFormat
        __ __horizontalHeaderFormat !_ QCalendarWidget.ShortDayNames:
            __horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
            __ __cw:
                __cw.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
    horizontalHeaderFormat _ pP..(QCalendarWidget.HorizontalHeaderFormat,
                                                 fget_getHorizontalHeaderFormat,
                                                 fset_setHorizontalHeaderFormat,
                                                 freset_resetHorizontalHeaderFormat)

    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    ___ getVerticalHeaderFormat
        r_ __verticalHeaderFormat
    ___ setVerticalHeaderFormat  f..):
        __ f.. !_ __verticalHeaderFormat:
            __verticalHeaderFormat _ f..
            __ __cw:
                __cw.setVerticalHeaderFormat(f..)
    ___ resetVerticalHeaderFormat
        __ __verticalHeaderFormat !_ QCalendarWidget.ISOWeekNumbers:
            __verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
            __ __cw:
                __cw.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
    verticalHeaderFormat _ pP..(QCalendarWidget.VerticalHeaderFormat,
                                               fget_getVerticalHeaderFormat,
                                               fset_setVerticalHeaderFormat,
                                               freset_resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    ___ isNavigationBarVisible
        r_ __navigationBarVisible
    ___ setNavigationBarVisible  visible):
        __ visible !_ __navigationBarVisible:
            __navigationBarVisible _ visible
            __ __cw:
                __cw.setNavigationBarVisible(visible)
    ___ resetNavigationBarVisible
        __ __navigationBarVisible !_ T..
            __navigationBarVisible _ T..
            __ __cw:
                __cw.setNavigationBarVisible( st.
    navigationBarVisible _ pP..(bool,
                                               fget_isNavigationBarVisible,
                                               fset_setNavigationBarVisible,
                                               freset_resetNavigationBarVisible)


#============================================================================#
# PyDateTimeEdit                                                             #
#----------------------------------------------------------------------------#
c_ PyDateTimeEdit(?DTE..):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    ___  -   *args):
        s__(PyDateTimeEdit, self). - (*args)

        setCalendarPopup( st.
        __cw _ N..
        __firstDayOfWeek _ __.Monday
        __gridVisible _ F..
        __horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
        __verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
        __navigationBarVisible _ T..

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    ___ mousePressEvent  event):
        s__(PyDateTimeEdit, self).mousePressEvent(event)

        __ no. __cw:
            __cw _ findChild(QCalendarWidget)
            __ __cw:
                __cw.setFirstDayOfWeek(__firstDayOfWeek)
                __cw.setGridVisible(__gridVisible)
                __cw.setHorizontalHeaderFormat(__horizontalHeaderFormat)
                __cw.setVerticalHeaderFormat(__verticalHeaderFormat)
                __cw.setNavigationBarVisible(__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    ___ getCalendarPopup
        r_ T..
    calendarPopup _ pP..(bool, fget_getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    ___ getFirstDayOfWeek
        r_ __firstDayOfWeek
    ___ setFirstDayOfWeek  dayOfWeek):
        __ dayOfWeek !_ __firstDayOfWeek:
            __firstDayOfWeek _ dayOfWeek
            __ __cw:
                __cw.setFirstDayOfWeek(dayOfWeek)
    ___ resetFirstDayOfWeek
        __ __firstDayOfWeek !_ __.Monday:
            __firstDayOfWeek _ __.Monday
            __ __cw:
                __cw.setFirstDayOfWeek(__.Monday)
    firstDayOfWeek _ pP..(__.DayOfWeek,
                                         fget_getFirstDayOfWeek,
                                         fset_setFirstDayOfWeek,
                                         freset_resetFirstDayOfWeek)

    #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    ___ isGridVisible
        r_ __gridVisible
    ___ setGridVisible  show):
        __ show !_ __gridVisible:
            __gridVisible _ show
            __ __cw:
                __cw.setGridVisible(show)
    ___ resetGridVisible
        __ __gridVisible !_ F..:
            __gridVisible _ F..
            __ __cw:
                __cw.setGridVisible F..
    gridVisible _ pP..(bool,
                                      fget_isGridVisible,
                                      fset_setGridVisible,
                                      freset_resetGridVisible)

    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    ___ getHorizontalHeaderFormat
        r_ __horizontalHeaderFormat
    ___ setHorizontalHeaderFormat  f..):
        __ f.. !_ __horizontalHeaderFormat:
            __horizontalHeaderFormat _ f..
            __ __cw:
                __cw.setHorizontalHeaderFormat(f..)
    ___ resetHorizontalHeaderFormat
        __ __horizontalHeaderFormat !_ QCalendarWidget.ShortDayNames:
            __horizontalHeaderFormat _ QCalendarWidget.ShortDayNames
            __ __cw:
                __cw.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
    horizontalHeaderFormat _ pP..(QCalendarWidget.HorizontalHeaderFormat,
                                                 fget_getHorizontalHeaderFormat,
                                                 fset_setHorizontalHeaderFormat,
                                                 freset_resetHorizontalHeaderFormat)

    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    ___ getVerticalHeaderFormat
        r_ __verticalHeaderFormat
    ___ setVerticalHeaderFormat  f..):
        __ f.. !_ __verticalHeaderFormat:
            __verticalHeaderFormat _ f..
            __ __cw:
                __cw.setVerticalHeaderFormat(f..)
    ___ resetVerticalHeaderFormat
        __ __verticalHeaderFormat !_ QCalendarWidget.ISOWeekNumbers:
            __verticalHeaderFormat _ QCalendarWidget.ISOWeekNumbers
            __ __cw:
                __cw.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)
    verticalHeaderFormat _ pP..(QCalendarWidget.VerticalHeaderFormat,
                                               fget_getVerticalHeaderFormat,
                                               fset_setVerticalHeaderFormat,
                                               freset_resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    ___ isNavigationBarVisible
        r_ __navigationBarVisible
    ___ setNavigationBarVisible  visible):
        __ visible !_ __navigationBarVisible:
            __navigationBarVisible _ visible
            __ __cw:
                __cw.setNavigationBarVisible(visible)
    ___ resetNavigationBarVisible
        __ __navigationBarVisible !_ T..
            __navigationBarVisible _ T..
            __ __cw:
                __cw.setNavigationBarVisible( st.
    navigationBarVisible _ pP..(bool,
                                               fget_isNavigationBarVisible,
                                               fset_setNavigationBarVisible,
                                               freset_resetNavigationBarVisible)


__ __name__ __ "__main__":

    ______ ___

    app _ ?A..(___.a..

    w _ ?W..
    lay _ ?HBL..

    lay.aW..(PyDateEdit())
    lay.aW..(PyDateTimeEdit())

    w.sL..(lay)
    w.s..

    ___.e.. ?.e..

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
