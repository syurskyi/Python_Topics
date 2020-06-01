______ sys
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ QtCore __ qtc


c_ ChoiceSpinBox(qtw.QSpinBox):
    """A spinbox for selecting choices."""

    ___ __init__  choices, *args, **kwargs):
        self.choices _ choices
        super().__init__(
            *args,
            maximum_len(self.choices) - 1,
            minimum_0,
            **kwargs
        )

    ___ valueFromText  text):
        r_ self.choices.index(text)

    ___ textFromValue  value):
        try:
            r_ self.choices[value]
        except IndexError:
            r_ '!Error!'

    ___ validate  string, index):
        __ string in self.choices:
            state _ qtg.QValidator.Acceptable
        ____ any([v.startswith(string) for v in self.choices]):
            state _ qtg.QValidator.Intermediate
        ____
            state _ qtg.QValidator.Invalid
        r_ (state, string, index)

c_ IPv4Validator(qtg.QValidator):
    """Enforce entry of IPv4 Addresses"""

    ___ validate  string, index):
        octets _ string.split('.')
        __ len(octets) > 4:
            state _ qtg.QValidator.Invalid
        ____ no. all([x.isdigit() for x in octets __ x !_ '']):
            state _ qtg.QValidator.Invalid
        ____ no. all([0 <_ int(x) <_ 255 for x in octets __ x !_ '']):
            state _ qtg.QValidator.Invalid
        ____ len(octets) < 4:
            state _ qtg.QValidator.Intermediate
        ____ any([x == '' for x in octets]):
            state _ qtg.QValidator.Intermediate
        ____
            state _ qtg.QValidator.Acceptable
        r_ (state, string, index)


c_ MainWindow(qtw.QWidget):

    ___ __init__(self):
        """MainWindow constructor"""
        super().__init__(windowTitle_'Qt Widget demo')

        #########################
        # Create widget objects #
        #########################

        # QWidget
        subwidget _ qtw.QWidget  toolTip_'This is my widget')
        subwidget.setToolTip('This is YOUR widget')
        print(subwidget.toolTip())

        # QLabel
        label _ qtw.QLabel('<b>Hello Widgets!</b>', self, margin_10)

        # QLineEdit
        line_edit _ qtw.QLineEdit(
            'default value',
            self,
            placeholderText_'Type here',
            clearButtonEnabled_True,
            maxLength_20
        )

        # QPushButton
        button _ qtw.?PB..(
            "Push Me",
            self,
            checkable_True,
            checked_True,
            shortcut_qtg.?KS..('Ctrl+p')
        )

        # QComboBox
        combobox _ qtw.QComboBox(
            self,
            editable_True,
            insertPolicy_qtw.QComboBox.InsertAtTop
        )
        combobox.addItem('Lemon', 1)
        combobox.addItem('Peach', 'Ohh I like Peaches!')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1, 'Radish', 2)

        # QSpinBox
        spinbox _ qtw.QSpinBox(
            self,
            value_12,
            maximum_100,
            minimum_10,
            prefix_'$',
            suffix_' + Tax',
            singleStep_5
        )


        # QDateTimeEdit
        ______ datetime
        datetimebox _ qtw.QDateTimeEdit(
            self,
            date_datetime.date.today(),
            time_datetime.time(12, 30),
            calendarPopup_True,
            maximumDate_datetime.date(2020, 1, 1),
            maximumTime_datetime.time(17, 0),
            displayFormat_'yyyy-MM-dd HH:mm'
        )

        # QTextEdit
        textedit _ qtw.QTextEdit(
            self,
            acceptRichText_False,
            lineWrapMode_qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth_25,
            placeholderText_'Enter your text here'
            )

        ##################
        # Layout Objects #
        ##################

        # Add widget objects to a layout
        layout _ qtw.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label)
        layout.addWidget(line_edit)

        # Add a layout to a layout
        sublayout _ qtw.QHBoxLayout()
        layout.addLayout(sublayout)

        sublayout.addWidget(button)
        sublayout.addWidget(combobox)


        # create a container widget

        container _ qtw.QWidget(self)
        grid_layout _ qtw.QGridLayout()
        #layout.addLayout(grid_layout)
        container.setLayout(grid_layout)

        grid_layout.addWidget(spinbox, 0, 0)
        grid_layout.addWidget(datetimebox, 0, 1)
        grid_layout.addWidget(textedit, 1, 0, 2, 2)


#        container.setSizePolicy(
#            qtw.QSizePolicy.Expanding,
#            qtw.QSizePolicy.Expanding
#            )

        # QFormLayout

        form_layout _ qtw.QFormLayout()
        layout.addLayout(form_layout)
        form_layout.addRow('Item 1', qtw.QLineEdit(self))
        form_layout.addRow('Item 2', qtw.QLineEdit(self))
        form_layout.addRow(qtw.QLabel('<b>This is a label-only row</b>'))

        ################
        # Size Control #
        ################

        # setting a fixed size
        # Fix at 150 pixels wide by 40 pixels high
        label.setFixedSize(150, 40)

        # setting minimum and maximum sizes
        line_edit.setMinimumSize(150, 15)
        line_edit.setMaximumSize(300, 30)

        # set the spinbox to a fixed width
        spinbox.setSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Preferred)

        # set the textedit to expand
        textedit.setSizePolicy(
            qtw.QSizePolicy.MinimumExpanding,
            qtw.QSizePolicy.MinimumExpanding
        )
        textedit.sizeHint _ lambda : qtc.QSize(500, 500)

        # use stretch factor

        stretch_layout _ qtw.QHBoxLayout()
        layout.addLayout(stretch_layout)
        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)

        #############################
        # Container Widgets         #
        #############################

        # QTabWidget
        tab_widget _ qtw.QTabWidget(
            movable_True,
            tabPosition_qtw.QTabWidget.West,
            tabShape_qtw.QTabWidget.Triangular
        )
        layout.addWidget(tab_widget)
        tab_widget.addTab(container, 'Tab the first')
        tab_widget.addTab(subwidget, 'Tab the second')

        tab_widget.setMovable(True)



        #QGroupBox
        groupbox _ qtw.QGroupBox(
            'Buttons',
            checkable_True,
            checked_True,
            alignment_qtc.Qt.AlignHCenter,
            flat_True
        )
        groupbox.setLayout(qtw.QHBoxLayout())
        groupbox.layout().addWidget(qtw.?PB..('OK'))
        groupbox.layout().addWidget(qtw.?PB..('Cancel'))

        layout.addWidget(groupbox)

        ##############
        # Validation #
        ##############
        line_edit.sT..('0.0.0.0')
        line_edit.setValidator(IPv4Validator())

        ratingbox _ ChoiceSpinBox(['bad', 'average', 'good', 'awesome'], self)
        sublayout.addWidget(ratingbox)
        self.s..

__ __name__ == '__main__':
    app _ qtw.?A..(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    sys.exit(app.exec())
