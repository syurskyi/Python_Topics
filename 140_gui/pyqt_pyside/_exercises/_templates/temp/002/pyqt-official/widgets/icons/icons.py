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


____ ?.QtCore ______ QFileInfo, QRegExp, QSize, Qt
____ ?.?G.. ______ QIcon, QImage, QPalette, QPixmap
____ ?.?W.. ______ (QAbstractItemView, ?A.., QActionGroup,
        ?A.., QComboBox, ?FD.., QFrame, QGridLayout, QGroupBox,
        QHBoxLayout, QHeaderView, QItemDelegate, QLabel, QMainWindow,
        ?MB.., QRadioButton, QSizePolicy, QSpinBox, QStyle,
        QStyleFactory, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


c_ IconSizeSpinBox(QSpinBox):
    @staticmethod
    ___ valueFromText(text):
        regExp _ QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")

        __ regExp.exactMatch(text):
            r_ int(regExp.cap(1))
        ____
            r_ 0

    @staticmethod
    ___ textFromValue(value):
        r_ "%d x %d" % (value, value)


c_ ImageDelegate(QItemDelegate):
    ___ createEditor  parent, option, index):
        comboBox _ QComboBox(parent)
        __ index.column() == 1:
            comboBox.addItem("Normal")
            comboBox.addItem("Active")
            comboBox.addItem("Disabled")
            comboBox.addItem("Selected")
        ____ index.column() == 2:
            comboBox.addItem("Off")
            comboBox.addItem("On")

        comboBox.activated.c..(self.emitCommitData)

        r_ comboBox

    ___ setEditorData  editor, index):
        comboBox _ editor
        __ no. comboBox:
            r_

        pos _ comboBox.findText(index.model().data(index), Qt.MatchExactly)
        comboBox.setCurrentIndex(pos)

    ___ setModelData  editor, model, index):
        comboBox _ editor
        __ no. comboBox:
            r_

        model.setData(index, comboBox.currentText())

    ___ emitCommitData(self):
        self.commitData.emit(self.sender())


c_ IconPreviewArea(QWidget):
    ___ __init__  parent_None):
        super(IconPreviewArea, self).__init__(parent)

        mainLayout _ QGridLayout()
        self.setLayout(mainLayout)

        self.icon _ QIcon()
        self.size _ QSize()
        self.stateLabels _ []
        self.modeLabels _ []
        self.pixmapLabels _ []

        self.stateLabels.append(self.createHeaderLabel("Off"))
        self.stateLabels.append(self.createHeaderLabel("On"))

        self.modeLabels.append(self.createHeaderLabel("Normal"))
        self.modeLabels.append(self.createHeaderLabel("Active"))
        self.modeLabels.append(self.createHeaderLabel("Disabled"))
        self.modeLabels.append(self.createHeaderLabel("Selected"))

        for j, label in enumerate(self.stateLabels):
            mainLayout.addWidget(label, j + 1, 0)

        for i, label in enumerate(self.modeLabels):
            mainLayout.addWidget(label, 0, i + 1)

            self.pixmapLabels.append([])
            for j in range(len(self.stateLabels)):
                self.pixmapLabels[i].append(self.createPixmapLabel())
                mainLayout.addWidget(self.pixmapLabels[i][j], j + 1, i + 1)

    ___ setIcon  icon):
        self.icon _ icon
        self.updatePixmapLabels()

    ___ setSize  size):
        __ size !_ self.size:
            self.size _ size
            self.updatePixmapLabels()

    ___ createHeaderLabel  text):
        label _ QLabel("<b>%s</b>" % text)
        label.setAlignment(Qt.AlignCenter)
        r_ label

    ___ createPixmapLabel(self):
        label _ QLabel()
        label.setEnabled F..
        label.setAlignment(Qt.AlignCenter)
        label.setFrameShape(QFrame.Box)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setBackgroundRole(QPalette.Base)
        label.setAutoFillBackground(True)
        label.setMinimumSize(132, 132)
        r_ label

    ___ updatePixmapLabels(self):
        for i in range(len(self.modeLabels)):
            __ i == 0:
                mode _ QIcon.Normal
            ____ i == 1:
                mode _ QIcon.Active
            ____ i == 2:
                mode _ QIcon.Disabled
            ____
                mode _ QIcon.Selected

            for j in range(len(self.stateLabels)):
                state _ QIcon.Off __ j == 0 else QIcon.On
                pixmap _ self.icon.pixmap(self.size, mode, state)
                self.pixmapLabels[i][j].setPixmap(pixmap)
                self.pixmapLabels[i][j].setEnabled(no. pixmap.isNull())


