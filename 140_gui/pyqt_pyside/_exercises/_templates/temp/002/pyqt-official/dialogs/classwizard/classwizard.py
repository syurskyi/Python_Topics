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


____ ?.?C.. ______ QDir, QFile, QRegExp
____ ?.?G.. ______ QPixmap
____ ?.?W.. ______ (?A.., QCheckBox, QGridLayout, QGroupBox,
        QLabel, QLineEdit, ?MB.., QRadioButton, QVBoxLayout, QWizard,
        QWizardPage)

______ classwizard_rc


c_ ClassWizard(QWizard):
    ___ __init__  parent_None):
        super(ClassWizard, self).__init__(parent)

        self.addPage(IntroPage())
        self.addPage(ClassInfoPage())
        self.addPage(CodeStylePage())
        self.addPage(OutputFilesPage())
        self.addPage(ConclusionPage())

        self.setPixmap(QWizard.BannerPixmap, QPixmap(':/images/banner.png'))
        self.setPixmap(QWizard.BackgroundPixmap,
                QPixmap(':/images/background.png'))

        self.setWindowTitle("Class Wizard")

    ___ accept(self):
        className _ self.field('className')
        baseClass _ self.field('baseClass')
        macroName _ self.field('macroName')
        baseInclude _ self.field('baseInclude')

        outputDir _ self.field('outputDir')
        header _ self.field('header')
        implementation _ self.field('implementation')

        block _ ''

        __ self.field('comment'):
            block +_ '/*\n'
            block +_ '    ' + header + '\n'
            block +_ '*/\n'
            block +_ '\n'

        __ self.field('protect'):
            block +_ '#ifndef ' + macroName + '\n'
            block +_ '#define ' + macroName + '\n'
            block +_ '\n'

        __ self.field('includeBase'):
            block +_ '#include ' + baseInclude + '\n'
            block +_ '\n'

        block +_ 'class ' + className
        __ baseClass:
            block +_ ' : public ' + baseClass

        block +_ '\n'
        block +_ '{\n'

        __ self.field('qobjectMacro'):
            block +_ '    Q_OBJECT\n'
            block +_ '\n'

        block +_ 'public:\n'

        __ self.field('qobjectCtor'):
            block +_ '    ' + className + '(QObject *parent = 0);\n'
        ____ self.field('qwidgetCtor'):
            block +_ '    ' + className + '(QWidget *parent = 0);\n'
        ____ self.field('defaultCtor'):
            block +_ '    ' + className + '();\n'

            __ self.field('copyCtor'):
                block +_ '    ' + className + '(const ' + className + ' &other);\n'
                block +_ '\n'
                block +_ '    ' + className + ' &operator=' + '(const ' + className + ' &other);\n'

        block +_ '};\n'

        __ self.field('protect'):
            block +_ '\n'
            block +_ '#endif\n'

        headerFile _ QFile(outputDir + '/' + header)

        __ no. headerFile.o..(QFile.WriteOnly | QFile.Text):
            ?MB...warning(N.., "Class Wizard",
                    "Cannot write file %s:\n%s" % (headerFile.fileName(), headerFile.errorString()))
            r_

        headerFile.w..(block)

        block _ ''

        __ self.field('comment'):
            block +_ '/*\n'
            block +_ '    ' + implementation + '\n'
            block +_ '*/\n'
            block +_ '\n'

        block +_ '#include "' + header + '"\n'
        block +_ '\n'

        __ self.field('qobjectCtor'):
            block +_ className + '::' + className + '(QObject *parent)\n'
            block +_ '    : ' + baseClass + '(parent)\n'
            block +_ '{\n'
            block +_ '}\n'
        ____ self.field('qwidgetCtor'):
            block +_ className + '::' + className + '(QWidget *parent)\n'
            block +_ '    : ' + baseClass + '(parent)\n'
            block +_ '{\n'
            block +_ '}\n'
        ____ self.field('defaultCtor'):
            block +_ className + '::' + className + '()\n'
            block +_ '{\n'
            block +_ '    // missing code\n'
            block +_ '}\n'

            __ self.field('copyCtor'):
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
            ?MB...warning(N.., "Class Wizard",
                    "Cannot write file %s:\n%s" % (implementationFile.fileName(), implementationFile.errorString()))
            r_

        implementationFile.w..(block)

        super(ClassWizard, self).accept()


