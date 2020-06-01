#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


______ ___

____ ?.?C.. ______ (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,
        QRegExp, QSettings, QSize, __, QTime, QTimer)
____ ?.?G.. ______ ?C.., QIcon, QRegExpValidator, QValidator
____ ?.?W.. ______ (QAbstractItemView, ?A.., ?A..,
        QComboBox, QDialog, QDialogButtonBox, ?FD.., QGridLayout,
        QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,
        QMainWindow, ?MB.., QStyle, QStyleOptionViewItem, QTableWidget,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout)


c_ MainWindow ?MW..
    ___  -   parent_None):
        super(MainWindow, self). - (parent)

        settingsTree _ SettingsTree()
        sCW..(settingsTree)

        locationDialog _ N..

        createActions()
        createMenus()

        autoRefreshAct.setChecked(True)
        fallbacksAct.setChecked(True)

        setWindowTitle("Settings Editor")
        resize(500, 600)

    ___ openSettings
        __ locationDialog __ N..:
            locationDialog _ LocationDialog

        __ locationDialog.exec_
            settings _ QSettings(locationDialog.format(),
                                        locationDialog.scope(),
                                        locationDialog.organization(),
                                        locationDialog.application())
            setSettingsObject(settings)
            fallbacksAct.setEnabled(True)

    ___ openIniFile
        fileName, _ _ ?FD...gOFN..  "Open INI File", '',
                "INI Files (*.ini *.conf)")

        __ fileName:
            settings _ QSettings(fileName, QSettings.IniFormat)
            setSettingsObject(settings)
            fallbacksAct.setEnabled F..

    ___ openPropertyList
        fileName, _ _ ?FD...gOFN..  "Open Property List",
                '', "Property List Files (*.plist)")

        __ fileName:
            settings _ QSettings(fileName, QSettings.NativeFormat)
            setSettingsObject(settings)
            fallbacksAct.setEnabled F..

    ___ openRegistryPath
        path, ok _ QInputDialog.getText  "Open Registry Path",
                "Enter the path in the Windows registry:", QLineEdit.Normal,
                'HKEY_CURRENT_USER\\')

        __ ok and path !_ '':
            settings _ QSettings(path, QSettings.NativeFormat)
            setSettingsObject(settings)
            fallbacksAct.setEnabled F..

    ___ about
        ?MB...about  "About Settings Editor",
                "The <b>Settings Editor</b> example shows how to access "
                "application settings using Qt.")

    ___ createActions
        openSettingsAct _ ?A..("&Open Application Settings...", self,
                shortcut_"Ctrl+O", triggered_self.openSettings)

        openIniFileAct _ ?A..("Open I&NI File...", self,
                shortcut_"Ctrl+N", triggered_self.openIniFile)

        openPropertyListAct _ ?A..("Open Mac &Property List...", self,
                shortcut_"Ctrl+P", triggered_self.openPropertyList)
        __ ___.platform !_ 'darwin':
            openPropertyListAct.setEnabled F..

        openRegistryPathAct _ ?A..("Open Windows &Registry Path...",
                self, shortcut_"Ctrl+G", triggered_self.openRegistryPath)
        __ ___.platform !_ 'win32':
            openRegistryPathAct.setEnabled F..

        refreshAct _ ?A..("&Refresh", self, shortcut_"Ctrl+R",
                enabled_False, triggered_self.settingsTree.refresh)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        autoRefreshAct _ ?A..("&Auto-Refresh", self, shortcut_"Ctrl+A",
                checkable_True, enabled_False)
        autoRefreshAct.t__.c..(settingsTree.setAutoRefresh)
        autoRefreshAct.t__.c..(refreshAct.setDisabled)

        fallbacksAct _ ?A..("&Fallbacks", self, shortcut_"Ctrl+F",
                checkable_True, enabled_False,
                triggered_self.settingsTree.setFallbacksEnabled)

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(openSettingsAct)
        fileMenu.aA..(openIniFileAct)
        fileMenu.aA..(openPropertyListAct)
        fileMenu.aA..(openRegistryPathAct)
        fileMenu.addSeparator()
        fileMenu.aA..(refreshAct)
        fileMenu.addSeparator()
        fileMenu.aA..(exitAct)

        optionsMenu _ mB.. .aM..("&Options")
        optionsMenu.aA..(autoRefreshAct)
        optionsMenu.aA..(fallbacksAct)

        mB.. .addSeparator()

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ setSettingsObject  settings):
        settings.setFallbacksEnabled(fallbacksAct.isChecked())
        settingsTree.setSettingsObject(settings)

        refreshAct.setEnabled(True)
        autoRefreshAct.setEnabled(True)

        niceName _ settings.fileName()
        niceName.replace('\\', '/')
        niceName _ niceName.split('/')[-1]

        __ no. settings.isWritable
            niceName +_ " (read only)"

        setWindowTitle("%s - Settings Editor" % niceName)


