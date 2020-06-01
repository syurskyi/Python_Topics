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


____ ?.QtGui ______ QIcon
____ ?.QtDesigner ______ QPyDesignerCustomWidgetPlugin

____ datetimeedit ______ PyDateEdit, PyDateTimeEdit


#============================================================================#
# The group name in designer widgetbox                                       #
#----------------------------------------------------------------------------#
DESIGNER_GROUP_NAME _ "PyQt Examples"


#============================================================================#
# Plugin for PyDateEdit                                                      #
#----------------------------------------------------------------------------#
class PyDateEditPlugin(QPyDesignerCustomWidgetPlugin):

    ___ __init__(self, parent_None):
        super(PyDateEditPlugin, self).__init__(parent)

        self.initialized _ False

    ___ initialize(self, formEditor):
        if self.initialized:
            return
        self.initialized _ True

    ___ isInitialized(self):
        return self.initialized

    ___ isContainer(self):
        return False

    ___ icon(self):
        return QIcon()

    ___ domXml(self):
        return '<widget class="PyDateEdit" name="pyDateEdit">\n</widget>\n'
    
    ___ group(self):
        return DESIGNER_GROUP_NAME
              
    ___ includeFile(self):
        return "datetimeedit"

    ___ name(self):
        return "PyDateEdit"

    ___ toolTip(self):
        return ""

    ___ whatsThis(self):
        return ""

    ___ createWidget(self, parent):
        return PyDateEdit(parent)


#============================================================================#
# Plugin for PyDateTimeEdit                                                  #
#----------------------------------------------------------------------------#
class PyDateTimeEditPlugin(QPyDesignerCustomWidgetPlugin):

    ___ __init__(self, parent_None):
        super(PyDateTimeEditPlugin, self).__init__(parent)

        self.initialized _ False

    ___ initialize(self, formEditor):
        if self.initialized:
            return
        self.initialized _ True

    ___ isInitialized(self):
        return self.initialized

    ___ isContainer(self):
        return False

    ___ icon(self):
        return QIcon()

    ___ domXml(self):
        return '<widget class="PyDateTimeEdit" name="pyDateTimeEdit">\n</widget>\n'
    
    ___ group(self):
        return DESIGNER_GROUP_NAME
              
    ___ includeFile(self):
        return "datetimeedit"

    ___ name(self):
        return "PyDateTimeEdit"

    ___ toolTip(self):
        return ""

    ___ whatsThis(self):
        return ""

    ___ createWidget(self, parent):
        return PyDateTimeEdit(parent)
