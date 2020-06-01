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


______ sys

____ ?.QtCore ______ (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,
        QRegExp, QSettings, QSize, Qt, QTime, QTimer)
____ ?.?G.. ______ QColor, QIcon, QRegExpValidator, QValidator
____ ?.?W.. ______ (QAbstractItemView, ?A.., ?A..,
        QComboBox, QDialog, QDialogButtonBox, ?FD.., QGridLayout,
        QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,
        QMainWindow, ?MB.., QStyle, QStyleOptionViewItem, QTableWidget,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout)


c_ MainWindow ?MW..
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.settingsTree _ SettingsTree()
        self.sCW..(self.settingsTree)

        self.locationDialog _ N..

        self.createActions()
        self.createMenus()

        self.autoRefreshAct.setChecked(True)
        self.fallbacksAct.setChecked(True)

        self.setWindowTitle("Settings Editor")
        self.resize(500, 600)

    ___ openSettings(self):
        __ self.locationDialog __ N..:
            self.locationDialog _ LocationDialog(self)

        __ self.locationDialog.exec_
            settings _ QSettings(self.locationDialog.format(),
                                        self.locationDialog.scope(),
                                        self.locationDialog.organization(),
                                        self.locationDialog.application())
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(True)

    ___ openIniFile(self):
        fileName, _ _ ?FD...gOFN..  "Open INI File", '',
                "INI Files (*.ini *.conf)")

        __ fileName:
            settings _ QSettings(fileName, QSettings.IniFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled F..

    ___ openPropertyList(self):
        fileName, _ _ ?FD...gOFN..  "Open Property List",
                '', "Property List Files (*.plist)")

        __ fileName:
            settings _ QSettings(fileName, QSettings.NativeFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled F..

    ___ openRegistryPath(self):
        path, ok _ QInputDialog.getText  "Open Registry Path",
                "Enter the path in the Windows registry:", QLineEdit.Normal,
                'HKEY_CURRENT_USER\\')

        __ ok and path !_ '':
            settings _ QSettings(path, QSettings.NativeFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled F..

    ___ about(self):
        ?MB...about  "About Settings Editor",
                "The <b>Settings Editor</b> example shows how to access "
                "application settings using Qt.")

    ___ createActions(self):
        self.openSettingsAct _ ?A..("&Open Application Settings...", self,
                shortcut_"Ctrl+O", triggered_self.openSettings)

        self.openIniFileAct _ ?A..("Open I&NI File...", self,
                shortcut_"Ctrl+N", triggered_self.openIniFile)

        self.openPropertyListAct _ ?A..("Open Mac &Property List...", self,
                shortcut_"Ctrl+P", triggered_self.openPropertyList)
        __ sys.platform !_ 'darwin':
            self.openPropertyListAct.setEnabled F..

        self.openRegistryPathAct _ ?A..("Open Windows &Registry Path...",
                self, shortcut_"Ctrl+G", triggered_self.openRegistryPath)
        __ sys.platform !_ 'win32':
            self.openRegistryPathAct.setEnabled F..

        self.refreshAct _ ?A..("&Refresh", self, shortcut_"Ctrl+R",
                enabled_False, triggered_self.settingsTree.refresh)

        self.exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.autoRefreshAct _ ?A..("&Auto-Refresh", self, shortcut_"Ctrl+A",
                checkable_True, enabled_False)
        self.autoRefreshAct.t__.c..(self.settingsTree.setAutoRefresh)
        self.autoRefreshAct.t__.c..(self.refreshAct.setDisabled)

        self.fallbacksAct _ ?A..("&Fallbacks", self, shortcut_"Ctrl+F",
                checkable_True, enabled_False,
                triggered_self.settingsTree.setFallbacksEnabled)

        self.aboutAct _ ?A..("&About", self, triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.openSettingsAct)
        self.fileMenu.aA..(self.openIniFileAct)
        self.fileMenu.aA..(self.openPropertyListAct)
        self.fileMenu.aA..(self.openRegistryPathAct)
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.refreshAct)
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.exitAct)

        self.optionsMenu _ self.mB.. .aM..("&Options")
        self.optionsMenu.aA..(self.autoRefreshAct)
        self.optionsMenu.aA..(self.fallbacksAct)

        self.mB.. .addSeparator()

        self.helpMenu _ self.mB.. .aM..("&Help")
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

    ___ setSettingsObject  settings):
        settings.setFallbacksEnabled(self.fallbacksAct.isChecked())
        self.settingsTree.setSettingsObject(settings)

        self.refreshAct.setEnabled(True)
        self.autoRefreshAct.setEnabled(True)

        niceName _ settings.fileName()
        niceName.replace('\\', '/')
        niceName _ niceName.split('/')[-1]

        __ no. settings.isWritable
            niceName +_ " (read only)"

        self.setWindowTitle("%s - Settings Editor" % niceName)


