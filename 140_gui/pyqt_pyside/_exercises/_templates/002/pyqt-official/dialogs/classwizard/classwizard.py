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


____ ?.?C.. ______ ?D.., QFile, QRegExp
____ ?.?G.. ______ ?P..
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, ?GB..,
        ?L.., QLineEdit, ?MB.., QRadioButton, ?VBL.., QWizard,
        QWizardPage)

______ classwizard_rc


c_ ClassWizard(QWizard):
    ___  -   parent_None):
        s__(ClassWizard, self). - (parent)

        addPage(IntroPage())
        addPage(ClassInfoPage())
        addPage(CodeStylePage())
        addPage(OutputFilesPage())
        addPage(ConclusionPage())

        sP..(QWizard.BannerPixmap, ?P..(':/images/banner.png'))
        sP..(QWizard.BackgroundPixmap,
                ?P..(':/images/background.png'))

        sWT..("Class Wizard")

    ___ accept
        className _ field('className')
        baseClass _ field('baseClass')
        macroName _ field('macroName')
        baseInclude _ field('baseInclude')

        outputDir _ field('outputDir')
        header _ field('header')
        implementation _ field('implementation')

        block _ ''

        __ field('comment'):
            block +_ '/*\n'
            block +_ '    ' + header + '\n'
            block +_ '*/\n'
            block +_ '\n'

        __ field('protect'):
            block +_ '#ifndef ' + macroName + '\n'
            block +_ '#define ' + macroName + '\n'
            block +_ '\n'

        __ field('includeBase'):
            block +_ '#include ' + baseInclude + '\n'
            block +_ '\n'

        block +_ 'class ' + className
        __ baseClass:
            block +_ ' : public ' + baseClass

        block +_ '\n'
        block +_ '{\n'

        __ field('qobjectMacro'):
            block +_ '    Q_OBJECT\n'
            block +_ '\n'

        block +_ 'public:\n'

        __ field('qobjectCtor'):
            block +_ '    ' + className + '(QObject *parent = 0);\n'
        ____ field('qwidgetCtor'):
            block +_ '    ' + className + '(QWidget *parent = 0);\n'
        ____ field('defaultCtor'):
            block +_ '    ' + className + '();\n'

            __ field('copyCtor'):
                block +_ '    ' + className + '(const ' + className + ' &other);\n'
                block +_ '\n'
                block +_ '    ' + className + ' &operator=' + '(const ' + className + ' &other);\n'

        block +_ '};\n'

        __ field('protect'):
            block +_ '\n'
            block +_ '#endif\n'

        headerFile _ QFile(outputDir + '/' + header)

        __ no. headerFile.o..(QFile.WriteOnly | QFile.Text):
            ?MB...w..(N.., "Class Wizard",
                    "Cannot write file %s:\n%s" % (headerFile.fN.., headerFile.errorString()))
            r_

        headerFile.w..(block)

        block _ ''

        __ field('comment'):
            block +_ '/*\n'
            block +_ '    ' + implementation + '\n'
            block +_ '*/\n'
            block +_ '\n'

        block +_ '#include "' + header + '"\n'
        block +_ '\n'

        __ field('qobjectCtor'):
            block +_ className + '::' + className + '(QObject *parent)\n'
            block +_ '    : ' + baseClass + '(parent)\n'
            block +_ '{\n'
            block +_ '}\n'
        ____ field('qwidgetCtor'):
            block +_ className + '::' + className + '(QWidget *parent)\n'
            block +_ '    : ' + baseClass + '(parent)\n'
            block +_ '{\n'
            block +_ '}\n'
        ____ field('defaultCtor'):
            block +_ className + '::' + className + '()\n'
            block +_ '{\n'
            block +_ '    // missing code\n'
            block +_ '}\n'

            __ field('copyCtor'):
                block +_ '\n'
                block +_ className + '::' + className + '(const ' + className + ' &other)\n'
                block +_ '{\n'
                block +_ '    *this = other;\n'
                block +_ '}\n'
                block +_ '\n'
                block +_ className + ' &' + className + '::operator=(const ' + className + ' &other)\n'
                block +_ '{\n'

                __ baseClass:
                    block +_ '    ' + baseClass + '::operator=(other);\n'

                block +_ '    // missing code\n'
                block +_ '    return *this;\n'
                block +_ '}\n'

        implementationFile _ QFile(outputDir + '/' + implementation)

        __ no. implementationFile.o..(QFile.WriteOnly | QFile.Text):
            ?MB...w..(N.., "Class Wizard",
                    "Cannot write file %s:\n%s" % (implementationFile.fN.., implementationFile.errorString()))
            r_

        implementationFile.w..(block)

        s__(ClassWizard, self).accept()


