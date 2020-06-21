____ ? _______ ?W.., ?G.., ?C.., Qt, uic
_______ ___
_______ secrets
____ pathlib _______ Path


guiFolder = Path(__file__).resolve().parent
uiFilePath = guiFolder.__str__() + \
    '/user_window.ui'
# print('uiFilePath= ', uiFilePath)


c_ MiniUserWindow(?W...?MW..):
    ___  - (self,
                 userName: st.,
                 userDescription: st.,
                 userPixmap: ?G...QPixmap,
                 p.._N..
        s__(MiniUserWindow, self). - ?

        uic.loadUi(uiFilePath, self)

        CVDescription: ?W...QTextEdit
        CVDescription = findChild(
            ?W...QTextEdit, 'CVUserDescription')

        CVUserName: ?W...QTextEdit
        CVUserName = findChild(?W...QTextEdit, 'CVUserName')

        CVImage: ?W...?L..
        CVImage = findChild(?W...?L.., 'CVImage')

        QListWidgetCVList: ?W...QListWidget
        QListWidgetCVList = findChild(
            ?W...QListWidget, 'QListWidgetCVList')

        #set user text
        CVUserName.sT..(userName)
        CVDescription.sT..(userDescription)

        #set and configure user image
        pixmap = userPixmap.scaled(100, 100, ?C...Qt.IgnoreAspectRatio)
        CVImage.setPixmap(pixmap)

        s..

__ __name__ __ "__main__":
    # app =
    tmp_app = ?W...?A..(___.argv)
    window = MiniUserWindow()
    tmp_app.e..
    