c_ LocationDialog(QDialog):
    ___ __init__  parent_None):
        super(LocationDialog, self).__init__(parent)

        self.formatComboBox _ QComboBox()
        self.formatComboBox.addItem("Native")
        self.formatComboBox.addItem("INI")

        self.scopeComboBox _ QComboBox()
        self.scopeComboBox.addItem("User")
        self.scopeComboBox.addItem("System")

        self.organizationComboBox _ QComboBox()
        self.organizationComboBox.addItem("Trolltech")
        self.organizationComboBox.setEditable(True)

        self.applicationComboBox _ QComboBox()
        self.applicationComboBox.addItem("Any")
        self.applicationComboBox.addItem("Application Example")
        self.applicationComboBox.addItem("Assistant")
        self.applicationComboBox.addItem("Designer")
        self.applicationComboBox.addItem("Linguist")
        self.applicationComboBox.setEditable(True)
        self.applicationComboBox.setCurrentIndex(3)

        formatLabel _ QLabel("&Format:")
        formatLabel.setBuddy(self.formatComboBox)

        scopeLabel _ QLabel("&Scope:")
        scopeLabel.setBuddy(self.scopeComboBox)

        organizationLabel _ QLabel("&Organization:")
        organizationLabel.setBuddy(self.organizationComboBox)

        applicationLabel _ QLabel("&Application:")
        applicationLabel.setBuddy(self.applicationComboBox)

        self.locationsGroupBox _ QGroupBox("Setting Locations")

        self.locationsTable _ QTableWidget()
        self.locationsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.locationsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.locationsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.locationsTable.setColumnCount(2)
        self.locationsTable.setHorizontalHeaderLabels(("Location", "Access"))
        self.locationsTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.locationsTable.horizontalHeader().resizeSection(1, 180)

        self.buttonBox _ QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.formatComboBox.activated.c..(self.updateLocationsTable)
        self.scopeComboBox.activated.c..(self.updateLocationsTable)
        self.organizationComboBox.lineEdit().editingFinished.c..(self.updateLocationsTable)
        self.applicationComboBox.lineEdit().editingFinished.c..(self.updateLocationsTable)
        self.buttonBox.accepted.c..(self.accept)
        self.buttonBox.rejected.c..(self.reject)

        locationsLayout _ QVBoxLayout()
        locationsLayout.addWidget(self.locationsTable)
        self.locationsGroupBox.setLayout(locationsLayout)

        mainLayout _ QGridLayout()
        mainLayout.addWidget(formatLabel, 0, 0)
        mainLayout.addWidget(self.formatComboBox, 0, 1)
        mainLayout.addWidget(scopeLabel, 1, 0)
        mainLayout.addWidget(self.scopeComboBox, 1, 1)
        mainLayout.addWidget(organizationLabel, 2, 0)
        mainLayout.addWidget(self.organizationComboBox, 2, 1)
        mainLayout.addWidget(applicationLabel, 3, 0)
        mainLayout.addWidget(self.applicationComboBox, 3, 1)
        mainLayout.addWidget(self.locationsGroupBox, 4, 0, 1, 2)
        mainLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.setLayout(mainLayout)

        self.updateLocationsTable()

        self.setWindowTitle("Open Application Settings")
        self.resize(650, 400)

    ___ format(self):
        __ self.formatComboBox.currentIndex() == 0:
            r_ QSettings.NativeFormat
        ____
            r_ QSettings.IniFormat

    ___ scope(self):
        __ self.scopeComboBox.currentIndex() == 0:
            r_ QSettings.UserScope
        ____
            r_ QSettings.SystemScope

    ___ organization(self):
        r_ self.organizationComboBox.currentText()

    ___ application(self):
        __ self.applicationComboBox.currentText() == "Any":
            r_ ''

        r_ self.applicationComboBox.currentText()

    ___ updateLocationsTable(self):
        self.locationsTable.setUpdatesEnabled F..
        self.locationsTable.setRowCount(0)

        for i in range(2):
            __ i == 0:
                __ self.scope() == QSettings.SystemScope:
                    continue

                actualScope _ QSettings.UserScope
            ____
                actualScope _ QSettings.SystemScope

            for j in range(2):
                __ j == 0:
                    __ no. self.application
                        continue

                    actualApplication _ self.application()
                ____
                    actualApplication _ ''

                settings _ QSettings(self.format(), actualScope,
                        self.organization(), actualApplication)

                row _ self.locationsTable.rowCount()
                self.locationsTable.setRowCount(row + 1)

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
                    self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(disable)
                ____
                    item1.sT..("Read-only fallback")

                __ disable:
                    item0.setFlags(item0.flags() & ~Qt.ItemIsEnabled)
                    item1.setFlags(item1.flags() & ~Qt.ItemIsEnabled)

                self.locationsTable.setItem(row, 0, item0)
                self.locationsTable.setItem(row, 1, item1)

        self.locationsTable.setUpdatesEnabled(True)


