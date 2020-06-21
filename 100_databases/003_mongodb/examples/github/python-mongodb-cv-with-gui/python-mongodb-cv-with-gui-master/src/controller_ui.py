from PyQt5 import QtWidgets, QtGui, QtCore, Qt, uic
from pathlib import Path
from customwidget import MyCustomWidget

import os
import sys
import time
import copy
import secrets

import sys
# sys.path.append(".") # Adds higher directory to python modules path.
from Mongo import client

# cwd = os.getcwd()
# print('working directory:', cwd)

# import sys
# for p in sys.path:
#     print(p)
print('\n')
print("PyQt version:", Qt.PYQT_VERSION_STR)

guiFolder = Path(__file__).resolve().parent
print('\nguiFolder type=', type(guiFolder), '\n guiFolder=', guiFolder)
imageFolder = Path(guiFolder.__str__()+'/images_of_profiles/')
print('\nimageFolder type=', type(imageFolder), '\n imageFolder=', imageFolder)
uiFilePath = guiFolder.__str__() + \
    '/raw_gui_latest.ui'
print('uiFilePath= ', uiFilePath)

# myClient=client.Client()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        super(Ui, self).__init__()
        # print('\npath of parent folder:\n ',Path(__file__).resolve().parent)

        uic.loadUi(uiFilePath, self)
        # buttons
        self.ButtonAddUser: QtWidgets.QPushButton
        self.ButtonAddUser = self.findChild(
            QtWidgets.QPushButton, 'PushButton_AddUser')
        self.ButtonAddUser.clicked.connect(self.AddUser)

        self.ButtonAddImageCV: QtWidgets.QPushButton
        self.ButtonAddImageCV = self.findChild(
            QtWidgets.QPushButton, 'PushButton_AddImage')
        self.ButtonAddImageCV.clicked.connect(self.SelectImageCV)

        self.ButtonDeleteAllUsers: QtWidgets.QPushButton
        self.ButtonDeleteAllUsers = self.findChild(
            QtWidgets.QPushButton, 'PushButton_DeleteAllUsers')
        self.ButtonDeleteAllUsers.clicked.connect(self.DeleteAllUsers)

        # QTextEdits
        self.CVDescription: QtWidgets.QTextEdit
        self.CVDescription = self.findChild(
            QtWidgets.QTextEdit, 'CVUserDescription')

        self.CVUserName: QtWidgets.QTextEdit
        self.CVUserName = self.findChild(QtWidgets.QTextEdit, 'CVUserName')
        # QLabels
        self.CVImage: QtWidgets.QLabel
        self.CVImage = self.findChild(QtWidgets.QLabel, 'CVImage')
        # QListWidgets
        self.QListWidgetCVList: QtWidgets.QListWidget
        self.QListWidgetCVList = self.findChild(
            QtWidgets.QListWidget, 'QListWidgetCVList')

        self.show()

        self.InitializeClient()

    def InitializeClient(self):
        self.myClient = client.Client()
        self.LoadUsersFromDatabase()

    def LoadUsersFromDatabase(self):
        tmpList = self.myClient.GetAllUsers()
        print('counted numbers in list=', len(tmpList))
        for i in range(len(tmpList)):
            print('name=<', tmpList[i]['name'], '> description=<', tmpList[i]
                  ['description'], '>image_id=<', tmpList[i]['image_id'], '>')
            self.LoadUserToWidgetList(
                tmpList[i]['name'], tmpList[i]['description'], tmpList[i]['image_id'])

    def LoadUserToWidgetList(self, userName: str,
                             description: str,
                             imageID: str):
        # set parent? of item
        item = QtWidgets.QListWidgetItem(self.QListWidgetCVList)
        # search image based on imagID
        imageFile = imageFolder.__str__()+'/'+imageID+'.png'
        pixmap = QtGui.QPixmap(imageFile)

        print('imageFile=<', imageFile, '>')
        # create a new custom widget
        customWidget = MyCustomWidget(self,
                                      pixmap,
                                      userName,
                                      description,
                                      item,
                                      self.QListWidgetCVList)

        # set the item to the sizehint of the custom widget
        item.setSizeHint(customWidget.sizeHint())

        # add item to the list
        self.QListWidgetCVList.addItem(item)

        # change item to custom widget
        self.QListWidgetCVList.setItemWidget(item, customWidget)

    def AddUser(self):
        # check if all inputs are given
        if (not self.CVImage.pixmap()):
            print('no image set')
            return 0
        if (not self.CVUserName.toPlainText()):
            print('no name set')
            return 0
        if (not self.CVDescription.toPlainText()):
            print('no description set')
            return 0
        imageID = self.GetRandomID(5)
        self.myClient.InsertUser(self.CVUserName.toPlainText(),
                                 self.CVDescription.toPlainText(),
                                 imageID)
        # set parent? of item
        item = QtWidgets.QListWidgetItem(self.QListWidgetCVList)

        # create a new custom widget
        customWidget = MyCustomWidget(self,
                                      #   self.fileNameLastImageUsed,
                                      self.tmpPixmap,
                                      self.CVUserName.toPlainText(),
                                      self.CVDescription.toPlainText(),
                                      item,
                                      self.QListWidgetCVList)

        # set the item to the sizehint of the custom widget
        item.setSizeHint(customWidget.sizeHint())

        # add item to the list
        self.QListWidgetCVList.addItem(item)

        # change item to custom widget
        self.QListWidgetCVList.setItemWidget(item, customWidget)

        # save the image on the file
        imageName = str(imageFolder.__str__()+'/' +
                        str(imageID)+'.png')
        # print('image name=', imageName)
        tmp = self.tmpPixmap.save(imageName, "PNG")
        # clear user input
        self.CVDescription.clear()
        self.CVUserName.clear()
        self.CVImage.clear()

    def DeleteAllUsers(self):
        '''
        removes all users from the database and their respective images
        '''
        self.myClient.DeleteAllUsers()
        self.QListWidgetCVList.clear()
        self.ClearFolderFromImages()
        print('Deleted all users successfully')

    def ClearFolderFromImages(self):
        '''
        clears all images from image folder
        '''
        dir_name = imageFolder
        folders = os.listdir(dir_name)
        for item in folders:
            if item.endswith(".png"):
                os.remove(os.path.join(dir_name, item))

    def DeleteUser(self, name: str, description: str):
        print(__name__, ' passing user= <', name,
              '> description= <', description, '>')
        imageID = self.myClient.FinderImageID(name, description)
        self.myClient.DeleteUser(name, description)
        print('\nimageID=', imageID, '\n')
        imageFileName=imageFolder.__str__()+'/'+imageID+'.png'
        os.remove(imageFileName)

    def FlashButtonAsGreen(self, name, user_description):
        # color from 0,255,0 (pure green) to 255,255,255 (pure white)
        # flash the button
        pass

    def DeleteImage(self, imagePath):
        os.remove(imagePath)

    def SelectImageCV(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *jpeg  *.bpm)")

        self.fileNameLastImageUsed = fileName
        print(self.fileNameLastImageUsed)
        if fileName:
            # load image in pixmap
            pixmap = QtGui.QPixmap(fileName)

            pixmap = pixmap.scaled(self.CVImage.width(),
                                   self.CVImage.height(),
                                   QtCore.Qt.IgnoreAspectRatio)
            self.tmpPixmap = pixmap
            # print('pixmap is: ', self.tmpPixmap)
            self.CVImage.setPixmap(pixmap)

            self.CVImage.setAlignment(QtCore.Qt.AlignCenter)

    def GetRandomID(self, byteSize):
        '''
        generate a secret id and return it
        '''
        return secrets.token_hex(byteSize)


def RunGUI():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


if __name__ == "__main__":
    RunGUI()
    # client=client.Client() #requires multi threading, will check later
