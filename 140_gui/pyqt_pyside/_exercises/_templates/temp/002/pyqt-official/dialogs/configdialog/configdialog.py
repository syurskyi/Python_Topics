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


____ ?.QtCore ______ QDate, QSize, Qt
____ ?.?G.. ______ QIcon
____ ?.?W.. ______ (?A.., QCheckBox, QComboBox, QDateTimeEdit,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListView, QListWidget, QListWidgetItem, ?PB.., QSpinBox,
        QStackedWidget, QVBoxLayout, QWidget)

______ configdialog_rc


c_ ConfigurationPage(QWidget):
    ___ __init__  parent_None):
        super(ConfigurationPage, self).__init__(parent)

        configGroup _ QGroupBox("Server configuration")

        serverLabel _ QLabel("Server:")
        serverCombo _ QComboBox()
        serverCombo.addItem("Trolltech (Australia)")
        serverCombo.addItem("Trolltech (Germany)")
        serverCombo.addItem("Trolltech (Norway)")
        serverCombo.addItem("Trolltech (People's Republic of China)")
        serverCombo.addItem("Trolltech (USA)")

        serverLayout _ QHBoxLayout()
        serverLayout.addWidget(serverLabel)
        serverLayout.addWidget(serverCombo)

        configLayout _ QVBoxLayout()
        configLayout.addLayout(serverLayout)
        configGroup.setLayout(configLayout)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


c_ UpdatePage(QWidget):
    ___ __init__  parent_None):
        super(UpdatePage, self).__init__(parent)

        updateGroup _ QGroupBox("Package selection")
        systemCheckBox _ QCheckBox("Update system")
        appsCheckBox _ QCheckBox("Update applications")
        docsCheckBox _ QCheckBox("Update documentation")

        packageGroup _ QGroupBox("Existing packages")

        packageList _ QListWidget()
        qtItem _ QListWidgetItem(packageList)
        qtItem.sT..("Qt")
        qsaItem _ QListWidgetItem(packageList)
        qsaItem.sT..("QSA")
        teamBuilderItem _ QListWidgetItem(packageList)
        teamBuilderItem.sT..("Teambuilder")

        startUpdateButton _ ?PB..("Start update")

        updateLayout _ QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateLayout.addWidget(appsCheckBox)
        updateLayout.addWidget(docsCheckBox)
        updateGroup.setLayout(updateLayout)

        packageLayout _ QVBoxLayout()
        packageLayout.addWidget(packageList)
        packageGroup.setLayout(packageLayout)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(updateGroup)
        mainLayout.addWidget(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startUpdateButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


c_ QueryPage(QWidget):
    ___ __init__  parent_None):
        super(QueryPage, self).__init__(parent)

        packagesGroup _ QGroupBox("Look for packages")

        nameLabel _ QLabel("Name:")
        nameEdit _ QLineEdit()

        dateLabel _ QLabel("Released after:")
        dateEdit _ QDateTimeEdit(QDate.currentDate())

        releasesCheckBox _ QCheckBox("Releases")
        upgradesCheckBox _ QCheckBox("Upgrades")

        hitsSpinBox _ QSpinBox()
        hitsSpinBox.setPrefix("Return up to ")
        hitsSpinBox.setSuffix(" results")
        hitsSpinBox.setSpecialValueText("Return only the first result")
        hitsSpinBox.setMinimum(1)
        hitsSpinBox.setMaximum(100)
        hitsSpinBox.setSingleStep(10)

        startQueryButton _ ?PB..("Start query")

        packagesLayout _ QGridLayout()
        packagesLayout.addWidget(nameLabel, 0, 0)
        packagesLayout.addWidget(nameEdit, 0, 1)
        packagesLayout.addWidget(dateLabel, 1, 0)
        packagesLayout.addWidget(dateEdit, 1, 1)
        packagesLayout.addWidget(releasesCheckBox, 2, 0)
        packagesLayout.addWidget(upgradesCheckBox, 3, 0)
        packagesLayout.addWidget(hitsSpinBox, 4, 0, 1, 2)
        packagesGroup.setLayout(packagesLayout)

        mainLayout _ QVBoxLayout()
        mainLayout.addWidget(packagesGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


c_ ConfigDialog(QDialog):
    ___ __init__  parent_None):
        super(ConfigDialog, self).__init__(parent)

        self.contentsWidget _ QListWidget()
        self.contentsWidget.setViewMode(QListView.IconMode)
        self.contentsWidget.setIconSize(QSize(96, 84))
        self.contentsWidget.setMovement(QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget _ QStackedWidget()
        self.pagesWidget.addWidget(ConfigurationPage())
        self.pagesWidget.addWidget(UpdatePage())
        self.pagesWidget.addWidget(QueryPage())

        closeButton _ ?PB..("Close")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.c__.c..(self.close)

        horizontalLayout _ QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout _ QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)

        mainLayout _ QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle("Config Dialog")

    ___ changePage  current, previous):
        __ no. current:
            current _ previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    ___ createIcons(self):
        configButton _ QListWidgetItem(self.contentsWidget)
        configButton.setIcon(QIcon(':/images/config.png'))
        configButton.sT..("Configuration")
        configButton.setTextAlignment(Qt.AlignHCenter)
        configButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        updateButton _ QListWidgetItem(self.contentsWidget)
        updateButton.setIcon(QIcon(':/images/update.png'))
        updateButton.sT..("Update")
        updateButton.setTextAlignment(Qt.AlignHCenter)
        updateButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        queryButton _ QListWidgetItem(self.contentsWidget)
        queryButton.setIcon(QIcon(':/images/query.png'))
        queryButton.sT..("Query")
        queryButton.setTextAlignment(Qt.AlignHCenter)
        queryButton.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.c..(self.changePage)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    dialog _ ConfigDialog()
    sys.exit(dialog.exec_())    