c_ SettingsTree(QTreeWidget):
    ___ __init__  parent_None):
        super(SettingsTree, self).__init__(parent)

        self.setItemDelegate(VariantDelegate(self))

        self.setHeaderLabels(("Setting", "Type", "Value"))
        self.header().setSectionResizeMode(0, QHeaderView.Stretch)
        self.header().setSectionResizeMode(2, QHeaderView.Stretch)

        self.settings _ N..
        self.refreshTimer _ QTimer()
        self.refreshTimer.setInterval(2000)
        self.autoRefresh _ False

        self.groupIcon _ QIcon()
        self.groupIcon.addPixmap(self.style().standardPixmap(QStyle.SP_DirClosedIcon),
                QIcon.Normal, QIcon.Off)
        self.groupIcon.addPixmap(self.style().standardPixmap(QStyle.SP_DirOpenIcon),
                QIcon.Normal, QIcon.On)
        self.keyIcon _ QIcon()
        self.keyIcon.addPixmap(self.style().standardPixmap(QStyle.SP_FileIcon))

        self.refreshTimer.timeout.c..(self.maybeRefresh)

    ___ setSettingsObject  settings):
        self.settings _ settings
        self.clear()

        __ self.settings __ no. N..:
            self.settings.setParent(self)
            self.refresh()
            __ self.autoRefresh:
                self.refreshTimer.start()
        ____
            self.refreshTimer.stop()

    ___ sizeHint(self):
        r_ QSize(800, 600)

    ___ setAutoRefresh  autoRefresh):
        self.autoRefresh _ autoRefresh

        __ self.settings __ no. N..:
            __ self.autoRefresh:
                self.maybeRefresh()
                self.refreshTimer.start()
            ____
                self.refreshTimer.stop()

    ___ setFallbacksEnabled  enabled):
        __ self.settings __ no. N..:
            self.settings.setFallbacksEnabled(enabled)
            self.refresh()

    ___ maybeRefresh(self):
        __ self.state() !_ QAbstractItemView.EditingState:
            self.refresh()

    ___ refresh(self):
        __ self.settings __ N..:
            r_

        # The signal might not be connected.
        try:
            self.itemChanged.disconnect(self.updateSetting)
        except:
            pass

        self.settings.sync()
        self.updateChildItems(N..)

        self.itemChanged.c..(self.updateSetting)

    ___ event  event):
        __ event.type() == QEvent.WindowActivate:
            __ self.isActiveWindow() and self.autoRefresh:
                self.maybeRefresh()

        r_ super(SettingsTree, self).event(event)

    ___ updateSetting  item):
        key _ item.text(0)
        ancestor _ item.parent()

        while ancestor:
            key _ ancestor.text(0) + '/' + key
            ancestor _ ancestor.parent()

        d _ item.data(2, Qt.UserRole)
        self.settings.setValue(key, item.data(2, Qt.UserRole))

        __ self.autoRefresh:
            self.refresh()

    ___ updateChildItems  parent):
        dividerIndex _ 0

        for group in self.settings.childGroups
            childIndex _ self.findChild(parent, group, dividerIndex)
            __ childIndex !_ -1:
                child _ self.childAt(parent, childIndex)
                child.sT..(1, '')
                child.sT..(2, '')
                child.setData(2, Qt.UserRole, N..)
                self.moveItemForward(parent, childIndex, dividerIndex)
            ____
                child _ self.createItem(group, parent, dividerIndex)

            child.setIcon(0, self.groupIcon)
            dividerIndex +_ 1

            self.settings.beginGroup(group)
            self.updateChildItems(child)
            self.settings.endGroup()

        for key in self.settings.childKeys
            childIndex _ self.findChild(parent, key, 0)
            __ childIndex == -1 or childIndex >_ dividerIndex:
                __ childIndex !_ -1:
                    child _ self.childAt(parent, childIndex)
                    for i in range(child.childCount()):
                        self.deleteItem(child, i)
                    self.moveItemForward(parent, childIndex, dividerIndex)
                ____
                    child _ self.createItem(key, parent, dividerIndex)
                child.setIcon(0, self.keyIcon)
                dividerIndex +_ 1
            ____
                child _ self.childAt(parent, childIndex)

            value _ self.settings.value(key)
            __ value __ N..:
                child.sT..(1, 'Invalid')
            ____
                child.sT..(1, value.__class__.__name__)
            child.sT..(2, VariantDelegate.displayText(value))
            child.setData(2, Qt.UserRole, value)

        while dividerIndex < self.childCount(parent):
            self.deleteItem(parent, dividerIndex)

    ___ createItem  text, parent, index):
        after _ N..

        __ index !_ 0:
            after _ self.childAt(parent, index - 1)

        __ parent __ no. N..:
            item _ QTreeWidgetItem(parent, after)
        ____
            item _ QTreeWidgetItem  after)

        item.sT..(0, text)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        r_ item

    ___ deleteItem  parent, index):
        __ parent __ no. N..:
            item _ parent.takeChild(index)
        ____
            item _ self.takeTopLevelItem(index)
        del item

    ___ childAt  parent, index):
        __ parent __ no. N..:
            r_ parent.child(index)
        ____
            r_ self.topLevelItem(index)

    ___ childCount  parent):
        __ parent __ no. N..:
            r_ parent.childCount()
        ____
            r_ self.topLevelItemCount()

    ___ findChild  parent, text, startIndex):
        for i in range(self.childCount(parent)):
            __ self.childAt(parent, i).text(0) == text:
                r_ i
        r_ -1

    ___ moveItemForward  parent, oldIndex, newIndex):
        for int in range(oldIndex - newIndex):
            self.deleteItem(parent, newIndex)


