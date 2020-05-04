____ ?.?C.. _____ _
____ ?.?G.. _____ _
_____  iconWidget_UIs __ ui
____ icons.icons _____ icons
_____ random, __
_____ ctypes
____ icons _____ icons_rcs
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


c_ iconWidgetClass(?M.., ui.Ui_MainWindow
    ___  -  
        s__(iconWidgetClass, self). -
        setupUi
        # ui
        setWindowIcon(QIcon(icons['create']))
        fill_btn.sT..('')
        fill_btn.setFixedSize(QSize(40,40))
        fill_btn.setIconSize(QSize(32,32))
        fill_btn.setFlat(1)
        # self.fill_btn.setIcon(QIcon(icons['create']))
        fill_btn.setIcon(QIcon(':/create.png'))
        clear_btn.sT..('')
        clear_btn.setFixedSize(QSize(40,40))
        clear_btn.setIconSize(QSize(32,32))
        clear_btn.setFlat(1)
        clear_btn.setIcon(QIcon(icons['clear']))

        fill_act.setIcon(QIcon(icons['create']))
        clear_act.setIcon(QIcon(icons['clear']))
        open_act.setIcon(QIcon(icons['open']))
        save_act.setIcon(QIcon(icons['save']))
        exit_act.setIcon(QIcon(icons['close']))

        pix _ ?P..(icons['sphere']).scaled( 40, 40,
                                               __.KeepAspectRatio,
                                               __.SmoothTransformation )
        image_lb.sP..(pix)

        list_lwd.sVM..(QListView.IconMode)
        list_lwd.setIconSize(QSize(64,64))
        list_lwd.setResizeMode(?LW...ResizeMode.Adjust)
        list_lwd.sDDM..(?AIV...NDD..)

        #connects
        fill_btn.c___.c..(filList)
        clear_btn.c___.c..(clearList)
        fill_act.t__.c..(fillCombo)
        clear_act.t__.c..(clearCombo)


    ___ filList 
        path _ __.path.j..(__.path.d_n..(__file__), 'textures')
        clearList
        ___ i __ __.listdir(path
            item _ ?LWI..(i)
            item.setIcon( QIcon( __.path.j..(path, i) ) )
            list_lwd.aI..(item)
    ___ clearList 
        list_lwd.c..

    ___ fillCombo 
        clearCombo
        ___ i __ ra..(10
            combo_cbb.aI..('Item %s' % i)
            combo_cbb.setItemIcon(i, getRandomIcon())
    ___ clearCombo 
        combo_cbb.c..

    ___ getRandomIcon 
        r_ QIcon(icons[random.choice(['item1','item2','item3'])])

__ _____ __ ______
    app _ ?A..
    w _ iconWidgetClass
    w.s..
    app.e..