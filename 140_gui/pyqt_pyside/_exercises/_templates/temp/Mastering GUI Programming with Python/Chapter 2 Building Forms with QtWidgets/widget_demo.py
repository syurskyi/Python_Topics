______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ ChoiceSpinBox(qtw.QSpinBox):
    """A spinbox for selecting choices."""

    ___  -   choices, *args, **kwargs):
        choices _ choices
        s_. - (
            *args,
            maximum_len(choices) - 1,
            minimum_0,
            **kwargs
        )

    ___ valueFromText  t__):
        r_ choices.index(t__)

    ___ textFromValue  value):
        try:
            r_ choices[value]
        except IndexError:
            r_ '!Error!'

    ___ validate  string, index):
        __ string __ choices:
            state _ qtg.QValidator.Acceptable
        ____ any([v.startswith(string) ___ v __ choices]):
            state _ qtg.QValidator.Intermediate
        ____
            state _ qtg.QValidator.Invalid
        r_ (state, string, index)

c_ IPv4Validator(qtg.QValidator):
    """Enforce entry of IPv4 Addresses"""

    ___ validate  string, index):
        octets _ string.split('.')
        __ le.(octets) > 4:
            state _ qtg.QValidator.Invalid
        ____ no. all([x.isdigit() ___ x __ octets __ x !_ '']):
            state _ qtg.QValidator.Invalid
        ____ no. all([0 <_ int(x) <_ 255 ___ x __ octets __ x !_ '']):
            state _ qtg.QValidator.Invalid
        ____ le.(octets) < 4:
            state _ qtg.QValidator.Intermediate
        ____ any([x == '' ___ x __ octets]):
            state _ qtg.QValidator.Intermediate
        ____
            state _ qtg.QValidator.Acceptable
        r_ (state, string, index)


c_ MainWindow ?.?W..

    ___  - 
        """MainWindow constructor"""
        s_. - (windowTitle_'Qt Widget demo')

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
        line_edit _ ?.?LE..(
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
        layout _ qtw.?VBL..
        sL..(layout)

        layout.aW..(label)
        layout.aW..(line_edit)

        # Add a layout to a layout
        sublayout _ qtw.QHBoxLayout()
        layout.aL..(sublayout)

        sublayout.aW..(button)
        sublayout.aW..(combobox)


        # create a container widget

        container _ qtw.QWidget
        grid_layout _ ?.?GL..
        #layout.addLayout(grid_layout)
        container.sL..(grid_layout)

        grid_layout.aW..(spinbox, 0, 0)
        grid_layout.aW..(datetimebox, 0, 1)
        grid_layout.aW..(textedit, 1, 0, 2, 2)


#        container.setSizePolicy(
#            qtw.QSizePolicy.Expanding,
#            qtw.QSizePolicy.Expanding
#            )

        # QFormLayout

        form_layout _ qtw.QFormLayout()
        layout.aL..(form_layout)
        form_layout.addRow('Item 1', ?.?LE..(self))
        form_layout.addRow('Item 2', ?.?LE..(self))
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
        spinbox.sSP..(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Preferred)

        # set the textedit to expand
        textedit.sSP..(
            qtw.QSizePolicy.MinimumExpanding,
            qtw.QSizePolicy.MinimumExpanding
        )
        textedit.sizeHint _ lambda : qtc.QSize(500, 500)

        # use stretch factor

        stretch_layout _ qtw.QHBoxLayout()
        layout.aL..(stretch_layout)
        stretch_layout.aW..(?.?LE..('Short'), 1)
        stretch_layout.aW..(?.?LE..('Long'), 2)

        #############################
        # Container Widgets         #
        #############################

        # QTabWidget
        tab_widget _ qtw.QTabWidget(
            movable_True,
            tabPosition_qtw.QTabWidget.West,
            tabShape_qtw.QTabWidget.Triangular
        )
        layout.aW..(tab_widget)
        tab_widget.addTab(container, 'Tab the first')
        tab_widget.addTab(subwidget, 'Tab the second')

        tab_widget.setMovable(True)



        #QGroupBox
        groupbox _ qtw.QGroupBox(
            'Buttons',
            checkable_True,
            checked_True,
            alignment_qtc.__.AlignHCenter,
            flat_True
        )
        groupbox.sL..(qtw.QHBoxLayout())
        groupbox.layout().aW..(qtw.?PB..('OK'))
        groupbox.layout().aW..(qtw.?PB..('Cancel'))

        layout.aW..(groupbox)

        ##############
        # Validation #
        ##############
        line_edit.sT..('0.0.0.0')
        line_edit.setValidator(IPv4Validator())

        ratingbox _ ChoiceSpinBox(['bad', 'average', 'good', 'awesome'], self)
        sublayout.aW..(ratingbox)
        s..

__ ______ __ ______
    app _ qtw.?A..(___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ MainWindow()
    ___.exit(app.exec())