c_ IntroPage(QWizardPage):
    ___ __init__  parent_None):
        super(IntroPage, self).__init__(parent)

        self.setTitle("Introduction")
        self.setPixmap(QWizard.WatermarkPixmap,
                QPixmap(':/images/watermark1.png'))

        label _ QLabel("This wizard will generate a skeleton C++ class "
                "definition, including a few functions. You simply need to "
                "specify the class name and set a few options to produce a "
                "header file and an implementation file for your new C++ "
                "class.")
        label.setWordWrap(True)

        layout _ ?VBL..
        layout.aW..(label)
        self.sL..(layout)


c_ ClassInfoPage(QWizardPage):
    ___ __init__  parent_None):
        super(ClassInfoPage, self).__init__(parent)

        self.setTitle("Class Information")
        self.setSubTitle("Specify basic information about the class for "
                "which you want to generate skeleton source code files.")
        self.setPixmap(QWizard.LogoPixmap, QPixmap(':/images/logo1.png'))

        classNameLabel _ QLabel("&Class name:")
        classNameLineEdit _ ?LE..
        classNameLabel.setBuddy(classNameLineEdit)

        baseClassLabel _ QLabel("B&ase class:")
        baseClassLineEdit _ ?LE..
        baseClassLabel.setBuddy(baseClassLineEdit)

        qobjectMacroCheckBox _ QCheckBox("Generate Q_OBJECT &macro")

        groupBox _ QGroupBox("C&onstructor")

        qobjectCtorRadioButton _ QRadioButton("&QObject-style constructor")
        qwidgetCtorRadioButton _ QRadioButton("Q&Widget-style constructor")
        defaultCtorRadioButton _ QRadioButton("&Default constructor")
        copyCtorCheckBox _ QCheckBox("&Generate copy constructor and operator=")

        defaultCtorRadioButton.setChecked(True)

        defaultCtorRadioButton.toggled.c..(copyCtorCheckBox.setEnabled)

        self.registerField('className*', classNameLineEdit)
        self.registerField('baseClass', baseClassLineEdit)
        self.registerField('qobjectMacro', qobjectMacroCheckBox)
        self.registerField('qobjectCtor', qobjectCtorRadioButton)
        self.registerField('qwidgetCtor', qwidgetCtorRadioButton)
        self.registerField('defaultCtor', defaultCtorRadioButton)
        self.registerField('copyCtor', copyCtorCheckBox)

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
        self.sL..(layout)


c_ CodeStylePage(QWizardPage):
    ___ __init__  parent_None):
        super(CodeStylePage, self).__init__(parent)

        self.setTitle("Code Style Options")
        self.setSubTitle("Choose the formatting of the generated code.")
        self.setPixmap(QWizard.LogoPixmap, QPixmap(':/images/logo2.png'))

        commentCheckBox _ QCheckBox("&Start generated files with a comment")
        commentCheckBox.setChecked(True)

        protectCheckBox _ QCheckBox("&Protect header file against multiple "
                "inclusions")
        protectCheckBox.setChecked(True)

        macroNameLabel _ QLabel("&Macro name:")
        self.macroNameLineEdit _ ?LE..
        macroNameLabel.setBuddy(self.macroNameLineEdit)

        self.includeBaseCheckBox _ QCheckBox("&Include base class definition")
        self.baseIncludeLabel _ QLabel("Base class include:")
        self.baseIncludeLineEdit _ ?LE..
        self.baseIncludeLabel.setBuddy(self.baseIncludeLineEdit)

        protectCheckBox.toggled.c..(macroNameLabel.setEnabled)
        protectCheckBox.toggled.c..(self.macroNameLineEdit.setEnabled)
        self.includeBaseCheckBox.toggled.c..(self.baseIncludeLabel.setEnabled)
        self.includeBaseCheckBox.toggled.c..(self.baseIncludeLineEdit.setEnabled)

        self.registerField('comment', commentCheckBox)
        self.registerField('protect', protectCheckBox)
        self.registerField('macroName', self.macroNameLineEdit)
        self.registerField('includeBase', self.includeBaseCheckBox)
        self.registerField('baseInclude', self.baseIncludeLineEdit)

        layout _ QGridLayout()
        layout.setColumnMinimumWidth(0, 20)
        layout.aW..(commentCheckBox, 0, 0, 1, 3)
        layout.aW..(protectCheckBox, 1, 0, 1, 3)
        layout.aW..(macroNameLabel, 2, 1)
        layout.aW..(self.macroNameLineEdit, 2, 2)
        layout.aW..(self.includeBaseCheckBox, 3, 0, 1, 3)
        layout.aW..(self.baseIncludeLabel, 4, 1)
        layout.aW..(self.baseIncludeLineEdit, 4, 2)
        self.sL..(layout)

    ___ initializePage(self):
        className _ self.field('className')
        self.macroNameLineEdit.sT..(className.upper() + "_H")

        baseClass _ self.field('baseClass')
        is_baseClass _ bool(baseClass)

        self.includeBaseCheckBox.setChecked(is_baseClass)
        self.includeBaseCheckBox.setEnabled(is_baseClass)
        self.baseIncludeLabel.setEnabled(is_baseClass)
        self.baseIncludeLineEdit.setEnabled(is_baseClass)

        __ no. is_baseClass:
            self.baseIncludeLineEdit.clear()
        ____ QRegExp('Q[A-Z].*').exactMatch(baseClass):
            self.baseIncludeLineEdit.sT..('<' + baseClass + '>')
        ____
            self.baseIncludeLineEdit.sT..('"' + baseClass.lower() + '.h"')


