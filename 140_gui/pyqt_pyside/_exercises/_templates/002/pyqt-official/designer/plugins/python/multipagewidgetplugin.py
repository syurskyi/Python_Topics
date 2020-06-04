#============================================================================#
# PyQt5 port of the designer/containerextension example from Qt v4.x         #
#----------------------------------------------------------------------------#
______ sip
____ ?.?G.. ______ ?I..
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
    ___  -   widget, parent_None):
        s__(MultiPageWidgetContainerExtension, self). - (parent)

        _widget _ widget
            
    ___ aW..  widget):
        _widget.addPage(widget)
    
    ___ count
        r_ _widget.count()
    
    ___ currentIndex
        r_ _widget.getCurrentIndex()
    
    ___ insertWidget  index, widget):
        _widget.insertPage(index, widget)
    
    ___ remove  index):
        _widget.removePage(index)
    
    ___ sCI..  index):
        _widget.sCI..(index)
    
    ___ widget  index):
        r_ _widget.widget(index)
    

#============================================================================#
# ExtensionFactory                                                           #
#----------------------------------------------------------------------------#
c_ MultiPageWidgetExtensionFactory(QExtensionFactory):
    ___  -   parent_None):
        s__(MultiPageWidgetExtensionFactory, self). - (parent)

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

    ___  -   parent_None):
        s__(MultiPageWidgetPlugin, self). - (parent)

        initialized _ F..

    ___ initialize  formEditor):
        __ initialized:
            r_
        manager _ formEditor.extensionManager()
        __ manager:
            factory _ MultiPageWidgetExtensionFactory(manager)
            manager.registerExtensions(factory, Q_TYPEID['QDesignerContainerExtension'])
        initialized _ T..

    ___ isInitialized
        r_ initialized

    ___ createWidget  parent):
        widget _ PyMultiPageWidget(parent)
        widget.currentIndexChanged.c..(currentIndexChanged)
        widget.pageTitleChanged.c..(pageTitleChanged)
        r_ widget

    ___ name
        r_ "PyMultiPageWidget"

    ___ group
        r_ "PyQt Examples"

    ___ icon
        r_ ?I..

    ___ toolTip
        r_ ""

    ___ whatsThis
        r_ ""

    ___ isContainer
        r_ T..

    ___ domXml
        r_ ('<widget class="PyMultiPageWidget" name="multipagewidget">'
                '  <widget class="QWidget" name="page" />'
                '</widget>')

    ___ includeFile
        r_ "multipagewidget"

    ___ currentIndexChanged  index):
        widget _ sender()
        __ widget and isinstance(widget, PyMultiPageWidget):
            form _ QDesignerFormWindowInterface.findFormWindow(widget)
            __ form:
                form.e..SelectionChanged()

    ___ pageTitleChanged  title):
        widget _ sender()
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
                sheet.setChanged(propertyIndex,  st.

#============================================================================#
# EOF                                                                        #
#----------------------------------------------------------------------------#
