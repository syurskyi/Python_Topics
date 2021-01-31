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

        users_label = QLabel("Users")
        users_list_widget = QListWidget()
        users_list_widget.setDragEnabled T..
        search_label = QLabel("Search")
        users_search_line_edit = QLineEdit()
        stack_label = QLabel("Stack")
        stack_list_widget = QListWidget()
        stack_list_widget.setAcceptDrops T..
        text_note_text_edit = QPlainTextEdit()
        send_push_button = QPushButton("Send")
        send_close_push_button = QPushButton("Close")
        history_label = QLabel("History")
        history_table_widget = HistoryTableWidget()
        notes_label = QLabel("Notes")
        received_notes_text_edit = QPlainTextEdit()
        paste_push_button = QPushButton("Paste")
        paste_push_button.setShortcut("Space")
        received_close_push_button = QPushButton("Close")

        send_main_widget = _W..()
        received_main_widget = _W..()

        # Layout

        send_layout = QHBoxLayout()
        send_layout_left = QVBoxLayout()
        send_layout_left.addWidget(users_label)
        send_layout_left.addWidget(users_list_widget)
        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(users_search_line_edit)
        send_layout_left.addLayout(search_layout)

        send_layout_right = QVBoxLayout()
        send_layout_right.addWidget(stack_label)
        send_layout_right.addWidget(stack_list_widget)
        send_layout_right.addWidget(text_note_text_edit)
        send_action_layout = QHBoxLayout()
        send_action_layout.addWidget(send_push_button)
        send_action_layout.addWidget(send_close_push_button)
        send_layout_right.addLayout(send_action_layout)

        send_layout.addLayout(send_layout_left)
        send_layout.addLayout(send_layout_right)

        received_layout = QHBoxLayout()
        received_layout_left = QVBoxLayout()
        received_layout_left.addWidget(history_label)
        received_layout_left.addWidget(history_table_widget)
        received_action_layout = QHBoxLayout()
        received_action_layout.addWidget(paste_push_button)
        received_action_layout.addWidget(received_close_push_button)
        received_layout_left.addLayout(received_action_layout)

        received_layout_right = QVBoxLayout()
        received_layout_right.addWidget(notes_label)
        received_layout_right.addWidget(received_notes_text_edit)

        received_layout.addLayout(received_layout_left)
        received_layout.addLayout(received_layout_right)

        send_main_widget.setLayout(send_layout)
        received_main_widget.setLayout(received_layout)

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
