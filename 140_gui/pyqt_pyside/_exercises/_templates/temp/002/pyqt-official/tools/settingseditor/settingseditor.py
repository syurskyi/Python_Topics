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
____ ?.QtGui ______ QColor, QIcon, QRegExpValidator, QValidator
____ ?.?W.. ______ (QAbstractItemView, QAction, QApplication,
        QComboBox, QDialog, QDialogButtonBox, QFileDialog, QGridLayout,
        QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,
        QMainWindow, QMessageBox, QStyle, QStyleOptionViewItem, QTableWidget,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout)


class MainWindow(QMainWindow):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)

        self.settingsTree _ SettingsTree()
        self.setCentralWidget(self.settingsTree)

        self.locationDialog _ None

        self.createActions()
        self.createMenus()

        self.autoRefreshAct.setChecked(True)
        self.fallbacksAct.setChecked(True)

        self.setWindowTitle("Settings Editor")
        self.resize(500, 600)

    ___ openSettings(self):
        if self.locationDialog is None:
            self.locationDialog _ LocationDialog(self)

        if self.locationDialog.exec_
            settings _ QSettings(self.locationDialog.format(),
                                        self.locationDialog.scope(),
                                        self.locationDialog.organization(),
                                        self.locationDialog.application())
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(True)

    ___ openIniFile(self):
        fileName, _ _ QFileDialog.getOpenFileName(self, "Open INI File", '',
                "INI Files (*.ini *.conf)")

        if fileName:
            settings _ QSettings(fileName, QSettings.IniFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(False)

    ___ openPropertyList(self):
        fileName, _ _ QFileDialog.getOpenFileName(self, "Open Property List",
                '', "Property List Files (*.plist)")

        if fileName:
            settings _ QSettings(fileName, QSettings.NativeFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(False)

    ___ openRegistryPath(self):
        path, ok _ QInputDialog.getText(self, "Open Registry Path",
                "Enter the path in the Windows registry:", QLineEdit.Normal,
                'HKEY_CURRENT_USER\\')

        if ok and path !_ '':
            settings _ QSettings(path, QSettings.NativeFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(False)

    ___ about(self):
        QMessageBox.about(self, "About Settings Editor",
                "The <b>Settings Editor</b> example shows how to access "
                "application settings using Qt.")

    ___ createActions(self):
        self.openSettingsAct _ QAction("&Open Application Settings...", self,
                shortcut_"Ctrl+O", triggered_self.openSettings)

        self.openIniFileAct _ QAction("Open I&NI File...", self,
                shortcut_"Ctrl+N", triggered_self.openIniFile)

        self.openPropertyListAct _ QAction("Open Mac &Property List...", self,
                shortcut_"Ctrl+P", triggered_self.openPropertyList)
        if sys.platform !_ 'darwin':
            self.openPropertyListAct.setEnabled(False)

        self.openRegistryPathAct _ QAction("Open Windows &Registry Path...",
                self, shortcut_"Ctrl+G", triggered_self.openRegistryPath)
        if sys.platform !_ 'win32':
            self.openRegistryPathAct.setEnabled(False)

        self.refreshAct _ QAction("&Refresh", self, shortcut_"Ctrl+R",
                enabled_False, triggered_self.settingsTree.refresh)

        self.exitAct _ QAction("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.autoRefreshAct _ QAction("&Auto-Refresh", self, shortcut_"Ctrl+A",
                checkable_True, enabled_False)
        self.autoRefreshAct.triggered.c..(self.settingsTree.setAutoRefresh)
        self.autoRefreshAct.triggered.c..(self.refreshAct.setDisabled)

        self.fallbacksAct _ QAction("&Fallbacks", self, shortcut_"Ctrl+F",
                checkable_True, enabled_False,
                triggered_self.settingsTree.setFallbacksEnabled)

        self.aboutAct _ QAction("&About", self, triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.openSettingsAct)
        self.fileMenu.addAction(self.openIniFileAct)
        self.fileMenu.addAction(self.openPropertyListAct)
        self.fileMenu.addAction(self.openRegistryPathAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.refreshAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.optionsMenu _ self.menuBar().addMenu("&Options")
        self.optionsMenu.addAction(self.autoRefreshAct)
        self.optionsMenu.addAction(self.fallbacksAct)

        self.menuBar().addSeparator()

        self.helpMenu _ self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    ___ setSettingsObject(self, settings):
        settings.setFallbacksEnabled(self.fallbacksAct.isChecked())
        self.settingsTree.setSettingsObject(settings)

        self.refreshAct.setEnabled(True)
        self.autoRefreshAct.setEnabled(True)

        niceName _ settings.fileName()
        niceName.replace('\\', '/')
        niceName _ niceName.split('/')[-1]

        if not settings.isWritable
            niceName +_ " (read only)"

        self.setWindowTitle("%s - Settings Editor" % niceName)


class LocationDialog(QDialog):
    ___ __init__(self, parent_None):
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
        if self.formatComboBox.currentIndex() == 0:
            return QSettings.NativeFormat
        else:
            return QSettings.IniFormat

    ___ scope(self):
        if self.scopeComboBox.currentIndex() == 0:
            return QSettings.UserScope
        else:
            return QSettings.SystemScope

    ___ organization(self):
        return self.organizationComboBox.currentText()

    ___ application(self):
        if self.applicationComboBox.currentText() == "Any":
            return ''

        return self.applicationComboBox.currentText()

    ___ updateLocationsTable(self):
        self.locationsTable.setUpdatesEnabled(False)
        self.locationsTable.setRowCount(0)

        for i in range(2):
            if i == 0:
                if self.scope() == QSettings.SystemScope:
                    continue

                actualScope _ QSettings.UserScope
            else:
                actualScope _ QSettings.SystemScope

            for j in range(2):
                if j == 0:
                    if not self.application
                        continue

                    actualApplication _ self.application()
                else:
                    actualApplication _ ''

                settings _ QSettings(self.format(), actualScope,
                        self.organization(), actualApplication)

                row _ self.locationsTable.rowCount()
                self.locationsTable.setRowCount(row + 1)

                item0 _ QTableWidgetItem()
                item0.sT..(settings.fileName())

                item1 _ QTableWidgetItem()
                disable _ not (settings.childKeys() or settings.childGroups())

                if row == 0:
                    if settings.isWritable
                        item1.sT..("Read-write")
                        disable _ False
                    else:
                        item1.sT..("Read-only")
                    self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(disable)
                else:
                    item1.sT..("Read-only fallback")

                if disable:
                    item0.setFlags(item0.flags() & ~Qt.ItemIsEnabled)
                    item1.setFlags(item1.flags() & ~Qt.ItemIsEnabled)

                self.locationsTable.setItem(row, 0, item0)
                self.locationsTable.setItem(row, 1, item1)

        self.locationsTable.setUpdatesEnabled(True)


class SettingsTree(QTreeWidget):
    ___ __init__(self, parent_None):
        super(SettingsTree, self).__init__(parent)

        self.setItemDelegate(VariantDelegate(self))

        self.setHeaderLabels(("Setting", "Type", "Value"))
        self.header().setSectionResizeMode(0, QHeaderView.Stretch)
        self.header().setSectionResizeMode(2, QHeaderView.Stretch)

        self.settings _ None
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

    ___ setSettingsObject(self, settings):
        self.settings _ settings
        self.clear()

        if self.settings is not None:
            self.settings.setParent(self)
            self.refresh()
            if self.autoRefresh:
                self.refreshTimer.start()
        else:
            self.refreshTimer.stop()

    ___ sizeHint(self):
        return QSize(800, 600)

    ___ setAutoRefresh(self, autoRefresh):
        self.autoRefresh _ autoRefresh

        if self.settings is not None:
            if self.autoRefresh:
                self.maybeRefresh()
                self.refreshTimer.start()
            else:
                self.refreshTimer.stop()

    ___ setFallbacksEnabled(self, enabled):
        if self.settings is not None:
            self.settings.setFallbacksEnabled(enabled)
            self.refresh()

    ___ maybeRefresh(self):
        if self.state() !_ QAbstractItemView.EditingState:
            self.refresh()

    ___ refresh(self):
        if self.settings is None:
            return

        # The signal might not be connected.
        try:
            self.itemChanged.disconnect(self.updateSetting)
        except:
            pass

        self.settings.sync()
        self.updateChildItems(None)

        self.itemChanged.c..(self.updateSetting)

    ___ event(self, event):
        if event.type() == QEvent.WindowActivate:
            if self.isActiveWindow() and self.autoRefresh:
                self.maybeRefresh()

        return super(SettingsTree, self).event(event)

    ___ updateSetting(self, item):
        key _ item.text(0)
        ancestor _ item.parent()

        while ancestor:
            key _ ancestor.text(0) + '/' + key
            ancestor _ ancestor.parent()

        d _ item.data(2, Qt.UserRole)
        self.settings.setValue(key, item.data(2, Qt.UserRole))

        if self.autoRefresh:
            self.refresh()

    ___ updateChildItems(self, parent):
        dividerIndex _ 0

        for group in self.settings.childGroups
            childIndex _ self.findChild(parent, group, dividerIndex)
            if childIndex !_ -1:
                child _ self.childAt(parent, childIndex)
                child.sT..(1, '')
                child.sT..(2, '')
                child.setData(2, Qt.UserRole, None)
                self.moveItemForward(parent, childIndex, dividerIndex)
            else:
                child _ self.createItem(group, parent, dividerIndex)

            child.setIcon(0, self.groupIcon)
            dividerIndex +_ 1

            self.settings.beginGroup(group)
            self.updateChildItems(child)
            self.settings.endGroup()

        for key in self.settings.childKeys
            childIndex _ self.findChild(parent, key, 0)
            if childIndex == -1 or childIndex >_ dividerIndex:
                if childIndex !_ -1:
                    child _ self.childAt(parent, childIndex)
                    for i in range(child.childCount()):
                        self.deleteItem(child, i)
                    self.moveItemForward(parent, childIndex, dividerIndex)
                else:
                    child _ self.createItem(key, parent, dividerIndex)
                child.setIcon(0, self.keyIcon)
                dividerIndex +_ 1
            else:
                child _ self.childAt(parent, childIndex)

            value _ self.settings.value(key)
            if value is None:
                child.sT..(1, 'Invalid')
            else:
                child.sT..(1, value.__class__.__name__)
            child.sT..(2, VariantDelegate.displayText(value))
            child.setData(2, Qt.UserRole, value)

        while dividerIndex < self.childCount(parent):
            self.deleteItem(parent, dividerIndex)

    ___ createItem(self, text, parent, index):
        after _ None

        if index !_ 0:
            after _ self.childAt(parent, index - 1)

        if parent is not None:
            item _ QTreeWidgetItem(parent, after)
        else:
            item _ QTreeWidgetItem(self, after)

        item.sT..(0, text)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        return item

    ___ deleteItem(self, parent, index):
        if parent is not None:
            item _ parent.takeChild(index)
        else:
            item _ self.takeTopLevelItem(index)
        del item

    ___ childAt(self, parent, index):
        if parent is not None:
            return parent.child(index)
        else:
            return self.topLevelItem(index)

    ___ childCount(self, parent):
        if parent is not None:
            return parent.childCount()
        else:
            return self.topLevelItemCount()

    ___ findChild(self, parent, text, startIndex):
        for i in range(self.childCount(parent)):
            if self.childAt(parent, i).text(0) == text:
                return i
        return -1

    ___ moveItemForward(self, parent, oldIndex, newIndex):
        for int in range(oldIndex - newIndex):
            self.deleteItem(parent, newIndex)


class VariantDelegate(QItemDelegate):
    ___ __init__(self, parent_None):
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

    ___ paint(self, painter, option, index):
        if index.column() == 2:
            value _ index.model().data(index, Qt.UserRole)
            if not self.isSupportedType(value):
                myOption _ QStyleOptionViewItem(option)
                myOption.state &_ ~QStyle.State_Enabled
                super(VariantDelegate, self).paint(painter, myOption, index)
                return

        super(VariantDelegate, self).paint(painter, option, index)

    ___ createEditor(self, parent, option, index):
        if index.column() !_ 2:
            return None

        originalValue _ index.model().data(index, Qt.UserRole)
        if not self.isSupportedType(originalValue):
            return None

        lineEdit _ QLineEdit(parent)
        lineEdit.setFrame(False)

        if isinstance(originalValue, bool):
            regExp _ self.boolExp
        elif isinstance(originalValue, float):
            regExp _ self.doubleExp
        elif isinstance(originalValue, int):
            regExp _ self.signedIntegerExp
        elif isinstance(originalValue, QByteArray):
            regExp _ self.byteArrayExp
        elif isinstance(originalValue, QColor):
            regExp _ self.colorExp
        elif isinstance(originalValue, QDate):
            regExp _ self.dateExp
        elif isinstance(originalValue, QDateTime):
            regExp _ self.dateTimeExp
        elif isinstance(originalValue, QTime):
            regExp _ self.timeExp
        elif isinstance(originalValue, QPoint):
            regExp _ self.pointExp
        elif isinstance(originalValue, QRect):
            regExp _ self.rectExp
        elif isinstance(originalValue, QSize):
            regExp _ self.sizeExp
        else:
            regExp _ QRegExp()

        if not regExp.isEmpty
            validator _ QRegExpValidator(regExp, lineEdit)
            lineEdit.setValidator(validator)

        return lineEdit

    ___ setEditorData(self, editor, index):
        value _ index.model().data(index, Qt.UserRole)
        if editor is not None:
            editor.sT..(self.displayText(value))

    ___ setModelData(self, editor, model, index):
        if not editor.isModified
            return

        text _ editor.text()
        validator _ editor.validator()
        if validator is not None:
            state, text, _ _ validator.validate(text, 0)
            if state !_ QValidator.Acceptable:
                return

        originalValue _ index.model().data(index, Qt.UserRole)

        if isinstance(originalValue, QColor):
            self.colorExp.exactMatch(text)
            value _ QColor(min(int(self.colorExp.cap(1)), 255),
                           min(int(self.colorExp.cap(2)), 255),
                           min(int(self.colorExp.cap(3)), 255),
                           min(int(self.colorExp.cap(4)), 255))
        elif isinstance(originalValue, QDate):
            value _ QDate.fromString(text, Qt.ISODate)
            if not value.isValid
                return
        elif isinstance(originalValue, QDateTime):
            value _ QDateTime.fromString(text, Qt.ISODate)
            if not value.isValid
                return
        elif isinstance(originalValue, QTime):
            value _ QTime.fromString(text, Qt.ISODate)
            if not value.isValid
                return
        elif isinstance(originalValue, QPoint):
            self.pointExp.exactMatch(text)
            value _ QPoint(int(self.pointExp.cap(1)),
                           int(self.pointExp.cap(2)))
        elif isinstance(originalValue, QRect):
            self.rectExp.exactMatch(text)
            value _ QRect(int(self.rectExp.cap(1)),
                          int(self.rectExp.cap(2)),
                          int(self.rectExp.cap(3)),
                          int(self.rectExp.cap(4)))
        elif isinstance(originalValue, QSize):
            self.sizeExp.exactMatch(text)
            value _ QSize(int(self.sizeExp.cap(1)),
                          int(self.sizeExp.cap(2)))
        elif isinstance(originalValue, list):
            value _ text.split(',')
        else:
            value _ type(originalValue)(text)

        model.setData(index, self.displayText(value), Qt.DisplayRole)
        model.setData(index, value, Qt.UserRole)

    @staticmethod
    ___ isSupportedType(value):
        return isinstance(value, (bool, float, int, QByteArray, str, QColor,
                QDate, QDateTime, QTime, QPoint, QRect, QSize, list))

    @staticmethod
    ___ displayText(value):
        if isinstance(value, (bool, int, QByteArray)):
            return str(value)
        if isinstance(value, str):
            return value
        elif isinstance(value, float):
            return '%g' % value
        elif isinstance(value, QColor):
            return '(%u,%u,%u,%u)' % (value.red(), value.green(), value.blue(), value.alpha())
        elif isinstance(value, (QDate, QDateTime, QTime)):
            return value.toString(Qt.ISODate)
        elif isinstance(value, QPoint):
            return '(%d,%d)' % (value.x(), value.y())
        elif isinstance(value, QRect):
            return '(%d,%d,%d,%d)' % (value.x(), value.y(), value.width(), value.height())
        elif isinstance(value, QSize):
            return '(%d,%d)' % (value.width(), value.height())
        elif isinstance(value, list):
            return ','.join(value)
        elif value is None:
            return '<Invalid>'

        return '<%s>' % value


if __name__ == '__main__':
    app _ QApplication(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