c_ LocationDialog(QDialog):
    ___  -   parent_None):
        super(LocationDialog, self). - (parent)

        formatComboBox _ QComboBox()
        formatComboBox.addItem("Native")
        formatComboBox.addItem("INI")

        scopeComboBox _ QComboBox()
        scopeComboBox.addItem("User")
        scopeComboBox.addItem("System")

        organizationComboBox _ QComboBox()
        organizationComboBox.addItem("Trolltech")
        organizationComboBox.setEditable(True)

        applicationComboBox _ QComboBox()
        applicationComboBox.addItem("Any")
        applicationComboBox.addItem("Application Example")
        applicationComboBox.addItem("Assistant")
        applicationComboBox.addItem("Designer")
        applicationComboBox.addItem("Linguist")
        applicationComboBox.setEditable(True)
        applicationComboBox.setCurrentIndex(3)

        formatLabel _ QLabel("&Format:")
        formatLabel.setBuddy(formatComboBox)

        scopeLabel _ QLabel("&Scope:")
        scopeLabel.setBuddy(scopeComboBox)

        organizationLabel _ QLabel("&Organization:")
        organizationLabel.setBuddy(organizationComboBox)

        applicationLabel _ QLabel("&Application:")
        applicationLabel.setBuddy(applicationComboBox)

        locationsGroupBox _ QGroupBox("Setting Locations")

        locationsTable _ QTableWidget()
        locationsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        locationsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        locationsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        locationsTable.setColumnCount(2)
        locationsTable.setHorizontalHeaderLabels(("Location", "Access"))
        locationsTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        locationsTable.horizontalHeader().resizeSection(1, 180)

        buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        formatComboBox.activated.c..(updateLocationsTable)
        scopeComboBox.activated.c..(updateLocationsTable)
        organizationComboBox.lineEdit().editingFinished.c..(updateLocationsTable)
        applicationComboBox.lineEdit().editingFinished.c..(updateLocationsTable)
        buttonBox.accepted.c..(accept)
        buttonBox.rejected.c..(reject)

        locationsLayout _ ?VBL..
        locationsLayout.aW..(locationsTable)
        locationsGroupBox.sL..(locationsLayout)

        mainLayout _ QGridLayout()
        mainLayout.aW..(formatLabel, 0, 0)
        mainLayout.aW..(formatComboBox, 0, 1)
        mainLayout.aW..(scopeLabel, 1, 0)
        mainLayout.aW..(scopeComboBox, 1, 1)
        mainLayout.aW..(organizationLabel, 2, 0)
        mainLayout.aW..(organizationComboBox, 2, 1)
        mainLayout.aW..(applicationLabel, 3, 0)
        mainLayout.aW..(applicationComboBox, 3, 1)
        mainLayout.aW..(locationsGroupBox, 4, 0, 1, 2)
        mainLayout.aW..(buttonBox, 5, 0, 1, 2)
        sL..(mainLayout)

        updateLocationsTable()

        setWindowTitle("Open Application Settings")
        resize(650, 400)

    ___ format
        __ formatComboBox.currentIndex() == 0:
            r_ QSettings.NativeFormat
        ____
            r_ QSettings.IniFormat

    ___ scope
        __ scopeComboBox.currentIndex() == 0:
            r_ QSettings.UserScope
        ____
            r_ QSettings.SystemScope

    ___ organization
        r_ organizationComboBox.currentText()

    ___ application
        __ applicationComboBox.currentText() == "Any":
            r_ ''

        r_ applicationComboBox.currentText()

    ___ updateLocationsTable
        locationsTable.setUpdatesEnabled F..
        locationsTable.setRowCount(0)

        ___ i __ range(2):
            __ i == 0:
                __ scope() == QSettings.SystemScope:
                    continue

                actualScope _ QSettings.UserScope
            ____
                actualScope _ QSettings.SystemScope

            ___ j __ range(2):
                __ j == 0:
                    __ no. application
                        continue

                    actualApplication _ application()
                ____
                    actualApplication _ ''

                settings _ QSettings(format(), actualScope,
                        organization(), actualApplication)

                row _ locationsTable.rowCount()
                locationsTable.setRowCount(row + 1)

                item0 _ QTableWidgetItem()
                item0.sT..(settings.fileName())

                item1 _ QTableWidgetItem()
                disable _ no. (settings.childKeys() or settings.childGroups())

                __ row == 0:
                    __ settings.isWritable
                        item1.sT..("Read-write")
                        disable _ False
                    ____
                        item1.sT..("Read-only")
                    buttonBox.button(QDialogButtonBox.Ok).setDisabled(disable)
                ____
                    item1.sT..("Read-only fallback")

                __ disable:
                    item0.setFlags(item0.flags() & ~__.ItemIsEnabled)
                    item1.setFlags(item1.flags() & ~__.ItemIsEnabled)

                locationsTable.setItem(row, 0, item0)
                locationsTable.setItem(row, 1, item1)

        locationsTable.setUpdatesEnabled(True)


