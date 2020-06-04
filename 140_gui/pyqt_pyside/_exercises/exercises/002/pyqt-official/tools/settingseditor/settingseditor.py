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

____ ?.?C.. ______ (QByteArray, ?D.., ?DT__, QEvent, QPoint, QRect,
        QRegExp, QSettings, ?S.., __, ?T.., ?T..)
____ ?.?G.. ______ ?C.., ?I.., QRegExpValidator, ?V..
____ ?.?W.. ______ (?AIV.., ?A.., ?A..,
        ?CB, ?D.., ?DBB..., ?FD.., QGridLayout,
        ?GB.., ?HV.., QInputDialog, QItemDelegate, ?L.., QLineEdit,
        ?MW.., ?MB.., ?S.., QStyleOptionViewItem, ?TW..,
        ?TWI.., QTreeWidget, ?TWI.., ?VBL..)


c_ MainWindow ?MW..
    ___  -   parent_None):
        s__(MainWindow, self). - (parent)

        settingsTree _ SettingsTree()
        sCW..(settingsTree)

        locationDialog _ N..

        createActions()
        createMenus()

        autoRefreshAct.sC__( st.
        fallbacksAct.sC__( st.

        sWT..("Settings Editor")
        r..(500, 600)

    ___ openSettings
        __ locationDialog __ N..:
            locationDialog _ LocationDialog

        __ locationDialog.e..
            settings _ QSettings(locationDialog.f..(),
                                        locationDialog.scope(),
                                        locationDialog.organization(),
                                        locationDialog.application())
            setSettingsObject(settings)
            fallbacksAct.sE..( st.

    ___ openIniFile
        fileName, _ _ ?FD...gOFN..  "Open INI File", '',
                "INI Files (*.ini *.conf)")

        __ fileName:
            settings _ QSettings(fileName, QSettings.IniFormat)
            setSettingsObject(settings)
            fallbacksAct.sE.. F..

    ___ openPropertyList
        fileName, _ _ ?FD...gOFN..  "Open Property List",
                '', "Property List Files (*.plist)")

        __ fileName:
            settings _ QSettings(fileName, QSettings.NativeFormat)
            setSettingsObject(settings)
            fallbacksAct.sE.. F..

    ___ openRegistryPath
        pa__, ok _ QInputDialog.getText  "Open Registry Path",
                "Enter the path in the Windows registry:", QLineEdit.Normal,
                'HKEY_CURRENT_USER\\')

        __ ok and pa__ !_ '':
            settings _ QSettings(pa__, QSettings.NativeFormat)
            setSettingsObject(settings)
            fallbacksAct.sE.. F..

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
            openPropertyListAct.sE.. F..

        openRegistryPathAct _ ?A..("Open Windows &Registry Path...",
                self, shortcut_"Ctrl+G", triggered_self.openRegistryPath)
        __ ___.platform !_ 'win32':
            openRegistryPathAct.sE.. F..

        refreshAct _ ?A..("&Refresh", self, shortcut_"Ctrl+R",
                enabled_False, triggered_self.settingsTree.refresh)

        exitAct _ ?A..("E&xit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        autoRefreshAct _ ?A..("&Auto-Refresh", self, shortcut_"Ctrl+A",
                checkable_True, enabled_False)
        autoRefreshAct.t__.c..(settingsTree.setAutoRefresh)
        autoRefreshAct.t__.c..(refreshAct.sD..)

        fallbacksAct _ ?A..("&Fallbacks", self, shortcut_"Ctrl+F",
                checkable_True, enabled_False,
                triggered_self.settingsTree.setFallbacksEnabled)

        aboutAct _ ?A..("&About", self, triggered_self.about)

        aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.i.. .aboutQt)

    ___ createMenus
        fileMenu _ mB.. .aM..("&File")
        fileMenu.aA..(openSettingsAct)
        fileMenu.aA..(openIniFileAct)
        fileMenu.aA..(openPropertyListAct)
        fileMenu.aA..(openRegistryPathAct)
        fileMenu.aS..)
        fileMenu.aA..(refreshAct)
        fileMenu.aS..)
        fileMenu.aA..(exitAct)

        optionsMenu _ mB.. .aM..("&Options")
        optionsMenu.aA..(autoRefreshAct)
        optionsMenu.aA..(fallbacksAct)

        mB.. .aS..)

        helpMenu _ mB.. .aM..("&Help")
        helpMenu.aA..(aboutAct)
        helpMenu.aA..(aboutQtAct)

    ___ setSettingsObject  settings):
        settings.setFallbacksEnabled(fallbacksAct.isChecked())
        settingsTree.setSettingsObject(settings)

        refreshAct.sE..( st.
        autoRefreshAct.sE..( st.

        niceName _ settings.fN..
        niceName.replace('\\', '/')
        niceName _ niceName.sp..('/')[-1]

        __ no. settings.isWritable
            niceName +_ " (read only)"

        sWT..("%s - Settings Editor" % niceName)


c_ LocationDialog(?D..):
    ___  -   parent_None):
        s__(LocationDialog, self). - (parent)

        formatComboBox _ ?CB()
        formatComboBox.aI..("Native")
        formatComboBox.aI..("INI")

        scopeComboBox _ ?CB()
        scopeComboBox.aI..("User")
        scopeComboBox.aI..("System")

        organizationComboBox _ ?CB()
        organizationComboBox.aI..("Trolltech")
        organizationComboBox.sE..( st.

        applicationComboBox _ ?CB()
        applicationComboBox.aI..("Any")
        applicationComboBox.aI..("Application Example")
        applicationComboBox.aI..("Assistant")
        applicationComboBox.aI..("Designer")
        applicationComboBox.aI..("Linguist")
        applicationComboBox.sE..( st.
        applicationComboBox.sCI..(3)

        formatLabel _ ?L..("&Format:")
        formatLabel.setBuddy(formatComboBox)

        scopeLabel _ ?L..("&Scope:")
        scopeLabel.setBuddy(scopeComboBox)

        organizationLabel _ ?L..("&Organization:")
        organizationLabel.setBuddy(organizationComboBox)

        applicationLabel _ ?L..("&Application:")
        applicationLabel.setBuddy(applicationComboBox)

        locationsGroupBox _ ?GB..("Setting Locations")

        locationsTable _ ?TW..()
        locationsTable.setSelectionMode(?AIV...SingleSelection)
        locationsTable.setSelectionBehavior(?AIV...SelectRows)
        locationsTable.setEditTriggers(?AIV...NoEditTriggers)
        locationsTable.sCC..(2)
        locationsTable.sHHL..(("Location", "Access"))
        locationsTable.hH.. .sSRM..(0, ?HV...Stretch)
        locationsTable.hH.. .resizeSection(1, 180)

        buttonBox _ ?DBB...(?DBB....Ok | ?DBB....Cancel)

        formatComboBox.activated.c..(updateLocationsTable)
        scopeComboBox.activated.c..(updateLocationsTable)
        organizationComboBox.lineEdit().eF__.c..(updateLocationsTable)
        applicationComboBox.lineEdit().eF__.c..(updateLocationsTable)
        buttonBox.a___.c..(accept)
        buttonBox.r___.c..(reject)

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

        sWT..("Open Application Settings")
        r..(650, 400)

    ___ f..
        __ formatComboBox.currentIndex() __ 0:
            r_ QSettings.NativeFormat
        ____
            r_ QSettings.IniFormat

    ___ scope
        __ scopeComboBox.currentIndex() __ 0:
            r_ QSettings.UserScope
        ____
            r_ QSettings.SystemScope

    ___ organization
        r_ organizationComboBox.currentText()

    ___ application
        __ applicationComboBox.currentText() __ "Any":
            r_ ''

        r_ applicationComboBox.currentText()

    ___ updateLocationsTable
        locationsTable.setUpdatesEnabled F..
        locationsTable.sRC..(0)

        ___ i __ ra..(2):
            __ i __ 0:
                __ scope() __ QSettings.SystemScope:
                    c___

                actualScope _ QSettings.UserScope
            ____
                actualScope _ QSettings.SystemScope

            ___ j __ ra..(2):
                __ j __ 0:
                    __ no. application
                        c___

                    actualApplication _ application()
                ____
                    actualApplication _ ''

                settings _ QSettings(f..(), actualScope,
                        organization(), actualApplication)

                row _ locationsTable.rowCount()
                locationsTable.sRC..(row + 1)

                item0 _ ?TWI..()
                item0.sT..(settings.fileName())

                item1 _ ?TWI..()
                disable _ no. (settings.childKeys() or settings.childGroups())

                __ row __ 0:
                    __ settings.isWritable
                        item1.sT..("Read-write")
                        disable _ F..
                    ____
                        item1.sT..("Read-only")
                    buttonBox.button(?DBB....Ok).sD..(disable)
                ____
                    item1.sT..("Read-only fallback")

                __ disable:
                    item0.setFlags(item0.flags() & ~__.ItemIsEnabled)
                    item1.setFlags(item1.flags() & ~__.ItemIsEnabled)

                locationsTable.setItem(row, 0, item0)
                locationsTable.setItem(row, 1, item1)

        locationsTable.setUpdatesEnabled( st.


c_ SettingsTree(QTreeWidget):
    ___  -   parent_None):
        s__(SettingsTree, self). - (parent)

        sID..(VariantDelegate(self))

        setHeaderLabels(("Setting", "Type", "Value"))
        header().sSRM..(0, ?HV...Stretch)
        header().sSRM..(2, ?HV...Stretch)

        settings _ N..
        refreshTimer _ ?T..
        refreshTimer.sI..(2000)
        autoRefresh _ F..

        groupIcon _ ?I..
        groupIcon.aP..(style().standardPixmap(?S...SP_DirClosedIcon),
                ?I...Normal, ?I...Off)
        groupIcon.aP..(style().standardPixmap(?S...SP_DirOpenIcon),
                ?I...Normal, ?I...On)
        keyIcon _ ?I..
        keyIcon.aP..(style().standardPixmap(?S...SP_FileIcon))

        refreshTimer.timeout.c..(maybeRefresh)

    ___ setSettingsObject  settings):
        settings _ settings
        c..

        __ settings __ no. N..:
            settings.setParent
            refresh()
            __ autoRefresh:
                refreshTimer.start()
        ____
            refreshTimer.s..

    ___ sH..
        r_ ?S..(800, 600)

    ___ setAutoRefresh  autoRefresh):
        autoRefresh _ autoRefresh

        __ settings __ no. N..:
            __ autoRefresh:
                maybeRefresh()
                refreshTimer.start()
            ____
                refreshTimer.s..

    ___ setFallbacksEnabled  enabled):
        __ settings __ no. N..:
            settings.setFallbacksEnabled(enabled)
            refresh()

    ___ maybeRefresh
        __ s.. !_ ?AIV...EditingState:
            refresh()

    ___ refresh
        __ settings __ N..:
            r_

        # The signal might not be connected.
        ___
            itemChanged.disconnect(updateSetting)
        _____:
            p..

        settings.sync()
        updateChildItems(N..)

        itemChanged.c..(updateSetting)

    ___ event  event):
        __ event.type() __ QEvent.WindowActivate:
            __ isActiveWindow() and autoRefresh:
                maybeRefresh()

        r_ s__(SettingsTree, self).event(event)

    ___ updateSetting  item):
        key _ item.t__(0)
        ancestor _ item.parent()

        w__ ancestor:
            key _ ancestor.t__(0) + '/' + key
            ancestor _ ancestor.parent()

        d _ item.data(2, __.UserRole)
        settings.sV..(key, item.data(2, __.UserRole))

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

            child.sI..(0, groupIcon)
            dividerIndex +_ 1

            settings.beginGroup(group)
            updateChildItems(child)
            settings.endGroup()

        ___ key __ settings.childKeys
            childIndex _ findChild(parent, key, 0)
            __ childIndex __ -1 or childIndex >_ dividerIndex:
                __ childIndex !_ -1:
                    child _ childAt(parent, childIndex)
                    ___ i __ ra..(child.childCount()):
                        deleteItem(child, i)
                    moveItemForward(parent, childIndex, dividerIndex)
                ____
                    child _ createItem(key, parent, dividerIndex)
                child.sI..(0, keyIcon)
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
            item _ ?TWI..(parent, after)
        ____
            item _ ?TWI..  after)

        item.sT..(0, t__)
        item.setFlags(item.flags() | __.IIE..)
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
        ___ i __ ra..(childCount(parent)):
            __ childAt(parent, i).t__(0) __ t__:
                r_ i
        r_ -1

    ___ moveItemForward  parent, oldIndex, newIndex):
        ___ in. __ ra..(oldIndex - newIndex):
            deleteItem(parent, newIndex)


