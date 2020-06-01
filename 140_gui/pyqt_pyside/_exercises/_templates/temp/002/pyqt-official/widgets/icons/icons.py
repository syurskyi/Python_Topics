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
____ ?.QtGui ______ QIcon, QImage, QPalette, QPixmap
____ ?.?W.. ______ (QAbstractItemView, QAction, QActionGroup,
        QApplication, QComboBox, QFileDialog, QFrame, QGridLayout, QGroupBox,
        QHBoxLayout, QHeaderView, QItemDelegate, QLabel, QMainWindow,
        QMessageBox, QRadioButton, QSizePolicy, QSpinBox, QStyle,
        QStyleFactory, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class IconSizeSpinBox(QSpinBox):
    @staticmethod
    ___ valueFromText(text):
        regExp _ QRegExp("(\\d+)(\\s*[xx]\\s*\\d+)?")

        if regExp.exactMatch(text):
            return int(regExp.cap(1))
        else:
            return 0

    @staticmethod
    ___ textFromValue(value):
        return "%d x %d" % (value, value)


class ImageDelegate(QItemDelegate):
    ___ createEditor(self, parent, option, index):
        comboBox _ QComboBox(parent)
        if index.column() == 1:
            comboBox.addItem("Normal")
            comboBox.addItem("Active")
            comboBox.addItem("Disabled")
            comboBox.addItem("Selected")
        elif index.column() == 2:
            comboBox.addItem("Off")
            comboBox.addItem("On")

        comboBox.activated.c..(self.emitCommitData)

        return comboBox

    ___ setEditorData(self, editor, index):
        comboBox _ editor
        if not comboBox:
            return

        pos _ comboBox.findText(index.model().data(index), Qt.MatchExactly)
        comboBox.setCurrentIndex(pos)

    ___ setModelData(self, editor, model, index):
        comboBox _ editor
        if not comboBox:
            return

        model.setData(index, comboBox.currentText())

    ___ emitCommitData(self):
        self.commitData.emit(self.sender())


class IconPreviewArea(QWidget):
    ___ __init__(self, parent_None):
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

    ___ setIcon(self, icon):
        self.icon _ icon
        self.updatePixmapLabels()

    ___ setSize(self, size):
        if size !_ self.size:
            self.size _ size
            self.updatePixmapLabels()

    ___ createHeaderLabel(self, text):
        label _ QLabel("<b>%s</b>" % text)
        label.setAlignment(Qt.AlignCenter)
        return label

    ___ createPixmapLabel(self):
        label _ QLabel()
        label.setEnabled(False)
        label.setAlignment(Qt.AlignCenter)
        label.setFrameShape(QFrame.Box)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setBackgroundRole(QPalette.Base)
        label.setAutoFillBackground(True)
        label.setMinimumSize(132, 132)
        return label

    ___ updatePixmapLabels(self):
        for i in range(len(self.modeLabels)):
            if i == 0:
                mode _ QIcon.Normal
            elif i == 1:
                mode _ QIcon.Active
            elif i == 2:
                mode _ QIcon.Disabled
            else:
                mode _ QIcon.Selected

            for j in range(len(self.stateLabels)):
                state _ QIcon.Off if j == 0 else QIcon.On
                pixmap _ self.icon.pixmap(self.size, mode, state)
                self.pixmapLabels[i][j].setPixmap(pixmap)
                self.pixmapLabels[i][j].setEnabled(not pixmap.isNull())


class MainWindow(QMainWindow):
    ___ __init__(self, parent_None):
        super(MainWindow, self).__init__(parent)

        self.centralWidget _ QWidget()
        self.setCentralWidget(self.centralWidget)

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
        QMessageBox.about(self, "About Icons",
                "The <b>Icons</b> example illustrates how Qt renders an icon "
                "in different modes (active, normal, disabled and selected) "
                "and states (on and off) based on a set of images.")

    ___ changeStyle(self, checked):
        if not checked:
            return

        action _ self.sender()
        style _ QStyleFactory.create(action.data())
        if not style:
            return

        QApplication.setStyle(style)

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

    ___ changeSize(self, checked_True):
        if not checked:
            return

        if self.otherRadioButton.isChecked
            extent _ self.otherSpinBox.value()
        else:
            if self.smallRadioButton.isChecked
                metric _ QStyle.PM_SmallIconSize
            elif self.largeRadioButton.isChecked
                metric _ QStyle.PM_LargeIconSize
            elif self.toolBarRadioButton.isChecked
                metric _ QStyle.PM_ToolBarIconSize
            elif self.listViewRadioButton.isChecked
                metric _ QStyle.PM_ListViewIconSize
            elif self.iconViewRadioButton.isChecked
                metric _ QStyle.PM_IconViewIconSize
            else:
                metric _ QStyle.PM_TabBarIconSize

            extent _ QApplication.style().pixelMetric(metric)

        self.previewArea.setSize(QSize(extent, extent))
        self.otherSpinBox.setEnabled(self.otherRadioButton.isChecked())

    ___ changeIcon(self):
        icon _ QIcon()

        for row in range(self.imagesTable.rowCount()):
            item0 _ self.imagesTable.item(row, 0)
            item1 _ self.imagesTable.item(row, 1)
            item2 _ self.imagesTable.item(row, 2)

            if item0.checkState() == Qt.Checked:
                if item1.text() == "Normal":
                    mode _ QIcon.Normal
                elif item1.text() == "Active":
                    mode _ QIcon.Active
                elif item1.text() == "Disabled":
                    mode _ QIcon.Disabled
                else:
                    mode _ QIcon.Selected

                if item2.text() == "On":
                    state _ QIcon.On
                else:
                    state _ QIcon.Off

                fileName _ item0.data(Qt.UserRole)
                image _ QImage(fileName)
                if not image.isNull
                    icon.addPixmap(QPixmap.fromImage(image), mode, state)

        self.previewArea.setIcon(icon)

    ___ addImage(self):
        fileNames, _ _ QFileDialog.getOpenFileNames(self, "Open Images", '',
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

            if self.guessModeStateAct.isChecked
                if '_act' in fileName:
                    item1.sT..("Active")
                elif '_dis' in fileName:
                    item1.sT..("Disabled")
                elif '_sel' in fileName:
                    item1.sT..("Selected")

                if '_on' in fileName:
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
        self.addImagesAct _ QAction("&Add Images...", self, shortcut_"Ctrl+A",
                triggered_self.addImage)

        self.removeAllImagesAct _ QAction("&Remove All Images", self,
                shortcut_"Ctrl+R", triggered_self.removeAllImages)

        self.exitAct _ QAction("&Quit", self, shortcut_"Ctrl+Q",
                triggered_self.close)

        self.styleActionGroup _ QActionGroup(self)
        for styleName in QStyleFactory.keys
            action _ QAction(self.styleActionGroup,
                    text_"%s Style" % styleName, checkable_True,
                    triggered_self.changeStyle)
            action.setData(styleName)

        self.guessModeStateAct _ QAction("&Guess Image Mode/State", self,
                checkable_True, checked_True)

        self.aboutAct _ QAction("&About", self, triggered_self.about)

        self.aboutQtAct _ QAction("About &Qt", self,
                triggered_QApplication.instance().aboutQt)

    ___ createMenus(self):
        self.fileMenu _ self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.addImagesAct)
        self.fileMenu.addAction(self.removeAllImagesAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu _ self.menuBar().addMenu("&View")
        for action in self.styleActionGroup.actions
            self.viewMenu.addAction(action)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.guessModeStateAct)

        self.menuBar().addSeparator()

        self.helpMenu _ self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    ___ createContextMenu(self):
        self.imagesTable.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.imagesTable.addAction(self.addImagesAct)
        self.imagesTable.addAction(self.removeAllImagesAct)

    ___ checkCurrentStyle(self):
        for action in self.styleActionGroup.actions
            styleName _ action.data()
            candidate _ QStyleFactory.create(styleName)

            if candidate is None:
                return

            if candidate.metaObject().className() == QApplication.style().metaObject().className
                action.trigger()


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    mainWin _ MainWindow()
    mainWin.s..
    sys.exit(app.exec_())
