______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc

c_ MainWindow ?.?W..

    ___  -
        """MainWindow constructor."""
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
        event_form.sL..(event_form_layout)

        event_form_layout.aW..(event_title, 1, 1, 1, 3)
        event_form_layout.aW..(event_category, 2, 1)
        event_form_layout.aW..(event_time, 2, 2,)
        event_form_layout.aW..(allday_check, 2, 3)
        event_form_layout.aW..(event_detail, 3, 1, 1, 3)
        event_form_layout.aW..(add_button, 4, 2)
        event_form_layout.aW..(del_button, 4, 3)

        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