c_ MainWindow ?MW..
    ___ __init__  parent_None):
        super(MainWindow, self).__init__(parent)

        self.centralWidget _ QWidget()
        self.sCW..(self.centralWidget)

        self.createPreviewGroupBox()
        self.createImagesGroupBox()
        self.createIconSizeGroupBox()

        self.createActions()
        self.createMenus()
        self.createContextMenu()

        mainLayout _ QGridLayout()
        mainLayout.addWidget(self.previewGroupBox, 0, 0, 1, 2)
        mainLayout.addWidget(self.imagesGroupBox, 1, 0)
        mainLayout.addWidget(self.iconSizeGroupBox, 1, 1)
        self.centralWidget.setLayout(mainLayout)

        self.setWindowTitle("Icons")
        self.checkCurrentStyle()
        self.otherRadioButton.click()

        self.resize(self.minimumSizeHint())

    ___ about(self):
        ?MB...about  "About Icons",
                "The <b>Icons</b> example illustrates how Qt renders an icon "
                "in different modes (active, normal, disabled and selected) "
                "and states (on and off) based on a set of images.")

    ___ changeStyle  checked):
        __ no. checked:
            r_

        action _ self.sender()
        style _ QStyleFactory.create(action.data())
        __ no. style:
            r_

        ?A...setStyle(style)

        self.setButtonText(self.smallRadioButton, "Small (%d x %d)",
                style, QStyle.PM_SmallIconSize)
        self.setButtonText(self.largeRadioButton, "Large (%d x %d)",
                style, QStyle.PM_LargeIconSize)
        self.setButtonText(self.toolBarRadioButton, "Toolbars (%d x %d)",
                style, QStyle.PM_ToolBarIconSize)
        self.setButtonText(self.listViewRadioButton, "List views (%d x %d)",
                style, QStyle.PM_ListViewIconSize)
        self.setButtonText(self.iconViewRadioButton, "Icon views (%d x %d)",
                style, QStyle.PM_IconViewIconSize)
        self.setButtonText(self.tabBarRadioButton, "Tab bars (%d x %d)",
                style, QStyle.PM_TabBarIconSize)

        self.changeSize()

    @staticmethod
    ___ setButtonText(button, label, style, metric):
        metric_value _ style.pixelMetric(metric)
        button.sT..(label % (metric_value, metric_value))

    ___ changeSize  checked_True):
        __ no. checked:
            r_

        __ self.otherRadioButton.isChecked
            extent _ self.otherSpinBox.value()
        ____
            __ self.smallRadioButton.isChecked
                metric _ QStyle.PM_SmallIconSize
            ____ self.largeRadioButton.isChecked
                metric _ QStyle.PM_LargeIconSize
            ____ self.toolBarRadioButton.isChecked
                metric _ QStyle.PM_ToolBarIconSize
            ____ self.listViewRadioButton.isChecked
                metric _ QStyle.PM_ListViewIconSize
            ____ self.iconViewRadioButton.isChecked
                metric _ QStyle.PM_IconViewIconSize
            ____
                metric _ QStyle.PM_TabBarIconSize

            extent _ ?A...style().pixelMetric(metric)

        self.previewArea.setSize(QSize(extent, extent))
        self.otherSpinBox.setEnabled(self.otherRadioButton.isChecked())

    ___ changeIcon(self):
        icon _ QIcon()

        for row in range(self.imagesTable.rowCount()):
            item0 _ self.imagesTable.item(row, 0)
            item1 _ self.imagesTable.item(row, 1)
            item2 _ self.imagesTable.item(row, 2)

            __ item0.checkState() == Qt.Checked:
                __ item1.text() == "Normal":
                    mode _ QIcon.Normal
                ____ item1.text() == "Active":
                    mode _ QIcon.Active
                ____ item1.text() == "Disabled":
                    mode _ QIcon.Disabled
                ____
                    mode _ QIcon.Selected

                __ item2.text() == "On":
                    state _ QIcon.On
                ____
                    state _ QIcon.Off

                fileName _ item0.data(Qt.UserRole)
                image _ QImage(fileName)
                __ no. image.isNull
                    icon.addPixmap(QPixmap.fromImage(image), mode, state)

        self.previewArea.setIcon(icon)

    ___ addImage(self):
        fileNames, _ _ ?FD...getOpenFileNames  "Open Images", '',
                "Images (*.png *.xpm *.jpg);;All Files (*)")

        for fileName in fileNames:
            row _ self.imagesTable.rowCount()
            self.imagesTable.setRowCount(row + 1)

            imageName _ QFileInfo(fileName).baseName()
            item0 _ QTableWidgetItem(imageName)
            item0.setData(Qt.UserRole, fileName)
            item0.setFlags(item0.flags() & ~Qt.ItemIsEditable)

            item1 _ QTableWidgetItem("Normal")
            item2 _ QTableWidgetItem("Off")

            __ self.guessModeStateAct.isChecked
                __ '_act' in fileName:
                    item1.sT..("Active")
                ____ '_dis' in fileName:
                    item1.sT..("Disabled")
                ____ '_sel' in fileName:
                    item1.sT..("Selected")

                __ '_on' in fileName:
                    item2.sT..("On")

            self.imagesTable.setItem(row, 0, item0)
            self.imagesTable.setItem(row, 1, item1)
            self.imagesTable.setItem(row, 2, item2)
            self.imagesTable.openPersistentEditor(item1)
            self.imagesTable.openPersistentEditor(item2)

            item0.setCheckState(Qt.Checked)

    ___ removeAllImages(self):
        self.imagesTable.setRowCount(0)
        self.changeIcon()

    ___ createPreviewGroupBox(self):
        self.previewGroupBox _ QGroupBox("Preview")

        self.previewArea _ IconPreviewArea()

        layout _ QVBoxLayout()
        layout.addWidget(self.previewArea)
        self.previewGroupBox.setLayout(layout)

    ___ createImagesGroupBox(self):
        self.imagesGroupBox _ QGroupBox("Images")

        self.imagesTable _ QTableWidget()
        self.imagesTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.imagesTable.setItemDelegate(ImageDelegate(self))

        self.imagesTable.horizontalHeader().setDefaultSectionSize(90)
        self.imagesTable.setColumnCount(3)
        self.imagesTable.setHorizontalHeaderLabels(("Image", "Mode", "State"))
        self.imagesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.imagesTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.imagesTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.imagesTable.verticalHeader().hide()

        self.imagesTable.itemChanged.c..(self.changeIcon)

        layout _ QVBoxLayout()
        layout.addWidget(self.imagesTable)
        self.imagesGroupBox.setLayout(layout)

    ___ createIconSizeGroupBox(self):
        self.iconSizeGroupBox _ QGroupBox("Icon Size")

        self.smallRadioButton _ QRadioButton()
        self.largeRadioButton _ QRadioButton()
        self.toolBarRadioButton _ QRadioButton()
        self.listViewRadioButton _ QRadioButton()
        self.iconViewRadioButton _ QRadioButton()
        self.tabBarRadioButton _ QRadioButton()
        self.otherRadioButton _ QRadioButton("Other:")

        self.otherSpinBox _ IconSizeSpinBox()
        self.otherSpinBox.setRange(8, 128)
        self.otherSpinBox.setValue(64)

        self.smallRadioButton.toggled.c..(self.changeSize)
        self.largeRadioButton.toggled.c..(self.changeSize)
        self.toolBarRadioButton.toggled.c..(self.changeSize)
        self.listViewRadioButton.toggled.c..(self.changeSize)
        self.iconViewRadioButton.toggled.c..(self.changeSize)
        self.tabBarRadioButton.toggled.c..(self.changeSize)
        self.otherRadioButton.toggled.c..(self.changeSize)
        self.otherSpinBox.valueChanged.c..(self.changeSize)

        otherSizeLayout _ QHBoxLayout()
        otherSizeLayout.addWidget(self.otherRadioButton)
        otherSizeLayout.addWidget(self.otherSpinBox)
        otherSizeLayout.addStretch()

        layout _ QGridLayout()
        layout.addWidget(self.smallRadioButton, 0, 0)
        layout.addWidget(self.largeRadioButton, 1, 0)
        layout.addWidget(self.toolBarRadioButton, 2, 0)
        layout.addWidget(self.listViewRadioButton, 0, 1)
        layout.addWidget(self.iconViewRadioButton, 1, 1)
        layout.addWidget(self.tabBarRadioButton, 2, 1)
        layout.addLayout(otherSizeLayout, 3, 0, 1, 2)
        layout.setRowStretch(4, 1)
        self.iconSizeGroupBox.setLayout(layout)

    ___ createActions(self):
        self.addImagesAct _ ?A..("&Add Images...", self, shortcut_"Ctrl+A",
                triggered_self.addImage)

        self.removeAllImagesAct _ ?A..("&Remove All Images", self,
                shortcut_"Ctrl+R", triggered_self.removeAllImages)

        self.exitAct _ ?A..("&Quit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.styleActionGroup _ QActionGroup(self)
        for styleName in QStyleFactory.keys
            action _ ?A..(self.styleActionGroup,
                    text_"%s Style" % styleName, checkable_True,
                    triggered_self.changeStyle)
            action.setData(styleName)

        self.guessModeStateAct _ ?A..("&Guess Image Mode/State", self,
                checkable_True, checked_True)

        self.aboutAct _ ?A..("&About", self, triggered_self.about)

        self.aboutQtAct _ ?A..("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.mB.. .aM..("&File")
        self.fileMenu.aA..(self.addImagesAct)
        self.fileMenu.aA..(self.removeAllImagesAct)
        self.fileMenu.addSeparator()
        self.fileMenu.aA..(self.exitAct)

        self.viewMenu _ self.mB.. .aM..("&View")
        for action in self.styleActionGroup.actions
            self.viewMenu.aA..(action)
        self.viewMenu.addSeparator()
        self.viewMenu.aA..(self.guessModeStateAct)

        self.mB.. .addSeparator()

        self.helpMenu _ self.mB.. .aM..("&Help")
        self.helpMenu.aA..(self.aboutAct)
        self.helpMenu.aA..(self.aboutQtAct)

    ___ createContextMenu(self):
        self.imagesTable.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.imagesTable.aA..(self.addImagesAct)
        self.imagesTable.aA..(self.removeAllImagesAct)

    ___ checkCurrentStyle(self):
        for action in self.styleActionGroup.actions
            styleName _ action.data()
            candidate _ QStyleFactory.create(styleName)

            __ candidate __ N..:
                r_

            __ candidate.metaObject().className() == ?A...style().metaObject().className
                action.trigger()


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
