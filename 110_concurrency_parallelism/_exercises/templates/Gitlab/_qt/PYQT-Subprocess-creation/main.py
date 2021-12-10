______ sys
from PyQt5 ______ QtCore, QtWidgets
from PyQt5.QtWidgets ______ QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets ______ QPushButton
from PyQt5.QtCore ______ QSize
______ psutil
______ subprocess
______ os
______ t__
from _ ______ ?

class MainWindow(QMainWindow):
    ___ __init__(self):
        QMainWindow.__init__(self)
        self.close=False
        self.setWindowTitle('Boom')
        self.setMinimumSize(QSize(300, 200))

        self.refreshButton = QPushButton('Refresh files', self)
        self.refreshButton.clicked.connect(self.refresh)
        self.refreshButton.show()
        self.refreshButton.move(100,150)

        self.buttons={}
        self.fileButtons=[]

    ___ clickMethod(self,fileName,dataName):
        p=subprocess.Popen(["python","scripts/"+fileName,"-f","data/"+dataName])
        self.buttons[dataName]['p']= psutil.Process(pid=p.pid)
        self.buttons[dataName]['pauseButton'].setEnabled(True)
        self.buttons[dataName]['killButton'].setEnabled(True)
        self.buttons[dataName]['newButton'].setDisabled(True)
        ? ?_lambda x=p,dataName=dataName:self.poller(x,dataName)).s..

    ___ poller(self,p,dataName):
        w___ True:
            if self.close:
                break
            t__.s..(0.1)
            if p.poll() is not N..:
                self.buttons[dataName]['pauseButton'].setEnabled(False)
                self.buttons[dataName]['killButton'].setEnabled(False)
                self.buttons[dataName]['newButton'].setDisabled(False)
                self.buttons[dataName]['resumeButton'].setDisabled(True)
                break

    ___ pauseMethod(self,dataName):
        self.buttons[dataName]['p'].suspend()
        self.buttons[dataName]['pauseButton'].setDisabled(True)
        self.buttons[dataName]['resumeButton'].setDisabled(False)

    ___ resumeMethod(self,dataName):
        self.buttons[dataName]['p'].resume()
        self.buttons[dataName]['pauseButton'].setDisabled(False)
        self.buttons[dataName]['resumeButton'].setDisabled(True)

    ___ killMethod(self,dataName):
        self.buttons[dataName]['p'].kill()
        self.buttons[dataName]['pauseButton'].setEnabled(False)
        self.buttons[dataName]['resumeButton'].setEnabled(False)
        self.buttons[dataName]['killButton'].setEnabled(False)
        self.buttons[dataName]['newButton'].setEnabled(True)

    ___ refresh(self):
        ___ button __ self.buttons:
            self.buttons[button]['newLabel'].deleteLater()
            self.buttons[button]['newButton'].deleteLater()
            self.buttons[button]['pauseButton'].deleteLater()
            self.buttons[button]['resumeButton'].deleteLater()
            self.buttons[button]['killButton'].deleteLater()

        ___ fileButton __ self.fileButtons:
            fileButton.deleteLater()

        self.buttons={}
        self.fileButtons=[]
        x=0
        ___ file __ os.listdir('./scripts'):
            fileButton = QPushButton(s..(file), self)
            
            # state is used below because it get passed a bool value so if you use val=file directly, 
            # then val will get a bool value i.e. False
            fileButton.clicked.connect(lambda state,val=file :self.loadFile(val))
            fileButton.show()
            fileButton.move(100,x)
            x+=50
            self.fileButtons.append(fileButton)

    ___ loadFile(self,fileName):
        ___ fileButton __ self.fileButtons:
            fileButton.deleteLater()
        self.fileButtons=[]
        
        x=0
        ___ dataName __ os.listdir('./data'):
            newLabel= QLabel(dataName,self)
            newLabel.show()
            newLabel.move(x+40, 0)

            newButton = QPushButton('Process Start', self)
            newButton.show()
            newButton.move(x, 30)
            newButton.clicked.connect(lambda state, fileName=fileName,dataName=dataName:self.clickMethod(fileName,dataName))

            pauseButton = QPushButton('Process Pause', self)
            pauseButton.clicked.connect(lambda state, dataName=dataName:self.pauseMethod(dataName))
            pauseButton.show()
            pauseButton.move(x, 60)
            pauseButton.setEnabled(False)

            resumeButton = QPushButton('Process Resume', self)
            resumeButton.clicked.connect(lambda state, dataName=dataName:self.resumeMethod(dataName))
            resumeButton.show()
            resumeButton.move(x, 90)
            resumeButton.setEnabled(False)

            killButton = QPushButton('Process Kill', self)
            killButton.clicked.connect(lambda state, dataName=dataName:self.killMethod(dataName))
            killButton.show()
            killButton.move(x, 120)
            killButton.setEnabled(False)

            self.buttons[dataName]={}
            self.buttons[dataName]['newButton']=newButton
            self.buttons[dataName]['newLabel']=newLabel
            self.buttons[dataName]['pauseButton']=pauseButton
            self.buttons[dataName]['resumeButton']=resumeButton
            self.buttons[dataName]['killButton']=killButton

            x+=100

    ___ closeEvent(self, event):
        self.close=True
        event.accept()
        print('Window closed')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )