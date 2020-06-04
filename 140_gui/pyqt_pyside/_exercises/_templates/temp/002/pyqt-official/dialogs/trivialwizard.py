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


____ ?.?W.. ______ (?A.., QGridLayout, ?L.., QLineEdit,
        ?VBL.., QWizard, QWizardPage)


___ createIntroPage
    page _ QWizardPage()
    page.setTitle("Introduction")

    label _ ?L..(
            "This wizard will help you register your copy of Super Product "
            "Two.")
    label.setWordWrap( st.

    layout _ ?VBL..
    layout.aW..(label)
    page.sL..(layout)

    r_ page


___ createRegistrationPage
    page _ QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    nameLabel _ ?L..("Name:")
    nameLineEdit _ ?LE..

    emailLabel _ ?L..("Email address:")
    emailLineEdit _ ?LE..

    layout _ QGridLayout()
    layout.aW..(nameLabel, 0, 0)
    layout.aW..(nameLineEdit, 0, 1)
    layout.aW..(emailLabel, 1, 0)
    layout.aW..(emailLineEdit, 1, 1)
    page.sL..(layout)

    r_ page


___ createConclusionPage
    page _ QWizardPage()
    page.setTitle("Conclusion")

    label _ ?L..("You are now successfully registered. Have a nice day!")
    label.setWordWrap( st.

    layout _ ?VBL..
    layout.aW..(label)
    page.sL..(layout)

    r_ page


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..

    wizard _ QWizard()
    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage())
    wizard.addPage(createConclusionPage())

    wizard.sWT..("Trivial Wizard")
    wizard.s..

    ___.e.. ?.e..
