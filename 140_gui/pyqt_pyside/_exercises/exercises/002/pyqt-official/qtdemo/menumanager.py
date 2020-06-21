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

____ ?.?C.. ______ (QByteArray, ?D.., QEasingCurve, QFile, QFileInfo,
        QLibraryInfo, ?O.., QPointF, QProcess, QProcessEnvironment,
        QStandardPaths, __, QT_VERSION, QT_VERSION_STR, QTextStream, ?U..)
____ ?.?W.. ______ ?A.., ?MB..

____ colors ______ Colors
____ demoitemanimation ______ DemoItemAnimation
____ examplecontent ______ ExampleContent
____ itemcircleanimation ______ ItemCircleAnimation
____ menucontent ______ MenuContentItem
____ score ______ Score
____ textbutton ______ TextButton


c_ MenuManager(?O..):
    ROOT, MENU1, MENU2, LAUNCH, DOCUMENTATION, QUIT, FULLSCREEN, UP, DOWN, \
            BACK, LAUNCH_QML _ ra..(11)

    pInstance _ N..

    ___  - 
        s__(MenuManager, self). - ()

        contentsDoc _ N..
        assistantProcess _ QProcess()
        helpRootUrl _ ''
        docDir _ ?D..()
        imgDir _ ?D..()

        info _   # dict
        window _ N..

        ticker _ N..
        tickerInAnim _ N..
        upButton _ N..
        downButton _ N..
        score _ Score()
        currentMenu _ "[no menu visible]"
        currentCategory _ "[no category visible]"
        currentMenuButtons _ "[no menu buttons visible]"
        currentInfo _ "[no info visible]"
        currentMenuCode _ -1
        readXmlDocument()

    @classmethod
    ___ instance(cls):
        __ cls.pInstance __ N..:
            cls.pInstance _ cls()

        r_ cls.pInstance

    ___ getResource  name):
        r_ QByteArray()

    ___ readXmlDocument
        root _ QFileInfo(__file__).absolutePath()
        xml_file _ QFile(root + '/examples.xml')
        xml_file.o..(QFile.ReadOnly | QFile.Text)
        contents _ xml_file.rA...data()
        xml_file.c..

        contentsDoc _ parseString(contents)

    ___ itemSelected  userCode, menuName):
        __ userCode __ MenuManager.LAUNCH:
            launchExample(currentInfo)
        ____ userCode __ MenuManager.LAUNCH_QML:
            launchQml(currentInfo)
        ____ userCode __ MenuManager.DOCUMENTATION:
            showDocInAssistant(currentInfo)
        ____ userCode __ MenuManager.QUIT:
            ?A...quit()
        ____ userCode __ MenuManager.FULLSCREEN:
            window.toggleFullscreen()
        ____ userCode __ MenuManager.ROOT:
            # Out.
            score.queueMovie(currentMenu + ' -out', Score.FROM_START,
                    Score.LOCK_ITEMS)
            score.queueMovie(currentMenuButtons + ' -out',
                    Score.FROM_START, Score.LOCK_ITEMS)
            score.queueMovie(currentInfo + ' -out')
            score.queueMovie(currentInfo + ' -buttons -out',
                    Score.NEW_ANIMATION_ONLY)
            score.queueMovie('back -out', Score.ONLY_IF_VISIBLE)

            # Book-keeping.
            currentMenuCode _ MenuManager.ROOT
            currentMenu _ menuName + ' -menu1'
            currentMenuButtons _ menuName + ' -buttons'
            currentInfo _ menuName + ' -info'

            # In.
            score.queueMovie('upndown -shake')
            score.queueMovie(currentMenu, Score.FROM_START,
                    Score.UNLOCK_ITEMS)
            score.queueMovie(currentMenuButtons, Score.FROM_START,
                    Score.UNLOCK_ITEMS)
            score.queueMovie(currentInfo)

            __ no. Colors.noTicker:
                ticker.doIntroTransitions _ T..
                tickerInAnim.setStartDelay(2000)
                ticker.useGuideQt()
                score.queueMovie('ticker', Score.NEW_ANIMATION_ONLY)
        ____ userCode __ MenuManager.MENU1:
            # Out.
            score.queueMovie(currentMenu + ' -out', Score.FROM_START,
                    Score.LOCK_ITEMS)
            score.queueMovie(currentMenuButtons + ' -out',
                    Score.FROM_START, Score.LOCK_ITEMS)
            score.queueMovie(currentInfo + ' -out')

            # Book-keeping.
            currentMenuCode _ MenuManager.MENU1
            currentCategory _ menuName
            currentMenu _ menuName + ' -menu1'
            currentInfo _ menuName + ' -info'

            # In.
            score.queueMovie('upndown -shake')
            score.queueMovie('back -in')
            score.queueMovie(currentMenu, Score.FROM_START,
                    Score.UNLOCK_ITEMS)
            score.queueMovie(currentInfo)

            __ no. Colors.noTicker:
                ticker.useGuideTt()
        ____ userCode __ MenuManager.MENU2:
            # Out.
            score.queueMovie(currentInfo + ' -out',
                    Score.NEW_ANIMATION_ONLY)
            score.queueMovie(currentInfo + ' -buttons -out',
                    Score.NEW_ANIMATION_ONLY)

            # Book-keeping.
            currentMenuCode _ MenuManager.MENU2
            currentInfo _ menuName

            # In/shake.
            score.queueMovie('upndown -shake')
            score.queueMovie('back -shake')
            score.queueMovie(currentMenu + ' -shake')
            score.queueMovie(currentInfo, Score.NEW_ANIMATION_ONLY)
            score.queueMovie(currentInfo + ' -buttons',
                    Score.NEW_ANIMATION_ONLY)

            __ no. Colors.noTicker:
                score.queueMovie('ticker -out', Score.NEW_ANIMATION_ONLY)
        ____ userCode __ MenuManager.UP:
            backMenu _ info[currentMenu]['back']
            __ backMenu:
                score.queueMovie(currentMenu + ' -top_out',
                        Score.FROM_START, Score.LOCK_ITEMS)
                score.queueMovie(backMenu + ' -bottom_in',
                        Score.FROM_START, Score.UNLOCK_ITEMS)
                currentMenu _ backMenu
        ____ userCode __ MenuManager.DOWN:
            moreMenu _ i..[currentMenu]['more']
            __ moreMenu:
                score.queueMovie(currentMenu + ' -bottom_out',
                        Score.FROM_START, Score.LOCK_ITEMS)
                score.queueMovie(moreMenu + ' -top_in', Score.FROM_START,
                        Score.UNLOCK_ITEMS)
                currentMenu _ moreMenu
        ____ userCode __ MenuManager.BACK:
            __ currentMenuCode __ MenuManager.MENU2:
                # Out.
                score.queueMovie(currentInfo + ' -out',
                        Score.NEW_ANIMATION_ONLY)
                score.queueMovie(currentInfo + ' -buttons -out',
                        Score.NEW_ANIMATION_ONLY)

                # Book-keeping.
                currentMenuCode _ MenuManager.MENU1
                currentMenuButtons _ currentCategory + ' -buttons'
                currentInfo _ currentCategory + ' -info'

                # In/shake.
                score.queueMovie('upndown -shake')
                score.queueMovie(currentMenu + ' -shake')
                score.queueMovie(currentInfo,
                        Score.NEW_ANIMATION_ONLY)
                score.queueMovie(currentInfo + ' -buttons',
                        Score.NEW_ANIMATION_ONLY)

                __ no. Colors.noTicker:
                    ticker.doIntroTransitions _ F..
                    tickerInAnim.setStartDelay(500)
                    score.queueMovie('ticker', Score.NEW_ANIMATION_ONLY)
            ____ currentMenuCode !_ MenuManager.ROOT:
                itemSelected(MenuManager.ROOT, Colors.rootMenuName)

        # Update back and more buttons.
        __ i...setdefault(currentMenu,   # dict).g..('back'):
            back_state _ TextButton.OFF
        ____
            back_state _ TextButton.DISABLED

        __ i..[currentMenu].g..('more'):
            more_state _ TextButton.OFF
        ____
            more_state _ TextButton.DISABLED

        upButton.setState(back_state)
        downButton.setState(more_state)

        __ score.hasQueuedMovies
            score.playQue()
            # Playing new movies might include loading etc., so ignore the FPS
            # at this point.
            window.fpsHistory _   # list

    ___ showDocInAssistant  name):
        url _ resolveDocUrl(name)
        Colors.debug("Sending URL to Assistant:", url)

        # Start assistant if it's not already running.
        __ assistantProcess.s.. !_ QProcess.Running:
            app _ QLibraryInfo.location(QLibraryInfo.BinariesPath) + ?D...separator()

            __ ___.platform __ 'darwin':
                app +_ 'Assistant.app/Contents/MacOS/Assistant'
            ____
                app +_ 'assistant'

            args _ ['-enableRemoteControl']
            assistantProcess.start ?, args)
            __ no. assistantProcess.waitForStarted
                ?MB...c..(N.., "PyQt Demo",
                        "Could not start %s." % app)
                r_

        # Send command through remote control even if the process was just
        # started to activate assistant and bring it to the front.
        cmd_str _ QTextStream(assistantProcess)
        cmd_str << 'SetSource ' << url << '\n'

    ___ launchExample  name):
        executable _ resolveExeFile(name)

        process _ QProcess
        process.error.c..(launchError)

        __ ___.platform __ 'win32':
            # Make sure it finds the DLLs on Windows.
            env _ QProcessEnvironment.systemEnvironment()
            env.insert('PATH',
                    QLibraryInfo.location(QLibraryInfo.BinariesPath) + ';' +
                            env.value('PATH'))
            process.setProcessEnvironment(env)

        __ i..[name]['changedirectory'] !_ 'false':
            workingDirectory _ resolveDataDir(name)
            process.setWorkingDirectory(workingDirectory)
            Colors.debug("Setting working directory:", workingDirectory)

        Colors.debug("Launching:", executable)
        process.start(___.executable, [executable])

    ___ launchQml  name):
        import_path _ resolveDataDir(name)
        qml _ resolveQmlFile(name)

        process _ QProcess
        process.error.c..(launchError)

        env _ QProcessEnvironment.systemEnvironment()
        env.insert('QML2_IMPORT_PATH', import_path)
        process.setProcessEnvironment(env)

        executable _ QLibraryInfo.location(QLibraryInfo.BinariesPath) + '/qmlscene'
        Colors.debug("Launching:", executable)
        process.start(executable, [qml])

    ___ launchError  error):
        __ error !_ QProcess.Crashed:
            ?MB...c..(N.., "Failed to launch the example",
                    "Could not launch the example. Ensure that it has been "
                    "built.",
                    ?MB...Cancel)

    ___ init  window):
        window _ window

        # Create div.
        createTicker()
        createUpnDownButtons()
        createBackButton()

        # Create first level menu.
        rootElement _ contentsDoc.documentElement
        createRootMenu(rootElement)

        # Create second level menus.
        level2Menu _ _first_element(rootElement)
        w__ level2Menu __ no. N..:
            createSubMenu(level2Menu)

            # Create leaf menu and example info.
            example _ _first_element(level2Menu)
            w__ example __ no. N..:
                readInfoAboutExample(example)
                createLeafMenu(example)
                example _ _next_element(example)

            level2Menu _ _next_element(level2Menu)

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
        __ name __ info:
            Colors.debug("__WARNING: MenuManager.readInfoAboutExample: "
                         "Demo/example with name", name, "appears twice in "
                         "the xml-file!__")

        info.setdefault(name,   # dict)['filename'] _ example.getAttribute('filename')
        info[name]['dirname'] _ example.parentNode.getAttribute('dirname')
        info[name]['changedirectory'] _ example.getAttribute('changedirectory')
        info[name]['image'] _ example.getAttribute('image')
        info[name]['qml'] _ example.getAttribute('qml')

    ___ resolveDir  name):
        dirName _ info[name]['dirname']
        fileName _ info[name]['filename'].sp..('/')

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
        r_ resolveDir(name).absolutePath()

    ___ resolveExeFile  name):
        dir _ resolveDir(name)

        fileName _ info[name]['filename'].sp..('/')[-1]

        pyFile _ QFile(dir.pa__() + '/' + fileName + '.py')
        __ pyFile.e..
            r_ pyFile.fN..

        pywFile _ QFile(dir.pa__() + '/' + fileName + '.pyw')
        __ pywFile.e..
            r_ pywFile.fN..

        Colors.debug("- WARNING: Could not resolve executable:", dir.pa__(),
                fileName)
        r_ '__executable not found__'

    ___ resolveQmlFile  name):
        dir _ resolveDir(name)

        fileName _ info[name]['filename'].sp..('/')[-1]

        qmlFile _ QFile(dir.pa__() + '/' + fileName + '.qml')
        __ qmlFile.e..
            r_ qmlFile.fN..

        Colors.debug("- WARNING: Could not resolve QML file:", dir.pa__(),
                fileName)
        r_ '__QML not found__'

    ___ resolveDocUrl  name):
        dirName _ info[name]['dirname']
        fileName _ info[name]['filename']

        r_ helpRootUrl + dirName.replace('/', '-') + '-' + fileName + '.html'

    ___ resolveImageUrl  name):
        r_ helpRootUrl + 'images/' + name

    ___ getHtml  name):
        r_ getResource(resolveDocUrl(name))

    ___ getImage  name):
        imageName _ info[name]['image']
        fileName _ info[name]['filename']

        __ info[name]['qml'] __ 'true':
            fileName _ 'qml-' + fileName.sp..('/')[-1]

        __ no. imageName:
            imageName _ fileName + '-example.png'

            __ getResource(resolveImageUrl(imageName)).isEmpty
                imageName _ fileName + '.png'

            __ getResource(resolveImageUrl(imageName)).isEmpty
                imageName _ fileName + 'example.png'

        r_ getResource(resolveImageUrl(imageName))

    ___ createRootMenu  el):
        name _ el.getAttribute('name')
        createMenu(el, MenuManager.MENU1)
        createInfo(
                MenuContentItem(el, window.mainSceneRoot),
                name + ' -info')

        menuButtonsIn _ score.insertMovie(name + ' -buttons')
        menuButtonsOut _ score.insertMovie(name + ' -buttons -out')
        createLowLeftButton("Quit", MenuManager.QUIT, menuButtonsIn,
                menuButtonsOut, N..)
        createLowRightButton("Toggle fullscreen", MenuManager.FULLSCREEN,
                menuButtonsIn, menuButtonsOut, N..)

    ___ createSubMenu  el):
        name _ el.getAttribute('name')
        createMenu(el, MenuManager.MENU2)
        createInfo(
                MenuContentItem(el, window.mainSceneRoot),
                name + ' -info')

    ___ createLeafMenu  el):
        name _ el.getAttribute('name')
        createInfo(ExampleContent(name, window.mainSceneRoot), name)

        infoButtonsIn _ score.insertMovie(name + ' -buttons')
        infoButtonsOut _ score.insertMovie(name + ' -buttons -out')
        createLowRightLeafButton("Documentation", 600,
                MenuManager.DOCUMENTATION, infoButtonsIn, infoButtonsOut, N..)
        __ el.getAttribute('executable') !_ 'false':
            createLowRightLeafButton("Launch", 405, MenuManager.LAUNCH,
                    infoButtonsIn, infoButtonsOut, N..)
        ____ el.getAttribute('qml') __ 'true':
            createLowRightLeafButton("Display", 405,
                    MenuManager.LAUNCH_QML, infoButtonsIn, infoButtonsOut,
                    N..)

    ___ createMenu  category, type):
        sw _ window.scene.sceneRect().width()
        xOffset _ 15
        yOffset _ 10
        maxExamples _ Colors.menuCount
        menuIndex _ 1
        name _ category.getAttribute('name')
        currentNode _ _first_element(category)
        currentMenu _ '%s -menu%d' % (name, menuIndex)

        w__ currentNode __ no. N..:
            movieIn _ score.insertMovie(currentMenu)
            movieOut _ score.insertMovie(currentMenu + ' -out')
            movieNextTopOut _ score.insertMovie(currentMenu + ' -top_out')
            movieNextBottomOut _ score.insertMovie(currentMenu + ' -bottom_out')
            movieNextTopIn _ score.insertMovie(currentMenu + ' -top_in')
            movieNextBottomIn _ score.insertMovie(currentMenu + ' -bottom_in')
            movieShake _ score.insertMovie(currentMenu + ' -shake')

            i _ 0
            w__ currentNode __ no. N.. and i < maxExamples:
                # Create a normal menu button.
                label _ currentNode.getAttribute('name')
                item _ TextButton(label, TextButton.LEFT, type,
                        window.mainSceneRoot)

                item.setRecursiveVisible F..
                item.setZValue(10)
                ih _ item.sceneBoundingRect().height()
                iw _ item.sceneBoundingRect().width()
                ihp _ ih + 3

                # Create in-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.sD..(1000 + (i * 20))
                anim.sSV..(QPointF(xOffset, -ih))
                anim.sKVA..(0.20, QPointF(xOffset, -ih))
                anim.sKVA..(0.50, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY + (10 * fl..(i / 4.0))))
                anim.sKVA..(0.60, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.70, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY + (5 * fl..(i / 4.0))))
                anim.sKVA..(0.80, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.90, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY + (2 * fl..(i / 4.0))))
                anim.sEV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieIn.ap..(anim)

                # Create out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished( st.
                anim.sD..(700 + (30 * i))
                anim.sSV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.60, QPointF(xOffset, 600 - ih - ih))
                anim.sKVA..(0.65, QPointF(xOffset + 20, 600 - ih))
                anim.sEV..(QPointF(sw + iw, 600 - ih))
                movieOut.ap..(anim)

                # Create shake-animation.
                anim _ DemoItemAnimation(item)
                anim.sD..(700)
                anim.sSV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.55, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY - i*2.0))
                anim.sKVA..(0.70, QPointF(xOffset - 10, (i * ihp) + yOffset + Colors.contentStartY - i*1.5))
                anim.sKVA..(0.80, QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY - i*1.0))
                anim.sKVA..(0.90, QPointF(xOffset - 2, (i * ihp) + yOffset + Colors.contentStartY - i*0.5))
                anim.sEV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieShake.ap..(anim)

                # Create next-menu top-out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished( st.
                anim.sD..(200 + (30 * i))
                anim.sSV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.70, QPointF(xOffset, yOffset + Colors.contentStartY))
                anim.sEV..(QPointF(-iw, yOffset + Colors.contentStartY))
                movieNextTopOut.ap..(anim)

                # Create next-menu bottom-out-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
                anim.setHideOnFinished( st.
                anim.sD..(200 + (30 * i))
                anim.sSV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.70, QPointF(xOffset, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.sEV..(QPointF(-iw, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                movieNextBottomOut.ap..(anim)

                # Create next-menu top-in-animation.
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.sD..(700 - (30 * i))
                anim.sSV..(QPointF(-iw, yOffset + Colors.contentStartY))
                anim.sKVA..(0.30, QPointF(xOffset, yOffset + Colors.contentStartY))
                anim.sEV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieNextTopIn.ap..(anim)

                # Create next-menu bottom-in-animation.
                reverse _ maxExamples - i
                anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
                anim.sD..(1000 - (30 * reverse))
                anim.sSV..(QPointF(-iw, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.sKVA..(0.30, QPointF(xOffset, (maxExamples * ihp) + yOffset + Colors.contentStartY))
                anim.sEV..(QPointF(xOffset, (i * ihp) + yOffset + Colors.contentStartY))
                movieNextBottomIn.ap..(anim)

                i +_ 1
                currentNode _ _next_element(currentNode)

            __ currentNode __ no. N.. and i __ maxExamples:
                # We need another menu, so register for 'more' and 'back'
                # buttons.
                menuIndex +_ 1
                info.setdefault(currentMenu,   # dict)['more'] _ '%s -menu%d' % (name, menuIndex)
                currentMenu _ '%s -menu%d' % (name, menuIndex)
                info.setdefault(currentMenu,   # dict)['back'] _ '%s -menu%d' % (name, menuIndex - 1)

    ___ createLowLeftButton  label, type, movieIn, movieOut, movieShake, menuString_""):
        button _ TextButton(label, TextButton.RIGHT, type,
                window.mainSceneRoot, TextButton.PANEL)
        __ menuString:
            button.setMenuString(menuString)
        button.setRecursiveVisible F..
        button.setZValue(10)

        iw _ button.sceneBoundingRect().width()
        xOffset _ 15

        # Create in-animation.
        buttonIn _ DemoItemAnimation(button, DemoItemAnimation.ANIM_IN)
        buttonIn.sD..(1800)
        buttonIn.sSV..(QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 35))
        buttonIn.sKVA..(0.5, QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 35))
        buttonIn.sKVA..(0.7, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        buttonIn.sEV..(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        movieIn.ap..(buttonIn)

        # Create out-animation.
        buttonOut _ DemoItemAnimation(button, DemoItemAnimation.ANIM_OUT)
        buttonOut.setHideOnFinished( st.
        buttonOut.sD..(400)
        buttonOut.sSV..(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        buttonOut.sEV..(QPointF(-iw, Colors.contentStartY + Colors.contentHeight - 26))
        movieOut.ap..(buttonOut)

        __ movieShake __ no. N..:
            shakeAnim _ DemoItemAnimation(button, DemoItemAnimation.ANIM_UNSPECIFIED)
            shakeAnim.sD..(650)
            shakeAnim.sSV..(buttonIn.endValue())
            shakeAnim.sKVA..(0.60, buttonIn.endValue())
            shakeAnim.sKVA..(0.70, buttonIn.endValue() + QPointF(-3, 0))
            shakeAnim.sKVA..(0.80, buttonIn.endValue() + QPointF(2, 0))
            shakeAnim.sKVA..(0.90, buttonIn.endValue() + QPointF(-1, 0))
            shakeAnim.sEV..(buttonIn.endValue())
            movieShake.ap..(shakeAnim)

    ___ createLowRightButton  label, type, movieIn, movieOut, movieShake):
        item _ TextButton(label, TextButton.RIGHT, type,
                window.mainSceneRoot, TextButton.PANEL)
        item.setRecursiveVisible F..
        item.setZValue(10)

        sw _ window.scene.sceneRect().width()
        xOffset _ 70

        # Create in-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        anim.sD..(1800)
        anim.sSV..(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.5, QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.7, QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sEV..(QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 26))
        movieIn.ap..(anim)

        # Create out-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        anim.setHideOnFinished( st.
        anim.sD..(400)
        anim.sSV..(QPointF(xOffset + 535, Colors.contentStartY + Colors.contentHeight - 26))
        anim.sEV..(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 26))
        movieOut.ap..(anim)

    ___ createLowRightLeafButton  label, xOffset, type, movieIn, movieOut, movieShake):
        item _ TextButton(label, TextButton.RIGHT, type,
                window.mainSceneRoot, TextButton.PANEL)
        item.setRecursiveVisible F..
        item.setZValue(10)

        sw _ window.scene.sceneRect().width()
        sh _ window.scene.sceneRect().height()

        # Create in-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        anim.sD..(1050)
        anim.sSV..(QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.10, QPointF(sw, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.30, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.35, QPointF(xOffset + 30, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.40, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.45, QPointF(xOffset + 5, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sKVA..(0.50, QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 35))
        anim.sEV..(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        movieIn.ap..(anim)

        # Create out-animation.
        anim _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        anim.setHideOnFinished( st.
        anim.sD..(300)
        anim.sSV..(QPointF(xOffset, Colors.contentStartY + Colors.contentHeight - 26))
        anim.sEV..(QPointF(xOffset, sh))
        movieOut.ap..(anim)

    ___ createInfo  item, name):
        movie_in _ score.insertMovie(name)
        movie_out _ score.insertMovie(name + ' -out')
        item.setZValue(8)
        item.setRecursiveVisible F..

        xOffset _ 230.0
        infoIn _ DemoItemAnimation(item, DemoItemAnimation.ANIM_IN)
        infoIn.sD..(650)
        infoIn.sSV..(QPointF(window.scene.sceneRect().width(), Colors.contentStartY))
        infoIn.sKVA..(0.60, QPointF(xOffset, Colors.contentStartY))
        infoIn.sKVA..(0.70, QPointF(xOffset + 20, Colors.contentStartY))
        infoIn.sKVA..(0.80, QPointF(xOffset, Colors.contentStartY))
        infoIn.sKVA..(0.90, QPointF(xOffset + 7, Colors.contentStartY))
        infoIn.sEV..(QPointF(xOffset, Colors.contentStartY))
        movie_in.ap..(infoIn)

        infoOut _ DemoItemAnimation(item, DemoItemAnimation.ANIM_OUT)
        infoOut.setCurveShape(QEasingCurve.InQuad)
        infoOut.sD..(300)
        infoOut.setHideOnFinished( st.
        infoOut.sSV..(QPointF(xOffset, Colors.contentStartY))
        infoOut.sEV..(QPointF(-600, Colors.contentStartY))
        movie_out.ap..(infoOut)

    ___ createTicker
        __ Colors.noTicker:
            r_

        movie_in _ score.insertMovie('ticker')
        movie_out _ score.insertMovie('ticker -out')
        movie_activate _ score.insertMovie('ticker -activate')
        movie_deactivate _ score.insertMovie('ticker -deactivate')

        ticker _ ItemCircleAnimation()
        ticker.setZValue(50)
        ticker.hide()

        # Move ticker in.
        qtendpos _ 485
        qtPosY _ 120
        tickerInAnim _ DemoItemAnimation(ticker,
                DemoItemAnimation.ANIM_IN)
        tickerInAnim.sD..(500)
        tickerInAnim.sSV..(QPointF(window.scene.sceneRect().width(), Colors.contentStartY + qtPosY))
        tickerInAnim.sKVA..(0.60, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        tickerInAnim.sKVA..(0.70, QPointF(qtendpos + 30, Colors.contentStartY + qtPosY))
        tickerInAnim.sKVA..(0.80, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        tickerInAnim.sKVA..(0.90, QPointF(qtendpos + 5, Colors.contentStartY + qtPosY))
        tickerInAnim.sEV..(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        movie_in.ap..(tickerInAnim)

        # Move ticker out.
        qtOut _ DemoItemAnimation(ticker, DemoItemAnimation.ANIM_OUT)
        qtOut.setHideOnFinished( st.
        qtOut.sD..(500)
        qtOut.sSV..(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtOut.sEV..(QPointF(window.scene.sceneRect().width() + 700, Colors.contentStartY + qtPosY))
        movie_out.ap..(qtOut)

        # Move ticker in on activate.
        qtActivate _ DemoItemAnimation(ticker)
        qtActivate.sD..(400)
        qtActivate.sSV..(QPointF(window.scene.sceneRect().width(), Colors.contentStartY + qtPosY))
        qtActivate.sKVA..(0.60, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtActivate.sKVA..(0.70, QPointF(qtendpos + 30, Colors.contentStartY + qtPosY))
        qtActivate.sKVA..(0.80, QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtActivate.sKVA..(0.90, QPointF(qtendpos + 5, Colors.contentStartY + qtPosY))
        qtActivate.sEV..(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        movie_activate.ap..(qtActivate)

        # Move ticker out on deactivate.
        qtDeactivate _ DemoItemAnimation(ticker)
        qtDeactivate.setHideOnFinished( st.
        qtDeactivate.sD..(400)
        qtDeactivate.sSV..(QPointF(qtendpos, Colors.contentStartY + qtPosY))
        qtDeactivate.sEV..(QPointF(qtendpos, 800))
        movie_deactivate.ap..(qtDeactivate)

    ___ createUpnDownButtons
        xOffset _ 15.0
        yOffset _ 450.0

        upButton _ TextButton("", TextButton.LEFT, MenuManager.UP,
                window.mainSceneRoot, TextButton.UP)
        upButton.prepare()
        upButton.setPos(xOffset, yOffset)
        upButton.setState(TextButton.DISABLED)

        downButton _ TextButton("", TextButton.LEFT, MenuManager.DOWN,
                window.mainSceneRoot, TextButton.DOWN)
        downButton.prepare()
        downButton.setPos(xOffset + 10 + downButton.sceneBoundingRect().width(), yOffset)

        movieShake _ score.insertMovie('upndown -shake')

        shakeAnim _ DemoItemAnimation(upButton,
                DemoItemAnimation.ANIM_UNSPECIFIED)
        shakeAnim.sD..(650)
        shakeAnim.sSV..(upButton.pos())
        shakeAnim.sKVA..(0.60, upButton.pos())
        shakeAnim.sKVA..(0.70, upButton.pos() + QPointF(-2, 0))
        shakeAnim.sKVA..(0.80, upButton.pos() + QPointF(1, 0))
        shakeAnim.sKVA..(0.90, upButton.pos() + QPointF(-1, 0))
        shakeAnim.sEV..(upButton.pos())
        movieShake.ap..(shakeAnim)

        shakeAnim _ DemoItemAnimation(downButton,
                DemoItemAnimation.ANIM_UNSPECIFIED)
        shakeAnim.sD..(650)
        shakeAnim.sSV..(downButton.pos())
        shakeAnim.sKVA..(0.60, downButton.pos())
        shakeAnim.sKVA..(0.70, downButton.pos() + QPointF(-5, 0))
        shakeAnim.sKVA..(0.80, downButton.pos() + QPointF(-3, 0))
        shakeAnim.sKVA..(0.90, downButton.pos() + QPointF(-1, 0))
        shakeAnim.sEV..(downButton.pos())
        movieShake.ap..(shakeAnim)

    ___ createBackButton
        backIn _ score.insertMovie('back -in')
        backOut _ score.insertMovie('back -out')
        backShake _ score.insertMovie('back -shake')
        createLowLeftButton("Back", MenuManager.ROOT, backIn, backOut,
                backShake, Colors.rootMenuName)
