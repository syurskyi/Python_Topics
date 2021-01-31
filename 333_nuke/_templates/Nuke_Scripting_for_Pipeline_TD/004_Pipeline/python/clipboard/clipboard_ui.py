____ ______._G.. _____ *
____ ______._C.. _____ *
____ ______._W.. _____ *
_____ ___


c_ ClipboardUi(QTabWidget):
    ___  -
        s__(ClipboardUi, ). - ()

        setWindowTitle("Clipboard")
        sWF..(__.WindowStaysOnTopHint)
        resize(500, 600)
        setMinimumSize(500, 600)

        # Widgets

        users_label _ QLabel("Users")
        users_list_widget _ QListWidget()
        users_list_widget.setDragEnabled T..
        search_label _ QLabel("Search")
        users_search_line_edit _ QLineEdit()
        stack_label _ QLabel("Stack")
        stack_list_widget _ QListWidget()
        stack_list_widget.setAcceptDrops T..
        text_note_text_edit _ QPlainTextEdit()
        send_push_button _ QPushButton("Send")
        send_close_push_button _ QPushButton("Close")
        history_label _ QLabel("History")
        history_table_widget _ HistoryTableWidget()
        notes_label _ QLabel("Notes")
        received_notes_text_edit _ QPlainTextEdit()
        paste_push_button _ QPushButton("Paste")
        paste_push_button.setShortcut("Space")
        received_close_push_button _ QPushButton("Close")

        send_main_widget _ _W..()
        received_main_widget _ _W..()

        # Layout

        send_layout _ QHBoxLayout()
        send_layout_left _ QVBoxLayout()
        send_layout_left.aW..(users_label)
        send_layout_left.aW..(users_list_widget)
        search_layout _ QHBoxLayout()
        search_layout.aW..(search_label)
        search_layout.aW..(users_search_line_edit)
        send_layout_left.addLayout(search_layout)

        send_layout_right _ QVBoxLayout()
        send_layout_right.aW..(stack_label)
        send_layout_right.aW..(stack_list_widget)
        send_layout_right.aW..(text_note_text_edit)
        send_action_layout _ QHBoxLayout()
        send_action_layout.aW..(send_push_button)
        send_action_layout.aW..(send_close_push_button)
        send_layout_right.addLayout(send_action_layout)

        send_layout.addLayout(send_layout_left)
        send_layout.addLayout(send_layout_right)

        received_layout _ QHBoxLayout()
        received_layout_left _ QVBoxLayout()
        received_layout_left.aW..(history_label)
        received_layout_left.aW..(history_table_widget)
        received_action_layout _ QHBoxLayout()
        received_action_layout.aW..(paste_push_button)
        received_action_layout.aW..(received_close_push_button)
        received_layout_left.addLayout(received_action_layout)

        received_layout_right _ QVBoxLayout()
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
        s__(HistoryTableWidget, ). - ()

        setColumnCount(2)
        setSelectionBehavior(QAbstractItemView.SelectRows)
        setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        setHorizontalHeaderItem(1, QTableWidgetItem("Date"))
        horizontalHeader().setStretchLastSection T..
        verticalHeader().setVisible F..
        setEditTriggers(QAbstractItemView.NoEditTriggers)
        setSelectionMode(QAbstractItemView.SingleSelection)