c_ IntroPage(QWizardPage):
    ___  -   parent_None):
        s__(IntroPage, self). - (parent)

        setTitle("Introduction")
        sP..(QWizard.WatermarkPixmap,
                ?P..(':/images/watermark1.png'))

        label _ ?L..("This wizard will generate a skeleton C++ class "
                "definition, including a few functions. You simply need to "
                "specify the class name and set a few options to produce a "
                "header file and an implementation file for your new C++ "
                "class.")
        label.setWordWrap( st.

        layout _ ?VBL..
        layout.aW..(label)
        sL..(layout)


c_ ClassInfoPage(QWizardPage):
    ___  -   parent_None):
        s__(ClassInfoPage, self). - (parent)

        setTitle("Class Information")
        setSubTitle("Specify basic information about the class for "
                "which you want to generate skeleton source code files.")
        sP..(QWizard.LogoPixmap, ?P..(':/images/logo1.png'))

        classNameLabel _ ?L..("&Class name:")
        classNameLineEdit _ ?LE..
        classNameLabel.setBuddy(classNameLineEdit)

        baseClassLabel _ ?L..("B&ase class:")
        baseClassLineEdit _ ?LE..
        baseClassLabel.setBuddy(baseClassLineEdit)

        qobjectMacroCheckBox _ QCheckBox("Generate Q_OBJECT &macro")

        groupBox _ ?GB..("C&onstructor")

        qobjectCtorRadioButton _ QRadioButton("&QObject-style constructor")
        qwidgetCtorRadioButton _ QRadioButton("Q&Widget-style constructor")
        defaultCtorRadioButton _ QRadioButton("&Default constructor")
        copyCtorCheckBox _ QCheckBox("&Generate copy constructor and operator=")

        defaultCtorRadioButton.sC__( st.

        defaultCtorRadioButton.t__.c..(copyCtorCheckBox.sE..)

        registerField('className*', classNameLineEdit)
        registerField('baseClass', baseClassLineEdit)
        registerField('qobjectMacro', qobjectMacroCheckBox)
        registerField('qobjectCtor', qobjectCtorRadioButton)
        registerField('qwidgetCtor', qwidgetCtorRadioButton)
        registerField('defaultCtor', defaultCtorRadioButton)
        registerField('copyCtor', copyCtorCheckBox)

        groupBoxLayout _ ?VBL..
        groupBoxLayout.aW..(qobjectCtorRadioButton)
        groupBoxLayout.aW..(qwidgetCtorRadioButton)
        groupBoxLayout.aW..(defaultCtorRadioButton)
        groupBoxLayout.aW..(copyCtorCheckBox)
        groupBox.sL..(groupBoxLayout)

        layout _ QGridLayout()
        layout.aW..(classNameLabel, 0, 0)
        layout.aW..(classNameLineEdit, 0, 1)
        layout.aW..(baseClassLabel, 1, 0)
        layout.aW..(baseClassLineEdit, 1, 1)
        layout.aW..(qobjectMacroCheckBox, 2, 0, 1, 2)
        layout.aW..(groupBox, 3, 0, 1, 2)
        sL..(layout)


c_ CodeStylePage(QWizardPage):
    ___  -   parent_None):
        s__(CodeStylePage, self). - (parent)

        setTitle("Code Style Options")
        setSubTitle("Choose the formatting of the generated code.")
        sP..(QWizard.LogoPixmap, ?P..(':/images/logo2.png'))

        commentCheckBox _ QCheckBox("&Start generated files with a comment")
        commentCheckBox.sC__( st.

        protectCheckBox _ QCheckBox("&Protect header file against multiple "
                "inclusions")
        protectCheckBox.sC__( st.

        macroNameLabel _ ?L..("&Macro name:")
        macroNameLineEdit _ ?LE..
        macroNameLabel.setBuddy(macroNameLineEdit)

        includeBaseCheckBox _ QCheckBox("&Include base class definition")
        baseIncludeLabel _ ?L..("Base class include:")
        baseIncludeLineEdit _ ?LE..
        baseIncludeLabel.setBuddy(baseIncludeLineEdit)

        protectCheckBox.t__.c..(macroNameLabel.sE..)
        protectCheckBox.t__.c..(macroNameLineEdit.sE..)
        includeBaseCheckBox.t__.c..(baseIncludeLabel.sE..)
        includeBaseCheckBox.t__.c..(baseIncludeLineEdit.sE..)

        registerField('comment', commentCheckBox)
        registerField('protect', protectCheckBox)
        registerField('macroName', macroNameLineEdit)
        registerField('includeBase', includeBaseCheckBox)
        registerField('baseInclude', baseIncludeLineEdit)

        layout _ QGridLayout()
        layout.setColumnMinimumWidth(0, 20)
        layout.aW..(commentCheckBox, 0, 0, 1, 3)
        layout.aW..(protectCheckBox, 1, 0, 1, 3)
        layout.aW..(macroNameLabel, 2, 1)
        layout.aW..(macroNameLineEdit, 2, 2)
        layout.aW..(includeBaseCheckBox, 3, 0, 1, 3)
        layout.aW..(baseIncludeLabel, 4, 1)
        layout.aW..(baseIncludeLineEdit, 4, 2)
        sL..(layout)

    ___ initializePage
        className _ field('className')
        macroNameLineEdit.sT..(className.upper() + "_H")

        baseClass _ field('baseClass')
        is_baseClass _ bool(baseClass)

        includeBaseCheckBox.sC__(is_baseClass)
        includeBaseCheckBox.sE..(is_baseClass)
        baseIncludeLabel.sE..(is_baseClass)
        baseIncludeLineEdit.sE..(is_baseClass)

        __ no. is_baseClass:
            baseIncludeLineEdit.c..
        ____ QRegExp('Q[A-Z].*').exactMatch(baseClass):
            baseIncludeLineEdit.sT..('<' + baseClass + '>')
        ____
            baseIncludeLineEdit.sT..('"' + baseClass.lower() + '.h"')


c_ OutputFilesPage(QWizardPage):
    ___  -   parent_None):
        s__(OutputFilesPage, self). - (parent)

        setTitle("Output Files")
        setSubTitle("Specify where you want the wizard to put the "
                "generated skeleton code.")
        sP..(QWizard.LogoPixmap, ?P..(':/images/logo3.png'))

        outputDirLabel _ ?L..("&Output directory:")
        outputDirLineEdit _ ?LE..
        outputDirLabel.setBuddy(outputDirLineEdit)

        headerLabel _ ?L..("&Header file name:")
        headerLineEdit _ ?LE..
        headerLabel.setBuddy(headerLineEdit)

        implementationLabel _ ?L..("&Implementation file name:")
        implementationLineEdit _ ?LE..
        implementationLabel.setBuddy(implementationLineEdit)

        registerField('outputDir*', outputDirLineEdit)
        registerField('header*', headerLineEdit)
        registerField('implementation*', implementationLineEdit)

        layout _ QGridLayout()
        layout.aW..(outputDirLabel, 0, 0)
        layout.aW..(outputDirLineEdit, 0, 1)
        layout.aW..(headerLabel, 1, 0)
        layout.aW..(headerLineEdit, 1, 1)
        layout.aW..(implementationLabel, 2, 0)
        layout.aW..(implementationLineEdit, 2, 1)
        sL..(layout)

    ___ initializePage
        className _ field('className')
        headerLineEdit.sT..(className.lower() + '.h')
        implementationLineEdit.sT..(className.lower() + '.cpp')
        outputDirLineEdit.sT..(?D...toNativeSeparators(?D...tempPath()))


c_ ConclusionPage(QWizardPage):
    ___  -   parent_None):
        s__(ConclusionPage, self). - (parent)

        setTitle("Conclusion")
        sP..(QWizard.WatermarkPixmap,
                ?P..(':/images/watermark2.png'))

        label _ ?L..
        label.setWordWrap( st.

        layout _ ?VBL..
        layout.aW..(label)
        sL..(layout)

    ___ initializePage
        finishText _ wizard().buttonText(QWizard.FinishButton)
        finishText.replace('&', '')
        label.sT..("Click %s to generate the class skeleton." % finishText)


__ ______ __ ______

    ______ ___

    app _ ?A..(___.a..
    wizard _ ClassWizard()
    wizard.s..
    ___.e.. ?.e..
