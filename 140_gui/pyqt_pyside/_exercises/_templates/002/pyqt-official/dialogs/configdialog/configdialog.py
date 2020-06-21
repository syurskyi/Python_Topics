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


____ ?.?C.. ______ ?D.., ?S.., __
____ ?.?G.. ______ ?I..
____ ?.?W.. ______ (?A.., QCheckBox, ?CB, ?DTE..,
        ?D.., QGridLayout, ?GB.., ?HBL.., ?L.., QLineEdit,
        ?LV.., QListWidget, QListWidgetItem, ?PB.., SB..,
        ?SW.., ?VBL.., ?W..)

______ configdialog_rc


c_ ConfigurationPage(?W..):
    ___  -   parent_None):
        s__(ConfigurationPage, self). - (parent)

        configGroup _ ?GB..("Server configuration")

        serverLabel _ ?L..("Server:")
        serverCombo _ ?CB()
        serverCombo.aI..("Trolltech (Australia)")
        serverCombo.aI..("Trolltech (Germany)")
        serverCombo.aI..("Trolltech (Norway)")
        serverCombo.aI..("Trolltech (People's Republic of China)")
        serverCombo.aI..("Trolltech (USA)")

        serverLayout _ ?HBL..
        serverLayout.aW..(serverLabel)
        serverLayout.aW..(serverCombo)

        configLayout _ ?VBL..
        configLayout.aL..(serverLayout)
        configGroup.sL..(configLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(configGroup)
        mainLayout.addStretch(1)

        sL..(mainLayout)


c_ UpdatePage(?W..):
    ___  -   parent_None):
        s__(UpdatePage, self). - (parent)

        updateGroup _ ?GB..("Package selection")
        systemCheckBox _ QCheckBox("Update system")
        appsCheckBox _ QCheckBox("Update applications")
        docsCheckBox _ QCheckBox("Update documentation")

        packageGroup _ ?GB..("Existing packages")

        packageList _ QListWidget()
        qtItem _ QListWidgetItem(packageList)
        qtItem.sT..("Qt")
        qsaItem _ QListWidgetItem(packageList)
        qsaItem.sT..("QSA")
        teamBuilderItem _ QListWidgetItem(packageList)
        teamBuilderItem.sT..("Teambuilder")

        startUpdateButton _ ?PB..("Start update")

        updateLayout _ ?VBL..
        updateLayout.aW..(systemCheckBox)
        updateLayout.aW..(appsCheckBox)
        updateLayout.aW..(docsCheckBox)
        updateGroup.sL..(updateLayout)

        packageLayout _ ?VBL..
        packageLayout.aW..(packageList)
        packageGroup.sL..(packageLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(updateGroup)
        mainLayout.aW..(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.aW..(startUpdateButton)
        mainLayout.addStretch(1)

        sL..(mainLayout)


c_ QueryPage(?W..):
    ___  -   parent_None):
        s__(QueryPage, self). - (parent)

        packagesGroup _ ?GB..("Look for packages")

        nameLabel _ ?L..("Name:")
        nameEdit _ ?LE..

        dateLabel _ ?L..("Released after:")
        dateEdit _ ?DTE..(?D...currentDate())

        releasesCheckBox _ QCheckBox("Releases")
        upgradesCheckBox _ QCheckBox("Upgrades")

        hitsSpinBox _ SB..()
        hitsSpinBox.setPrefix("Return up to ")
        hitsSpinBox.setSuffix(" results")
        hitsSpinBox.setSpecialValueText("Return only the first result")
        hitsSpinBox.setMinimum(1)
        hitsSpinBox.sM..(100)
        hitsSpinBox.setSingleStep(10)

        startQueryButton _ ?PB..("Start query")

        packagesLayout _ QGridLayout()
        packagesLayout.aW..(nameLabel, 0, 0)
        packagesLayout.aW..(nameEdit, 0, 1)
        packagesLayout.aW..(dateLabel, 1, 0)
        packagesLayout.aW..(dateEdit, 1, 1)
        packagesLayout.aW..(releasesCheckBox, 2, 0)
        packagesLayout.aW..(upgradesCheckBox, 3, 0)
        packagesLayout.aW..(hitsSpinBox, 4, 0, 1, 2)
        packagesGroup.sL..(packagesLayout)

        mainLayout _ ?VBL..
        mainLayout.aW..(packagesGroup)
        mainLayout.addSpacing(12)
        mainLayout.aW..(startQueryButton)
        mainLayout.addStretch(1)

        sL..(mainLayout)


c_ ConfigDialog(?D..):
    ___  -   parent_None):
        s__(ConfigDialog, self). - (parent)

        contentsWidget _ QListWidget()
        contentsWidget.setViewMode(?LV...IconMode)
        contentsWidget.setIconSize(?S..(96, 84))
        contentsWidget.setMovement(?LV...Static)
        contentsWidget.setMaximumWidth(128)
        contentsWidget.setSpacing(12)

        pagesWidget _ ?SW..()
        pagesWidget.aW..(ConfigurationPage())
        pagesWidget.aW..(UpdatePage())
        pagesWidget.aW..(QueryPage())

        closeButton _ ?PB..("Close")

        createIcons()
        contentsWidget.setCurrentRow(0)

        closeButton.c__.c..(close)

        horizontalLayout _ ?HBL..
        horizontalLayout.aW..(contentsWidget)
        horizontalLayout.aW..(pagesWidget, 1)

        buttonsLayout _ ?HBL..
        buttonsLayout.addStretch(1)
        buttonsLayout.aW..(closeButton)

        mainLayout _ ?VBL..
        mainLayout.aL..(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.aL..(buttonsLayout)

        sL..(mainLayout)

        sWT..("Config Dialog")

    ___ changePage  current, previous):
        __ no. current:
            current _ previous

        pagesWidget.sCI..(contentsWidget.row(current))

    ___ createIcons 
        configButton _ QListWidgetItem(contentsWidget)
        configButton.sI..(?I..(':/images/config.png'))
        configButton.sT..("Configuration")
        configButton.setTextAlignment(__.AlignHCenter)
        configButton.setFlags(__.ItemIsSelectable | __.ItemIsEnabled)

        updateButton _ QListWidgetItem(contentsWidget)
        updateButton.sI..(?I..(':/images/update.png'))
        updateButton.sT..("Update")
        updateButton.setTextAlignment(__.AlignHCenter)
        updateButton.setFlags(__.ItemIsSelectable | __.ItemIsEnabled)

        queryButton _ QListWidgetItem(contentsWidget)
        queryButton.sI..(?I..(':/images/query.png'))
        queryButton.sT..("Query")
        queryButton.setTextAlignment(__.AlignHCenter)
        queryButton.setFlags(__.ItemIsSelectable | __.ItemIsEnabled)

        contentsWidget.currentItemChanged.c..(changePage)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    dialog _ ConfigDialog()
    ___.e..(dialog.e..
