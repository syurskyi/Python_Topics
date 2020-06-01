# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?G.. __ qtg
# ____ ? ______ ?C.. __ qtc
#
#
# c_ ChoiceSpinBox ?.?SB..
#     """A spinbox for selecting choices."""
#
#     ___  -   choices, $ $$
#         choices _ choices
#         s_. -
#             $
#             maximum_len ? - 1
#             minimum_0
#             $$
#
#
#     ___ valueFromText  t__
#         r_ ch__.i.. t__
#
#     ___ textFromValue  value
#         ___
#             r_ c..|?
#         _____ IE..
#             r_ '!Error!'
#
#     ___ validate  string index
#         __ string __ c..
#             state _ ?.?V...A..
#         ____ an. v.s_w_ st.. ___ ? __ c..
#             state _ qtg.?V...I..
#         ____
#             state _ qtg.?V...I..
#         r_ s.. s.. i..
#
# c_ IPv4Validator ?.?V..
#     """Enforce entry of IPv4 Addresses"""
#
#     ___ validate  string index
#         octets _ st__.sp.. '.'
#         __ le. ? > 4
#             state _ ?.?V...I..
#         ____ no. al. x.i_d.. ___ ? __ octets __ ? !_ ''
#             state _ ?.?V...I..
#         ____ no. al.0 <_ in. x <_ 255 ___ ? __ ? __ ? !_ ''
#             state _ ?.?V...I..
#         ____ le. ? < 4
#             state _ ?.?V...I..
#         ____ an. x == '' ___ ? __ ?
#             state _ ?.?V...I..
#         ____
#             state _ ?.?V...A..
#         r_ s.. s.. i..
#
#
# c_ MainWindow ?.?W..
#
#     ___  -
#         """MainWindow constructor"""
#         s_. - windowTitle_'Qt Widget demo'
#
#         #########################
#         # Create widget objects #
#         #########################
#
#         # QWidget
#         subwidget _ ?.?W..  toolTip_'This is my widget')
#         ?.sTT.. This is YOUR widget
#         print ?.tT..
#
#         # QLabel
#         label _ ?.?L..('<b>Hello Widgets!</b>', self, margin_10)
#
#         # QLineEdit
#         line_edit _ ?.?LE..(
#             'default value'
#             ____
#             pT.._'Type here',
#             cBE.._T...
#             mL.._20
#
#
#         # QPushButton
#         button _ ?.?PB..
#             "Push Me",
#
#             c.._T..
#             c.._T..
#             sh_?.?KS.. Ctrl+p
#         )
#
#         # QComboBox
#         combobox _ ?.?CB
#
#             e.._T..
#             iP.._?.?CB.IAT..
#         )
#         ?.aI.. 'Lemon', 1
#         ?.aI.. 'Peach', 'Ohh I like Peaches!'
#         ?.aI.. 'Strawberry' ?.?W..
#         ?.iI.. 1, 'Radish', 2
#
#         # QSpinBox
#         spinbox _ qtw.SB..
#             s
#             v.._12
#             m.._100
#             mi.._10
#             p.._'$'
#             s.._' + Tax'
#             sS.._5
#
#
#
#         # QDateTimeEdit
#         ______ d_t_
#         datetimebox _ qtw.?DTE..
#             s
#             date_d_t_.da__.to..
#             time_d_t_.ti.. 2, 30
#             calendarPopup_T..
#             maximumDate_d_t_.d.. 2020, 1, 1
#             maximumTime_d_t_.ti.. 17, 0
#             displayFormat_'yyyy-MM-dd HH:mm'
#         )
#
#         # QTextEdit
#         textedit _ ?.?TE..
#
#             aRT.._F..
#             lWM.._?.?TE...FCW..
#             lWCOW.._25,
#             phT.._'Enter your text here'
#             )
#
#         ##################
#         # Layout Objects #
#         ##################
#
#         # Add widget objects to a layout
#         layout _ ?.?VBL..
#         sL.. ?
#
#         ?.aW.. l..
#         ?.aW.. l_e..
#
#         # Add a layout to a layout
#         sublayout _ ?.?HBL..
#         l__.aL.. ?
#
#         ?.aW.. b..
#         ?.aW.. c..
#
#
#         # create a container widget
#
#         container _ ?.?W..
#         grid_layout _ ?.?GL..
#         #layout.addLayout(grid_layout)
#         c__.sL.. ?
#
#         ?.aW.. s.. 0, 0
#         ?.aW.. d.. 0, 1
#         ?.aW.. t.. 1, 0, 2, 2
#
#
# #        container.setSizePolicy(
# #            qtw.QSizePolicy.Expanding,
# #            qtw.QSizePolicy.Expanding
# #            )
#
#         # QFormLayout
#
#         form_layout _ ?.?FL..
#         l__.aL.. ?
#         ?.aR.. 'Item 1', ?.?LE..
#         ?.aR.. 'Item 2', ?.?LE..
#         ?.aR.. ?.?L..('<b>This is a label-only row</b>'))
#
#         ################
#         # Size Control #
#         ################
#
#         # setting a fixed size
#         # Fix at 150 pixels wide by 40 pixels high
#         l__.sFS.. 150, 40
#
#         # setting minimum and maximum sizes
#         l_e_.sMS.. 150, 15
#         l_e_.sMS.. 300, 30
#
#         # set the spinbox to a fixed width
#         s__.sSP.. ?.?SP...F.. ?.?SP...P..
#
#         # set the textedit to expand
#         t__.sSP..
#             ?.?SP...ME..
#             ?.?SP...ME..
#         )
#         t__.sH.. _ l___  ?.?S.. 500, 500
#
#         # use stretch factor
#
#         stretch_layout _ ?.?HBL..
#         l__.aL.. ?
#         ?.aW.. ?.?LE.. 'Short'), 1
#         ?.aW.. ?.?LE.. 'Long'), 2)
#         #############################
#         # Container Widgets         #
#         #############################
#
#         # QTabWidget
#         tab_widget _ ?.?TW..
#             m.._T..
#             tP.._?.?TW...West,
#             tS.._?.?TW...Tri..
#
#         l__.aW.. ?
#         ?.aT.. c.. 'Tab the first'
#         ?.aT.. s.. 'Tab the second'
#
#         ?.sM.. T..
#
#
#
#         #QGroupBox
#         groupbox _ ?.?GB..
#             'Buttons'
#             c.._T..
#             c.._T..
#             a.._qtc.__.AHC..
#             f.._T..
#
#         g__.sL.. qtw.?HBL..
#         g__.l...aW.. ?.?PB.. OK
#         g__.l...aW.. ?.?PB.. Cancel
#
#         l__.aW.. g..
#
#         ##############
#         # Validation #
#         ##############
#         l_e_.sT.. '0.0.0.0'
#         l_e_.sV.. IPv4V..
#
#         ratingbox _ CSB.. 'bad', 'average', 'good', 'awesome'|
#         s__.aW.. ?
#         s..
#
# __ ______ __ ______
#     app _ ?.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
