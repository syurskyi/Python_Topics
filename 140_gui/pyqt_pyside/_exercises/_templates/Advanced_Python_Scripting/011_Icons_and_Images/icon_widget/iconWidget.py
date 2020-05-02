____ PySide.?C.. _____ *
____ PySide.QtGui _____ *
_____  iconWidget_UIs as ui
____ icons.icons _____ icons
_____ random, os
_____ ctypes
____ icons _____ icons_rcs
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')


c_ iconWidgetClass(QMainWindow, ui.Ui_MainWindow
    ___  -  
        super(iconWidgetClass, self). - ()
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

        pix = QPixmap(icons['sphere']).scaled( 40, 40,
                                               Qt.KeepAspectRatio,
                                               Qt.SmoothTransformation )
        image_lb.setPixmap(pix)

        list_lwd.setViewMode(QListView.IconMode)
        list_lwd.setIconSize(QSize(64,64))
        list_lwd.setResizeMode(QListWidget.ResizeMode.Adjust)
        list_lwd.setDragDropMode(QAbstractItemView.NoDragDrop)

        #connects
        fill_btn.clicked.c..(filList)
        clear_btn.clicked.c..(clearList)
        fill_act.triggered.c..(fillCombo)
        clear_act.triggered.c..(clearCombo)


    ___ filList 
        path = os.path.join(os.path.dirname(__file__), 'textures')
        clearList()
        for i in os.listdir(path
            item = QListWidgetItem(i)
            item.setIcon( QIcon( os.path.join(path, i) ) )
            list_lwd.addItem(item)
    ___ clearList 
        list_lwd.clear()

    ___ fillCombo 
        clearCombo()
        for i in range(10
            combo_cbb.addItem('Item %s' % i)
            combo_cbb.setItemIcon(i, getRandomIcon())
    ___ clearCombo 
        combo_cbb.clear()

    ___ getRandomIcon 
        return QIcon(icons[random.choice(['item1','item2','item3'])])

__ __name__ __ '__main__':
    app = ?A..([])
    w = iconWidgetClass()
    w.s..
    app.exec_()