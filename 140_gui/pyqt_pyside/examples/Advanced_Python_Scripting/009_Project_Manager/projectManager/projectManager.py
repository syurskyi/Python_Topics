from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from widgets import projectManager_UIs as ui
from widgets import projectListWidget
import createProjectDialog, settingsDialog, templateEditor, settings, createProject
import webbrowser

class projectManagerClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(projectManagerClass, self).__init__()
        self.setupUi(self)

        # widgets

        self.projectList_lwd = projectListWidget.projectListClass()
        self.projectList_ly.addWidget(self.projectList_lwd)

        # connects

        self.create_btn.clicked.connect(self.createProject)
        self.settings_btn.clicked.connect(self.openSettingsDialog)
        self.templateEditor_btn.clicked.connect(self.openTemplateEditorDialog)
        self.projectList_lwd.itemClicked.connect(self.showInfo)
        self.projectList_lwd.itemDoubleClicked.connect(self.openProject)

        # start

        self.info_lb.setText('')
        self.updateList()

    def updateList(self):

        if not self.projectList_lwd.updateProjectList():
            self.create_btn.setEnabled(0)
        else:
            self.create_btn.setEnabled(1)

    def openSettingsDialog(self):
        self.dial = settingsDialog.settingsDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getTableData()
            settings.settingsClass().save(data)
        self.updateList()

    def openTemplateEditorDialog(self):
        self.dial = templateEditor.templateEditorClass()
        self.dial.show()

    def createProject(self):
        self.dial = createProjectDialog.createProjectDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getDialogData()
            createProject.createProject(data)
            self.updateList()

    def showInfo(self, item):
        info = createProject.getProjectInfo(item.data(32))
        if info:
            text = '''Name:
%s

Comment:
%s
''' % (info['name'], info['comment'])
        else:
            text = ''
        self.info_lb.setText(text)

    def openProject(self, item):
        path = item.data(32)
        webbrowser.open(path)

if __name__ == '__main__':
    app = QApplication([])
    w = projectManagerClass()
    w.show()
    app.exec_()