c_ VariantDelegate(QItemDelegate):
    ___ __init__  parent_None):
        super(VariantDelegate, self).__init__(parent)

        self.boolExp _ QRegExp()
        self.boolExp.setPattern('true|false')
        self.boolExp.setCaseSensitivity(Qt.CaseInsensitive)

        self.byteArrayExp _ QRegExp()
        self.byteArrayExp.setPattern('[\\x00-\\xff]*')

        self.charExp _ QRegExp()
        self.charExp.setPattern('.')

        self.colorExp _ QRegExp()
        self.colorExp.setPattern('\\(([0-9]*),([0-9]*),([0-9]*),([0-9]*)\\)')

        self.doubleExp _ QRegExp()
        self.doubleExp.setPattern('')

        self.pointExp _ QRegExp()
        self.pointExp.setPattern('\\((-?[0-9]*),(-?[0-9]*)\\)')

        self.rectExp _ QRegExp()
        self.rectExp.setPattern('\\((-?[0-9]*),(-?[0-9]*),(-?[0-9]*),(-?[0-9]*)\\)')

        self.signedIntegerExp _ QRegExp()
        self.signedIntegerExp.setPattern('-?[0-9]*')

        self.sizeExp _ QRegExp(self.pointExp)

        self.unsignedIntegerExp _ QRegExp()
        self.unsignedIntegerExp.setPattern('[0-9]*')

        self.dateExp _ QRegExp()
        self.dateExp.setPattern('([0-9]{,4})-([0-9]{,2})-([0-9]{,2})')

        self.timeExp _ QRegExp()
        self.timeExp.setPattern('([0-9]{,2}):([0-9]{,2}):([0-9]{,2})')

        self.dateTimeExp _ QRegExp()
        self.dateTimeExp.setPattern(self.dateExp.pattern() + 'T' + self.timeExp.pattern())

    ___ paint  painter, option, index):
        __ index.column() == 2:
            value _ index.model().data(index, Qt.UserRole)
            __ no. self.isSupportedType(value):
                myOption _ QStyleOptionViewItem(option)
                myOption.state &_ ~QStyle.State_Enabled
                super(VariantDelegate, self).paint(painter, myOption, index)
                r_

        super(VariantDelegate, self).paint(painter, option, index)

    ___ createEditor  parent, option, index):
        __ index.column() !_ 2:
            r_ N..

        originalValue _ index.model().data(index, Qt.UserRole)
        __ no. self.isSupportedType(originalValue):
            r_ N..

        lineEdit _ QLineEdit(parent)
        lineEdit.setFrame F..

        __ isinstance(originalValue, bool):
            regExp _ self.boolExp
        ____ isinstance(originalValue, float):
            regExp _ self.doubleExp
        ____ isinstance(originalValue, int):
            regExp _ self.signedIntegerExp
        ____ isinstance(originalValue, QByteArray):
            regExp _ self.byteArrayExp
        ____ isinstance(originalValue, QColor):
            regExp _ self.colorExp
        ____ isinstance(originalValue, QDate):
            regExp _ self.dateExp
        ____ isinstance(originalValue, QDateTime):
            regExp _ self.dateTimeExp
        ____ isinstance(originalValue, QTime):
            regExp _ self.timeExp
        ____ isinstance(originalValue, QPoint):
            regExp _ self.pointExp
        ____ isinstance(originalValue, QRect):
            regExp _ self.rectExp
        ____ isinstance(originalValue, QSize):
            regExp _ self.sizeExp
        ____
            regExp _ QRegExp()

        __ no. regExp.isEmpty
            validator _ QRegExpValidator(regExp, lineEdit)
            lineEdit.setValidator(validator)

        r_ lineEdit

    ___ setEditorData  editor, index):
        value _ index.model().data(index, Qt.UserRole)
        __ editor __ no. N..:
            editor.sT..(self.displayText(value))

    ___ setModelData  editor, model, index):
        __ no. editor.iM..
            r_

        text _ editor.text()
        validator _ editor.validator()
        __ validator __ no. N..:
            state, text, _ _ validator.validate(text, 0)
            __ state !_ QValidator.Acceptable:
                r_

        originalValue _ index.model().data(index, Qt.UserRole)

        __ isinstance(originalValue, QColor):
            self.colorExp.exactMatch(text)
            value _ QColor(min(int(self.colorExp.cap(1)), 255),
                           min(int(self.colorExp.cap(2)), 255),
                           min(int(self.colorExp.cap(3)), 255),
                           min(int(self.colorExp.cap(4)), 255))
        ____ isinstance(originalValue, QDate):
            value _ QDate.fromString(text, Qt.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QDateTime):
            value _ QDateTime.fromString(text, Qt.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QTime):
            value _ QTime.fromString(text, Qt.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QPoint):
            self.pointExp.exactMatch(text)
            value _ QPoint(int(self.pointExp.cap(1)),
                           int(self.pointExp.cap(2)))
        ____ isinstance(originalValue, QRect):
            self.rectExp.exactMatch(text)
            value _ QRect(int(self.rectExp.cap(1)),
                          int(self.rectExp.cap(2)),
                          int(self.rectExp.cap(3)),
                          int(self.rectExp.cap(4)))
        ____ isinstance(originalValue, QSize):
            self.sizeExp.exactMatch(text)
            value _ QSize(int(self.sizeExp.cap(1)),
                          int(self.sizeExp.cap(2)))
        ____ isinstance(originalValue, list):
            value _ text.split(',')
        ____
            value _ type(originalValue)(text)

        model.setData(index, self.displayText(value), Qt.DisplayRole)
        model.setData(index, value, Qt.UserRole)

    @staticmethod
    ___ isSupportedType(value):
        r_ isinstance(value, (bool, float, int, QByteArray, str, QColor,
                QDate, QDateTime, QTime, QPoint, QRect, QSize, list))

    @staticmethod
    ___ displayText(value):
        __ isinstance(value, (bool, int, QByteArray)):
            r_ str(value)
        __ isinstance(value, str):
            r_ value
        ____ isinstance(value, float):
            r_ '%g' % value
        ____ isinstance(value, QColor):
            r_ '(%u,%u,%u,%u)' % (value.red(), value.green(), value.blue(), value.alpha())
        ____ isinstance(value, (QDate, QDateTime, QTime)):
            r_ value.toString(Qt.ISODate)
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


__ __name__ == '__main__':
    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
