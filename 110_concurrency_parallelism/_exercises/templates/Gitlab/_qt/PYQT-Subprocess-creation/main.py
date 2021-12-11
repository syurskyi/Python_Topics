______ sys
____ PyQt5 ______ QtCore, QtWidgets
____ PyQt5.QtWidgets ______ QMainWindow, QLabel, QGridLayout, QWidget
____ PyQt5.QtWidgets ______ QPushButton
____ PyQt5.QtCore ______ QSize
______ psutil
______ subprocess
______ os
______ t__
____ _ ______ ?

c_ MainWindow(QMainWindow):
    ___ - 
        QMainWindow.-
        close=F..
        setWindowTitle('Boom')
        setMinimumSize(QSize(300, 200))

        refreshButton = QPushButton('Refresh files', self)
        refreshButton.clicked.connect(refresh)
        refreshButton.show()
        refreshButton.move(100,150)

        buttons={}
        fileButtons=[]

    ___ clickMethodfileName,dataName):
        p=subprocess.Popen(["python","scripts/"+fileName,"-f","data/"+dataName])
        buttons[dataName]['p']= psutil.Process(pid=p.pid)
        buttons[dataName]['pauseButton'].setEnabled(T..)
        buttons[dataName]['killButton'].setEnabled(T..)
        buttons[dataName]['newButton'].setDisabled(T..)
        ? ?_lambda x=p,dataName=dataName:poller(x,dataName)).s..

    ___ pollerp,dataName):
        w___ T..:
            __ close:
                ____
            t__.s..(0.1)
            __ p.poll() __ n.. N..:
                buttons[dataName]['pauseButton'].setEnabled(F..)
                buttons[dataName]['killButton'].setEnabled(F..)
                buttons[dataName]['newButton'].setDisabled(F..)
                buttons[dataName]['resumeButton'].setDisabled(T..)
                ____

    ___ pauseMethoddataName):
        buttons[dataName]['p'].suspend()
        buttons[dataName]['pauseButton'].setDisabled(T..)
        buttons[dataName]['resumeButton'].setDisabled(F..)

    ___ resumeMethoddataName):
        buttons[dataName]['p'].resume()
        buttons[dataName]['pauseButton'].setDisabled(F..)
        buttons[dataName]['resumeButton'].setDisabled(T..)

    ___ killMethoddataName):
        buttons[dataName]['p'].kill()
        buttons[dataName]['pauseButton'].setEnabled(F..)
        buttons[dataName]['resumeButton'].setEnabled(F..)
        buttons[dataName]['killButton'].setEnabled(F..)
        buttons[dataName]['newButton'].setEnabled(T..)

    ___ refresh
        ___ button __ buttons:
            buttons[button]['newLabel'].deleteLater()
            buttons[button]['newButton'].deleteLater()
            buttons[button]['pauseButton'].deleteLater()
            buttons[button]['resumeButton'].deleteLater()
            buttons[button]['killButton'].deleteLater()

        ___ fileButton __ fileButtons:
            fileButton.deleteLater()

        buttons={}
        fileButtons=[]
        x=0
        ___ file __ os.listdir('./scripts'):
            fileButton = QPushButton(s..(file), self)
            
            # state is used below because it get passed a bool value so if you use val=file directly, 
            # then val will get a bool value i.e. False
            fileButton.clicked.connect(lambda state,val=file :loadFile(val))
            fileButton.show()
            fileButton.move(100,x)
            x+=50
            fileButtons.a.. (fileButton)

    ___ loadFilefileName):
        ___ fileButton __ fileButtons:
            fileButton.deleteLater()
        fileButtons=[]
        
        x=0
        ___ dataName __ os.listdir('./data'):
            newLabel= QLabel(dataName,self)
            newLabel.show()
            newLabel.move(x+40, 0)

            newButton = QPushButton('Process Start', self)
            newButton.show()
            newButton.move(x, 30)
            newButton.clicked.connect(lambda state, fileName=fileName,dataName=dataName:clickMethod(fileName,dataName))

            pauseButton = QPushButton('Process Pause', self)
            pauseButton.clicked.connect(lambda state, dataName=dataName:pauseMethod(dataName))
            pauseButton.show()
            pauseButton.move(x, 60)
            pauseButton.setEnabled(F..)

            resumeButton = QPushButton('Process Resume', self)
            resumeButton.clicked.connect(lambda state, dataName=dataName:resumeMethod(dataName))
            resumeButton.show()
            resumeButton.move(x, 90)
            resumeButton.setEnabled(F..)

            killButton = QPushButton('Process Kill', self)
            killButton.clicked.connect(lambda state, dataName=dataName:killMethod(dataName))
            killButton.show()
            killButton.move(x, 120)
            killButton.setEnabled(F..)

            buttons[dataName]={}
            buttons[dataName]['newButton']=newButton
            buttons[dataName]['newLabel']=newLabel
            buttons[dataName]['pauseButton']=pauseButton
            buttons[dataName]['resumeButton']=resumeButton
            buttons[dataName]['killButton']=killButton

            x+=100

    ___ closeEvent event):
        close=T..
        event.accept()
        print('Window closed')


__ ____ __ ______:
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )