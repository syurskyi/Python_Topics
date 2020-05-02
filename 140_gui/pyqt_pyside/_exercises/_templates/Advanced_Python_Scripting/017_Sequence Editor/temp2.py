# -*- coding: utf-8 -*-
"""
Created on Fri May 06 15:46:27 2016
@author: jenovencio
"""

____ PyQt4 _____ ?C.., ?G..
_____ ___
_____ os
____ PyQt4.?C.. _____ py_S.., SIGNAL, SLOT
_____ ___, pygame, pygame.midi
____ pygame _____ mixer  # Load the required library
_____ time
____ threading _____ Thread
_____ json
____ multiprocessing _____ Process


c_ eDrum(?G...?W..
    ___  -  , inputDict_None
        super(eDrum, self). - ()

        # get input dictionary
        inputDict _ inputDict

        # tab for input
        pushButtonOK _ ?G...?PB..("OK")
        pushButtonOK.c___.c..(setPreferences)

        vBoxlayout _ ?G...QVBoxLayout()
        hBoxlayout _ ?G...QHBoxLayout()

        hBoxlayout.addWidget(pushButtonOK)

        table _ ?G...QTableWidget()
        table.itemChanged.c..(itemChanged)
        table.horizontalHeader().setMinimumSectionSize(120)

        vBoxlayout.addWidget(table)
        vBoxlayout.addLayout(hBoxlayout)

        setLayout(vBoxlayout)

        setTable()
        setMaximumWidth(350)
        setMinimumWidth(180)
        resize(180, 170)
        setWindowTitle('Scalar Seetings')


c_ pad1(?G...QGraphicsEllipseItem
    __counter _ 0

    ___  -  , x_0, y_0, c_50, parent_None, parentScene_None
        super(pad1, self). - (x, y, c, c, parent, parentScene)
        # super(Node, self).__init__(x,y,c,v,parent,sceneparent)
        # setting node name based on counter

        # ---------------------------
        inputDict _ {}
        seq _ None

        stop _ False
        playing _ False

        parent _ parent
        parentScene _ parentScene

        setAcceptDrops(T..)
        # self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        # self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        setAcceptHoverEvents(T..)
        acceptTouchEvents()

        color _ ?G...QColor("Blue")
        setBrush(color)
        setAcceptDrops(T..)
        acceptTouchEvents()

        setToolTip("Click to start song sequence")

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

    ___ mouseMoveEvent , e
        super(pad1, self).mouseMoveEvent(e)
        updateConnectors()

    ___ updateColor , colorString
        color _ ?G...QColor(colorString)
        setBrush(color)

    ___ mousePressEvent , e

        super(pad1, self).mousePressEvent(e)

        __ e.button() __ ?C...Qt.LeftButton:
            print('left')
            # self.TriggerPad()
            startSong()

        __ e.button() __ ?C...Qt.RightButton:
            print('midi')
            print(pad1.__counter)
            try:
                mixer.music.stop()
                playing _ False
                # self.updateColor("Blue")
                __ pad1.__counter < le.(songListdecoded) - 1:
                    pad1.__counter +_ 1
                ____
                    # restart
                    pad1.__counter _ 0
            except:
                print("Nothing to do")
                # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")

    ___ mouseReleaseEvent , e
        # super(pad1, self).mouseReleaseEvent(e)
        print("Release")
        # self.updateColor("Blue")

    ___ startSong

        # self.updateColor("Red")
        try:

            songPath _ songListdecoded[pad1.__counter][0]
            offset _ fl..(songListdecoded[pad1.__counter][1])
            playSong(songPath, offset)

            # update counter

            __ pad1.__counter < le.(songListdecoded) - 1:
                pad1.__counter +_ 1
                print("count = %i" % pad1.__counter)
            ____
                # restart
                pad1.__counter _ 0
                print("count = %i" % pad1.__counter)
        except:

            # update counter

            __ pad1.__counter < le.(songListdecoded) - 1:
                pad1.__counter +_ 1
                print("count = %i" % pad1.__counter)
            ____
                # restart
                pad1.__counter _ 0
                print("count = %i" % pad1.__counter)
                # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")
                # self.updateColor("Blue")

    ___ TriggerPad
        print("TriggerPad")

        try:
            print("self.inputDict[self.seq]['song']")
            print(inputDict[seq]['song'])
            songListcoded _ inputDict[seq]['song']
            songListdecoded _ []

            ___ s in songListcoded:
                ___ rep in range(int(s[0])):
                    songListdecoded.ap..([s[1], fl..(s[2])])
            print(songListdecoded)
            songListdecoded _ songListdecoded

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

    ___ playSong , songPath, offset
        playing _ T..
        mixer.init()
        mixer.pre_init(44100, -16, 2, 2048)
        mixer.music.load(songPath)
        endEvent _ 234
        mixer.music.set_endevent(endEvent)

        # cur = mixer.music.get_pos()
        # print("cur=",cur)
        # mixer.music.set_pos(offset)
        mixer.music.play(start_offset)

        p _ Thread(target_isPlaying)
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

    ___ dragEnterEvent , e
        print(e)

    ___ keyPressEvent , e
        super(pad1, self).keyPressEvent(e)
        print(e.key)

    ___ eventFilter , object, event
        print("mousemove!")
        print(event.type())

    ___ isPlaying
        w__ pygame.mixer.music.get_busy(
            pygame.time.Clock().tick(2)
        playing _ False
        # self.updateColor("Blue")


c_ mainWindow(?G...QMainWindow
    ___  -  , parent_None, flag_0
        super(mainWindow, self). - (parent)

        tableList _ []
        songDict _ {}
        deviceList _ {}
        midiNote _ None

        resize(800, 600)
        scene _ ?G...QGraphicsScene()
        centralwidget _ ?G...QGraphicsView(scene)
        # vbox = QtGui.QHBoxLayout()
        qgrid _ ?G...QGridLayout(centralwidget)
        # vbox.addStretch(1)
        pad1 _ pad1()
        ntabs _ 1
        countTabs _ 0

        tabs _ ?G...QTabWidget()
        tabs.currentChanged.c..(updateDict)
        tabPad _ ?G...?W..()
        tabIn _ ?G...?W..()
        tabPlus _ ?G...?W..()

        tabButton _ ?G...QToolButton
        tabButton.sT..('+')
        font _ tabButton.font()
        font.setBold(T..)
        tabButton.sF..(font)
        tabButton.setToolTip("Click to add new songs sequence")
        tabs.setTabsClosable(T..)
        tabs.tabsClosable
        tabs.setCornerWidget(tabButton)
        tabButton.c___.c..(createTab)
        tabs.tabCloseRequested.c..(closeTab)

        # createting V layout
        vBox _ ?G...QVBoxLayout()

        # midi note and midi output
        hBoxlayout _ ?G...QHBoxLayout()
        linedit _ ?G...QLineEdit("")
        linedit.setPlaceholderText("Set Midi Note for Song Sequence")
        # self.linedit.setEnabled(False)
        linedit.tC...c..(setMidiNote)

        # add combo selection
        createCombo()

        # add combo and qline to H layout
        hBoxlayout.addWidget(combo)
        hBoxlayout.addWidget(linedit)

        vBox.addLayout(hBoxlayout)
        # self.vBox.addWidget()

        # tab for Pad  -------------------------------------------
        view _ ?G...QGraphicsView(scene)
        scene.aI..(pad1)

        # add midi note hitted
        bottom _ ?G...QFrame()
        bottom.setFrameShape(?G...QFrame.StyledPanel)
        bottom.setMaximumHeight(20)

        infoline _ ?G...QLineEdit("")
        infoline.setReadOnly(T..)

        statusBar _ ?G...QStatusBar()
        # statusBar.setMaximumHeight(10)
        statusBar.setFixedHeight(20)

        midiNoteInput _ "Midi note:"
        midiNoteLabel _ ?G...QLabel(midiNoteInput)

        # self.statusBar.addWidget(self.midiNoteLabel,1)
        statusBar.showMessage(midiNoteInput)

        # add widget to layout
        splitter2 _ ?G...QSplitter(?C...Qt.Vertical)
        splitter2.addWidget(view)
        splitter2.addWidget(statusBar)

        # self.vBox.addWidget(view)
        # self.vBox.addWidget(bottom)
        vBox.addWidget(splitter2)
        tabPad.setLayout(vBox)

        # self.setCentralWidget(self.centralwidget)


        # ---------------------------------------------------------------
        # add tabs to app
        tabs.addTab(tabPad, "Play")
        createTab()

        # ---------------------------------------------------------------
        # add menu file
        menubar _ menuBar()
        fileMenu _ menubar.addMenu('&File')

        openAction _ ?G...QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.c..(openFile)

        saveAction _ ?G...QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.c..(saveFile)

        # appending actions in file menu
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)

        # ---------------------------------------------------------------
        # add menu file

        midiMenu _ menubar.addMenu('&Midi_Device')

        refreshAction _ ?G...QAction('Refresh', self)
        refreshAction.setShortcut('F5')
        refreshAction.triggered.c..(midiDevice)

        refreshAction2 _ ?G...QAction('Refresh 2', self)
        refreshAction2.setShortcut('F6')
        refreshAction2.triggered.c..(midiDevice)

        # appending actions in file menu
        midiMenu.addAction(refreshAction)

        # self.updateStatusBar(45)

        # -----------------------------------------------------------------------

        # ---------------------------------------------------------------
        setCentralWidget(tabs)
        setWindowTitle('open Song Sequencer')

    ___ updateStatusBar , value

        midiNoteInput _ "Midi note: " + st.(value)
        midiNoteLabel _ ?G...QLabel(midiNoteInput)
        statusBar.showMessage(midiNoteInput, 0)

    ___ setMidiNote
        # print("set midi note")
        midiNote _ int(sender().t..())
        # print(self.midiNote)

    ___ midiDevice
        deviceList _ {}
        # set up pygame
        pygame.init()
        pygame.midi.init()

        # list all midi devices, maximum of 10
        device _ [None] * 10
        index _ 0
        ___ x in range(0, pygame.midi.get_count()):
            print(pygame.midi.get_device_info(x))
            device _ pygame.midi.get_device_info(x)
            # if is a input append in the menu bar

            __ device[2] __ 1:
                print(st.(device[1]))

                device[index] _ ?G...QAction(st.(device[1]), self, checkable_T..)
                # self.device[index].setShortcut('F6')
                device[index].triggered.c..(setMidiDevice)
                midiMenu.addAction(device[index])

                #                 self.device[index] = QtGui.QAction(device[1] , self) #, checkable=True)
                #
                #                 self.device[index].triggered.connect(self.setMidiDevice)
                #
                #                 self.midiMenu.addAction(self.device[index])

                deviceList[index] _ [device[1].decode("utf-8"), x]
                index +_ 1

                # self.setMidiDevice()

    ___ setMidiDevice
        print("setMidiDevice")
        sender _ sender().t..()
        print(sender)
        print(type(sender))

        ___ index in deviceList.keys(

            device _ deviceList[index][0]
            x _ deviceList[index][1]
            print('device %s' % device)
            print('type %s' % type(device))
            print('x = %i' % x)
            __ type(device) __ type(sender
                print('device==sender')
                device[index].setChecked(T..)
                inp _ pygame.midi.Input(x)
            ____
                device[index].setChecked(False)

        getMidi _ T..
        # starting midi looping event
        p _ Thread(target_getMidiEvent)
        p.start()

    ___ getMidiEvent

        w__ getMidi:
            # print("read to receive midi input")

            __ inp.poll(
                # no way to find number of messages in queue
                # so we just specify a high max value
                midiinfo _ inp.read(100)
                midinote _ midiinfo[0][0][1]
                midiint _ midiinfo[0][0][2]

                updateStatusBar(midinote)

                # if midinote == self.midiNote:
                # try:
                print(midiinfo)
                print(midinote)
                print('midiint = %i' % midiint)

                __ midiint > 10 an. midinote __ midiNote:
                    s _ Thread(target_pad1.startSong)
                    s.start()
                    # pygame.time.wait(20)

                    # pygame.time.wait(200)
                    # self.pad1.startSong()
                    # except:
                    #    self.getMidi = False
                    #    self.errorHandeling

    ___ errorHandeling
        pass
        # QtGui.QMessageBox.about( QtGui.QWidget()	,"Warning", "Please, define a song sequence!")
        # self.pad1.updateColor("Blue")

    ___ openFile
        print("open")

        filename _ ?G...QFileDialog.getOpenFileName , 'Open File', os.getenv('HOME'), "oss *.*")
        f _ open(filename, 'r')
        json _ json.loads(f.read())
        f.close()

        # parse json to dict
        songDict _ json

        print(songDict)

        # update plyer dict
        pad1.inputDict _ songDict

        # update combo selection
        updateCombo()

        updateTabs()

        # setting tab and tables

    ___ updateTabs
        # remove all tabs
        ___ i in range(ntabs
            tabs.removeTab(i + 1)

        ntabs _ 1
        ___ key in songDict:
            print(key)
            # self.countTabs+=1
            tabString _ key
            songList _ songDict[tabString]['song']
            s _ songCreator(tabs, songList)

            mytab _ tabs.addTab(s, tabString)
            songDict[tabString]["id"] _ mytab
            # adding default variable name to table

            # self.s.addseq(songList)


            ntabs +_ 1

    ___ saveFile
        print("save")
        updateDict(1)
        jsonvar _ json.dumps(pad1.inputDict, indent_4)
        filename _ ?G...QFileDialog.getSaveFileName , 'Save File', os.getenv('HOME'), 'oss')

        __ os.path.exists(filename
            os.remove(filename)

        __ filename:
            try:
                f _ open(filename, 'w')
                f.write(jsonvar)
                f.close()
            except ValueError:
                print("Oops!  That was not a valid path.  Try again...")
        ____
            print("Do nothing")

    ___ keyPressEvent , e
        print(e.key)

    ___ songSequence
        # tab for input -------------------------------------------

        index _ tabs.cI..() + 1
        s _ songCreator()
        tabs.addTab(s, "Song Sequence_" + st.(index))

    ___ deleteTab
        print("delete tab")
        # print(index)
        sending_button _ sender()

        print(dir(sending_button))
        # self.status_label.setText('%s Clicked!' % str(sending_button.objectName()))

        # index = self.tabs.currentIndex()
        # index = self.tabs.underMouse()

        # print("index =",index)
        ___ i in range(ntabs
            print("index=", i)
            tabs.setCurrentIndex(i)
            tabs.cI..()

        ntabs -_ 1

    ___ createTab

        index _ tabs.cI..()
        print(index)
        curtab _ tabs.currentWidget()

        countTabs +_ 1
        s _ songCreator(tabs)
        tabString _ "Song Sequence_" + st.(countTabs)

        mytab _ tabs.addTab(s, tabString)
        songDict[tabString] _ {"id": mytab}
        ntabs +_ 1

    ___ closeTab , cI..
        __ cI.. > 0:
            key _ tabs.tabText(cI..)
            print(key)
            __ key in songDict:
                del songDict[key]
            currentQWidget _ tabs.widget(cI..)
            currentQWidget.deleteLater()
            tabs.removeTab(cI..)

        ____
            ?G...QMessageBox.about , "Warning", "Do not close this tab")

    ___ updateDict , index
        print("updateDict")
        print(index)
        curindex _ tabs.cI..()
        __ curindex __ 0:
            ___ elem in songDict:
                print(elem)
                tabid _ songDict[elem]["id"]
                songDict[elem]["song"] _ []
                # self.tabs.setCurrentIndex(tabid)
                # w = self.tabs.currentWidget()
                w _ tabs.widget(tabid)
                print(w.table)
                numRows _ w.table.rowCount()
                print(numRows)
                ___ row in range(numRows
                    c _ w.table.item(row, 0).t..()
                    s _ w.table.item(row, 1).t..()
                    o _ w.table.item(row, 2).t..()
                    songDict[elem]["song"].ap..([c, s, o])
            tabs.setCurrentIndex(0)
            print(songDict)

            # update plyer dict
            pad1.inputDict _ songDict

            # update combo selection
            updateCombo()

            index _ combo.cI..()

            pad1.seq _ combo.iT..(index)
            pad1.__counter _ 0
            pad1.TriggerPad()

    ___ createCombo
        combo _ ?G...QComboBox()
        combo.activated['QString'].c..(handleActivated)
        combo.cIC..['QString'].c..(handleChanged)
        combo.setMinimumWidth(350)
        # return self.combo

    ___ updateCombo
        combo.c..
        ___ key in songDict:
            __ "song" in songDict[key]:
                __ songDict[key]["song"]:
                    combo.aI..(key)

    ___ handleActivated
        print("Activate")
        index _ combo.cI..()
        print(combo.iT..(index))
        pad1.seq _ combo.iT..(index)
        # self.pad1.TriggerPad()

    ___ handleChanged
        print("Change")
        index _ combo.cI..()
        print(combo.iT..(index))
        pad1.seq _ combo.iT..(index)
        # self.pad1.TriggerPad()


c_ songCreator(?G...QTabWidget
    ___  -  , tabs, songList_None
        super(songCreator, self). - ()

        tableIndex _ 0
        # tab for input -------------------------------------------
        pushButton1 _ ?G...?PB..("Add song")
        pushButton1.c___.c..(addsong)
        pushButton2 _ ?G...?PB..("Remove song")
        pushButton2.c___.c..(deletesong)

        # self.pushButton3 = QtGui.QPushButton("Delete Entire Sequence")
        # self.pushButton3.clicked.connect(self.deleteTab)

        vBoxlayout _ ?G...QVBoxLayout()
        hBoxlayout _ ?G...QHBoxLayout()

        hBoxlayout.addWidget(pushButton1)
        hBoxlayout.addWidget(pushButton2)

        table _ ?G...QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["  Counter ", "  Song  ", "  offset   "])
        # self.table.itemChanged.connect(self.itemChanged)




        __ songList !_ None:
            addseq(songList)

        vBoxlayout.addLayout(hBoxlayout)
        vBoxlayout.addWidget(table)
        # self.vBoxlayout.addWidget(self.pushButton3)

        setLayout(vBoxlayout)

    ___ addsong
        print("add song")

        index _ tableIndex
        print("index = %i" % index)
        table.setRowCount(tableIndex + 1)
        filename _ ?G...QFileDialog.getOpenFileName , 'Open File', os.getenv('HOME'), "song files (*.mp3 *.wav)")

        # adding default variable name to table
        default_name _ ?G...?TWI..("1")
        table.sI..(index, 0, default_name)
        # adding default variable name to table
        default_name _ ?G...?TWI..(filename)
        table.sI..(index, 1, default_name)
        # adding default variable name to table
        default_name _ ?G...?TWI..("0")
        table.sI..(index, 2, default_name)

        tableIndex +_ 1
        # setting table format
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    ___ deletesong
        print("delete item")
        rows _ sorted(set(index.row() ___ index in
                          table.selectedIndexes()))
        l _ le.(rows)
        ___ row in rows:
            print('Row %d is selected' % row)
            table.removeRow(row)
        tableIndex -_ l

    ___ addseq , songList
        index _ tableIndex
        table.setRowCount(le.(songList))
        ___ song in songList:
            print("-------------------------------------")
            print(song[0])
            default_name _ ?G...?TWI..(song[0])
            table.sI..(index, 0, default_name)
            # adding default variable name to table
            default_name _ ?G...?TWI..(song[1])
            table.sI..(index, 1, default_name)
            # adding default variable name to table
            default_name _ ?G...?TWI..(song[2])
            table.sI..(index, 2, default_name)
            index +_ 1

        tableIndex _ index
        # setting table format
        table.resizeColumnsToContents()
        table.resizeRowsToContents()


c_ Player(
    ___  - (songPath, offset
        mixer.init()
        mixer.music.load(songPath)
        mixer.music.play()
        w__ pygame.mixer.music.get_busy(
            pygame.time.Clock().tick(10)


___ main(
    app _ ?G...?A..([])
    # ex = Canvas()
    ex _ mainWindow()
    ex.s..
    ___.e..(app.e


__ __name__ __ '__main__':
    main()