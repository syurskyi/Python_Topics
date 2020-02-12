# -*- coding: utf-8 -*-
"""
Created on Fri May 06 15:46:27 2016
@author: jenovencio
"""

from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT
import sys, pygame, pygame.midi
from pygame import mixer  # Load the required library
import time
from threading import Thread
import json
from multiprocessing import Process


class eDrum(QtGui.QWidget):
    def __init__(self, inputDict=None):
        super(eDrum, self).__init__()

        # get input dictionary
        self.inputDict = inputDict

        # tab for input
        pushButtonOK = QtGui.QPushButton("OK")
        pushButtonOK.clicked.connect(self.setPreferences)

        self.vBoxlayout = QtGui.QVBoxLayout()
        self.hBoxlayout = QtGui.QHBoxLayout()

        self.hBoxlayout.addWidget(pushButtonOK)

        self.table = QtGui.QTableWidget()
        self.table.itemChanged.connect(self.itemChanged)
        self.table.horizontalHeader().setMinimumSectionSize(120)

        self.vBoxlayout.addWidget(self.table)
        self.vBoxlayout.addLayout(self.hBoxlayout)

        self.setLayout(self.vBoxlayout)

        self.setTable()
        self.setMaximumWidth(350)
        self.setMinimumWidth(180)
        self.resize(180, 170)
        self.setWindowTitle('Scalar Seetings')


class pad1(QtGui.QGraphicsEllipseItem):
    __counter = 0

    def __init__(self, x=0, y=0, c=50, parent=None, parentScene=None):
        super(pad1, self).__init__(x, y, c, c, parent, parentScene)
        # super(Node, self).__init__(x,y,c,v,parent,sceneparent)
        # setting node name based on counter

        # ---------------------------
        self.inputDict = {}
        self.seq = None

        self.stop = False
        self.playing = False

        self.parent = parent
        self.parentScene = parentScene

        self.setAcceptDrops(True)
        # self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)
        self.acceptTouchEvents()

        color = QtGui.QColor("Blue")
        self.setBrush(color)
        self.setAcceptDrops(True)
        self.acceptTouchEvents()

        self.setToolTip("Click to start song sequence")

        # mixer.pre_init(44100,-16,2,2048)
        mixer.pre_init(44100, -16, 2, 512)
        # mixer.init(22100, -16, 2, 64)
        mixer.init()
        pygame.midi.init()

    #    def hoverMoveEvent(self, event):
    #        #print "Mouse Entered"
    #        color = QtGui.QColor("Green")
    #        self.setBrush(color)
    #
    #    def hoverLeaveEvent(self, event):
    #        #print "Mouse has gone"
    #        color = QtGui.QColor("Blue")
    #        self.setBrush(color)

    def mouseMoveEvent(self, e):
        super(pad1, self).mouseMoveEvent(e)
        self.updateConnectors()

    def updateColor(self, colorString):
        color = QtGui.QColor(colorString)
        self.setBrush(color)

    def mousePressEvent(self, e):

        super(pad1, self).mousePressEvent(e)

        if e.button() == QtCore.Qt.LeftButton:
            print('left')
            # self.TriggerPad()
            self.startSong()

        if e.button() == QtCore.Qt.RightButton:
            print('midi')
            print(pad1.__counter)
            try:
                mixer.music.stop()
                self.playing = False
                # self.updateColor("Blue")
                if pad1.__counter < len(self.songListdecoded) - 1:
                    pad1.__counter += 1
                else:
                    # restart
                    pad1.__counter = 0
            except:
                print("Nothing to do")
                # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")

    def mouseReleaseEvent(self, e):
        # super(pad1, self).mouseReleaseEvent(e)
        print("Release")
        # self.updateColor("Blue")

    def startSong(self):

        # self.updateColor("Red")
        try:

            self.songPath = self.songListdecoded[pad1.__counter][0]
            self.offset = float(self.songListdecoded[pad1.__counter][1])
            self.playSong(self.songPath, self.offset)

            # update counter

            if pad1.__counter < len(self.songListdecoded) - 1:
                pad1.__counter += 1
                print("count = %i" % pad1.__counter)
            else:
                # restart
                pad1.__counter = 0
                print("count = %i" % pad1.__counter)
        except:

            # update counter

            if pad1.__counter < len(self.songListdecoded) - 1:
                pad1.__counter += 1
                print("count = %i" % pad1.__counter)
            else:
                # restart
                pad1.__counter = 0
                print("count = %i" % pad1.__counter)
                # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")
                # self.updateColor("Blue")

    def TriggerPad(self):
        print("TriggerPad")

        try:
            print("self.inputDict[self.seq]['song']")
            print(self.inputDict[self.seq]['song'])
            songListcoded = self.inputDict[self.seq]['song']
            songListdecoded = []

            for s in songListcoded:
                for rep in range(int(s[0])):
                    songListdecoded.append([s[1], float(s[2])])
            print(songListdecoded)
            self.songListdecoded = songListdecoded

            # play song
            # print('---------------------------------------')
            # print(songListdecoded)
            # self.songPath = songListdecoded[pad1.__counter][0]
            # self.offset = float(songListdecoded[pad1.__counter][1])
            # print(songPath)


        except:
            # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")
            # self.updateColor("Blue")
            pass

    def playSong(self, songPath, offset):
        self.playing = True
        mixer.init()
        mixer.pre_init(44100, -16, 2, 2048)
        mixer.music.load(songPath)
        self.endEvent = 234
        mixer.music.set_endevent(self.endEvent)

        # cur = mixer.music.get_pos()
        # print("cur=",cur)
        # mixer.music.set_pos(offset)
        mixer.music.play(start=offset)

        p = Thread(target=self.isPlaying)
        p.start()

    #        while pygame.mixer.music.get_busy():
    # pygame.time.Clock().tick(2)

    #    def mouseDoubleClickEvent(self,e):

    #        print("Double click")
    #        #self.nodeScript()
    #        print('midi')
    #        print(pad1.__counter)
    #        try:
    #            self.playing = False
    #            mixer.music.stop()
    #            if pad1.__counter<len(self.songListdecoded)-1:
    #                pad1.__counter+=1
    #            else:
    #                # restart
    #                pad1.__counter=0
    #        except:
    #            print("Nothing to do")
    # QtGui.QMessageBox.about( QtGui.QWidget(),"Warning", "Please, define a song sequence!")

    def dragEnterEvent(self, e):
        print(e)

    def keyPressEvent(self, e):
        super(pad1, self).keyPressEvent(e)
        print(e.key)

    def eventFilter(self, object, event):
        print("mousemove!")
        print(event.type())

    def isPlaying(self):
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(2)
        self.playing = False
        # self.updateColor("Blue")


class mainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None, flag=0):
        super(mainWindow, self).__init__(parent)

        self.tableList = []
        self.songDict = {}
        self.deviceList = {}
        self.midiNote = None

        self.resize(800, 600)
        self.scene = QtGui.QGraphicsScene()
        self.centralwidget = QtGui.QGraphicsView(self.scene)
        # vbox = QtGui.QHBoxLayout()
        self.qgrid = QtGui.QGridLayout(self.centralwidget)
        # vbox.addStretch(1)
        self.pad1 = pad1()
        self.ntabs = 1
        self.countTabs = 0

        self.tabs = QtGui.QTabWidget()
        self.tabs.currentChanged.connect(self.updateDict)
        self.tabPad = QtGui.QWidget()
        self.tabIn = QtGui.QWidget()
        self.tabPlus = QtGui.QWidget()

        self.tabButton = QtGui.QToolButton(self)
        self.tabButton.setText('+')
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tabButton.setToolTip("Click to add new songs sequence")
        self.tabs.setTabsClosable(True)
        self.tabs.tabsClosable
        self.tabs.setCornerWidget(self.tabButton)
        self.tabButton.clicked.connect(self.createTab)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        # createting V layout
        self.vBox = QtGui.QVBoxLayout()

        # midi note and midi output
        self.hBoxlayout = QtGui.QHBoxLayout()
        self.linedit = QtGui.QLineEdit("")
        self.linedit.setPlaceholderText("Set Midi Note for Song Sequence")
        # self.linedit.setEnabled(False)
        self.linedit.textChanged.connect(self.setMidiNote)

        # add combo selection
        self.createCombo()

        # add combo and qline to H layout
        self.hBoxlayout.addWidget(self.combo)
        self.hBoxlayout.addWidget(self.linedit)

        self.vBox.addLayout(self.hBoxlayout)
        # self.vBox.addWidget()

        # tab for Pad  -------------------------------------------
        view = QtGui.QGraphicsView(self.scene)
        self.scene.addItem(self.pad1)

        # add midi note hitted
        bottom = QtGui.QFrame()
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        bottom.setMaximumHeight(20)

        self.infoline = QtGui.QLineEdit("")
        self.infoline.setReadOnly(True)

        self.statusBar = QtGui.QStatusBar()
        # statusBar.setMaximumHeight(10)
        self.statusBar.setFixedHeight(20)

        self.midiNoteInput = "Midi note:"
        self.midiNoteLabel = QtGui.QLabel(self.midiNoteInput)

        # self.statusBar.addWidget(self.midiNoteLabel,1)
        self.statusBar.showMessage(self.midiNoteInput)

        # add widget to layout
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(view)
        splitter2.addWidget(self.statusBar)

        # self.vBox.addWidget(view)
        # self.vBox.addWidget(bottom)
        self.vBox.addWidget(splitter2)
        self.tabPad.setLayout(self.vBox)

        # self.setCentralWidget(self.centralwidget)


        # ---------------------------------------------------------------
        # add tabs to app
        self.tabs.addTab(self.tabPad, "Play")
        self.createTab()

        # ---------------------------------------------------------------
        # add menu file
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        openAction = QtGui.QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)

        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)

        # appending actions in file menu
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)

        # ---------------------------------------------------------------
        # add menu file

        self.midiMenu = menubar.addMenu('&Midi_Device')

        refreshAction = QtGui.QAction('Refresh', self)
        refreshAction.setShortcut('F5')
        refreshAction.triggered.connect(self.midiDevice)

        refreshAction2 = QtGui.QAction('Refresh 2', self)
        refreshAction2.setShortcut('F6')
        refreshAction2.triggered.connect(self.midiDevice)

        # appending actions in file menu
        self.midiMenu.addAction(refreshAction)

        # self.updateStatusBar(45)

        # -----------------------------------------------------------------------

        # ---------------------------------------------------------------
        self.setCentralWidget(self.tabs)
        self.setWindowTitle('open Song Sequencer')

    def updateStatusBar(self, value):

        self.midiNoteInput = "Midi note: " + str(value)
        self.midiNoteLabel = QtGui.QLabel(self.midiNoteInput)
        self.statusBar.showMessage(self.midiNoteInput, 0)

    def setMidiNote(self):
        # print("set midi note")
        self.midiNote = int(self.sender().text())
        # print(self.midiNote)

    def midiDevice(self):
        self.deviceList = {}
        # set up pygame
        pygame.init()
        pygame.midi.init()

        # list all midi devices, maximum of 10
        self.device = [None] * 10
        index = 0
        for x in range(0, pygame.midi.get_count()):
            print(pygame.midi.get_device_info(x))
            device = pygame.midi.get_device_info(x)
            # if is a input append in the menu bar

            if device[2] == 1:
                print(str(device[1]))

                self.device[index] = QtGui.QAction(str(device[1]), self, checkable=True)
                # self.device[index].setShortcut('F6')
                self.device[index].triggered.connect(self.setMidiDevice)
                self.midiMenu.addAction(self.device[index])

                #                 self.device[index] = QtGui.QAction(device[1] , self) #, checkable=True)
                #
                #                 self.device[index].triggered.connect(self.setMidiDevice)
                #
                #                 self.midiMenu.addAction(self.device[index])

                self.deviceList[index] = [device[1].decode("utf-8"), x]
                index += 1

                # self.setMidiDevice()

    def setMidiDevice(self):
        print("setMidiDevice")
        sender = self.sender().text()
        print(sender)
        print(type(sender))

        for index in self.deviceList.keys():

            device = self.deviceList[index][0]
            x = self.deviceList[index][1]
            print('device %s' % device)
            print('type %s' % type(device))
            print('x = %i' % x)
            if type(device) == type(sender):
                print('device==sender')
                self.device[index].setChecked(True)
                self.inp = pygame.midi.Input(x)
            else:
                self.device[index].setChecked(False)

        self.getMidi = True
        # starting midi looping event
        self.p = Thread(target=self.getMidiEvent)
        self.p.start()

    def getMidiEvent(self):

        while self.getMidi:
            # print("read to receive midi input")

            if self.inp.poll():
                # no way to find number of messages in queue
                # so we just specify a high max value
                midiinfo = self.inp.read(100)
                midinote = midiinfo[0][0][1]
                midiint = midiinfo[0][0][2]

                self.updateStatusBar(midinote)

                # if midinote == self.midiNote:
                # try:
                print(midiinfo)
                print(midinote)
                print('midiint = %i' % midiint)

                if midiint > 10 and midinote == self.midiNote:
                    self.s = Thread(target=self.pad1.startSong)
                    self.s.start()
                    # pygame.time.wait(20)

                    # pygame.time.wait(200)
                    # self.pad1.startSong()
                    # except:
                    #    self.getMidi = False
                    #    self.errorHandeling

    def errorHandeling(self):
        pass
        # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")
        # self.pad1.updateColor("Blue")

    def openFile(self):
        print("open")

        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'), "oss *.*")
        f = open(filename, 'r')
        self.json = json.loads(f.read())
        f.close()

        # parse json to dict
        self.songDict = self.json

        print(self.songDict)

        # update plyer dict
        self.pad1.inputDict = self.songDict

        # update combo selection
        self.updateCombo()

        self.updateTabs()

        # setting tab and tables

    def updateTabs(self):
        # remove all tabs
        for i in range(self.ntabs):
            self.tabs.removeTab(i + 1)

        self.ntabs = 1
        for key in self.songDict:
            print(key)
            # self.countTabs+=1
            tabString = key
            songList = self.songDict[tabString]['song']
            self.s = songCreator(self.tabs, songList)

            mytab = self.tabs.addTab(self.s, tabString)
            self.songDict[tabString]["id"] = mytab
            # adding default variable name to table

            # self.s.addseq(songList)


            self.ntabs += 1

    def saveFile(self):
        print("save")
        self.updateDict(1)
        jsonvar = json.dumps(self.pad1.inputDict, indent=4)
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'), 'oss')

        if os.path.exists(filename):
            os.remove(filename)

        if filename:
            try:
                f = open(filename, 'w')
                f.write(jsonvar)
                f.close()
            except ValueError:
                print("Oops!  That was not a valid path.  Try again...")
        else:
            print("Do nothing")

    def keyPressEvent(self, e):
        print(e.key)

    def songSequence(self):
        # tab for input -------------------------------------------

        index = self.tabs.currentIndex() + 1
        s = songCreator()
        self.tabs.addTab(s, "Song Sequence_" + str(index))

    def deleteTab(self):
        print("delete tab")
        # print(index)
        sending_button = self.sender()

        print(dir(sending_button))
        # self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))

        # index = self.tabs.currentIndex()
        # index = self.tabs.underMouse()

        # print("index =",index)
        for i in range(self.ntabs):
            print("index=", i)
            self.tabs.setCurrentIndex(i)
            self.tabs.currentIndex()

        self.ntabs -= 1

    def createTab(self):

        index = self.tabs.currentIndex()
        print(index)
        curtab = self.tabs.currentWidget()

        self.countTabs += 1
        s = songCreator(self.tabs)
        tabString = "Song Sequence_" + str(self.countTabs)

        mytab = self.tabs.addTab(s, tabString)
        self.songDict[tabString] = {"id": mytab}
        self.ntabs += 1

    def closeTab(self, currentIndex):
        if currentIndex > 0:
            key = self.tabs.tabText(currentIndex)
            print(key)
            if key in self.songDict:
                del self.songDict[key]
            currentQWidget = self.tabs.widget(currentIndex)
            currentQWidget.deleteLater()
            self.tabs.removeTab(currentIndex)

        else:
            QtGui.QMessageBox.about(self, "Warning", "Do not close this tab")

    def updateDict(self, index):
        print("updateDict")
        print(index)
        curindex = self.tabs.currentIndex()
        if curindex == 0:
            for elem in self.songDict:
                print(elem)
                tabid = self.songDict[elem]["id"]
                self.songDict[elem]["song"] = []
                # self.tabs.setCurrentIndex(tabid)
                # w = self.tabs.currentWidget()
                w = self.tabs.widget(tabid)
                print(w.table)
                numRows = w.table.rowCount()
                print(numRows)
                for row in range(numRows):
                    c = w.table.item(row, 0).text()
                    s = w.table.item(row, 1).text()
                    o = w.table.item(row, 2).text()
                    self.songDict[elem]["song"].append([c, s, o])
            self.tabs.setCurrentIndex(0)
            print(self.songDict)

            # update plyer dict
            self.pad1.inputDict = self.songDict

            # update combo selection
            self.updateCombo()

            index = self.combo.currentIndex()

            self.pad1.seq = self.combo.itemText(index)
            self.pad1.__counter = 0
            self.pad1.TriggerPad()

    def createCombo(self):
        self.combo = QtGui.QComboBox()
        self.combo.activated['QString'].connect(self.handleActivated)
        self.combo.currentIndexChanged['QString'].connect(self.handleChanged)
        self.combo.setMinimumWidth(350)
        # return self.combo

    def updateCombo(self):
        self.combo.clear()
        for key in self.songDict:
            if "song" in self.songDict[key]:
                if self.songDict[key]["song"]:
                    self.combo.addItem(key)

    def handleActivated(self):
        print("Activate")
        index = self.combo.currentIndex()
        print(self.combo.itemText(index))
        self.pad1.seq = self.combo.itemText(index)
        # self.pad1.TriggerPad()

    def handleChanged(self):
        print("Change")
        index = self.combo.currentIndex()
        print(self.combo.itemText(index))
        self.pad1.seq = self.combo.itemText(index)
        # self.pad1.TriggerPad()


