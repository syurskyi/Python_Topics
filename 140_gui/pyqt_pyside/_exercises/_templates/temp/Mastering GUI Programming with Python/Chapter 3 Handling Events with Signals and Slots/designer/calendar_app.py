______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
#from calendar_form import Ui_MainWindow
____ category_window ______ Ui_CategoryWindow
____ ? ______ uic

MW_Ui, MW_Base _ uic.lUT..('calendar_form.ui')


c_ CategoryWindow(qtw.QWidget):

    submitted _ qtc.pyqtSignal(str)

    ___ __init__(self):
        super().__init__()
        # using the ui object method
        self.ui _ Ui_CategoryWindow()
        self.ui.setupUi(self)
        self.s..

    @qtc.pyqtSlot()
    ___ on_submit_btn_clicked(self):
        # we can take advantage of connectSlotsByName here
        # to avoid explicit UI connections
        __ self.ui.category_entry.text
            self.submitted.emit(self.ui.category_entry.text())
        self.close()


#class MainWindow(qtw.QWidget, Ui_MainWindow):
c_ MainWindow(MW_Base, MW_Ui):
    events _ {}

    ___ __init__(self):
        """MainWindow constructor. """
        super().__init__()
        self.setupUi(self)

        # disable the first category item
        self.event_category.model().item(0).setEnabled F..

        ##################
        # Connect Events #
        ##################

        # disable time when "all day" is checked.
        # This is done for us in the UI file
        #self.allday_check.stateChanged.connect(self.event_time.setDisabled)

        # Populate the event list when the calendar is clicked
        self.calendar.selectionChanged.c..(self.populate_list)

        # Populate the event form when an item is selected
        self.event_list.itemSelectionChanged.c..(self.populate_form)

        # Save event when save is hit
        self.add_button.c__.c..(self.save_event)

        # connect delete button
        self.del_button.c__.c..(self.delete_event)

        # Enable 'delete' only when an event is selected
        self.event_list.itemSelectionChanged.c..(
            self.check_delete_btn)
        self.check_delete_btn()

        # check for selection of "new…" for category
        self.event_category.currentTextChanged.c..(self.on_category_change)

        self.s..

    ___ clear_form(self):
        self.event_title.clear()
        self.event_category.setCurrentIndex(0)
        self.event_time.setTime(qtc.QTime(8, 0))
        self.allday_check.setChecked F..
        self.event_detail.sPT..('')

    ___ populate_list(self):
        self.event_list.clear()
        self.clear_form()
        date _ self.calendar.selectedDate()
        for event in self.events.get(date, []):
            time _ (
                event['time'].toString('hh:mm')
                __ event['time']
                else 'All Day'
            )
            self.event_list.addItem(f"{time}: {event['title']}")

    ___ populate_form(self):
        self.clear_form()
        date _ self.calendar.selectedDate()
        event_number _ self.event_list.currentRow()
        __ event_number == -1:
            r_

        event_data _ self.events.get(date)[event_number]

        self.event_category.setCurrentText(event_data['category'])
        __ event_data['time'] __ N..:
            self.allday_check.setChecked(True)
        ____
            self.event_time.setTime(event_data['time'])
        self.event_title.sT..(event_data['title'])
        self.event_detail.sPT..(event_data['detail'])

    ___ save_event(self):
        event _ {
            'category': self.event_category.currentText(),
            'time': (
                N..
                __ self.allday_check.isChecked()
                else self.event_time.time()
                ),
            'title': self.event_title.text(),
            'detail': self.event_detail.toPlainText()
            }

        date _ self.calendar.selectedDate()
        event_list _ self.events.get(date, [])
        event_number _ self.event_list.currentRow()

        # if no events are selected, this is a new event
        __ event_number == -1:
            event_list.append(event)
        ____
            event_list[event_number] _ event

        event_list.sort(key_lambda x: x['time'] or qtc.QTime(0, 0))
        self.events[date] _ event_list
        self.populate_list()

    ___ delete_event(self):
        date _ self.calendar.selectedDate()
        row _ self.event_list.currentRow()
        del(self.events[date][row])
        self.event_list.setCurrentRow(-1)
        self.clear_form()
        self.populate_list()

    ___ check_delete_btn(self):
        self.del_button.setDisabled(self.event_list.currentRow() == -1)

    ___ on_category_change  text):
        __ text == 'New…':
            self.dialog _ CategoryWindow()
            self.dialog.submitted.c..(self.add_category)
            self.event_category.setCurrentIndex(0)

    ___ add_category  category):
        self.event_category.addItem(category)
        self.event_category.setCurrentText(category)

__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)

    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
