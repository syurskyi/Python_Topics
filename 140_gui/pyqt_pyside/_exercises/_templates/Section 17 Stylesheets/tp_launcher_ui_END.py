## TPAYNE APPLICATION LAUNCHER
##      OCT. 2017
##      IRVINE, CA, USA
##  [See license at end of file]

'''
The goal of this tool is to create a GUI that
allows the user to quickly create, select and
delete workspaces and add, remove and launch
applications within those workspaces.

This tool is the beginning of a pipeline
management application in which you could keep
multiple users using the same version of software,
copy distinct settings and files to the clients
machines and a whole bunch of other cool stuff.
'''

#!/usr/bin/env python

__author__ = 'Trevor Payne'
__version__ = '1.0'

____ collections _____ defaultdict
_____ os
_____ ___

_____ Qt
____ Qt _____ ?W.., ?C.., QtGui
_____ tp_launcher_model

QT_VER = Qt.__binding__
PY_VER = ___.version[:3]

_STYLE_MAIN = '''
    QWidget{
        color: white; 
        background-color: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #052e32, stop: 0.25 #030f00,
            stop: 0.75 #030f00, stop: 1 #382213);
        alternate-background-color: #072100;
    } 
    QComboBox{ 
        color: white;
        background: black;
        border: 1px inset gray;
        border-radius: 2px;
    }
    QGroupBox{ background-color: rgba(0,0,0,0)}
    QLineEdit{ color: white;  background-color: rgb(0,0,0); }
    '''
_STYLE_BTN = '''
    QPushButton{ 
        border: 1px outset gray;
        border-radius: 2px;
        background-color: #00351d;
        min-width: 40px;
    }
    QPushButton:checked { 
        border: 1px outset gray;
        border-radius: 2px;
        background-color: #701200;
        min-width: 40px;
    } 
    '''

