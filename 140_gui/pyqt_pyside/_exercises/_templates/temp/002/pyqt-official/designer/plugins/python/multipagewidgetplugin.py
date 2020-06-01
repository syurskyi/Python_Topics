#============================================================================#
# PyQt5 port of the designer/containerextension example from Qt v4.x         #
#----------------------------------------------------------------------------#
______ sip
____ ?.QtGui ______ QIcon
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
class MultiPageWidgetContainerExtension(QPyDesignerContainerExtension):
    ___ __init__(self, widget, parent_None):
        super(MultiPageWidgetContainerExtension, self).__init__(parent)

        self._widget _ widget
            
    ___ addWidget(self, widget):
        self._widget.addPage(widget)
    
    ___ count(self):
        return self._widget.count()
    
    ___ currentIndex(self):
        return self._widget.getCurrentIndex()
    
    ___ insertWidget(self, index, widget):
        self._widget.insertPage(index, widget)
    
    ___ remove(self, index):
        self._widget.removePage(index)
    
    ___ setCurrentIndex(self, index):
        self._widget.setCurrentIndex(index)
    
    ___ widget(self, index):
        return self._widget.widget(index)
    

#============================================================================#
# ExtensionFactory                                                           #
#----------------------------------------------------------------------------#
class MultiPageWidgetExtensionFactory(QExtensionFactory):
    ___ __init__(self, parent_None):
        super(MultiPageWidgetExtensionFactory, self).__init__(parent)

    ___ createExtension(self, obj, iid, parent):
        if iid !_ Q_TYPEID['QDesignerContainerExtension']:
            return None
        if isinstance(obj, PyMultiPageWidget):
            return MultiPageWidgetContainerExtension(obj, parent)
        return None


#============================================================================#
# CustomWidgetPlugin                                                         #
#----------------------------------------------------------------------------#
class MultiPageWidgetPlugin(QPyDesignerCustomWidgetPlugin):

    ___ __init__(self, parent_None):
        super(MultiPageWidgetPlugin, self).__init__(parent)

        self.initialized _ False

    ___ initialize(self, formEditor):
        if self.initialized:
            return
        manager _ formEditor.extensionManager()
        if manager:
            self.factory _ MultiPageWidgetExtensionFactory(manager)
            manager.registerExtensions(self.factory, Q_TYPEID['QDesignerContainerExtension'])
        self.initialized _ True

    ___ isInitialized(self):
        return self.initialized

    ___ createWidget(self, parent):
        widget _ PyMultiPageWidget(parent)
        widget.currentIndexChanged.c..(self.currentIndexChanged)
        widget.pageTitleChanged.c..(self.pageTitleChanged)
        return widget

    ___ name(self):
        return "PyMultiPageWidget"

    ___ group(self):
        return "PyQt Examples"

    ___ icon(self):
        return QIcon()

    ___ toolTip(self):
        return ""

    ___ whatsThis(self):
        return ""

    ___ isContainer(self):
        return True

    ___ domXml(self):
        return ('<widget class="PyMultiPageWidget" name="multipagewidget">'
                '  <widget class="QWidget" name="page" />'
                '</widget>')

    ___ includeFile(self):
        return "multipagewidget"

    ___ currentIndexChanged(self, index):
        widget _ self.sender()
        if widget and isinstance(widget, PyMultiPageWidget):
            form _ QDesignerFormWindowInterface.findFormWindow(widget)
            if form:
                form.emitSelectionChanged()

    ___ pageTitleChanged(self, title):
        widget _ self.sender()
        if widget and isinstance(widget, PyMultiPageWidget):
            page _ widget.widget(widget.getCurrentIndex())
            form _ QDesignerFormWindowInterface.findFormWindow(widget)
            if form:
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
