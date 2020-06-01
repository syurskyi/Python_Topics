______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc


c_ CategoryWindow ?.?W..
    """A basic dialog to demonstrate inter-widget communication"""

    # when submitted, we'll emit this signal
    # with the entered string
    submitted _ qtc.pyqtSignal(str)

    ___  -
        s_. - (N.., modal_True)

        sL.. ?.?VBL..
        layout().aW..(
            qtw.QLabel('Please enter a new catgory name:')
            )
        category_entry _ qtw.?LE..
        layout().aW..(category_entry)

        submit_btn _ qtw.?PB..(
            'Submit',
            c___self.onSubmit
            )
        layout().aW..(submit_btn)
        cancel_btn _ qtw.?PB..(
            'Cancel',
            c___self.destroy
            )
        layout().aW..(cancel_btn)
        s..

    @qtc.pyqtSlot()
    ___ onSubmit 
        __ category_entry.t__
            submitted.emit(category_entry.t__())
        close()


c_ MainWindow ?.?W..

    events _ {}

    ___  -
        """MainWindow constructor. """
        s_. - ()
        # Configure the window
        setWindowTitle("My Calendar App")
        resize(800, 600)


        # Create our widgets
        calendar _ qtw.QCalendarWidget()
        event_list _ qtw.QListWidget()
        event_title _ qtw.?LE..
        event_category _ qtw.QComboBox()
        event_time _ qtw.QTimeEdit(qtc.QTime(8, 0))
        allday_check _ qtw.QCheckBox('All Day')
        event_detail _ qtw.QTextEdit()
        add_button _ qtw.?PB..('Add/Update')
        del_button _ qtw.?PB..('Delete')

        # Configure some widgets

        # Add event categories
        event_category.addItems(
            ['Select category…', 'New…', 'Work',
             'Meeting', 'Doctor', 'Family']
            )
        # disable the first category item
        event_category.model().item(0).setEnabled F..

        # Arrange the widgets
        main_layout _ qtw.QHBoxLayout()
        sL..(main_layout)
        main_layout.aW..(calendar)
        # Calendar expands to fill the window
        calendar.sSP..(
            qtw.QSizePolicy.E..,
            qtw.QSizePolicy.E..
        )
        right_layout _ qtw.?VBL..
        main_layout.aL..(right_layout)
        right_layout.aW..(qtw.QLabel('Events on Date'))
        right_layout.aW..(event_list)
        # Event list expands to fill the right area
        event_list.sSP..(
            qtw.QSizePolicy.E..,
            qtw.QSizePolicy.E..
            )

        # Create a sub-layout for the event view/add form
        event_form _ qtw.QGroupBox('Event')
        right_layout.aW..(event_form)
        event_form_layout _ ?.?GL..
        event_form_layout.aW..(event_title, 1, 1, 1, 3)
        event_form_layout.aW..(event_category, 2, 1)
        event_form_layout.aW..(event_time, 2, 2,)
        event_form_layout.aW..(allday_check, 2, 3)
        event_form_layout.aW..(event_detail, 3, 1, 1, 3)
        event_form_layout.aW..(add_button, 4, 2)
        event_form_layout.aW..(del_button, 4, 3)
        event_form.sL..(event_form_layout)



        ##################
        # Connect Events #
        ##################

        # disable time when "all day" is checked.
        allday_check.toggled.c..(event_time.setDisabled)

        # Populate the event list when the calendar is clicked
        calendar.selectionChanged.c..(populate_list)

        # Populate the event form when an item is selected
        event_list.itemSelectionChanged.c..(populate_form)

        # Save event when save is hit
        add_button.c__.c..(save_event)

        # connect delete button
        del_button.c__.c..(delete_event)

        # Enable 'delete' only when an event is selected
        event_list.itemSelectionChanged.c..(
            check_delete_btn)
        check_delete_btn()

        # check for selection of "new…" for category
        event_category.currentTextChanged.c..(on_category_change)

        s..

    ___ clear_form 
        event_title.clear()
        event_category.setCurrentIndex(0)
        event_time.setTime(qtc.QTime(8, 0))
        allday_check.setChecked F..
        event_detail.sPT..('')

    ___ populate_list 
        event_list.clear()
        clear_form()
        date _ calendar.selectedDate()
        ___ event __ events.g..(date,   # list):
            time _ (
                event['time'].toString('hh:mm')
                __ event['time']
                else 'All Day'
            )
            event_list.addItem(f"{time}: {event['title']}")

    ___ populate_form 
        clear_form()
        date _ calendar.selectedDate()
        event_number _ event_list.currentRow()
        __ event_number == -1:
            r_

        event_data _ events.g..(date)[event_number]

        event_category.setCurrentText(event_data['category'])
        __ event_data['time'] __ N..:
            allday_check.setChecked(True)
        ____
            event_time.setTime(event_data['time'])
        event_title.sT..(event_data['title'])
        event_detail.sPT..(event_data['detail'])

    ___ save_event 
        event _ {
            'category': event_category.currentText(),
            'time': (
                N..
                __ allday_check.isChecked()
                else event_time.time()
                ),
            'title': event_title.t__(),
            'detail': event_detail.toPlainText()
            }

        date _ calendar.selectedDate()
        event_list _ events.g..(date,   # list)
        event_number _ event_list.currentRow()

        # if no events are selected, this is a new event
        __ event_number == -1:
            event_list.ap..(event)
        ____
            event_list[event_number] _ event

        event_list.sort(key_lambda x: x['time'] or qtc.QTime(0, 0))
        events[date] _ event_list
        populate_list()

    ___ delete_event 
        date _ calendar.selectedDate()
        row _ event_list.currentRow()
        del(events[date][row])
        event_list.setCurrentRow(-1)
        clear_form()
        populate_list()

    ___ check_delete_btn 
        del_button.setDisabled(event_list.currentRow() == -1)

    ___ on_category_change  t__):
        __ t__ == 'New…':
            dialog _ CategoryWindow()
            dialog.submitted.c..(add_category)
            event_category.setCurrentIndex(0)

    ___ add_category  category):
        event_category.addItem(category)
        event_category.setCurrentText(category)

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