c_ SettingsTree(QTreeWidget):
    ___  -   parent_None):
        super(SettingsTree, self). - (parent)

        setItemDelegate(VariantDelegate(self))

        setHeaderLabels(("Setting", "Type", "Value"))
        header().setSectionResizeMode(0, QHeaderView.Stretch)
        header().setSectionResizeMode(2, QHeaderView.Stretch)

        settings _ N..
        refreshTimer _ ?T..
        refreshTimer.setInterval(2000)
        autoRefresh _ False

        groupIcon _ QIcon()
        groupIcon.addPixmap(style().standardPixmap(QStyle.SP_DirClosedIcon),
                QIcon.Normal, QIcon.Off)
        groupIcon.addPixmap(style().standardPixmap(QStyle.SP_DirOpenIcon),
                QIcon.Normal, QIcon.On)
        keyIcon _ QIcon()
        keyIcon.addPixmap(style().standardPixmap(QStyle.SP_FileIcon))

        refreshTimer.timeout.c..(maybeRefresh)

    ___ setSettingsObject  settings):
        settings _ settings
        clear()

        __ settings __ no. N..:
            settings.setParent
            refresh()
            __ autoRefresh:
                refreshTimer.start()
        ____
            refreshTimer.stop()

    ___ sizeHint
        r_ QSize(800, 600)

    ___ setAutoRefresh  autoRefresh):
        autoRefresh _ autoRefresh

        __ settings __ no. N..:
            __ autoRefresh:
                maybeRefresh()
                refreshTimer.start()
            ____
                refreshTimer.stop()

    ___ setFallbacksEnabled  enabled):
        __ settings __ no. N..:
            settings.setFallbacksEnabled(enabled)
            refresh()

    ___ maybeRefresh
        __ state() !_ QAbstractItemView.EditingState:
            refresh()

    ___ refresh
        __ settings __ N..:
            r_

        # The signal might not be connected.
        try:
            itemChanged.disconnect(updateSetting)
        except:
            pass

        settings.sync()
        updateChildItems(N..)

        itemChanged.c..(updateSetting)

    ___ event  event):
        __ event.type() == QEvent.WindowActivate:
            __ isActiveWindow() and autoRefresh:
                maybeRefresh()

        r_ super(SettingsTree, self).event(event)

    ___ updateSetting  item):
        key _ item.t__(0)
        ancestor _ item.parent()

        w__ ancestor:
            key _ ancestor.t__(0) + '/' + key
            ancestor _ ancestor.parent()

        d _ item.data(2, __.UserRole)
        settings.setValue(key, item.data(2, __.UserRole))

        __ autoRefresh:
            refresh()

    ___ updateChildItems  parent):
        dividerIndex _ 0

        ___ group __ settings.childGroups
            childIndex _ findChild(parent, group, dividerIndex)
            __ childIndex !_ -1:
                child _ childAt(parent, childIndex)
                child.sT..(1, '')
                child.sT..(2, '')
                child.setData(2, __.UserRole, N..)
                moveItemForward(parent, childIndex, dividerIndex)
            ____
                child _ createItem(group, parent, dividerIndex)

            child.setIcon(0, groupIcon)
            dividerIndex +_ 1

            settings.beginGroup(group)
            updateChildItems(child)
            settings.endGroup()

        ___ key __ settings.childKeys
            childIndex _ findChild(parent, key, 0)
            __ childIndex == -1 or childIndex >_ dividerIndex:
                __ childIndex !_ -1:
                    child _ childAt(parent, childIndex)
                    ___ i __ range(child.childCount()):
                        deleteItem(child, i)
                    moveItemForward(parent, childIndex, dividerIndex)
                ____
                    child _ createItem(key, parent, dividerIndex)
                child.setIcon(0, keyIcon)
                dividerIndex +_ 1
            ____
                child _ childAt(parent, childIndex)

            value _ settings.value(key)
            __ value __ N..:
                child.sT..(1, 'Invalid')
            ____
                child.sT..(1, value.__class__.__name__)
            child.sT..(2, VariantDelegate.displayText(value))
            child.setData(2, __.UserRole, value)

        w__ dividerIndex < childCount(parent):
            deleteItem(parent, dividerIndex)

    ___ createItem  t__, parent, index):
        after _ N..

        __ index !_ 0:
            after _ childAt(parent, index - 1)

        __ parent __ no. N..:
            item _ QTreeWidgetItem(parent, after)
        ____
            item _ QTreeWidgetItem  after)

        item.sT..(0, t__)
        item.setFlags(item.flags() | __.ItemIsEditable)
        r_ item

    ___ deleteItem  parent, index):
        __ parent __ no. N..:
            item _ parent.takeChild(index)
        ____
            item _ takeTopLevelItem(index)
        del item

    ___ childAt  parent, index):
        __ parent __ no. N..:
            r_ parent.child(index)
        ____
            r_ topLevelItem(index)

    ___ childCount  parent):
        __ parent __ no. N..:
            r_ parent.childCount()
        ____
            r_ topLevelItemCount()

    ___ findChild  parent, t__, startIndex):
        ___ i __ range(childCount(parent)):
            __ childAt(parent, i).t__(0) == t__:
                r_ i
        r_ -1

    ___ moveItemForward  parent, oldIndex, newIndex):
        ___ int __ range(oldIndex - newIndex):
            deleteItem(parent, newIndex)


