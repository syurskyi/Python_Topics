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

__author__ _ 'Trevor Payne'
__version__ _ '1.0'

____ collections _____ defaultdict
_____ os
_____ ___

_____ Qt
____ Qt _____ ?W.., ?C.., QtGui
_____ tp_launcher_model

QT_VER _ Qt.__binding__
PY_VER _ ___.version[:3]


c_ Delete_Btn(?W...?PB..
    ''' Custom button that Triggers parent's 'delete_item' function. ''' 
    ___  -  , parent_None
        super(Delete_Btn, self). - (parent)
        _my_parent _ parent
        _type _ 'application/x-qabstractitemmodeldatalist'

    ___ dragEnterEvent , e
        __ e.mimeData().hasFormat(_type
            e.accept()
        else:
            e.ignore()

    ___ dropEvent , e
        __ e.mimeData().hasFormat(_type
            _my_parent.delete_item()
            e.accept()
        else:
            e.ignore()

c_ TP_Launcher_GUI(?W...?W..
    '''The goal of this tool is to create a GUI that 
        allows the user to quickly create, select and 
        delete workspaces and add, remove and launch
        applications within those workspaces.
    '''
    ___  -  , parent_None
        super(TP_Launcher_GUI, self). - (parent)

        _icons _ ?W...QFileIconProvider()
        _my_path _ os.path.dirname(os.path.realpath(__file__))
        images_path _ os.path.join(_my_path, 'images')
        full_path _ os.path.join(images_path, 'TPayne_Launcher.png')
        _tpl_icon _ QtGui.QIcon(full_path)
        
        _tp_launcher _ tp_launcher_model.TP_Launcher_Model()

        _edit_op _ {
            T..: _edit_on, 
            False: _edit_off
        }
        _app_instruction _ T..
        _file_dialogs _ defaultdict(lambda: _file_dialog)
        _file_dialogs['PyQt4'] _ _file_dialog_pyqt4
        _dragging _ None
        _delete_op _ {
            'workspace': _delete_workspace, 
            'application':_delete_app
        }
        
        txt _ 'TPayne_Experience'+QT_VER
        _settings _ ?C...QSettings(txt, 'TPayne\'s_Launcher')
        name _ '{}_{}_data.json'.format(PY_VER, QT_VER)
        path _ os.path.join(_my_path, 'data')
        _json_file _ os.path.join(path, name)

        d _ defaultdict(lambda: _get_settings)
        _settings_op _ defaultdict(lambda: d)
        _settings_op['2.7']['PyQt4'] _ _get_settings_27_pyqt4

        _setup()
        _load_settings()
        _edit_toggle()

    #======= SETUP UI =================================

    ___ _setup 
        v_layout _ ?W...QVBoxLayout

        v_layout.addLayout(_setup_header())
        v_layout.addLayout(_setup_edit_options())
        v_layout.addWidget(_setup_apps())

        _setup_tray_icon()
        _setup_connections()

        setWindowTitle('TPayne\'s Launcher ' + __version__)
        setWindowIcon(_tpl_icon)
        flag _ ?C...Qt.WindowCloseButtonHint
        setWindowFlags(?C...Qt.Window | flag)
        resize(190, 200)

    ___ _setup_header 
        h_layout _ ?W...QHBoxLayout()
        workspace_gb _ ?W...QGroupBox('Workspaces')
        v_layout _ ?W...QVBoxLayout(workspace_gb)

        _workspace_cb _ ?W...QComboBox()
        flag _ ?W...QAbstractItemView.DragOnly
        _workspace_cb.view().setDragDropMode(flag)

        _edit_btn _ ?W...?PB..('Edit')
        _edit_btn.setMaximumSize(?C...QSize(40,23))
        _edit_btn.setCheckable(T..)

        v_layout.addWidget(_workspace_cb)
        h_layout.addWidget(workspace_gb)
        h_layout.addStretch()
        h_layout.addWidget(_edit_btn)
        return h_layout

    ___ _setup_edit_options 
        add_del_l _ ?W...QHBoxLayout()

        _add_btn _ ?W...?PB..('Add')
        _add_btn.setMaximumSize(?C...QSize(60,23))
        add_menu _ ?W...QMenu
        add_menu.addAction('Workspace', _add_workspace)
        add_menu.addAction('App or File', _add_app)
        _add_btn.setMenu(add_menu)

        _del_btn _ Delete_Btn
        _del_btn.sT..('Delete')
        _del_btn.setAcceptDrops(T..)
        _del_btn.setIcon(_icons.icon(_icons.Trashcan))
        _del_btn.setIconSize(?C...QSize(32,32))
        _del_btn.setFlat(T..)

        add_del_l.addWidget(_add_btn)
        add_del_l.addWidget(_del_btn)
        return add_del_l

    ___ _setup_apps 
        _app_lw _ ?W...QListWidget()
        _app_lw.setAlternatingRowColors(T..)
        flag _ ?W...QAbstractItemView.InternalMove
        _app_lw.setDragDropMode(flag)
        return _app_lw

    ___ _setup_tray_icon 
        tray_icon _ ?W...QSystemTrayIcon
        tray_icon.setIcon(_tpl_icon)
        tray_icon.setToolTip('Launches other apps!')

        tray_menu _ ?W...QMenu
        tray_menu.addAction('Open', show)
        tray_menu.addAction('YouTube', _tp_launcher.run_youtube)
        tray_menu.addSeparator()
        q _ ?W...QAction('Quit', self, triggered__close)
        tray_menu.addAction(q)
        tray_icon.setContextMenu(tray_menu)
        tray_icon.s..

    ___ _setup_connections 
        ws _ _workspace_changed
        _workspace_cb.currentIndexChanged.c..(ws)
        _edit_btn.c___.c..(_edit_toggle)
        dw _ _dragging_workspace
        _workspace_cb.view().pressed.c..(dw)
        _app_lw.itemPressed.c..(_dragging_app)

    #======= DISPLAY =================================

    ___ _populate_workspaces 
        ws _ _workspace_changed
        _workspace_cb.currentIndexChanged.disconnect(ws)
        _workspace_cb.clear()
        _workspace_cb.addItems(_tp_launcher.get_workspaces())
        _workspace_cb.currentIndexChanged.c..(ws)
        _populate_apps()

    ___ _populate_apps 
        _app_lw.clear()
        ws _ get_workspace()
        for app_name in _tp_launcher.get_app_names(ws
            item _ ?W...QListWidgetItem(_app_lw)
            icon _ _tp_launcher.get_app_icon(ws, app_name)
            __ icon:
                item.setIcon(QtGui.QIcon(icon))
            else:
                item.setIcon(_icons.icon(_icons.File))
            item.sT..(app_name)

    ___ closeEvent , e
        hide()
        e.ignore()

    ___ _close 
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
        _tp_launcher.run_app(get_workspace(), st.(item.t..()))

    #======= EDIT MODE =================================

    ___ _edit_toggle 
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
        ws _ 'New WORKSPACE'
        msg _ 'What would you like to title the new WORKSPACE?'
        t.. _ ?W...QInputDialog.getText , ws, msg)[0]
        __ t..:
            _tp_launcher.add_workspace(st.(t..))
            _populate_workspaces()
            index _ _workspace_cb.findText(t..)
            _workspace_cb.setCurrentIndex(index)
            _save_settings()

    ___ _add_app 
        __ _app_instruction:
            msg _ '1) Select the application file\n'
            msg +_ '2) Select a app icon image (Optional)'
            ?W...QMessageBox.information , 'Add App', msg)
            _app_instruction _ False
        sel _ 'Select APP file'
        app _ _file_dialogs[QT_VER](sel, _my_path)
        __ app:
            path _ os.path.split(app)[0]
            msg _ 'Select ICON file (optional)'
            icon _ _file_dialogs[QT_VER](msg, path)
            _tp_launcher.add_app(get_workspace(), app, icon)
            _populate_apps()
            _save_settings()

    ___ _file_dialog , msg, path
        return ?W...QFileDialog.getOpenFileName , msg, path)[0]

    ___ _file_dialog_pyqt4 , msg, path
        fd _ ?W...QFileDialog.getOpenFileName , msg, path)
        return st.(fd)

    #======= DELETE =================================

    ___ _dragging_workspace , index
        ws _ st.(_workspace_cb.itemText(index.row()))
        _dragging _ ('workspace', ws)

    ___ _dragging_app , item
        _dragging _ ('application', st.(item.t..()))

    ___ _delete_app , app_name
        _tp_launcher.delete_app(get_workspace(), app_name)
        _populate_apps()

    ___ _delete_workspace , ws_name
        _tp_launcher.delete_workspace(ws_name)
        _populate_workspaces()

    ___ delete_item 
        ''' Delete the item dragged onto Delete button '''
        typ _ _dragging[0]
        name _ _dragging[1]
        title _ 'Delete {}?'.format(typ)
        msg _ 'Are you sure you want to delete {} "{}"'.format(typ, name)
        no _ ?W...QMessageBox.No
        yes _ ?W...QMessageBox.Yes
        btn _ ?W...QMessageBox.warning , title, msg, yes, no)
        __ btn __ yes:
            _delete_op[typ](name)
            _save_settings()

    #======= SETTINGS =================================

    ___ _save_settings 
        c _ _app_lw.count()
        names _ [_app_lw.item(i).t..() for i in range(c)]
        ws _ get_workspace()
        _tp_launcher.reorder_apps(ws, names)
        _settings.setValue('CurrentWorkspace', ws)
        _tp_launcher.write_json_file(_json_file)
        _settings.setValue('PosX', int(x()))
        _settings.setValue('PosY', int(y()))

    ___ _load_settings 
        __ 'CurrentWorkspace' in _settings.allKeys() and \
              os.path.exists(_json_file
            x, y, cws _ _settings_op[PY_VER][QT_VER]()
            _tp_launcher.read_json_file(_json_file)
            _populate_workspaces()
            index _ _workspace_cb.findText(cws)
            _workspace_cb.setCurrentIndex(index)
            move(x,y)
        else:
            _tp_launcher.add_workspace('Default_WS')
            _populate_workspaces()

    ___ _get_settings 
        x _ int(_settings.value('PosX')) #PyQt5 conversion
        y _ int(_settings.value('PosY'))
        cws _ st.(_settings.value('CurrentWorkspace'))
        return x, y, cws

    ___ _get_settings_27_pyqt4 
        x _ _settings.value('PosX').toInt()[0]
        y _ _settings.value('PosY').toInt()[0]
        cws _ st.(_settings.value('CurrentWorkspace'))
        return x, y, cws


__ __name__ __ '__main__':
    print (PY_VER)
    print (QT_VER)
    app _ ?W...?A..(___.argv)
    __ not ?W...QSystemTrayIcon.isSystemTrayAvailable(
        ?W...QMessageBox.critical(
            None, 'Error!',
            'No system tray available for this system! Exiting...'
        )
        ___.e..(1)
    ?W...?A...setQuitOnLastWindowClosed(False)
    ex _ TP_Launcher_GUI()
    ex.s..
    ___.e..(app.e

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