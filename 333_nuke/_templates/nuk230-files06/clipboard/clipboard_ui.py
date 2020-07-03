____ ?.QtGui ______ *
____ ?.QtCore ______ *
____ ?.?W.. ______ *
______ ___


c_ ClipboardUi(QTabWidget):
    ___  -
        s_(ClipboardUi, self). - ()

        sQT..("Clipboard")
        setWindowFlags(Qt.WindowStaysOnTopHint)
        resize(500, 600)
        setMinimumSize(500, 600)

        # Widgets

        users_label = ?L..("Users")
        users_list_widget = ?LW..
        users_list_widget.setDragEnabled(T..)
        search_label = ?L..("Search")
        users_search_line_edit = QLineEdit()
        stack_label = ?L..("Stack")
        stack_list_widget = ?LW..
        stack_list_widget.setAcceptDrops(T..)
        text_note_text_edit = QPlainTextEdit()
        send_push_button = ?PB..("Send")
        send_close_push_button = ?PB..("Close")
        history_label = ?L..("History")
        history_table_widget = HistoryTableWidget()
        notes_label = ?L..("Notes")
        received_notes_text_edit = QPlainTextEdit()
        paste_push_button = ?PB..("Paste")
        paste_push_button.setShortcut("Space")
        received_close_push_button = ?PB..("Close")

        send_main_widget = ?W..()
        received_main_widget = ?W..()

        # Layout

        send_layout = QHBoxLayout()
        send_layout_left = ?VB..
        send_layout_left.aW..(users_label)
        send_layout_left.aW..(users_list_widget)
        search_layout = QHBoxLayout()
        search_layout.aW..(search_label)
        search_layout.aW..(users_search_line_edit)
        send_layout_left.addLayout(search_layout)

        send_layout_right = ?VB..
        send_layout_right.aW..(stack_label)
        send_layout_right.aW..(stack_list_widget)
        send_layout_right.aW..(text_note_text_edit)
        send_action_layout = QHBoxLayout()
        send_action_layout.aW..(send_push_button)
        send_action_layout.aW..(send_close_push_button)
        send_layout_right.addLayout(send_action_layout)

        send_layout.addLayout(send_layout_left)
        send_layout.addLayout(send_layout_right)

        received_layout = QHBoxLayout()
        received_layout_left = ?VB..
        received_layout_left.aW..(history_label)
        received_layout_left.aW..(history_table_widget)
        received_action_layout = QHBoxLayout()
        received_action_layout.aW..(paste_push_button)
        received_action_layout.aW..(received_close_push_button)
        received_layout_left.addLayout(received_action_layout)

        received_layout_right = ?VB..
        received_layout_right.aW..(notes_label)
        received_layout_right.aW..(received_notes_text_edit)

        received_layout.addLayout(received_layout_left)
        received_layout.addLayout(received_layout_right)

        send_main_widget.sL..(send_layout)
        received_main_widget.sL..(received_layout)

        addTab(send_main_widget, "Send")
        addTab(received_main_widget, "History")

        users_search_line_edit.setStyleSheet(get_style_sheet())

    ___ get_style_sheet
        r_ '''padding: 2px 2px 2px 20px;
                        background-image: url(zoom.png);
                        background-position: left;
                        background-repeat: no-repeat'''


c_ HistoryTableWidget(QTableWidget):
    ___  -
        s_(HistoryTableWidget, self). - ()

        setColumnCount(2)
        setSelectionBehavior(QAbstractItemView.SelectRows)
        setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        setHorizontalHeaderItem(1, QTableWidgetItem("Date"))
        horizontalHeader().setStretchLastSection(T..)
        verticalHeader().setVisible(False)
        setEditTriggers(QAbstractItemView.NoEditTriggers)
        setSelectionMode(QAbstractItemView.SingleSelection)