c_ VariantDelegate(QItemDelegate):
    ___  -   parent_None):
        super(VariantDelegate, self). - (parent)

        boolExp _ QRegExp()
        boolExp.setPattern('true|false')
        boolExp.setCaseSensitivity(__.CaseInsensitive)

        byteArrayExp _ QRegExp()
        byteArrayExp.setPattern('[\\x00-\\xff]*')

        charExp _ QRegExp()
        charExp.setPattern('.')

        colorExp _ QRegExp()
        colorExp.setPattern('\\(([0-9]*),([0-9]*),([0-9]*),([0-9]*)\\)')

        doubleExp _ QRegExp()
        doubleExp.setPattern('')

        pointExp _ QRegExp()
        pointExp.setPattern('\\((-?[0-9]*),(-?[0-9]*)\\)')

        rectExp _ QRegExp()
        rectExp.setPattern('\\((-?[0-9]*),(-?[0-9]*),(-?[0-9]*),(-?[0-9]*)\\)')

        signedIntegerExp _ QRegExp()
        signedIntegerExp.setPattern('-?[0-9]*')

        sizeExp _ QRegExp(pointExp)

        unsignedIntegerExp _ QRegExp()
        unsignedIntegerExp.setPattern('[0-9]*')

        dateExp _ QRegExp()
        dateExp.setPattern('([0-9]{,4})-([0-9]{,2})-([0-9]{,2})')

        timeExp _ QRegExp()
        timeExp.setPattern('([0-9]{,2}):([0-9]{,2}):([0-9]{,2})')

        dateTimeExp _ QRegExp()
        dateTimeExp.setPattern(dateExp.pattern() + 'T' + timeExp.pattern())

    ___ paint  painter, option, index):
        __ index.column() == 2:
            value _ index.model().data(index, __.UserRole)
            __ no. isSupportedType(value):
                myOption _ QStyleOptionViewItem(option)
                myOption.state &_ ~QStyle.State_Enabled
                super(VariantDelegate, self).paint(painter, myOption, index)
                r_

        super(VariantDelegate, self).paint(painter, option, index)

    ___ createEditor  parent, option, index):
        __ index.column() !_ 2:
            r_ N..

        originalValue _ index.model().data(index, __.UserRole)
        __ no. isSupportedType(originalValue):
            r_ N..

        lineEdit _ QLineEdit(parent)
        lineEdit.setFrame F..

        __ isinstance(originalValue, bool):
            regExp _ boolExp
        ____ isinstance(originalValue, float):
            regExp _ doubleExp
        ____ isinstance(originalValue, int):
            regExp _ signedIntegerExp
        ____ isinstance(originalValue, QByteArray):
            regExp _ byteArrayExp
        ____ isinstance(originalValue, ?C..):
            regExp _ colorExp
        ____ isinstance(originalValue, QDate):
            regExp _ dateExp
        ____ isinstance(originalValue, QDateTime):
            regExp _ dateTimeExp
        ____ isinstance(originalValue, QTime):
            regExp _ timeExp
        ____ isinstance(originalValue, QPoint):
            regExp _ pointExp
        ____ isinstance(originalValue, QRect):
            regExp _ rectExp
        ____ isinstance(originalValue, QSize):
            regExp _ sizeExp
        ____
            regExp _ QRegExp()

        __ no. regExp.isEmpty
            validator _ QRegExpValidator(regExp, lineEdit)
            lineEdit.setValidator(validator)

        r_ lineEdit

    ___ setEditorData  editor, index):
        value _ index.model().data(index, __.UserRole)
        __ editor __ no. N..:
            editor.sT..(displayText(value))

    ___ setModelData  editor, model, index):
        __ no. editor.iM..
            r_

        t__ _ editor.t__()
        validator _ editor.validator()
        __ validator __ no. N..:
            state, t__, _ _ validator.validate(t__, 0)
            __ state !_ QValidator.Acceptable:
                r_

        originalValue _ index.model().data(index, __.UserRole)

        __ isinstance(originalValue, ?C..):
            colorExp.exactMatch(t__)
            value _ ?C..(min(int(colorExp.cap(1)), 255),
                           min(int(colorExp.cap(2)), 255),
                           min(int(colorExp.cap(3)), 255),
                           min(int(colorExp.cap(4)), 255))
        ____ isinstance(originalValue, QDate):
            value _ QDate.fromString(t__, __.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QDateTime):
            value _ QDateTime.fromString(t__, __.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QTime):
            value _ QTime.fromString(t__, __.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QPoint):
            pointExp.exactMatch(t__)
            value _ QPoint(int(pointExp.cap(1)),
                           int(pointExp.cap(2)))
        ____ isinstance(originalValue, QRect):
            rectExp.exactMatch(t__)
            value _ QRect(int(rectExp.cap(1)),
                          int(rectExp.cap(2)),
                          int(rectExp.cap(3)),
                          int(rectExp.cap(4)))
        ____ isinstance(originalValue, QSize):
            sizeExp.exactMatch(t__)
            value _ QSize(int(sizeExp.cap(1)),
                          int(sizeExp.cap(2)))
        ____ isinstance(originalValue, list):
            value _ t__.split(',')
        ____
            value _ type(originalValue)(t__)

        model.setData(index, displayText(value), __.DisplayRole)
        model.setData(index, value, __.UserRole)

    @staticmethod
    ___ isSupportedType(value):
        r_ isinstance(value, (bool, float, int, QByteArray, str, ?C..,
                QDate, QDateTime, QTime, QPoint, QRect, QSize, list))

    @staticmethod
    ___ displayText(value):
        __ isinstance(value, (bool, int, QByteArray)):
            r_ str(value)
        __ isinstance(value, str):
            r_ value
        ____ isinstance(value, float):
            r_ '%g' % value
        ____ isinstance(value, ?C..):
            r_ '(%u,%u,%u,%u)' % (value.red(), value.green(), value.blue(), value.alpha())
        ____ isinstance(value, (QDate, QDateTime, QTime)):
            r_ value.toString(__.ISODate)
        ____ isinstance(value, QPoint):
            r_ '(%d,%d)' % (value.x(), value.y())
        ____ isinstance(value, QRect):
            r_ '(%d,%d,%d,%d)' % (value.x(), value.y(), value.width(), value.height())
        ____ isinstance(value, QSize):
            r_ '(%d,%d)' % (value.width(), value.height())
        ____ isinstance(value, list):
            r_ ','.join(value)
        ____ value __ N..:
            r_ '<Invalid>'

        r_ '<%s>' % value


__ ______ __ ______
    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.exit(app.exec_())