c_ Delete_Btn(?W...?PB..
    ''' Custom button that Triggers parent's 'delete_item' function. '''
    ___  -  , parent=None
        super(Delete_Btn, self). - (parent)
        _my_parent = parent
        _type = 'application/x-qabstractitemmodeldatalist'

    ___ dragEnterEvent , event
        __ event.mimeData().hasFormat(_type
            event.accept()
        else:
            event.ignore()

    ___ dropEvent , event
        __ event.mimeData().hasFormat(_type
            _my_parent.delete_item()
            event.accept()
        else:
            event.ignore()

c_ TP_Launcher_GUI(?W...?W..
    '''The goal of this tool is to create a GUI that
        allows the user to quickly create, select and
        delete workspaces and add, remove and launch
        applications within those workspaces.
    '''
    ___  -  , parent=None
        super(TP_Launcher_GUI, self). - (parent)

        # System and tool icons
        _icons = ?W...QFileIconProvider()
        _my_path = os.path.dirname(os.path.realpath(__file__))
        images_path = os.path.join(_my_path, 'images')
        full_path = os.path.join(images_path, 'TPayne_Launcher.png')
        _tpl_icon = QtGui.QIcon(full_path)

        # Data holding instance
        _tp_launcher = tp_launcher_model.TP_Launcher_Model()

        # Toggle dictionary to replace 'if/else' statements
        _edit_op = {
            T..: _edit_on,
            False: _edit_off
        }
        _app_instruction = T..

        # Handle version specific file dialog box issues
        _file_dialogs = defaultdict(lambda: _file_dialog)
        _file_dialogs['PyQt4'] = _file_dialog_pyqt4
        _dragging = None
        _delete_op = {
            'workspace': _delete_workspace,
            'application':_delete_app
        }

        # Settings and json file read/write stuff
        txt = 'TPayne_Experience'+QT_VER
        _settings = ?C...QSettings(txt, 'TPayne\'s_Launcher')
        name = '{}_{}_data.json'.format(PY_VER, QT_VER)
        path = os.path.join(_my_path, 'data')
        _json_file = os.path.join(path, name)

        # Handle version specific reading/writing settings
        d = defaultdict(lambda: _get_settings)
        _settings_op = defaultdict(lambda: d)
        _settings_op['2.7']['PyQt4'] = _get_settings_27_pyqt4

        # Setup GUI, then load settings, then display editmode properly
        _setup()
        _load_settings()
        _edit_toggle()

    #======= SETUP UI =================================

    ___ _setup
        ''' Create tool GUI, set title, icon, remove
        minimize / maximize buttons, resize and style.
        '''
        v_layout = ?W...QVBoxLayout

        v_layout.addLayout(_setup_header())
        v_layout.addLayout(_setup_edit_options())
        v_layout.addWidget(_setup_apps())

        _setup_tray_icon()
        _setup_connections()

        setWindowTitle('TPayne\'s Launcher ' + __version__)
        setWindowIcon(_tpl_icon)
        flag = ?C...Qt.WindowCloseButtonHint
        setWindowFlags(?C...Qt.Window | flag)
        resize(190, 200)
        setStyleSheet(_STYLE_MAIN)

    ___ _setup_header
        ''' Create combobox for workspace and edit button '''
        h_layout = ?W...QHBoxLayout()
        workspace_gb = ?W...QGroupBox('Workspaces')
        v_layout = ?W...QVBoxLayout(workspace_gb)

        _workspace_cb = ?W...QComboBox()
        _workspace_cb.view().setDragDropMode(
            ?W...QAbstractItemView.DragOnly
            )

        _edit_btn = ?W...?PB..('Edit')
        _edit_btn.setMaximumSize(?C...QSize(40, 23))
        _edit_btn.setCheckable(T..)
        _edit_btn.setStyleSheet(_STYLE_BTN)

        v_layout.addWidget(_workspace_cb)
        h_layout.addWidget(workspace_gb)
        h_layout.addStretch()
        h_layout.addWidget(_edit_btn)
        return h_layout

    ___ _setup_edit_options
        ''' Create add / delete buttons with menus
        and overrides
        '''
        add_del_l = ?W...QHBoxLayout()

        _add_btn = ?W...?PB..('Add')
        _add_btn.setMaximumSize(?C...QSize(60, 23))
        add_menu = ?W...QMenu
        add_menu.addAction('Workspace', _add_workspace)
        add_menu.addAction('App or File', _add_app)
        _add_btn.setMenu(add_menu)

        _del_btn = Delete_Btn
        _del_btn.sT..('Delete')
        _del_btn.setAcceptDrops(T..)
        _del_btn.setIcon(_icons.icon(_icons.Trashcan))
        _del_btn.setIconSize(?C...QSize(32, 32))
        _del_btn.setFlat(T..)

        add_del_l.addWidget(_add_btn)
        add_del_l.addWidget(_del_btn)
        return add_del_l

    ___ _setup_apps
        ''' Create apps list widget with drag/drop, and stuff'''
        _app_lw = ?W...QListWidget()
        _app_lw.setAlternatingRowColors(T..)
        _app_lw.setDragDropMode(
            ?W...QAbstractItemView.InternalMove
            )
        return _app_lw

    ___ _setup_tray_icon
        ''' Create icon for system tray and actions menu '''
        tray_icon = ?W...QSystemTrayIcon
        tray_icon.setIcon(_tpl_icon)
        tray_icon.setToolTip('Launches other apps!')

        tray_menu = ?W...QMenu
        tray_menu.addAction('Open', show)
        tray_menu.addAction('YouTube', _tp_launcher.run_youtube)
        tray_menu.addSeparator()
        tray_menu.addAction(
            ?W...QAction('Quit', self, triggered=_close)
            )
        tray_icon.setContextMenu(tray_menu)
        tray_icon.s..

    ___ _setup_connections
        ''' Create connections between combobox, apps,
        edit to do stuff
        '''
        _workspace_cb.currentIndexChanged.c..(
            _workspace_changed
            )
        _edit_btn.clicked.c..(_edit_toggle)
        _workspace_cb.view().pressed.c..(
            _dragging_workspace
            )
        _app_lw.itemPressed.c..(_dragging_app)

    #======= DISPLAY =================================

    ___ _populate_workspaces
        ''' Clear and Populate the workspace combobox,
        disconnect and reconnect signal to avoid unintended refresh
        of populate apps.
        '''
        _workspace_cb.currentIndexChanged.disconnect(
            _workspace_changed
            )
        _workspace_cb.clear()
        _workspace_cb.addItems(_tp_launcher.get_workspaces())
        _workspace_cb.currentIndexChanged.c..(
            _workspace_changed
            )
        _populate_apps()

    ___ _populate_apps
        ''' Clear and Populate the apps list widget,
        set each application icon and name.
        '''
        _app_lw.clear()
        workspace = get_workspace()
        for app_name in _tp_launcher.get_app_names(workspace
            item = ?W...QListWidgetItem(_app_lw)
            icon = _tp_launcher.get_app_icon(workspace, app_name)
            __ icon:
                item.setIcon(QtGui.QIcon(icon))
            else:
                item.setIcon(_icons.icon(_icons.File))
            item.sT..(app_name)

    ___ closeEvent , e
        ''' Override Qt close event to instead hide tool '''
        hide()
        e.ignore()

    ___ _close
        ''' Save settings and Quit tool'''
        _save_settings()
        ?W...?A...instance().quit()

    #======= WORKSPACE + APP =================================

    ___ get_workspace
        ''' Returns the currently selection workspace from combobox. '''
        return st.(_workspace_cb.currentText())

    ___ _workspace_changed
        _populate_apps()
        _save_settings()

    ___ _run_app , item
        item.setSelected(False)
        _tp_launcher.run_app(get_workspace(), st.(item.text()))

    #======= EDIT MODE =================================

    ___ _edit_toggle
        ''' Whenever button is clicked, set add/del button vis,
        set drag drop and connect/disconnect run apps signal
        '''
        _edit_op[_edit_btn.iC..]()
        _app_lw.setDragEnabled(_edit_btn.isChecked())
        _add_btn.setVisible(_edit_btn.isChecked())
        _del_btn.setVisible(_edit_btn.isChecked())
        _save_settings()

    ___ _edit_on
        _app_lw.itemClicked.disconnect(_run_app)
        _edit_btn.sT..('Done')

    ___ _edit_off
        _app_lw.itemClicked.c..(_run_app)
        _edit_btn.sT..('Edit')

    #======= ADD =================================

    ___ _add_workspace
        ''' Prompt user with line edit input dialog for new name,
        store if valid, populate, then select it.'''
        text = ?W...QInputDialog.getText(
            self,
            'New WORKSPACE',
            'What would you like to title the new WORKSPACE?'
            )[0]
        __ text:
            _tp_launcher.add_workspace(st.(text))
            _populate_workspaces()
            index = _workspace_cb.findText(text)
            _workspace_cb.setCurrentIndex(index)
            _save_settings()

    ___ _add_app
        ''' Present user with instructions ONCE, then manditory
        file dialog for app, optional dialog for icon,
        store, populate, and save settings'''
        __ _app_instruction:
            msg = '1) Select the application file\n'
            msg += '2) Select a app icon image (Optional)'
            ?W...QMessageBox.information , 'Add App', msg)
            _app_instruction = False
        sel = 'Select APP file'
        app = _file_dialogs[QT_VER](sel, _my_path)
        __ app:
            path = os.path.split(app)[0]
            msg = 'Select ICON file (optional)'
            icon = _file_dialogs[QT_VER](msg, path)
            _tp_launcher.add_app(get_workspace(), app, icon)
            _populate_apps()
            _save_settings()

    ___ _file_dialog , msg, path
        ''' Default File dialog for Pyside, Pyside2, PyQt5 return file path
        and filter for the dialog. Only need the path.'''
        return ?W...QFileDialog.getOpenFileName , msg, path)[0]

    ___ _file_dialog_pyqt4 , msg, path
        ''' File dialog for PyQt4 only returns file path as QString,
        must be converted to a string'''
        fd = ?W...QFileDialog.getOpenFileName , msg, path)
        return st.(fd)

    #======= DELETE =================================

    ___ _dragging_workspace , index
        ''' When the user begins dragging a workspace,
        store the index of the item being dragged and
        note that it is a workspace.'''
        ws = st.(_workspace_cb.itemText(index.row()))
        _dragging = ('workspace', ws)

    ___ _dragging_app , item
        ''' When the user begins dragging a application,
        store the item text and note it's an app
        '''
        _dragging = ('application', st.(item.text()))

    ___ _delete_app , app_name
        _tp_launcher.delete_app(get_workspace(), app_name)
        _populate_apps()

    ___ _delete_workspace , ws_name
        _tp_launcher.delete_workspace(ws_name)
        _populate_workspaces()

    ___ delete_item
        ''' Delete the item dragged onto Delete button '''
        typ = _dragging[0]
        name = _dragging[1]
        title = 'Delete {}?'.format(typ)
        msg = 'Are you sure you want to delete {} "{}"'.format(typ, name)
        no = ?W...QMessageBox.No
        yes = ?W...QMessageBox.Yes
        btn = ?W...QMessageBox.warning , title, msg, yes, no)
        __ btn __ yes:
            _delete_op[typ](name)
            _save_settings()

    #======= SETTINGS =================================

    ___ _save_settings
        ''' Reorder the apps if necessary, then save the user settings
        to QSettings, and store the tool data to json file.
        '''
        count = _app_lw.count()
        names = [_app_lw.item(i).text() for i in range(count)]
        workspace = get_workspace()
        _tp_launcher.reorder_apps(workspace, names)
        _settings.setValue('CurrentWorkspace', workspace)
        _tp_launcher.write_json_file(_json_file)
        _settings.setValue('PosX', int(x()))
        _settings.setValue('PosY', int(y()))

    ___ _load_settings
        ''' If there is a QSettings file and the json file exists,
        read in the json file, then make selections based on the
        qsettings.
        '''
        __ 'CurrentWorkspace' in _settings.allKeys() and \
              os.path.exists(_json_file
            x, y, cws = _settings_op[PY_VER][QT_VER]()
            _tp_launcher.read_json_file(_json_file)
            _populate_workspaces()
            index = _workspace_cb.findText(cws)
            _workspace_cb.setCurrentIndex(index)
            move(x, y)
        else:
            _tp_launcher.add_workspace('Default_WS')
            _populate_workspaces()

    ___ _get_settings
        ''' Default get settings for x, y position for,
        tool and current workspace
        '''
        x = int(_settings.value('PosX')) #PyQt5 conversion
        y = int(_settings.value('PosY'))
        cws = st.(_settings.value('CurrentWorkspace'))
        return x, y, cws

    ___ _get_settings_27_pyqt4
        ''' This specific version of PyQt and python needed to be
        handled differently. '''
        x = _settings.value('PosX').toInt()[0]
        y = _settings.value('PosY').toInt()[0]
        cws = st.(_settings.value('CurrentWorkspace'))
        return x, y, cws


__ __name__ __ '__main__':
    # for debugging
    print (PY_VER)
    print (QT_VER)
    app = ?W...?A..(___.argv)

    # if os doesn't support Tray, quit
    __ not ?W...QSystemTrayIcon.isSystemTrayAvailable(
        ?W...QMessageBox.critical(
            None, 'Error!',
            'No system tray available for this system! Exiting...'
        )
        ___.e..(1)

    # do not close if tool is hidden
    ?W...?A...setQuitOnLastWindowClosed(False)

    # Create an instance of tool and run it
    ex = TP_Launcher_GUI()
    ex.s..
    ___.e..(app.exec_())

# Copyright (c) 2017 Trevor Payne
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
