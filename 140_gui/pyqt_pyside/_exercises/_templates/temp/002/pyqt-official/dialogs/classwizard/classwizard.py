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


____ ?.QtCore ______ QDir, QFile, QRegExp
____ ?.QtGui ______ QPixmap
____ ?.?W.. ______ (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QLabel, QLineEdit, QMessageBox, QRadioButton, QVBoxLayout, QWizard,
        QWizardPage)

______ classwizard_rc


class ClassWizard(QWizard):
    ___ __init__(self, parent_None):
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

        if self.field('comment'):
            block +_ '/*\n'
            block +_ '    ' + header + '\n'
            block +_ '*/\n'
            block +_ '\n'

        if self.field('protect'):
            block +_ '#ifndef ' + macroName + '\n'
            block +_ '#define ' + macroName + '\n'
            block +_ '\n'

        if self.field('includeBase'):
            block +_ '#include ' + baseInclude + '\n'
            block +_ '\n'

        block +_ 'class ' + className
        if baseClass:
            block +_ ' : public ' + baseClass

        block +_ '\n'
        block +_ '{\n'

        if self.field('qobjectMacro'):
            block +_ '    Q_OBJECT\n'
            block +_ '\n'

        block +_ 'public:\n'

        if self.field('qobjectCtor'):
            block +_ '    ' + className + '(QObject *parent = 0);\n'
        elif self.field('qwidgetCtor'):
            block +_ '    ' + className + '(QWidget *parent = 0);\n'
        elif self.field('defaultCtor'):
            block +_ '    ' + className + '();\n'

            if self.field('copyCtor'):
                block +_ '    ' + className + '(const ' + className + ' &other);\n'
                block +_ '\n'
                block +_ '    ' + className + ' &operator=' + '(const ' + className + ' &other);\n'

        block +_ '};\n'

        if self.field('protect'):
            block +_ '\n'
            block +_ '#endif\n'

        headerFile _ QFile(outputDir + '/' + header)

        if not headerFile.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(None, "Class Wizard",
                    "Cannot write file %s:\n%s" % (headerFile.fileName(), headerFile.errorString()))
            return

        headerFile.write(block)

        block _ ''

        if self.field('comment'):
            block +_ '/*\n'
            block +_ '    ' + implementation + '\n'
            block +_ '*/\n'
            block +_ '\n'

        block +_ '#include "' + header + '"\n'
        block +_ '\n'

        if self.field('qobjectCtor'):
            block +_ className + '::' + className + '(QObject *parent)\n'
            block +_ '    : ' + baseClass + '(parent)\n'
            block +_ '{\n'
            block +_ '}\n'
        elif self.field('qwidgetCtor'):
            block +_ className + '::' + className + '(QWidget *parent)\n'
            block +_ '    : ' + baseClass + '(parent)\n'
            block +_ '{\n'
            block +_ '}\n'
        elif self.field('defaultCtor'):
            block +_ className + '::' + className + '()\n'
            block +_ '{\n'
            block +_ '    // missing code\n'
            block +_ '}\n'

            if self.field('copyCtor'):
                block +_ '\n'
                block +_ className + '::' + className + '(const ' + className + ' &other)\n'
                block +_ '{\n'
                block +_ '    *this = other;\n'
                block +_ '}\n'
                block +_ '\n'
                block +_ className + ' &' + className + '::operator=(const ' + className + ' &other)\n'
                block +_ '{\n'

                if baseClass:
                    block +_ '    ' + baseClass + '::operator=(other);\n'

                block +_ '    // missing code\n'
                block +_ '    return *this;\n'
                block +_ '}\n'

        implementationFile _ QFile(outputDir + '/' + implementation)

        if not implementationFile.open(QFile.WriteOnly | QFile.Text):
            QMessageBox.warning(None, "Class Wizard",
                    "Cannot write file %s:\n%s" % (implementationFile.fileName(), implementationFile.errorString()))
            return

        implementationFile.write(block)

        super(ClassWizard, self).accept()


class IntroPage(QWizardPage):
    ___ __init__(self, parent_None):
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

        layout _ QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


class ClassInfoPage(QWizardPage):
    ___ __init__(self, parent_None):
        super(ClassInfoPage, self).__init__(parent)

        self.setTitle("Class Information")
        self.setSubTitle("Specify basic information about the class for "
                "which you want to generate skeleton source code files.")
        self.setPixmap(QWizard.LogoPixmap, QPixmap(':/images/logo1.png'))

        classNameLabel _ QLabel("&Class name:")
        classNameLineEdit _ QLineEdit()
        classNameLabel.setBuddy(classNameLineEdit)

        baseClassLabel _ QLabel("B&ase class:")
        baseClassLineEdit _ QLineEdit()
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

        groupBoxLayout _ QVBoxLayout()
        groupBoxLayout.addWidget(qobjectCtorRadioButton)
        groupBoxLayout.addWidget(qwidgetCtorRadioButton)
        groupBoxLayout.addWidget(defaultCtorRadioButton)
        groupBoxLayout.addWidget(copyCtorCheckBox)
        groupBox.setLayout(groupBoxLayout)

        layout _ QGridLayout()
        layout.addWidget(classNameLabel, 0, 0)
        layout.addWidget(classNameLineEdit, 0, 1)
        layout.addWidget(baseClassLabel, 1, 0)
        layout.addWidget(baseClassLineEdit, 1, 1)
        layout.addWidget(qobjectMacroCheckBox, 2, 0, 1, 2)
        layout.addWidget(groupBox, 3, 0, 1, 2)
        self.setLayout(layout)