class songCreator(QtGui.QTabWidget):
    def __init__(self, tabs, songList=None):
        super(songCreator, self).__init__()

        self.tableIndex = 0
        # tab for input -------------------------------------------
        self.pushButton1 = QtGui.QPushButton("Add song")
        self.pushButton1.clicked.connect(self.addsong)
        self.pushButton2 = QtGui.QPushButton("Remove song")
        self.pushButton2.clicked.connect(self.deletesong)

        # self.pushButton3 = QtGui.QPushButton("Delete Entire Sequence")
        # self.pushButton3.clicked.connect(self.deleteTab)

        self.vBoxlayout = QtGui.QVBoxLayout()
        self.hBoxlayout = QtGui.QHBoxLayout()

        self.hBoxlayout.addWidget(self.pushButton1)
        self.hBoxlayout.addWidget(self.pushButton2)

        self.table = QtGui.QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["  Counter ", "  Song  ", "  offset   "])
        # self.table.itemChanged.connect(self.itemChanged)




        if songList != None:
            self.addseq(songList)

        self.vBoxlayout.addLayout(self.hBoxlayout)
        self.vBoxlayout.addWidget(self.table)
        # self.vBoxlayout.addWidget(self.pushButton3)

        self.setLayout(self.vBoxlayout)

    def addsong(self):
        print("add song")

        index = self.tableIndex
        print("index = %i" % index)
        self.table.setRowCount(self.tableIndex + 1)
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'), "song files (*.mp3 *.wav)")

        # adding default variable name to table
        default_name = QtGui.QTableWidgetItem("1")
        self.table.setItem(index, 0, default_name)
        # adding default variable name to table
        default_name = QtGui.QTableWidgetItem(filename)
        self.table.setItem(index, 1, default_name)
        # adding default variable name to table
        default_name = QtGui.QTableWidgetItem("0")
        self.table.setItem(index, 2, default_name)

        self.tableIndex += 1
        # setting table format
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def deletesong(self):
        print("delete item")
        rows = sorted(set(index.row() for index in
                          self.table.selectedIndexes()))
        l = len(rows)
        for row in rows:
            print('Row %d is selected' % row)
            self.table.removeRow(row)
        self.tableIndex -= l

    def addseq(self, songList):
        index = self.tableIndex
        self.table.setRowCount(len(songList))
        for song in songList:
            print("-------------------------------------")
            print(song[0])
            default_name = QtGui.QTableWidgetItem(song[0])
            self.table.setItem(index, 0, default_name)
            # adding default variable name to table
            default_name = QtGui.QTableWidgetItem(song[1])
            self.table.setItem(index, 1, default_name)
            # adding default variable name to table
            default_name = QtGui.QTableWidgetItem(song[2])
            self.table.setItem(index, 2, default_name)
            index += 1

        self.tableIndex = index
        # setting table format
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


class Player():
    def __init__(songPath, offset):
        mixer.init()
        mixer.music.load(songPath)
        mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


def main():
    app = QtGui.QApplication([])
    # ex = Canvas()
    ex = mainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()