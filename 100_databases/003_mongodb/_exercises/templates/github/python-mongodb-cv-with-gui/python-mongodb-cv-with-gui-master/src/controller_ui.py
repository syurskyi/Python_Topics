____ ? _______ ?W.., ?G.., ?C.., Qt, uic
____ pathlib _______ Path
____ customwidget _______ MyCustomWidget

_______ os
_______ ___
_______ time
_______ copy
_______ secrets

_______ ___
# sys.path.append(".") # Adds higher directory to python modules path.
____ Mongo _______ client

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


c_ Ui(?W...?MW..):
    ___  -

        s__(Ui, self). - ()
        # print('\npath of parent folder:\n ',Path(__file__).resolve().parent)

        uic.loadUi(uiFilePath, self)
        # buttons
        ButtonAddUser: ?W...?PB..
        ButtonAddUser = findChild(
            ?W...?PB.., 'PushButton_AddUser')
        ButtonAddUser.c__.c..(AddUser)

        ButtonAddImageCV: ?W...?PB..
        ButtonAddImageCV = findChild(
            ?W...?PB.., 'PushButton_AddImage')
        ButtonAddImageCV.c__.c..(SelectImageCV)

        ButtonDeleteAllUsers: ?W...?PB..
        ButtonDeleteAllUsers = findChild(
            ?W...?PB.., 'PushButton_DeleteAllUsers')
        ButtonDeleteAllUsers.c__.c..(DeleteAllUsers)

        # QTextEdits
        CVDescription: ?W...QTextEdit
        CVDescription = findChild(
            ?W...QTextEdit, 'CVUserDescription')

        CVUserName: ?W...QTextEdit
        CVUserName = findChild(?W...QTextEdit, 'CVUserName')
        # QLabels
        CVImage: ?W...?L..
        CVImage = findChild(?W...?L.., 'CVImage')
        # QListWidgets
        QListWidgetCVList: ?W...QListWidget
        QListWidgetCVList = findChild(
            ?W...QListWidget, 'QListWidgetCVList')

        s..

        InitializeClient()

    ___ InitializeClient
        myClient = client.Client()
        LoadUsersFromDatabase()

    ___ LoadUsersFromDatabase
        tmpList = myClient.GetAllUsers()
        print('counted numbers in list=', le.(tmpList))
        ___ i __ ra..(le.(tmpList)):
            print('name=<', tmpList[i]['name'], '> description=<', tmpList[i]
                  ['description'], '>image_id=<', tmpList[i]['image_id'], '>')
            LoadUserToWidgetList(
                tmpList[i]['name'], tmpList[i]['description'], tmpList[i]['image_id'])

    ___ LoadUserToWidgetList(self, userName: st.,
                             description: st.,
                             imageID: st.):
        # set parent? of item
        item = ?W...?LWI..(QListWidgetCVList)
        # search image based on imagID
        imageFile = imageFolder.__str__()+'/'+imageID+'.png'
        pixmap = ?G...QPixmap(imageFile)

        print('imageFile=<', imageFile, '>')
        # create a new custom widget
        customWidget = MyCustomWidget(self,
                                      pixmap,
                                      userName,
                                      description,
                                      item,
                                      QListWidgetCVList)

        # set the item to the sizehint of the custom widget
        item.setSizeHint(customWidget.sizeHint())

        # add item to the list
        QListWidgetCVList.aI..(item)

        # change item to custom widget
        QListWidgetCVList.setItemWidget(item, customWidget)

    ___ AddUser
        # check if all inputs are given
        __ (not CVImage.pixmap()):
            print('no image set')
            return 0
        __ (not CVUserName.toPlainText()):
            print('no name set')
            return 0
        __ (not CVDescription.toPlainText()):
            print('no description set')
            return 0
        imageID = GetRandomID(5)
        myClient.InsertUser(CVUserName.toPlainText(),
                                 CVDescription.toPlainText(),
                                 imageID)
        # set parent? of item
        item = ?W...?LWI..(QListWidgetCVList)

        # create a new custom widget
        customWidget = MyCustomWidget(self,
                                      #   self.fileNameLastImageUsed,
                                      tmpPixmap,
                                      CVUserName.toPlainText(),
                                      CVDescription.toPlainText(),
                                      item,
                                      QListWidgetCVList)

        # set the item to the sizehint of the custom widget
        item.setSizeHint(customWidget.sizeHint())

        # add item to the list
        QListWidgetCVList.aI..(item)

        # change item to custom widget
        QListWidgetCVList.setItemWidget(item, customWidget)

        # save the image on the file
        imageName = st.(imageFolder.__str__()+'/' +
                        st.(imageID)+'.png')
        # print('image name=', imageName)
        tmp = tmpPixmap.save(imageName, "PNG")
        # clear user input
        CVDescription.c..
        CVUserName.c..
        CVImage.c..

    ___ DeleteAllUsers
        '''
        removes all users from the database and their respective images
        '''
        myClient.DeleteAllUsers()
        QListWidgetCVList.c..
        ClearFolderFromImages()
        print('Deleted all users successfully')

    ___ ClearFolderFromImages
        '''
        clears all images from image folder
        '''
        dir_name = imageFolder
        folders = os.listdir(dir_name)
        ___ item __ folders:
            __ item.endswith(".png"):
                os.r..(os.path.join(dir_name, item))

    ___ DeleteUser(self, name: st., description: st.):
        print(__name__, ' passing user= <', name,
              '> description= <', description, '>')
        imageID = myClient.FinderImageID(name, description)
        myClient.DeleteUser(name, description)
        print('\nimageID=', imageID, '\n')
        imageFileName=imageFolder.__str__()+'/'+imageID+'.png'
        os.r..(imageFileName)

    ___ FlashButtonAsGreen(self, name, user_description):
        # color from 0,255,0 (pure green) to 255,255,255 (pure white)
        # flash the button
        pass

    ___ DeleteImage(self, imagePath):
        os.r..(imagePath)

    ___ SelectImageCV
        fileName, _ = ?W...QFileDialog.getOpenFileName(
            N.., "Select Image", "", "Image Files (*.png *.jpg *jpeg  *.bpm)")

        fileNameLastImageUsed = fileName
        print(fileNameLastImageUsed)
        __ fileName:
            # load image in pixmap
            pixmap = ?G...QPixmap(fileName)

            pixmap = pixmap.scaled(CVImage.width(),
                                   CVImage.height(),
                                   ?C...Qt.IgnoreAspectRatio)
            tmpPixmap = pixmap
            # print('pixmap is: ', self.tmpPixmap)
            CVImage.setPixmap(pixmap)

            CVImage.setAlignment(?C...Qt.AlignCenter)

    ___ GetRandomID(self, byteSize):
        '''
        generate a secret id and return it
        '''
        return secrets.token_hex(byteSize)


___ RunGUI():
    app = ?W...?A..(___.argv)
    window = Ui()
    app.e..


__ __name__ __ "__main__":
    RunGUI()
    # client=client.Client() #requires multi threading, will check later
