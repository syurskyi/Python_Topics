_____ ___
_____ ?
_____ getpass
_____ uuid
_____ pymongo
_____ datetime

____ ______._G.. _____ *
____ ______._C.. _____ *
____ ______._W.. _____ *

SERVER = pymongo.MongoClient()
DB = SERVER['fxphd']
USER_COLLECTION = DB['users']
CLIPBOARD_COLLECTION = DB['clipboards']
SCRIPT_LOCATION = "c:/clipboard"
CURRENT_USER = getpass.getuser()

____ clipboard_ui _____ ClipboardUi


c_ ClipboardCore(ClipboardUi):
    ___  -
        s__(ClipboardCore, ). - ()

        all_users = [user ___ user __ USER_COLLECTION.find()]
        build_user_list_widget()

        users_search_line_edit.textChanged.connect(build_user_list_widget)
        send_close_push_button.clicked.connect(close)
        send_push_button.clicked.connect(send_clipboard)
        received_close_push_button.clicked.connect(close)
        paste_push_button.clicked.connect(paste_clipboard)
        history_table_widget.currentCellChanged.connect(set_note)

        build_history()

    ___ set_note(, index):
        item = history_table_widget.item(index, 0)
        obj = item.data(32)
        note = obj['note']
        received_notes_text_edit.setPlainText(note)

    ___ paste_clipboard
        row = history_table_widget.currentRow()
        item = history_table_widget.item(row, 0)
        doc = item.data(32)
        script = doc['nuke_file']
        ?.nodePaste("%s/%s" % (SCRIPT_LOCATION, script))

    ___ send_clipboard
        row_count = stack_list_widget.count()
        __ no. row_count:
            QMessageBox.information(, "Warning", "No user selected")
            r_

        now = datetime.datetime.now()
        script = "%s.nk" % uuid.uuid1()
        ?.nodeCopy("%s/%s" % (SCRIPT_LOCATION, script))
        ___ i __ range(row_count):
            obj = stack_list_widget.item(i).data(32)
            doc = dict()
            doc['sender'] = CURRENT_USER
            doc['submitted_at'] = now
            doc['destination_user'] = obj['login']
            doc['nuke_file'] = script
            doc['note'] = text_note_text_edit.toPlainText()
            CLIPBOARD_COLLECTION.save(doc)
        close()

    ___ build_history
        query = CLIPBOARD_COLLECTION.find({"destination_user": CURRENT_USER}).sort("submitted_at", -1)
        history_table_widget.setRowCount(query.count())
        ___ x, i __ enumerate(query):
            sender_query = USER_COLLECTION.find_one({"login": i['sender']})
            item1 = QTableWidgetItem(sender_query['name'])
            item1.setData(32, i)
            item2 = QTableWidgetItem(get_time_difference_as_string(i['submitted_at']))
            history_table_widget.setItem(x, 0, item1)
            history_table_widget.setItem(x, 1, item2)

    ___ get_time_difference_as_string(, date):
        delta = datetime.datetime.today() - date
        __ delta.days:
            r_ "%s day(s)" % delta.days
        seconds = delta.seconds
        __ seconds < 60:
            r_ "A few seconds ago"
        elif seconds < 3600:
            r_ "%s minute(s) ago" % (seconds / 60)
        elif seconds < 86400:
            r_ "%s hours(s) ago" % (seconds / 3600)

    ___ build_user_list_widget
        users_list_widget.clear()
        search_pattern = users_search_line_edit.text().lower()
        ___ user __ all_users:
            name = user['name']
            __ search_pattern __ name.lower
                item = QListWidgetItem(name)
                item.setData(32, user)
                item.setToolTip(get_user_tooltip(user))
                users_list_widget.addItem(item)
        users_list_widget.sortItems()

    ___ get_user_tooltip(, user):
        r_ "Email: %s\nLogin: %s\nAge: %s" % (user['email'], user['login'], user['age'])


___ start
    start.panel = ClipboardCore()
    start.panel.show()

# app = QApplication(sys.argv)
# panel = ClipboardCore()
# panel.show()
# app.exec_()