c_ VariantDelegate(QItemDelegate):
    ___  -   parent_None):
        s__(VariantDelegate, self). - (parent)

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
        __ i...column() __ 2:
            value _ i...model().data(index, __.UserRole)
            __ no. isSupportedType(value):
                myOption _ QStyleOptionViewItem(option)
                myOption.state &_ ~?S...State_Enabled
                s__(VariantDelegate, self).paint(painter, myOption, index)
                r_

        s__(VariantDelegate, self).paint(painter, option, index)

    ___ createEditor  parent, option, index):
        __ i...column() !_ 2:
            r_ N..

        originalValue _ i...model().data(index, __.UserRole)
        __ no. isSupportedType(originalValue):
            r_ N..

        lineEdit _ QLineEdit(parent)
        lineEdit.setFrame F..

        __ isinstance(originalValue, bool):
            regExp _ boolExp
        ____ isinstance(originalValue, fl..):
            regExp _ doubleExp
        ____ isinstance(originalValue, in.):
            regExp _ signedIntegerExp
        ____ isinstance(originalValue, QByteArray):
            regExp _ byteArrayExp
        ____ isinstance(originalValue, ?C..):
            regExp _ colorExp
        ____ isinstance(originalValue, ?D..):
            regExp _ dateExp
        ____ isinstance(originalValue, ?DT__):
            regExp _ dateTimeExp
        ____ isinstance(originalValue, ?T..):
            regExp _ timeExp
        ____ isinstance(originalValue, QPoint):
            regExp _ pointExp
        ____ isinstance(originalValue, QRect):
            regExp _ rectExp
        ____ isinstance(originalValue, ?S..):
            regExp _ sizeExp
        ____
            regExp _ QRegExp()

        __ no. regExp.isEmpty
            validator _ QRegExpValidator(regExp, lineEdit)
            lineEdit.sV..(validator)

        r_ lineEdit

    ___ setEditorData  editor, index):
        value _ i...model().data(index, __.UserRole)
        __ editor __ no. N..:
            editor.sT..(displayText(value))

    ___ setModelData  editor, model, index):
        __ no. editor.iM..
            r_

        t__ _ editor.t__()
        validator _ editor.validator()
        __ validator __ no. N..:
            state, t__, _ _ validator.validate(t__, 0)
            __ state !_ ?V...A..:
                r_

        originalValue _ i...model().data(index, __.UserRole)

        __ isinstance(originalValue, ?C..):
            colorExp.exactMatch(t__)
            value _ ?C..(min(in.(colorExp.cap(1)), 255),
                           min(in.(colorExp.cap(2)), 255),
                           min(in.(colorExp.cap(3)), 255),
                           min(in.(colorExp.cap(4)), 255))
        ____ isinstance(originalValue, ?D..):
            value _ ?D...fromString(t__, __.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, ?DT__):
            value _ ?DT__.fromString(t__, __.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, ?T..):
            value _ ?T...fromString(t__, __.ISODate)
            __ no. value.isValid
                r_
        ____ isinstance(originalValue, QPoint):
            pointExp.exactMatch(t__)
            value _ QPoint(in.(pointExp.cap(1)),
                           in.(pointExp.cap(2)))
        ____ isinstance(originalValue, QRect):
            rectExp.exactMatch(t__)
            value _ QRect(in.(rectExp.cap(1)),
                          in.(rectExp.cap(2)),
                          in.(rectExp.cap(3)),
                          in.(rectExp.cap(4)))
        ____ isinstance(originalValue, ?S..):
            sizeExp.exactMatch(t__)
            value _ ?S..(in.(sizeExp.cap(1)),
                          in.(sizeExp.cap(2)))
        ____ isinstance(originalValue, li..):
            value _ t__.sp..(',')
        ____
            value _ type(originalValue)(t__)

        model.setData(i.., displayText(value), __.DR..)
        model.setData(index, value, __.UserRole)

    @staticmethod
    ___ isSupportedType(value):
        r_ isinstance(value, (bool, fl.., in., QByteArray, st., ?C..,
                ?D.., ?DT__, ?T.., QPoint, QRect, ?S.., li..))

    @staticmethod
    ___ displayText(value):
        __ isinstance(value, (bool, in., QByteArray)):
            r_ st.(value)
        __ isinstance(value, st.):
            r_ value
        ____ isinstance(value, fl..):
            r_ '%g' % value
        ____ isinstance(value, ?C..):
            r_ '(%u,%u,%u,%u)' % (value.red(), value.green(), value.blue(), value.alpha())
        ____ isinstance(value, (?D.., ?DT__, ?T..)):
            r_ value.toString(__.ISODate)
        ____ isinstance(value, QPoint):
            r_ '(%d,%d)' % (value.x(), value.y())
        ____ isinstance(value, QRect):
            r_ '(%d,%d,%d,%d)' % (value.x(), value.y(), value.width(), value.height())
        ____ isinstance(value, ?S..):
            r_ '(%d,%d)' % (value.width(), value.height())
        ____ isinstance(value, li..):
            r_ ','.join(value)
        ____ value __ N..:
            r_ '<Invalid>'

        r_ '<%s>' % value


__ ______ __ ______
    app _ ?A..(___.a..
    mainWin _ MainWindow()
    mainWin.s..
    ___.e.. ?.e..
