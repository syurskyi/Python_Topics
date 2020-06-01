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


______ sys
____ xml.dom.minidom ______ parseString

____ ?.QtCore ______ (QByteArray, QDir, QEasingCurve, QFile, QFileInfo,
        QLibraryInfo, QObject, QPointF, QProcess, QProcessEnvironment,
        QStandardPaths, Qt, QT_VERSION, QT_VERSION_STR, QTextStream, QUrl)
____ ?.?W.. ______ QApplication, QMessageBox

____ colors ______ Colors
____ demoitemanimation ______ DemoItemAnimation
____ examplecontent ______ ExampleContent
____ itemcircleanimation ______ ItemCircleAnimation
____ menucontent ______ MenuContentItem
____ score ______ Score
____ textbutton ______ TextButton


class MenuManager(QObject):
    ROOT, MENU1, MENU2, LAUNCH, DOCUMENTATION, QUIT, FULLSCREEN, UP, DOWN, \
            BACK, LAUNCH_QML _ range(11)

    pInstance _ None

    ___ __init__(self):
        super(MenuManager, self).__init__()

        self.contentsDoc _ None
        self.assistantProcess _ QProcess()
        self.helpRootUrl _ ''
        self.docDir _ QDir()
        self.imgDir _ QDir()

        self.info _ {}
        self.window _ None

        self.ticker _ None
        self.tickerInAnim _ None
        self.upButton _ None
        self.downButton _ None
        self.score _ Score()
        self.currentMenu _ "[no menu visible]"
        self.currentCategory _ "[no category visible]"
        self.currentMenuButtons _ "[no menu buttons visible]"
        self.currentInfo _ "[no info visible]"
        self.currentMenuCode _ -1
        self.readXmlDocument()

    @classmethod
    ___ instance(cls):
        if cls.pInstance is None:
            cls.pInstance _ cls()

        return cls.pInstance

    ___ getResource(self, name):
        return QByteArray()

    ___ readXmlDocument(self):
        root _ QFileInfo(__file__).absolutePath()
        xml_file _ QFile(root + '/examples.xml')
        xml_file.open(QFile.ReadOnly | QFile.Text)
        contents _ xml_file.readAll().data()
        xml_file.close()

        self.contentsDoc _ parseString(contents)

    ___ itemSelected(self, userCode, menuName):
        if userCode == MenuManager.LAUNCH:
            self.launchExample(self.currentInfo)
        elif userCode == MenuManager.LAUNCH_QML:
            self.launchQml(self.currentInfo)
        elif userCode == MenuManager.DOCUMENTATION:
            self.showDocInAssistant(self.currentInfo)
        elif userCode == MenuManager.QUIT:
            QApplication.quit()
        elif userCode == MenuManager.FULLSCREEN:
            self.window.toggleFullscreen()
        elif userCode == MenuManager.ROOT:
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

            if not Colors.noTicker:
                self.ticker.doIntroTransitions _ True
                self.tickerInAnim.setStartDelay(2000)
                self.ticker.useGuideQt()
                self.score.queueMovie('ticker', Score.NEW_ANIMATION_ONLY)
        elif userCode == MenuManager.MENU1:
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

            if not Colors.noTicker:
                self.ticker.useGuideTt()
        elif userCode == MenuManager.MENU2:
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

            if not Colors.noTicker:
                self.score.queueMovie('ticker -out', Score.NEW_ANIMATION_ONLY)
        elif userCode == MenuManager.UP:
            backMenu _ self.info[self.currentMenu]['back']
            if backMenu:
                self.score.queueMovie(self.currentMenu + ' -top_out',
                        Score.FROM_START, Score.LOCK_ITEMS)
                self.score.queueMovie(backMenu + ' -bottom_in',
                        Score.FROM_START, Score.UNLOCK_ITEMS)
                self.currentMenu _ backMenu
        elif userCode == MenuManager.DOWN:
            moreMenu _ self.info[self.currentMenu]['more']
            if moreMenu:
                self.score.queueMovie(self.currentMenu + ' -bottom_out',
                        Score.FROM_START, Score.LOCK_ITEMS)
                self.score.queueMovie(moreMenu + ' -top_in', Score.FROM_START,
                        Score.UNLOCK_ITEMS)
                self.currentMenu _ moreMenu
        elif userCode == MenuManager.BACK:
            if self.currentMenuCode == MenuManager.MENU2:
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

                if not Colors.noTicker:
                    self.ticker.doIntroTransitions _ False
                    self.tickerInAnim.setStartDelay(500)
                    self.score.queueMovie('ticker', Score.NEW_ANIMATION_ONLY)
            elif self.currentMenuCode !_ MenuManager.ROOT:
                self.itemSelected(MenuManager.ROOT, Colors.rootMenuName)

        # Update back and more buttons.
        if self.info.setdefault(self.currentMenu, {}).get('back'):
            back_state _ TextButton.OFF
        else:
            back_state _ TextButton.DISABLED

        if self.info[self.currentMenu].get('more'):
            more_state _ TextButton.OFF
        else:
            more_state _ TextButton.DISABLED

        self.upButton.setState(back_state)
        self.downButton.setState(more_state)

        if self.score.hasQueuedMovies
            self.score.playQue()
            # Playing new movies might include loading etc., so ignore the FPS
            # at this point.
            self.window.fpsHistory _ []

    ___ showDocInAssistant(self, name):
        url _ self.resolveDocUrl(name)
        Colors.debug("Sending URL to Assistant:", url)

        # Start assistant if it's not already running.
        if self.assistantProcess.state() !_ QProcess.Running:
            app _ QLibraryInfo.location(QLibraryInfo.BinariesPath) + QDir.separator()

            if sys.platform == 'darwin':
                app +_ 'Assistant.app/Contents/MacOS/Assistant'
            else:
                app +_ 'assistant'

            args _ ['-enableRemoteControl']
            self.assistantProcess.start(app, args)
            if not self.assistantProcess.waitForStarted
                QMessageBox.critical(None, "PyQt Demo",
                        "Could not start %s." % app)
                return

        # Send command through remote control even if the process was just
        # started to activate assistant and bring it to the front.
        cmd_str _ QTextStream(self.assistantProcess)
        cmd_str << 'SetSource ' << url << '\n'

    ___ launchExample(self, name):
        executable _ self.resolveExeFile(name)

        process _ QProcess(self)
        process.error.c..(self.launchError)

        if sys.platform == 'win32':
            # Make sure it finds the DLLs on Windows.
            env _ QProcessEnvironment.systemEnvironment()
            env.insert('PATH',
                    QLibraryInfo.location(QLibraryInfo.BinariesPath) + ';' +
                            env.value('PATH'))
            process.setProcessEnvironment(env)

        if self.info[name]['changedirectory'] !_ 'false':
            workingDirectory _ self.resolveDataDir(name)
            process.setWorkingDirectory(workingDirectory)
            Colors.debug("Setting working directory:", workingDirectory)

        Colors.debug("Launching:", executable)
        process.start(sys.executable, [executable])

    ___ launchQml(self, name):
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

    ___ launchError(self, error):
        if error !_ QProcess.Crashed:
            QMessageBox.critical(None, "Failed to launch the example",
                    "Could not launch the example. Ensure that it has been "
                    "built.",
                    QMessageBox.Cancel)

    ___ init(self, window):
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
        while level2Menu is not None:
            self.createSubMenu(level2Menu)

            # Create leaf menu and example info.
            example _ self._first_element(level2Menu)
            while example is not None:
                self.readInfoAboutExample(example)
                self.createLeafMenu(example)
                example _ self._next_element(example)

            level2Menu _ self._next_element(level2Menu)

    @classmethod
    ___ _first_element(cls, node):
        return cls._skip_nonelements(node.firstChild)

    @classmethod
    ___ _next_element(cls, node):
        return cls._skip_nonelements(node.nextSibling)

    @staticmethod
    ___ _skip_nonelements(node):
        while node is not None and node.nodeType !_ node.ELEMENT_NODE:
            node _ node.nextSibling

        return node

    ___ readInfoAboutExample(self, example):
        name _ example.getAttribute('name')
        if name in self.info:
            Colors.debug("__WARNING: MenuManager.readInfoAboutExample: "
                         "Demo/example with name", name, "appears twice in "
                         "the xml-file!__")

        self.info.setdefault(name, {})['filename'] _ example.getAttribute('filename')
        self.info[name]['dirname'] _ example.parentNode.getAttribute('dirname')
        self.info[name]['changedirectory'] _ example.getAttribute('changedirectory')
        self.info[name]['image'] _ example.getAttribute('image')
        self.info[name]['qml'] _ example.getAttribute('qml')

    ___ resolveDir(self, name):
        dirName _ self.info[name]['dirname']
        fileName _ self.info[name]['filename'].split('/')

        dir _ QFileInfo(__file__).dir()
        # To the 'examples' directory.
        dir.cdUp()

        dir.cd(dirName)

        if len(fileName) > 1:
            dir.cd('/'.join(fileName[:-1]))

        # This may legitimately fail if the example is just a simple .py file.
        dir.cd(fileName[-1])

        return dir

    ___ resolveDataDir(self, name):
        return self.resolveDir(name).absolutePath()

    ___ resolveExeFile(self, name):
        dir _ self.resolveDir(name)

        fileName _ self.info[name]['filename'].split('/')[-1]

        pyFile _ QFile(dir.path() + '/' + fileName + '.py')
        if pyFile.exists
            return pyFile.fileName()

        pywFile _ QFile(dir.path() + '/' + fileName + '.pyw')
        if pywFile.exists
            return pywFile.fileName()

        Colors.debug("- WARNING: Could not resolve executable:", dir.path(),
                fileName)
        return '__executable not found__'

    ___ resolveQmlFile(self, name):
        dir _ self.resolveDir(name)

        fileName _ self.info[name]['filename'].split('/')[-1]

        qmlFile _ QFile(dir.path() + '/' + fileName + '.qml')
        if qmlFile.exists
            return qmlFile.fileName()

        Colors.debug("- WARNING: Could not resolve QML file:", dir.path(),
                fileName)
        return '__QML not found__'

    ___ resolveDocUrl(self, name):
        dirName _ self.info[name]['dirname']
        fileName _ self.info[name]['filename']

        return self.helpRootUrl + dirName.replace('/', '-') + '-' + fileName + '.html'

    ___ resolveImageUrl(self, name):
        return self.helpRootUrl + 'images/' + name

    ___ getHtml(self, name):
        return self.getResource(self.resolveDocUrl(name))

    ___ getImage(self, name):
        imageName _ self.info[name]['image']
        fileName _ self.info[name]['filename']

        if self.info[name]['qml'] == 'true':
            fileName _ 'qml-' + fileName.split('/')[-1]

        if not imageName:
            imageName _ fileName + '-example.png'

            if self.getResource(self.resolveImageUrl(imageName)).isEmpty
                imageName _ fileName + '.png'

            if self.getResource(self.resolveImageUrl(imageName)).isEmpty
                imageName _ fileName + 'example.png'

        return self.getResource(self.resolveImageUrl(imageName))

    ___ createRootMenu(self, el):
        name _ el.getAttribute('name')
        self.createMenu(el, MenuManager.MENU1)
        self.createInfo(
                MenuContentItem(el, self.window.mainSceneRoot),
                name + ' -info')

        menuButtonsIn _ self.score.insertMovie(name + ' -buttons')
        menuButtonsOut _ self.score.insertMovie(name + ' -buttons -out')
        self.createLowLeftButton("Quit", MenuManager.QUIT, menuButtonsIn,
                menuButtonsOut, None)
        self.createLowRightButton("Toggle fullscreen", MenuManager.FULLSCREEN,
                menuButtonsIn, menuButtonsOut, None)

    ___ createSubMenu(self, el):
        name _ el.getAttribute('name')
        self.createMenu(el, MenuManager.MENU2)
        self.createInfo(
                MenuContentItem(el, self.window.mainSceneRoot),
                name + ' -info')

    ___ createLeafMenu(self, el):
        name _ el.getAttribute('name')
        self.createInfo(ExampleContent(name, self.window.mainSceneRoot), name)

        infoButtonsIn _ self.score.insertMovie(name + ' -buttons')
        infoButtonsOut _ self.score.insertMovie(name + ' -buttons -out')
        self.createLowRightLeafButton("Documentation", 600,
                MenuManager.DOCUMENTATION, infoButtonsIn, infoButtonsOut, None)
        if el.getAttribute('executable') !_ 'false':
            self.createLowRightLeafButton("Launch", 405, MenuManager.LAUNCH,
                    infoButtonsIn, infoButtonsOut, None)
        elif el.getAttribute('qml') == 'true':
            self.createLowRightLeafButton("Display", 405,
                    MenuManager.LAUNCH_QML, infoButtonsIn, infoButtonsOut,
                    None)

    ___ createMenu(self, category, type):
        sw _ self.window.scene.sceneRect().width()
        xOffset _ 15
        yOffset _ 10
        maxExamples _ Colors.menuCount
        menuIndex _ 1
        name _ category.getAttribute('name')
        currentNode _ self._first_element(category)
        currentMenu _ '%s -menu%d' % (name, menuIndex)

        while currentNode is not None:
            movieIn _ self.score.insertMovie(currentMenu)
            movieOut _ self.score.insertMovie(currentMenu + ' -out')
            movieNextTopOut _ self.score.insertMovie(currentMenu + ' -top_out')
            movieNextBottomOut _ self.score.insertMovie(currentMenu + ' -bottom_out')
            movieNextTopIn _ self.score.insertMovie(currentMenu + ' -top_in')
            movieNextBottomIn _ self.score.insertMovie(currentMenu + ' -bottom_in')
            movieShake _ self.score.insertMovie(currentMenu + ' -shake')

            i _ 0
            while currentNode is not None and i < maxExamples:
                # Create a normal menu button.
                label _ currentNode.getAttribute('name')
                item _ TextButton(label, TextButton.LEFT, type,
                        self.window.mainSceneRoot)

                item.setRecursiveVisible(False)
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
                movieIn.append(anim)

                # Create out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished(True)
                anim.setDuration(700 + (30 * i))
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.60, QPointF(xOffset, 600 - ih - ih))
                anim.setKeyValueAt(0.65, QPointF(xOffset + 20, 600 - ih))
                anim.setEndValue(QPointF(sw + iw, 600 - ih))
                movieOut.append(anim)

                # Create shake-animation.
                anim _ DemoItemAnimation(item)
                anim.setDuration(700)
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.55, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY - i*2.0))
                anim.setKeyValueAt(0.70, QPointF(xOffset - 10, (i * ihp) + yOffset + Colors.contentStartY - i*1.5))
                anim.setKeyValueAt(0.80, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY - i*1.0))
                anim.setKeyValueAt(0.90, QPointF(xOffset - 2, (i * ihp) + yOffset + Colors.contentStartY - i*0.5))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieShake.append(anim)

                # Create next-menu top-out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished(True)
                anim.setDuration(200 + (30 * i))
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.70, QPointF(xOffset, yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(-iw, yOffset + Colors.contentStartY))
                movieNextTopOut.append(anim)

                # Create next-menu bottom-out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished(True)
                anim.setDuration(200 + (30 * i))
                anim.setStartValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.70, QPointF(xOffset, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(-iw, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                movieNextBottomOut.append(anim)

                # Create next-menu top-in-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.setDuration(700 - (30 * i))
                anim.setStartValue(QPointF(-iw, yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.30, QPointF(xOffset, yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieNextTopIn.append(anim)

                # Create next-menu bottom-in-animation.
                reverse _ maxExamples - i
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.setDuration(1000 - (30 * reverse))
                anim.setStartValue(QPointF(-iw, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.setKeyValueAt(0.30, QPointF(xOffset, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.setEndValue(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieNextBottomIn.append(anim)

                i +_ 1
                currentNode _ self._next_element(currentNode)

            if currentNode is not None and i == maxExamples:
                # We need another menu, so register for 'more' and 'back'
                # buttons.
                menuIndex +_ 1
                self.info.setdefault(currentMenu, {})['more'] _ '%s -menu%d' % (name, menuIndex)
                currentMenu _ '%s -menu%d' % (name, menuIndex)
                self.info.setdefault(currentMenu, {})['back'] _ '%s -menu%d' % (name, menuIndex - 1)

    ___ createLowLeftButton(self, label, type, movieIn, movieOut, movieShake, menuString_""):
        button _ TextButton(label, TextButton.RIGHT, type,
                self.window.mainSceneRoot, TextButton.PANEL)
        if menuString:
            button.setMenuString(menuString)
        button.setRecursiveVisible(False)
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
        movieIn.append(buttonIn)

        # Create out-animation.
        buttonOut _ DemoItemAnimation(button, DemoItemAnimation.ANIM_OUT)
        buttonOut.setHideOnFinished(True)
        buttonOut.setDuration(400)
        buttonOut.setStartValue(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        buttonOut.setEndValue(QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 26))
        movieOut.append(buttonOut)

        if movieShake is not None:
            shakeAnim _ DemoItemAnimation(button, DemoItemAnimation.ANIM_UNSPECIFIED)
            shakeAnim.setDuration(650)
            shakeAnim.setStartValue(buttonIn.endValue())
            shakeAnim.setKeyValueAt(0.60, buttonIn.endValue())
            shakeAnim.setKeyValueAt(0.70, buttonIn.endValue() + QPointF(-3, 0))
            shakeAnim.setKeyValueAt(0.80, buttonIn.endValue() + QPointF(2, 0))
            shakeAnim.setKeyValueAt(0.90, buttonIn.endValue() + QPointF(-1, 0))
            shakeAnim.setEndValue(buttonIn.endValue())
            movieShake.append(shakeAnim)

    ___ createLowRightButton(self, label, type, movieIn, movieOut, movieShake):
        item _ TextButton(label, TextButton.RIGHT, type,
                self.window.mainSceneRoot, TextButton.PANEL)
        item.setRecursiveVisible(False)
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
        movieIn.append(anim)

        # Create out-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        anim.setHideOnFinished(True)
        anim.setDuration(400)
        anim.setStartValue(QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 26))
        anim.setEndValue(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 26))
        movieOut.append(anim)

    ___ createLowRightLeafButton(self, label, xOffset, type, movieIn, movieOut, movieShake):
        item _ TextButton(label, TextButton.RIGHT, type,
                self.window.mainSceneRoot, TextButton.PANEL)
        item.setRecursiveVisible(False)
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
        movieIn.append(anim)

        # Create out-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        anim.setHideOnFinished(True)
        anim.setDuration(300)
        anim.setStartValue(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        anim.setEndValue(QPointF(xOffset, sh))
        movieOut.append(anim)

    ___ createInfo(self, item, name):
        movie_in _ self.score.insertMovie(name)
        movie_out _ self.score.insertMovie(name + ' -out')
        item.setZValue(8)
        item.setRecursiveVisible(False)

        xOffset _ 230.0
        infoIn _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        infoIn.setDuration(650)
        infoIn.setStartValue(QPointF(self.window.scene.sceneRect().width(), Colors.contentStartY))
        infoIn.setKeyValueAt(0.60, QPointF(xOffset, Colors.contentStartY))
        infoIn.setKeyValueAt(0.70, QPointF(xOffset + 20, Colors.contentStartY))
        infoIn.setKeyValueAt(0.80, QPointF(xOffset, Colors.contentStartY))
        infoIn.setKeyValueAt(0.90, QPointF(xOffset + 7, Colors.contentStartY))
        infoIn.setEndValue(QPointF(xOffset, Colors.contentStartY))
        movie_in.append(infoIn)

        infoOut _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        infoOut.setCurveShape(QEasingCurve.InQuad)
        infoOut.setDuration(300)
        infoOut.setHideOnFinished(True)
        infoOut.setStartValue(QPointF(xOffset, Colors.contentStartY))
        infoOut.setEndValue(QPointF(-600, Colors.contentStartY))
        movie_out.append(infoOut)

    ___ createTicker(self):
        if Colors.noTicker:
            return

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
        movie_in.append(self.tickerInAnim)

        # Move ticker out.
        qtOut _ DemoItemAnimation(self.ticker, DemoItemAnimation.ANIM_OUT)
        qtOut.setHideOnFinished(True)
        qtOut.setDuration(500)
        qtOut.setStartValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtOut.setEndValue(QPointF(self.window.scene.sceneRect().width() + 700, Colors.contentStartY + qtPosY))
        movie_out.append(qtOut)

        # Move ticker in on activate.
        qtActivate _ DemoItemAnimation(self.ticker)
        qtActivate.setDuration(400)
        qtActivate.setStartValue(QPointF(self.window.scene.sceneRect().width(), Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.60, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.70, QPointF(qtendpos + 30, Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.80, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtActivate.setKeyValueAt(0.90, QPointF(qtendpos + 5, Colors.contentStartY + qtPosY))
        qtActivate.setEndValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        movie_activate.append(qtActivate)

        # Move ticker out on deactivate.
        qtDeactivate _ DemoItemAnimation(self.ticker)
        qtDeactivate.setHideOnFinished(True)
        qtDeactivate.setDuration(400)
        qtDeactivate.setStartValue(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtDeactivate.setEndValue(QPointF(qtendpos, 800))
        movie_deactivate.append(qtDeactivate)

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
        movieShake.append(shakeAnim)

        shakeAnim _ DemoItemAnimation(self.downButton,
                DemoItemAnimation.ANIM_UNSPECIFIED)
        shakeAnim.setDuration(650)
        shakeAnim.setStartValue(self.downButton.pos())
        shakeAnim.setKeyValueAt(0.60, self.downButton.pos())
        shakeAnim.setKeyValueAt(0.70, self.downButton.pos() + QPointF(-5, 0))
        shakeAnim.setKeyValueAt(0.80, self.downButton.pos() + QPointF(-3, 0))
        shakeAnim.setKeyValueAt(0.90, self.downButton.pos() + QPointF(-1, 0))
        shakeAnim.setEndValue(self.downButton.pos())
        movieShake.append(shakeAnim)

    ___ createBackButton(self):
        backIn _ self.score.insertMovie('back -in')
        backOut _ self.score.insertMovie('back -out')
        backShake _ self.score.insertMovie('back -shake')
        self.createLowLeftButton("Back", MenuManager.ROOT, backIn, backOut,
                backShake, Colors.rootMenuName)
