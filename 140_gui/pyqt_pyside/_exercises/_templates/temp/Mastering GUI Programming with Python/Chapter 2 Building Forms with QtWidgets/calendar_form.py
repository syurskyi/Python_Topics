______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc

c_ MainWindow(qtw.QWidget):

    ___ __init__(self):
        """MainWindow constructor."""
        super().__init__()

        # Configure the window
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        # Create our widgets
        self.calendar _ qtw.QCalendarWidget()
        self.event_list _ qtw.QListWidget()
        self.event_title _ qtw.QLineEdit()
        self.event_category _ qtw.QComboBox()
        self.event_time _ qtw.QTimeEdit(qtc.QTime(8, 0))
        self.allday_check _ qtw.QCheckBox('All Day')
        self.event_detail _ qtw.QTextEdit()
        self.add_button _ qtw.?PB..('Add/Update')
        self.del_button _ qtw.?PB..('Delete')

        # Configure some widgets

        # Add event categories
        self.event_category.addItems(
            ['Select category…', 'New…', 'Work',
             'Meeting', 'Doctor', 'Family']
            )
        # disable the first category item
        self.event_category.model().item(0).setEnabled F..

        # Arrange the widgets
        main_layout _ qtw.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)
        # Calendar expands to fill the window
        self.calendar.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )
        right_layout _ qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(qtw.QLabel('Events on Date'))
        right_layout.addWidget(self.event_list)
        # Event list expands to fill the right area
        self.event_list.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )

        # Create a sub-layout for the event view/add form
        event_form _ qtw.QGroupBox('Event')
        right_layout.addWidget(event_form)
        event_form_layout _ qtw.QGridLayout()
        event_form.setLayout(event_form_layout)

        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
        event_form_layout.addWidget(self.event_category, 2, 1)
        event_form_layout.addWidget(self.event_time, 2, 2,)
        event_form_layout.addWidget(self.allday_check, 2, 3)
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
        event_form_layout.addWidget(self.add_button, 4, 2)
        event_form_layout.addWidget(self.del_button, 4, 3)

        self.s..


__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
