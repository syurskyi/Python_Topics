#============================================================================#
# Designer plugins for PyDateEdit and PyDateTimeEdit                         #
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


____ ?.?G.. ______ ?I..
____ ?.QtDesigner ______ QPyDesignerCustomWidgetPlugin

____ datetimeedit ______ PyDateEdit, PyDateTimeEdit


#============================================================================#
# The group name in designer widgetbox                                       #
#----------------------------------------------------------------------------#
DESIGNER_GROUP_NAME _ "PyQt Examples"


#============================================================================#
# Plugin for PyDateEdit                                                      #
#----------------------------------------------------------------------------#
c_ PyDateEditPlugin(QPyDesignerCustomWidgetPlugin):

    ___  -   parent_None):
        s__(PyDateEditPlugin, self). - (parent)

        initialized _ F..

    ___ initialize  formEditor):
        __ initialized:
            r_
        initialized _ T..

    ___ isInitialized 
        r_ initialized

    ___ isContainer 
        r_ F..

    ___ icon 
        r_ ?I..

    ___ domXml 
        r_ '<widget class="PyDateEdit" name="pyDateEdit">\n</widget>\n'
    
    ___ group 
        r_ DESIGNER_GROUP_NAME
              
    ___ includeFile 
        r_ "datetimeedit"

    ___ name 
        r_ "PyDateEdit"

    ___ toolTip 
        r_ ""

    ___ whatsThis 
        r_ ""

    ___ createWidget  parent):
        r_ PyDateEdit(parent)


#============================================================================#
# Plugin for PyDateTimeEdit                                                  #
#----------------------------------------------------------------------------#
c_ PyDateTimeEditPlugin(QPyDesignerCustomWidgetPlugin):

    ___  -   parent_None):
        s__(PyDateTimeEditPlugin, self). - (parent)

        initialized _ F..

    ___ initialize  formEditor):
        __ initialized:
            r_
        initialized _ T..

    ___ isInitialized 
        r_ initialized

    ___ isContainer 
        r_ F..

    ___ icon 
        r_ ?I..

    ___ domXml 
        r_ '<widget class="PyDateTimeEdit" name="pyDateTimeEdit">\n</widget>\n'
    
    ___ group 
        r_ DESIGNER_GROUP_NAME
              
    ___ includeFile 
        r_ "datetimeedit"

    ___ name 
        r_ "PyDateTimeEdit"

    ___ toolTip 
        r_ ""

    ___ whatsThis 
        r_ ""

    ___ createWidget  parent):
        r_ PyDateTimeEdit(parent)
