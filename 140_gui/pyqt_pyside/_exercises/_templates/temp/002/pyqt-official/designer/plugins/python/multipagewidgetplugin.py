#============================================================================#
# PyQt5 port of the designer/containerextension example from Qt v4.x         #
#----------------------------------------------------------------------------#
______ sip
____ ?.?G.. ______ QIcon
____ ?.QtDesigner ______ (QDesignerFormWindowInterface, QExtensionFactory,
        QPyDesignerContainerExtension, QPyDesignerCustomWidgetPlugin,
        QPyDesignerPropertySheetExtension)

____ multipagewidget ______ PyMultiPageWidget


Q_TYPEID _ {
    'QDesignerContainerExtension':     'org.qt-project.Qt.Designer.Container',
    'QDesignerPropertySheetExtension': 'org.qt-project.Qt.Designer.PropertySheet'
}


#============================================================================#
# ContainerExtension                                                         #
#----------------------------------------------------------------------------#
c_ MultiPageWidgetContainerExtension(QPyDesignerContainerExtension):
    ___ __init__  widget, parent_None):
        super(MultiPageWidgetContainerExtension, self).__init__(parent)

        self._widget _ widget
            
    ___ aW..  widget):
        self._widget.addPage(widget)
    
    ___ count(self):
        r_ self._widget.count()
    
    ___ currentIndex(self):
        r_ self._widget.getCurrentIndex()
    
    ___ insertWidget  index, widget):
        self._widget.insertPage(index, widget)
    
    ___ remove  index):
        self._widget.removePage(index)
    
    ___ setCurrentIndex  index):
        self._widget.setCurrentIndex(index)
    
    ___ widget  index):
        r_ self._widget.widget(index)
    

#============================================================================#
# ExtensionFactory                                                           #
#----------------------------------------------------------------------------#
c_ MultiPageWidgetExtensionFactory(QExtensionFactory):
    ___ __init__  parent_None):
        super(MultiPageWidgetExtensionFactory, self).__init__(parent)

    ___ createExtension  obj, iid, parent):
        __ iid !_ Q_TYPEID['QDesignerContainerExtension']:
            r_ N..
        __ isinstance(obj, PyMultiPageWidget):
            r_ MultiPageWidgetContainerExtension(obj, parent)
        r_ N..


#============================================================================#
# CustomWidgetPlugin                                                         #
#----------------------------------------------------------------------------#
c_ MultiPageWidgetPlugin(QPyDesignerCustomWidgetPlugin):

    ___ __init__  parent_None):
        super(MultiPageWidgetPlugin, self).__init__(parent)

        self.initialized _ False

    ___ initialize  formEditor):
        __ self.initialized:
            r_
        manager _ formEditor.extensionManager()
        __ manager:
            self.factory _ MultiPageWidgetExtensionFactory(manager)
            manager.registerExtensions(self.factory, Q_TYPEID['QDesignerContainerExtension'])
        self.initialized _ True

    ___ isInitialized(self):
        r_ self.initialized

    ___ createWidget  parent):
        widget _ PyMultiPageWidget(parent)
        widget.currentIndexChanged.c..(self.currentIndexChanged)
        widget.pageTitleChanged.c..(self.pageTitleChanged)
        r_ widget

    ___ name(self):
        r_ "PyMultiPageWidget"

    ___ group(self):
        r_ "PyQt Examples"

    ___ icon(self):
        r_ QIcon()

    ___ toolTip(self):
        r_ ""

    ___ whatsThis(self):
        r_ ""

    ___ isContainer(self):
        r_ True

    ___ domXml(self):
        r_ ('<widget class="PyMultiPageWidget" name="multipagewidget">'
                '  <widget class="QWidget" name="page" />'
                '</widget>')

    ___ includeFile(self):
        r_ "multipagewidget"

    ___ currentIndexChanged  index):
        widget _ self.sender()
        __ widget and isinstance(widget, PyMultiPageWidget):
            form _ QDesignerFormWindowInterface.findFormWindow(widget)
            __ form:
                form.emitSelectionChanged()

    ___ pageTitleChanged  title):
        widget _ self.sender()
        __ widget and isinstance(widget, PyMultiPageWidget):
            page _ widget.widget(widget.getCurrentIndex())
            form _ QDesignerFormWindowInterface.findFormWindow(widget)
            __ form:
                editor _ form.core()
                manager _ editor.extensionManager()
                sheet _ manager.extension(page, Q_TYPEID['QDesignerPropertySheetExtension'])
                # This explicit cast is necessary here
                sheet _ sip.cast(sheet, QPyDesignerPropertySheetExtension)
                propertyIndex _ sheet.indexOf('windowTitle')
                sheet.setChanged(propertyIndex, True)

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
