#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


______ ___
____ xml.dom.minidom ______ parseString

____ ?.?C.. ______ (QByteArray, QDir, QEasingCurve, QFile, QFileInfo,
        QLibraryInfo, QObject, QPointF, QProcess, QProcessEnvironment,
        QStandardPaths, __, QT_VERSION, QT_VERSION_STR, QTextStream, QUrl)
____ ?.?W.. ______ ?A.., ?MB..

____ colors ______ Colors
____ demoitemanimation ______ DemoItemAnimation
____ examplecontent ______ ExampleContent
____ itemcircleanimation ______ ItemCircleAnimation
____ menucontent ______ MenuContentItem
____ score ______ Score
____ textbutton ______ TextButton


c_ MenuManager(QObject):
    ROOT, MENU1, MENU2, LAUNCH, DOCUMENTATION, QUIT, FULLSCREEN, UP, DOWN, \
            BACK, LAUNCH_QML _ range(11)

    pInstance _ N..

    ___ __init__(self):
        super(MenuManager, self).__init__()

        self.contentsDoc _ N..
        self.assistantProcess _ QProcess()
        self.helpRootUrl _ ''
        self.docDir _ QDir()
        self.imgDir _ QDir()

        self.info _ {}
        self.window _ N..

        self.ticker _ N..
        self.tickerInAnim _ N..
        self.upButton _ N..
        self.downButton _ N..
        self.score _ Score()
        self.currentMenu _ "[no menu visible]"
        self.currentCategory _ "[no category visible]"
        self.currentMenuButtons _ "[no menu buttons visible]"
        self.currentInfo _ "[no info visible]"
        self.currentMenuCode _ -1
        self.readXmlDocument()

    @classmethod
    ___ instance(cls):
        __ cls.pInstance __ N..:
            cls.pInstance _ cls()

        r_ cls.pInstance

    ___ getResource  name):
        r_ QByteArray()

    ___ readXmlDocument(self):
        root _ QFileInfo(__file__).absolutePath()
        xml_file _ QFile(root + '/examples.xml')
        xml_file.o..(QFile.ReadOnly | QFile.Text)
        contents _ xml_file.readAll().data()
        xml_file.close()

        self.contentsDoc _ parseString(contents)

    ___ itemSelected  userCode, menuName):
        __ userCode == MenuManager.LAUNCH:
            self.launchExample(self.currentInfo)
        ____ userCode == MenuManager.LAUNCH_QML:
            self.launchQml(self.currentInfo)
        ____ userCode == MenuManager.DOCUMENTATION:
            self.showDocInAssistant(self.currentInfo)
        ____ userCode == MenuManager.QUIT:
            ?A...quit()
        ____ userCode == MenuManager.FULLSCREEN:
            self.window.toggleFullscreen()
        ____ userCode == MenuManager.ROOT:
            # Out.
            self.score.queueMovie(self.currentMenu + ' -out', Score.FROM_START,
                    Score.LOCK_ITEMS)
            self.score.queueMovie(self.currentMenuButtons + ' -out',
                    Score.FROM_START, Score.LOCK_ITEMS)
            self.score.queueMovie(self.currentInfo + ' -out')
            self.score.queueMovie(self.currentInfo + ' -buttons -out',
                    Score.NEW_ANIMATION_ONLY)
            self.score.queueMovie('back -out', Score.ONLY_IF_VISIBLE)

            # Book-keeping.
            self.currentMenuCode _ MenuManager.ROOT
            self.currentMenu _ menuName + ' -menu1'
            self.currentMenuButtons _ menuName + ' -buttons'
            self.currentInfo _ menuName + ' -info'

            # In.
            self.score.queueMovie('upndown -shake')
            self.score.queueMovie(self.currentMenu, Score.FROM_START,
                    Score.UNLOCK_ITEMS)
            self.score.queueMovie(self.currentMenuButtons, Score.FROM_START,
                    Score.UNLOCK_ITEMS)
            self.score.queueMovie(self.currentInfo)

            __ no. Colors.noTicker:
                self.ticker.doIntroTransitions _ True
                self.tickerInAnim.setStartDelay(2000)
                self.ticker.useGuideQt()
                self.score.queueMovie('ticker', Score.NEW_ANIMATION_ONLY)
        ____ userCode == MenuManager.MENU1:
            # Out.
            self.score.queueMovie(self.currentMenu + ' -out', Score.FROM_START,
                    Score.LOCK_ITEMS)
            self.score.queueMovie(self.currentMenuButtons + ' -out',
                    Score.FROM_START, Score.LOCK_ITEMS)
            self.score.queueMovie(self.currentInfo + ' -out')

            # Book-keeping.
            self.currentMenuCode _ MenuManager.MENU1
            self.currentCategory _ menuName
            self.currentMenu _ menuName + ' -menu1'
            self.currentInfo _ menuName + ' -info'

            # In.
            self.score.queueMovie('upndown -shake')
            self.score.queueMovie('back -in')
            self.score.queueMovie(self.currentMenu, Score.FROM_START,
                    Score.UNLOCK_ITEMS)
            self.score.queueMovie(self.currentInfo)

            __ no. Colors.noTicker:
                self.ticker.useGuideTt()
        ____ userCode == MenuManager.MENU2:
            # Out.
            self.score.queueMovie(self.currentInfo + ' -out',
                    Score.NEW_ANIMATION_ONLY)
            self.score.queueMovie(self.currentInfo + ' -buttons -out',
                    Score.NEW_ANIMATION_ONLY)

            # Book-keeping.
            self.currentMenuCode _ MenuManager.MENU2
            self.currentInfo _ menuName

            # In/shake.
            self.score.queueMovie('upndown -shake')
            self.score.queueMovie('back -shake')
            self.score.queueMovie(self.currentMenu + ' -shake')
            self.score.queueMovie(self.currentInfo, Score.NEW_ANIMATION_ONLY)
            self.score.queueMovie(self.currentInfo + ' -buttons',
                    Score.NEW_ANIMATION_ONLY)

            __ no. Colors.noTicker:
                self.score.queueMovie('ticker -out', Score.NEW_ANIMATION_ONLY)
        ____ userCode == MenuManager.UP:
            backMenu _ self.info[self.currentMenu]['back']
            __ backMenu:
                self.score.queueMovie(self.currentMenu + ' -top_out',
                        Score.FROM_START, Score.LOCK_ITEMS)
                self.score.queueMovie(backMenu + ' -bottom_in',
                        Score.FROM_START, Score.UNLOCK_ITEMS)
                self.currentMenu _ backMenu
        ____ userCode == MenuManager.DOWN:
            moreMenu _ self.info[self.currentMenu]['more']
            __ moreMenu:
                self.score.queueMovie(self.currentMenu + ' -bottom_out',
                        Score.FROM_START, Score.LOCK_ITEMS)
                self.score.queueMovie(moreMenu + ' -top_in', Score.FROM_START,
                        Score.UNLOCK_ITEMS)
                self.currentMenu _ moreMenu
        ____ userCode == MenuManager.BACK:
            __ self.currentMenuCode == MenuManager.MENU2:
                # Out.
                self.score.queueMovie(self.currentInfo + ' -out',
                        Score.NEW_ANIMATION_ONLY)
                self.score.queueMovie(self.currentInfo + ' -buttons -out',
                        Score.NEW_ANIMATION_ONLY)

                # Book-keeping.
                self.currentMenuCode _ MenuManager.MENU1
                self.currentMenuButtons _ self.currentCategory + ' -buttons'
                self.currentInfo _ self.currentCategory + ' -info'

                # In/shake.
                self.score.queueMovie('upndown -shake')
                self.score.queueMovie(self.currentMenu + ' -shake')
                self.score.queueMovie(self.currentInfo,
                        Score.NEW_ANIMATION_ONLY)
                self.score.queueMovie(self.currentInfo + ' -buttons',
                        Score.NEW_ANIMATION_ONLY)

                __ no. Colors.noTicker:
                    self.ticker.doIntroTransitions _ False
                    self.tickerInAnim.setStartDelay(500)
                    self.score.queueMovie('ticker', Score.NEW_ANIMATION_ONLY)
            ____ self.currentMenuCode !_ MenuManager.ROOT:
                self.itemSelected(MenuManager.ROOT, Colors.rootMenuName)

        # Update back and more buttons.
        __ self.info.setdefault(self.currentMenu, {}).g..('back'):
            back_state _ TextButton.OFF
        ____
            back_state _ TextButton.DISABLED

        __ self.info[self.currentMenu].g..('more'):
            more_state _ TextButton.OFF
        ____
            more_state _ TextButton.DISABLED

        self.upButton.setState(back_state)
        self.downButton.setState(more_state)

        __ self.score.hasQueuedMovies
            self.score.playQue()
            # Playing new movies might include loading etc., so ignore the FPS
            # at this point.
            self.window.fpsHistory _   # list

    ___ showDocInAssistant  name):
        url _ self.resolveDocUrl(name)
        Colors.debug("Sending URL to Assistant:", url)

        # Start assistant if it's not already running.
        __ self.assistantProcess.state() !_ QProcess.Running:
            app _ QLibraryInfo.location(QLibraryInfo.BinariesPath) + QDir.separator()

            __ ___.platform == 'darwin':
                app +_ 'Assistant.app/Contents/MacOS/Assistant'
            ____
                app +_ 'assistant'

            args _ ['-enableRemoteControl']
            self.assistantProcess.start(app, args)
            __ no. self.assistantProcess.waitForStarted
                ?MB...critical(N.., "PyQt Demo",
                        "Could not start %s." % app)
                r_

        # Send command through remote control even if the process was just
        # started to activate assistant and bring it to the front.
        cmd_str _ QTextStream(self.assistantProcess)
        cmd_str << 'SetSource ' << url << '\n'

    ___ launchExample  name):
        executable _ self.resolveExeFile(name)

        process _ QProcess(self)
        process.error.c..(self.launchError)

        __ ___.platform == 'win32':
            # Make sure it finds the DLLs on Windows.
            env _ QProcessEnvironment.systemEnvironment()
            env.insert('PATH',
                    QLibraryInfo.location(QLibraryInfo.BinariesPath) + ';' +
                            env.value('PATH'))
            process.setProcessEnvironment(env)

        __ self.info[name]['changedirectory'] !_ 'false':
            workingDirectory _ self.resolveDataDir(name)
            process.setWorkingDirectory(workingDirectory)
            Colors.debug("Setting working directory:", workingDirectory)

        Colors.debug("Launching:", executable)
        process.start(___.executable, [executable])

    ___ launchQml  name):
        import_path _ self.resolveDataDir(name)
        qml _ self.resolveQmlFile(name)

        process _ QProcess(self)
        process.error.c..(self.launchError)

        env _ QProcessEnvironment.systemEnvironment()
        env.insert('QML2_IMPORT_PATH', import_path)
        process.setProcessEnvironment(env)

        executable _ QLibraryInfo.location(QLibraryInfo.BinariesPath) + '/qmlscene'
        Colors.debug("Launching:", executable)
        process.start(executable, [qml])

    ___ launchError  error):
        __ error !_ QProcess.Crashed:
            ?MB...critical(N.., "Failed to launch the example",
                    "Could not launch the example. Ensure that it has been "
                    "built.",
                    ?MB...Cancel)

    ___ init  window):
        self.window _ window

        # Create div.
        self.createTicker()
        self.createUpnDownButtons()
        self.createBackButton()

        # Create first level menu.
        rootElement _ self.contentsDoc.documentElement
        self.createRootMenu(rootElement)

        # Create second level menus.
        level2Menu _ self._first_element(rootElement)
        w__ level2Menu __ no. N..:
            self.createSubMenu(level2Menu)

            # Create leaf menu and example info.
            example _ self._first_element(level2Menu)
            w__ example __ no. N..:
                self.readInfoAboutExample(example)
                self.createLeafMenu(example)
                example _ self._next_element(example)

            level2Menu _ self._next_element(level2Menu)

    @classmethod
    ___ _first_element(cls, node):
        r_ cls._skip_nonelements(node.firstChild)

    @classmethod
    ___ _next_element(cls, node):
        r_ cls._skip_nonelements(node.nextSibling)

    @staticmethod
    ___ _skip_nonelements(node):
        w__ node __ no. N.. and node.nodeType !_ node.ELEMENT_NODE:
            node _ node.nextSibling

        r_ node

    ___ readInfoAboutExample  example):
        name _ example.getAttribute('name')
        __ name in self.info:
            Colors.debug("__WARNING: MenuManager.readInfoAboutExample: "
                         "Demo/example with name", name, "appears twice in "
                         "the xml-file!__")

        self.info.setdefault(name, {})['filename'] _ example.getAttribute('filename')
        self.info[name]['dirname'] _ example.parentNode.getAttribute('dirname')
        self.info[name]['changedirectory'] _ example.getAttribute('changedirectory')
        self.info[name]['image'] _ example.getAttribute('image')
        self.info[name]['qml'] _ example.getAttribute('qml')

    ___ resolveDir  name):
        dirName _ self.info[name]['dirname']
        fileName _ self.info[name]['filename'].split('/')

        dir _ QFileInfo(__file__).dir()
        # To the 'examples' directory.
        dir.cdUp()

        dir.cd(dirName)

        __ le.(fileName) > 1:
            dir.cd('/'.join(fileName[:-1]))

        # This may legitimately fail if the example is just a simple .py file.
        dir.cd(fileName[-1])

        r_ dir

    ___ resolveDataDir  name):
        r_ self.resolveDir(name).absolutePath()

    ___ resolveExeFile  name):
        dir _ self.resolveDir(name)

        fileName _ self.info[name]['filename'].split('/')[-1]

        pyFile _ QFile(dir.path() + '/' + fileName + '.py')
        __ pyFile.exists
            r_ pyFile.fileName()

        pywFile _ QFile(dir.path() + '/' + fileName + '.pyw')
        __ pywFile.exists
            r_ pywFile.fileName()

        Colors.debug("- WARNING: Could not resolve executable:", dir.path(),
                fileName)
        r_ '__executable not found__'

    ___ resolveQmlFile  name):
        dir _ self.resolveDir(name)

        fileName _ self.info[name]['filename'].split('/')[-1]

        qmlFile _ QFile(dir.path() + '/' + fileName + '.qml')
        __ qmlFile.exists
            r_ qmlFile.fileName()

        Colors.debug("- WARNING: Could not resolve QML file:", dir.path(),
                fileName)
        r_ '__QML not found__'

    ___ resolveDocUrl  name):
        dirName _ self.info[name]['dirname']
        fileName _ self.info[name]['filename']

        r_ self.helpRootUrl + dirName.replace('/', '-') + '-' + fileName + '.html'

    ___ resolveImageUrl  name):
        r_ self.helpRootUrl + 'images/' + name

    ___ getHtml  name):
        r_ self.getResource(self.resolveDocUrl(name))

    ___ getImage  name):
        imageName _ self.info[name]['image']
        fileName _ self.info[name]['filename']

        __ self.info[name]['qml'] == 'true':
            fileName _ 'qml-' + fileName.split('/')[-1]

        __ no. imageName:
            imageName _ fileName + '-example.png'

            __ self.getResource(self.resolveImageUrl(imageName)).isEmpty
                imageName _ fileName + '.png'

            __ self.getResource(self.resolveImageUrl(imageName)).isEmpty
                imageName _ fileName + 'example.png'

        r_ self.getResource(self.resolveImageUrl(imageName))

    ___ createRootMenu  el):
        name _ el.getAttribute('name')
        self.createMenu(el, MenuManager.MENU1)
        self.createInfo(
                MenuContentItem(el, self.window.mainSceneRoot),
                name + ' -info')

        menuButtonsIn _ self.score.insertMovie(name + ' -buttons')
        menuButtonsOut _ self.score.insertMovie(name + ' -buttons -out')
        self.createLowLeftButton("Quit", MenuManager.QUIT, menuButtonsIn,
                menuButtonsOut, N..)
        self.createLowRightButton("Toggle fullscreen", MenuManager.FULLSCREEN,
                menuButtonsIn, menuButtonsOut, N..)

    ___ createSubMenu  el):
        name _ el.getAttribute('name')
        self.createMenu(el, MenuManager.MENU2)
        self.createInfo(
                MenuContentItem(el, self.window.mainSceneRoot),
                name + ' -info')

    ___ createLeafMenu  el):
        name _ el.getAttribute('name')
        self.createInfo(ExampleContent(name, self.window.mainSceneRoot), name)

        infoButtonsIn _ self.score.insertMovie(name + ' -buttons')
        infoButtonsOut _ self.score.insertMovie(name + ' -buttons -out')
        self.createLowRightLeafButton("Documentation", 600,
                MenuManager.DOCUMENTATION, infoButtonsIn, infoButtonsOut, N..)
        __ el.getAttribute('executable') !_ 'false':
            self.createLowRightLeafButton("Launch", 405, MenuManager.LAUNCH,
                    infoButtonsIn, infoButtonsOut, N..)
        ____ el.getAttribute('qml') == 'true':
            self.createLowRightLeafButton("Display", 405,
                    MenuManager.LAUNCH_QML, infoButtonsIn, infoButtonsOut,
                    N..)

    ___ createMenu  category, type):
        sw _ self.window.scene.sceneRect().width()
        xOffset _ 15
        yOffset _ 10
        maxExamples _ Colors.menuCount
        menuIndex _ 1
        name _ category.getAttribute('name')
        currentNode _ self._first_element(category)
        currentMenu _ '%s -menu%d' % (name, menuIndex)

        w__ currentNode __ no. N..:
            movieIn _ self.score.insertMovie(currentMenu)
            movieOut _ self.score.insertMovie(currentMenu + ' -out')
            movieNextTopOut _ self.score.insertMovie(currentMenu + ' -top_out')
            movieNextBottomOut _ self.score.insertMovie(currentMenu + ' -bottom_out')
            movieNextTopIn _ self.score.insertMovie(currentMenu + ' -top_in')
            movieNextBottomIn _ self.score.insertMovie(currentMenu + ' -bottom_in')
            movieShake _ self.score.insertMovie(currentMenu + ' -shake')

            i _ 0
            w__ currentNode __ no. N.. and i < maxExamples:
                # Create a normal menu button.
                label _ currentNode.getAttribute('name')
                item _ TextButton(label, TextButton.LEFT, type,
                        self.window.mainSceneRoot)

                item.setRecursiveVisible F..
                item.setZValue(10)
                ih _ item.sceneBoundingRect().height()
                iw _ item.sceneBoundingRect().width()
                ihp _ ih + 3

                # Create in-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.setDuration(1000 + (i * 20))
                anim.setStartValue(QPointF(xOffset, -ih))
                anim.setKeyValueAt(0.20, QPointF(xOffset, -ih))
                anim.setKeyValueAt(0.50, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY + (10 * float(i / 4.0))))
                anim.setKeyValueAt(0.60, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.70, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY + (5 * float(i / 4.0))))
                anim.setKeyValueAt(0.80, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.90, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY + (2 * float(i / 4.0))))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieIn.ap..(anim)

                # Create out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished(True)
                anim.setDuration(700 + (30 * i))
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.60, QPointF(xOffset, 600 - ih - ih))
                anim.setKeyValueAt(0.65, QPointF(xOffset + 20, 600 - ih))
                anim.setEndValue(QPointF(sw + iw, 600 - ih))
                movieOut.ap..(anim)

                # Create shake-animation.
                anim _ DemoItemAnimation(item)
                anim.setDuration(700)
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.55, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY - i*2.0))
                anim.setKeyValueAt(0.70, QPointF(xOffset - 10, (i * ihp) + yOffset + Colors.contentStartY - i*1.5))
                anim.setKeyValueAt(0.80, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY - i*1.0))
                anim.setKeyValueAt(0.90, QPointF(xOffset - 2, (i * ihp) + yOffset + Colors.contentStartY - i*0.5))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieShake.ap..(anim)

                # Create next-menu top-out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished(True)
                anim.setDuration(200 + (30 * i))
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.70, QPointF(xOffset, yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(-iw, yOffset + Colors.contentStartY))
                movieNextTopOut.ap..(anim)

                # Create next-menu bottom-out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished(True)
                anim.setDuration(200 + (30 * i))
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.70, QPointF(xOffset, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(-iw, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                movieNextBottomOut.ap..(anim)

                # Create next-menu top-in-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.setDuration(700 - (30 * i))
                anim.setStartValue(QPointF(-iw, yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.30, QPointF(xOffset, yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieNextTopIn.ap..(anim)

                # Create next-menu bottom-in-animation.
                reverse _ maxExamples - i
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.setDuration(1000 - (30 * reverse))
                anim.setStartValue(QPointF(-iw, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.30, QPointF(xOffset, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieNextBottomIn.ap..(anim)

                i +_ 1
                currentNode _ self._next_element(currentNode)

            __ currentNode __ no. N.. and i == maxExamples:
                # We need another menu, so register for 'more' and 'back'
                # buttons.
                menuIndex +_ 1
                self.info.setdefault(currentMenu, {})['more'] _ '%s -menu%d' % (name, menuIndex)
                currentMenu _ '%s -menu%d' % (name, menuIndex)
                self.info.setdefault(currentMenu, {})['back'] _ '%s -menu%d' % (name, menuIndex - 1)

    ___ createLowLeftButton  label, type, movieIn, movieOut, movieShake, menuString_""):
        button _ TextButton(label, TextButton.RIGHT, type,
                self.window.mainSceneRoot, TextButton.PANEL)
        __ menuString:
            button.setMenuString(menuString)
        button.setRecursiveVisible F..
        button.setZValue(10)

        iw _ button.sceneBoundingRect().width()
        xOffset _ 15

        # Create in-animation.
        buttonIn _ DemoItemAnimation(button, DemoItemAnimation.ANIM_IN)
        buttonIn.setDuration(1800)
        buttonIn.setStartValue(QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 35))
        buttonIn.setKeyValueAt(0.5, QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 35))
        buttonIn.setKeyValueAt(0.7, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        buttonIn.setEndValue(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        movieIn.ap..(buttonIn)

        # Create out-animation.
        buttonOut _ DemoItemAnimation(button, DemoItemAnimation.ANIM_OUT)
        buttonOut.setHideOnFinished(True)
        buttonOut.setDuration(400)
        buttonOut.setStartValue(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        buttonOut.setEndValue(QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 26))
        movieOut.ap..(buttonOut)

        __ movieShake __ no. N..:
            shakeAnim _ DemoItemAnimation(button, DemoItemAnimation.ANIM_UNSPECIFIED)
            shakeAnim.setDuration(650)
            shakeAnim.setStartValue(buttonIn.endValue())
            shakeAnim.setKeyValueAt(0.60, buttonIn.endValue())
            shakeAnim.setKeyValueAt(0.70, buttonIn.endValue() + QPointF(-3, 0))
            shakeAnim.setKeyValueAt(0.80, buttonIn.endValue() + QPointF(2, 0))
            shakeAnim.setKeyValueAt(0.90, buttonIn.endValue() + QPointF(-1, 0))
            shakeAnim.setEndValue(buttonIn.endValue())
            movieShake.ap..(shakeAnim)

    ___ createLowRightButton  label, type, movieIn, movieOut, movieShake):
        item _ TextButton(label, TextButton.RIGHT, type,
                self.window.mainSceneRoot, TextButton.PANEL)
        item.setRecursiveVisible F..
        item.setZValue(10)

        sw _ self.window.scene.sceneRect().width()
        xOffset _ 70

        # Create in-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        anim.setDuration(1800)
        anim.setStartValue(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.5, QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.7, QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setEndValue(QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 26))
        movieIn.ap..(anim)

        # Create out-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        anim.setHideOnFinished(True)
        anim.setDuration(400)
        anim.setStartValue(QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 26))
        anim.setEndValue(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 26))
        movieOut.ap..(anim)

    ___ createLowRightLeafButton  label, xOffset, type, movieIn, movieOut, movieShake):
        item _ TextButton(label, TextButton.RIGHT, type,
                self.window.mainSceneRoot, TextButton.PANEL)
        item.setRecursiveVisible F..
        item.setZValue(10)

        sw _ self.window.scene.sceneRect().width()
        sh _ self.window.scene.sceneRect().height()

        # Create in-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        anim.setDuration(1050)
        anim.setStartValue(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.10, QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.30, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.35, QPointF(xOffset + 30, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.40, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.45, QPointF(xOffset + 5, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setKeyValueAt(0.50, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        anim.setEndValue(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        movieIn.ap..(anim)

        # Create out-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        anim.setHideOnFinished(True)
        anim.setDuration(300)
        anim.setStartValue(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        anim.setEndValue(QPointF(xOffset, sh))
        movieOut.ap..(anim)

    ___ createInfo  item, name):
        movie_in _ self.score.insertMovie(name)
        movie_out _ self.score.insertMovie(name + ' -out')
        item.setZValue(8)
        item.setRecursiveVisible F..

        xOffset _ 230.0
        infoIn _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        infoIn.setDuration(650)
        infoIn.setStartValue(QPointF(self.window.scene.sceneRect().width(), Colors.contentStartY))
        infoIn.setKeyValueAt(0.60, QPointF(xOffset, Colors.contentStartY))
        infoIn.setKeyValueAt(0.70, QPointF(xOffset + 20, Colors.contentStartY))
        infoIn.setKeyValueAt(0.80, QPointF(xOffset, Colors.contentStartY))
        infoIn.setKeyValueAt(0.90, QPointF(xOffset + 7, Colors.contentStartY))
        infoIn.setEndValue(QPointF(xOffset, Colors.contentStartY))
        movie_in.ap..(infoIn)

        infoOut _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        infoOut.setCurveShape(QEasingCurve.InQuad)
        infoOut.setDuration(300)
        infoOut.setHideOnFinished(True)
        infoOut.setStartValue(QPointF(xOffset, Colors.contentStartY))
        infoOut.setEndValue(QPointF(-600, Colors.contentStartY))
        movie_out.ap..(infoOut)

    ___ createTicker(self):
        __ Colors.noTicker:
            r_

        movie_in _ self.score.insertMovie('ticker')
        movie_out _ self.score.insertMovie('ticker -out')
        movie_activate _ self.score.insertMovie('ticker -activate')
        movie_deactivate _ self.score.insertMovie('ticker -deactivate')

        self.ticker _ ItemCircleAnimation()
        self.ticker.setZValue(50)
        self.ticker.hide()

        # Move ticker in.
        qtendpos _ 485
        qtPosY _ 120
        self.tickerInAnim _ DemoItemAnimation(self.ticker,
                DemoItemAnimation.ANIM_IN)
        self.tickerInAnim.setDuration(500)
        self.tickerInAnim.setStartValue(QPointF(self.window.scene.sceneRect().width(), Colors.contentStartY + qtPosY))
        self.tickerInAnim.setKeyValueAt(0.60, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        self.tickerInAnim.setKeyValueAt(0.70, QPointF(qtendpos + 30, Colors.contentStartY + qtPosY))
        self.tickerInAnim.setKeyValueAt(0.80, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        self.tickerInAnim.setKeyValueAt(0.90, QPointF(qtendpos + 5, Colors.contentStartY + qtPosY))
        self.tickerInAnim.setEndValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        movie_in.ap..(self.tickerInAnim)

        # Move ticker out.
        qtOut _ DemoItemAnimation(self.ticker, DemoItemAnimation.ANIM_OUT)
        qtOut.setHideOnFinished(True)
        qtOut.setDuration(500)
        qtOut.setStartValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtOut.setEndValue(QPointF(self.window.scene.sceneRect().width() + 700, Colors.contentStartY + qtPosY))
        movie_out.ap..(qtOut)

        # Move ticker in on activate.
        qtActivate _ DemoItemAnimation(self.ticker)
        qtActivate.setDuration(400)
        qtActivate.setStartValue(QPointF(self.window.scene.sceneRect().width(), Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.60, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.70, QPointF(qtendpos + 30, Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.80, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.90, QPointF(qtendpos + 5, Colors.contentStartY + qtPosY))
        qtActivate.setEndValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        movie_activate.ap..(qtActivate)

        # Move ticker out on deactivate.
        qtDeactivate _ DemoItemAnimation(self.ticker)
        qtDeactivate.setHideOnFinished(True)
        qtDeactivate.setDuration(400)
        qtDeactivate.setStartValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtDeactivate.setEndValue(QPointF(qtendpos, 800))
        movie_deactivate.ap..(qtDeactivate)

    ___ createUpnDownButtons(self):
        xOffset _ 15.0
        yOffset _ 450.0

        self.upButton _ TextButton("", TextButton.LEFT, MenuManager.UP,
                self.window.mainSceneRoot, TextButton.UP)
        self.upButton.prepare()
        self.upButton.setPos(xOffset, yOffset)
        self.upButton.setState(TextButton.DISABLED)

        self.downButton _ TextButton("", TextButton.LEFT, MenuManager.DOWN,
                self.window.mainSceneRoot, TextButton.DOWN)
        self.downButton.prepare()
        self.downButton.setPos(xOffset + 10 + self.downButton.sceneBoundingRect().width(), yOffset)

        movieShake _ self.score.insertMovie('upndown -shake')

        shakeAnim _ DemoItemAnimation(self.upButton,
                DemoItemAnimation.ANIM_UNSPECIFIED)
        shakeAnim.setDuration(650)
        shakeAnim.setStartValue(self.upButton.pos())
        shakeAnim.setKeyValueAt(0.60, self.upButton.pos())
        shakeAnim.setKeyValueAt(0.70, self.upButton.pos() + QPointF(-2, 0))
        shakeAnim.setKeyValueAt(0.80, self.upButton.pos() + QPointF(1, 0))
        shakeAnim.setKeyValueAt(0.90, self.upButton.pos() + QPointF(-1, 0))
        shakeAnim.setEndValue(self.upButton.pos())
        movieShake.ap..(shakeAnim)

        shakeAnim _ DemoItemAnimation(self.downButton,
                DemoItemAnimation.ANIM_UNSPECIFIED)
        shakeAnim.setDuration(650)
        shakeAnim.setStartValue(self.downButton.pos())
        shakeAnim.setKeyValueAt(0.60, self.downButton.pos())
        shakeAnim.setKeyValueAt(0.70, self.downButton.pos() + QPointF(-5, 0))
        shakeAnim.setKeyValueAt(0.80, self.downButton.pos() + QPointF(-3, 0))
        shakeAnim.setKeyValueAt(0.90, self.downButton.pos() + QPointF(-1, 0))
        shakeAnim.setEndValue(self.downButton.pos())
        movieShake.ap..(shakeAnim)

    ___ createBackButton(self):
        backIn _ self.score.insertMovie('back -in')
        backOut _ self.score.insertMovie('back -out')
        backShake _ self.score.insertMovie('back -shake')
        self.createLowLeftButton("Back", MenuManager.ROOT, backIn, backOut,
                backShake, Colors.rootMenuName)