c_ OutputFilesPage(QWizardPage):
    ___ __init__  parent_None):
        super(OutputFilesPage, self).__init__(parent)

        self.setTitle("Output Files")
        self.setSubTitle("Specify where you want the wizard to put the "
                "generated skeleton code.")
        self.setPixmap(QWizard.LogoPixmap, QPixmap(':/images/logo3.png'))

        outputDirLabel _ QLabel("&Output directory:")
        self.outputDirLineEdit _ ?LE..
        outputDirLabel.setBuddy(self.outputDirLineEdit)

        headerLabel _ QLabel("&Header file name:")
        self.headerLineEdit _ ?LE..
        headerLabel.setBuddy(self.headerLineEdit)

        implementationLabel _ QLabel("&Implementation file name:")
        self.implementationLineEdit _ ?LE..
        implementationLabel.setBuddy(self.implementationLineEdit)

        self.registerField('outputDir*', self.outputDirLineEdit)
        self.registerField('header*', self.headerLineEdit)
        self.registerField('implementation*', self.implementationLineEdit)

        layout _ QGridLayout()
        layout.aW..(outputDirLabel, 0, 0)
        layout.aW..(self.outputDirLineEdit, 0, 1)
        layout.aW..(headerLabel, 1, 0)
        layout.aW..(self.headerLineEdit, 1, 1)
        layout.aW..(implementationLabel, 2, 0)
        layout.aW..(self.implementationLineEdit, 2, 1)
        self.sL..(layout)

    ___ initializePage(self):
        className _ self.field('className')
        self.headerLineEdit.sT..(className.lower() + '.h')
        self.implementationLineEdit.sT..(className.lower() + '.cpp')
        self.outputDirLineEdit.sT..(QDir.toNativeSeparators(QDir.tempPath()))


c_ ConclusionPage(QWizardPage):
    ___ __init__  parent_None):
        super(ConclusionPage, self).__init__(parent)

        self.setTitle("Conclusion")
        self.setPixmap(QWizard.WatermarkPixmap,
                QPixmap(':/images/watermark2.png'))

        self.label _ QLabel()
        self.label.setWordWrap(True)

        layout _ ?VBL..
        layout.aW..(self.label)
        self.sL..(layout)

    ___ initializePage(self):
        finishText _ self.wizard().buttonText(QWizard.FinishButton)
        finishText.replace('&', '')
        self.label.sT..("Click %s to generate the class skeleton." % finishText)


__ __name__ == '__main__':

    ______ sys

    app _ ?A..(sys.argv)
    wizard _ ClassWizard()
    wizard.s..
    sys.exit(app.exec_())
