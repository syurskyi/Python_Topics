_______ ___
#from PyQt4 import QtGui
____ ? _______ ?G.., ?W..


c_ QCustomQWidget (?W...QWidget):                       # QtWidgets
    ___  -  (self, parent = N..):
        s__(QCustomQWidget, self). - ?
        textQVBoxLayout = ?W...QVBoxLayout()          # QtWidgets
        textUpQLabel    = ?W...?L..()               # QtWidgets
        textDownQLabel  = ?W...?L..()               # QtWidgets
        textQVBoxLayout.aW..(textUpQLabel)
        textQVBoxLayout.aW..(textDownQLabel)
        allQHBoxLayout  = ?W...QHBoxLayout()          # QtWidgets
        iconQLabel      = ?W...?L..()               # QtWidgets
        allQHBoxLayout.aW..(iconQLabel, 0)
        allQHBoxLayout.addLayout(textQVBoxLayout, 1)
        sL..(allQHBoxLayout)
        # setStyleSheet
        textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    ___ setTextUp (self, text):
        textUpQLabel.sT..(text)

    ___ setTextDown (self, text):
        textDownQLabel.sT..(text)

    ___ sI.. (self, imagePath):
        iconQLabel.setPixmap(?G...QPixmap(imagePath).scaled(60, 60))   # + .scaled(60, 60

c_ exampleQMainWindow (?W...?MW..):                            # QtWidgets
    ___  -
        s__(exampleQMainWindow, self). - ()
        # Create QListWidget
        li.. = ?W...QListWidget(self)
        ___ index, name, icon __ [
            ('No.1', 'Meyoko',  'lena-2.png'),
            ('No.2', 'Nyaruko', 'im.png'),
            ('No.3', 'Louise',  'Ok.png')]:
            # Create QCustomQWidget
            customWidget = QCustomQWidget()
            customWidget.setTextUp(index)
            customWidget.setTextDown(name)
            customWidget.sI..(icon)
            # Create QListWidgetItem
            item = ?W...?LWI..()
            # Set size hint
            item.setSizeHint(customWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            li...aI..(item)
            li...setItemWidget(item, customWidget)
        sCW..(li..)


__ __name__ __ '__main__':
    app = ?W...?A..([])                                           # QtWidgets
    window = exampleQMainWindow()
    window.s..
    ___.e..(app.e..