class CodeStylePage(QWizardPage):
    ___ __init__(self, parent_None):
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
        self.macroNameLineEdit _ QLineEdit()
        macroNameLabel.setBuddy(self.macroNameLineEdit)

        self.includeBaseCheckBox _ QCheckBox("&Include base class definition")
        self.baseIncludeLabel _ QLabel("Base class include:")
        self.baseIncludeLineEdit _ QLineEdit()
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
        layout.addWidget(commentCheckBox, 0, 0, 1, 3)
        layout.addWidget(protectCheckBox, 1, 0, 1, 3)
        layout.addWidget(macroNameLabel, 2, 1)
        layout.addWidget(self.macroNameLineEdit, 2, 2)
        layout.addWidget(self.includeBaseCheckBox, 3, 0, 1, 3)
        layout.addWidget(self.baseIncludeLabel, 4, 1)
        layout.addWidget(self.baseIncludeLineEdit, 4, 2)
        self.setLayout(layout)

    ___ initializePage(self):
        className _ self.field('className')
        self.macroNameLineEdit.sT..(className.upper() + "_H")

        baseClass _ self.field('baseClass')
        is_baseClass _ bool(baseClass)

        self.includeBaseCheckBox.setChecked(is_baseClass)
        self.includeBaseCheckBox.setEnabled(is_baseClass)
        self.baseIncludeLabel.setEnabled(is_baseClass)
        self.baseIncludeLineEdit.setEnabled(is_baseClass)

        if not is_baseClass:
            self.baseIncludeLineEdit.clear()
        elif QRegExp('Q[A-Z].*').exactMatch(baseClass):
            self.baseIncludeLineEdit.sT..('<' + baseClass + '>')
        else:
            self.baseIncludeLineEdit.sT..('"' + baseClass.lower() + '.h"')


class OutputFilesPage(QWizardPage):
    ___ __init__(self, parent_None):
        super(OutputFilesPage, self).__init__(parent)

        self.setTitle("Output Files")
        self.setSubTitle("Specify where you want the wizard to put the "
                "generated skeleton code.")
        self.setPixmap(QWizard.LogoPixmap, QPixmap(':/images/logo3.png'))

        outputDirLabel _ QLabel("&Output directory:")
        self.outputDirLineEdit _ QLineEdit()
        outputDirLabel.setBuddy(self.outputDirLineEdit)

        headerLabel _ QLabel("&Header file name:")
        self.headerLineEdit _ QLineEdit()
        headerLabel.setBuddy(self.headerLineEdit)

        implementationLabel _ QLabel("&Implementation file name:")
        self.implementationLineEdit _ QLineEdit()
        implementationLabel.setBuddy(self.implementationLineEdit)

        self.registerField('outputDir*', self.outputDirLineEdit)
        self.registerField('header*', self.headerLineEdit)
        self.registerField('implementation*', self.implementationLineEdit)

        layout _ QGridLayout()
        layout.addWidget(outputDirLabel, 0, 0)
        layout.addWidget(self.outputDirLineEdit, 0, 1)
        layout.addWidget(headerLabel, 1, 0)
        layout.addWidget(self.headerLineEdit, 1, 1)
        layout.addWidget(implementationLabel, 2, 0)
        layout.addWidget(self.implementationLineEdit, 2, 1)
        self.setLayout(layout)

    ___ initializePage(self):
        className _ self.field('className')
        self.headerLineEdit.sT..(className.lower() + '.h')
        self.implementationLineEdit.sT..(className.lower() + '.cpp')
        self.outputDirLineEdit.sT..(QDir.toNativeSeparators(QDir.tempPath()))


class ConclusionPage(QWizardPage):
    ___ __init__(self, parent_None):
        super(ConclusionPage, self).__init__(parent)

        self.setTitle("Conclusion")
        self.setPixmap(QWizard.WatermarkPixmap,
                QPixmap(':/images/watermark2.png'))

        self.label _ QLabel()
        self.label.setWordWrap(True)

        layout _ QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    ___ initializePage(self):
        finishText _ self.wizard().buttonText(QWizard.FinishButton)
        finishText.replace('&', '')
        self.label.sT..("Click %s to generate the class skeleton." % finishText)


if __name__ == '__main__':

    ______ sys

    app _ QApplication(sys.argv)
    wizard _ ClassWizard()
    wizard.s..
    sys.exit(app.exec_())
