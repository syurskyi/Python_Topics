____ ? _______ ?W.., ?G.., ?C.., Qt, uic
____ pathlib _______ Path
____ user_window _______ MiniUserWindow
# from controller_ui import Ui

_______ os
_______ ___
_______ time
_______ copy


c_ MyCustomWidget(?W...QWidget):
    ___  - (self,
                 Ui,
                #  fileNameLastImageUsed: str,
                 userPixmap: ?G...QPixmap,
                 userName: st.,
                 userDescription: st.,
                 itemReference: ?W...?LWI..,
                 parentList: ?W...QListWidget,
                 p.._N..
        s__(MyCustomWidget, self). - ?

        mainUi=Ui

        userName=userName
        userDescription=userDescription

        itemReference = itemReference

        row = ?W...QHBoxLayout()

        label_user_image = ?W...?L..()

        pixmap = userPixmap.scaled(100, 100, ?C...Qt.IgnoreAspectRatio)
        label_user_image.setPixmap(pixmap)
        QPushButtonDeleteUser = ?W...?PB..('delete')
        QPushButtonDeleteUser.c__.c..(DeleteUser)

        parentList = parentList
        QPushButtonViewUser = ?W...?PB..('view profile')
        QPushButtonViewUser.c__.c..(
            lambda: ViewUser(userName, userPixmap, userDescription))
        # construct custom widget
        row.aW..(label_user_image)
        row.aW..(?W...?L..(userName))
        row.aW..(QPushButtonViewUser)
        row.aW..(QPushButtonDeleteUser)

        sL..(row)
        # create a list of windows
        dialogs = li..()

    ___ ViewUser(self,
                 userName: st.,
                 userPixmap: ?G...QPixmap,
                 userDescription: st.,):
        # print('user is:', userName, ' pixmap is:', userPixmap,
        #       ' descritpion is: ', userDescription)
        test = MiniUserWindow(userName,
                              userDescription,
                              userPixmap)
        dialogs.append(test)

    ___ DeleteUser
        #get item reference
        itemRow = parentList.row(itemReference)
        parentList.takeItem(itemRow)
        # print('new CVlist count:', self.parentList.count())
        print(__name__,' passing user= <',userName,'> description= <',userDescription,'>')
        mainUi.DeleteUser(userName,userDescription)
