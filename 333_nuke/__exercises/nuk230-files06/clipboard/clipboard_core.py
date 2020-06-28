import sys
import nuke
import getpass
import uuid
import pymongo
import datetime

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidget import *

SERVER = pymongo.MongoClient()
DB = SERVER['fxphd']
USER_COLLECTION = DB['users']
CLIPBOARD_COLLECTION = DB['clipboards']
SCRIPT_LOCATION = './clipboard'
CURRENT_USER = getpass.getuser()

from clipboard_ui import ClipboardUi


class ClipboardCore(ClipboardUi):
    def __init__(self):
        super(ClipboardCore, self).__init__()

        all_users = [user for user in USER_COLLECTION.find()]
        self.build_user_list_widget()

        self.users_search_line_edit.textChanged.connect(self.build_user_list_widget)
        self.send_close_push_button.clicked.connect(self.close)
        self.send_push_button.clicked.connect(self.send_clipboard)
        self.received_close_push_button.clicked.connect(self.close)
        self.paste_push_button.clicked.connect(self.paste_clipboard)
        self.history_table_widget.currentCellChanged.connect(self.set_note)

        self.build_history()

    def set_note(self, index):
        item _ h___.i.. ?, 0
        obj _ ?.d.. 32
        note _ ? *note
        r___.sPT.. ?

    def paste_clipboard(self):
        row _ h___.cR..
        item _ h___.i.. ? 0
        doc _ ?.d.. 32
        script _ ? *nuke_file
        n__.nP.. "@/@"   S.. ?

    def send_clipboard(self):
        row_count _ s_l_w__.c..
        __ no. ?
            ?MB__.i..  *Warning *No user selected
            r_

        now _ d_t_.d_t_.n..
        script _ "@.nk"  u__.u..
        n__.nC.. *@/@   S.. ?
        ___ i __ ra__ r_c..
            obj _ s_l_w__.i.. ?.d.. 32
            doc _ di..
            ? *sender _ C_U..
            ? *submitted_at _ now
            ? *destination_user _ o.. *login
            ? *nuke_file _ s..
            ? *note _ t_n_t_e.tPT..
            C_C__.s.. ?
        c..

    def build_history(self):
        query _ C_C_.f.. *destination_user : C_U..||.so.. *submitted_at -1
        h___.sRC.. ?.c..
        ___ x, i __ e.. ?
            sender_query _ U_C__.f_o.. *login : ?|*sender
            item1 _ ?TWI.. ? *name
            ?.sD.. 32 ?
            item2 _ ?TWI.. g_t_d_a_s.. ?|*submitted_at
            h___.I.. ? 0 _1
            h__w.sI.. ? 1 _2

    def get_time_difference_as_string(self, date):
        delta = d_t_.d_t_.t.. - ?
        __ de__.d..
            r_ *@ day(s) de__.d..
        seconds _ de__.s..
        __ ? < 60:
            r_ *A few seconds ago
        ____ ? < 3600
            r_ *@ minute(s) ago  ? / 60
        ____ ? < 86400:
            r_ @ hours(s) ago ? / 3600

    def build_user_list_widget(self):
        u___.c..
        search_pattern _ u__.t__ .l..
        ___ user __ all_u..
            name _ ? *name
            __ ? __ ?.l..
                item _ ?LWI.. ?
                ?.sD.. 32 ?
                ?.sTT.. g__t.. ?
                u____.aI.. ?
        u___.sI..

    def get_user_tooltip(self, user):
        r_ "Email: @\nLogin: @\nAge: @"  (? *? ? *? ? *?


def start():
    ?.p.. _ ?
    ?.p__.s..

# app _ QApplication(___.argv)
# panel _ ClipboardCore()
# panel.show()
# app.exec_()

