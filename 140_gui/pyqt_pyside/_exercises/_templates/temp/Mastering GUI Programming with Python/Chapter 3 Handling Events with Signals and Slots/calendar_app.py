# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?C.. __ qtc
#
#
# c_ CategoryWindow ?.?W..
#     """A basic dialog to demonstrate inter-widget communication"""
#
#     # when submitted, we'll emit this signal
#     # with the entered string
#     submitted _ qtc.pS.. st.
#
#     ___  -
#         s_. - N.. modal_ st.
#
#         sL.. ?.?VBL..
#         l__ .aW..
#             ?.?L.. 'Please enter a new catgory name:'
#             )
#         category_entry _ ?.?LE..
#         la__ .aW.. ?
#
#         submit_btn _ ?.?PB..
#             'Submit',
#             c___self.oS..
#
#         la__ .aW.. ?
#         cancel_btn _ ?.?PB..
#             Cancel
#             c___self.d..
#             )
#         la__ .aW.. ?
#         s..
#
#     ??.?
#     ___ oS..
#         __ c_e_.t__
#             su__.e.. c_e_.t__
#         c..
#
#
# c_ MainWindow ?.?W..
#
#     events _   # dict
#
#     ___  -
#         """MainWindow constructor. """
#         s_. -
#         # Configure the window
#         sWT..("My Calendar App")
#         r.. 800, 600
#
#
#         # Create our widgets
#         calendar _ ?.?CW..
#         event_list _ ?.?LW..
#         event_title _ ?.?LE..
#         event_category _ ?.?CB..
#         event_time _ ?.?TE.. ?.?T.. 8, 0
#         allday_check _ ?.?CB.. All Day
#         event_detail _ ?.?TE..
#         add_button _ ?.?PB.. Add/Update
#         del_button _ ?.?PB.. Delete
#
#         # Configure some widgets
#
#         # Add event categories
#         e_c_.aI..
#             'Select category…', 'New…', 'Work',
#              'Meeting', 'Doctor', 'Family'
#
#         # disable the first category item
#         e_c_.m.. .i.. 0 .sE.. F..
#
#         # Arrange the widgets
#         main_layout _ ?.?HBL..
#         sL.. ?
#         m_l_.aW.. c..
#         # Calendar expands to fill the window
#         c__.sSP..
#             ?.?SP...E..
#             ?.?SP...E..
#
#         right_layout _ ?.?VBL..
#         m_l_.aL.. ?
#         r_l_.aW.. ?.?L.. 'Events on Date'
#         r_l_.aW.. e_l..
#         # Event list expands to fill the right area
#         e_l_.sSP..
#             ?.?SP...E..
#             ?.?SP...E..
#
#
#         # Create a sub-layout for the event view/add form
#         event_form _ ?.?GB.. Event
#         r_l_.aW.. ?
#         event_form_layout _ ?.?GL..
#         ?.aW.. e_t.. 1, 1, 1, 3
#         ?.aW.. e_c_ 2, 1
#         ?.aW.. e_t.. 2, 2,
#         ?.aW.. a_c.. 2, 3
#         ?.aW.. e_d.. 3, 1, 1, 3
#         ?.aW.. a_b.. 4, 2
#         ?.aW.. d_b.. 4, 3
#         e_f_.sL.. ?
#
#
#
#         ##################
#         # Connect Events #
#         ##################
#
#         # disable time when "all day" is checked.
#         a_c__.t__.c.. e_t_.sD..
#
#         # Populate the event list when the calendar is clicked
#         c__.sC__.c.. p_l..
#
#         # Populate the event form when an item is selected
#         e_l_.iSC__.c.. p_f..
#
#         # Save event when save is hit
#         a_b_.c__.c.. s_e..
#
#         # connect delete button
#         d_b_.c__.c.. d_e..
#
#         # Enable 'delete' only when an event is selected
#         e_l_.iSC__.c..
#             c_d_b.
#         c_d_b..
#
#         # check for selection of "new…" for category
#         e_c_.cTC__.c.. o_c_c..
#
#         s..
#
#     ___ clear_form
#         e_t_.cl..
#         e_c_.sCI.. 0
#         e_t_.sT.. ?.?T.. 8, 0
#         a_c_.sC__ F..
#         e_d_.sPT.. ''
#
#     ___ populate_list
#         e_l_.c..
#         c_f..
#         date _ c__.sD..
#         ___ event __ events.g.. d..   # list):
#             time _
#                 ?|'time' .tS.. 'hh:mm'
#                 __ ?|'time'
#                 ____ 'All Day'
#
#             e_l_.aI.. _*|t.. |e..|'title'
#
#     ___ populate_form
#         c_f..
#         date _ c__.sD..
#         event_number _ e_l_.cR..
#         __ ? __ -1
#             r_
#
#         event_data _ e__.g.. d..|e_n..
#
#         e_c_.sCT.. e_d..|'category'
#         __ ? 'time' __ N..
#             a_c_.sC__ st.
#         ____
#             e_t_.sT.. e_d..|'time
#         e_t_.sT.. e_d..|'title
#         e_d_.sPT.. e_d..|'detail
#
#     ___ save_event
#         event _
#             'category': e_c_.cT..
#             'time':
#                 N..
#                 __ a_c_.iC..
#                 ____ e_t_.t..
#
#             'title' e_t__.t__
#             'detail' e_d_.tPT..
#
#
#         date _ c__.sD..
#         event_list _ e__.g.. d..   # list)
#         event_number _ e_l_.cR..
#
#         # if no events are selected, this is a new event
#         __ e_n.. __ -1
#             e_l_.ap.. e..
#         ____
#             e_l_|e_n.. _ e..
#
#         e_l_.s.. key_l___ x ?|'time' o. ?.?T.. 0, 0
#         e..|d.. _ e_l_
#         p_l..
#
#     ___ delete_event
#         date _ c__.sD..
#         row _ e_l_.cR..
#         de. e..|d..||r..
#         e_l_.sCR.. -1
#         c_f..
#         p_l..
#
#     ___ check_delete_btn
#         d_b_.sD.. e_l_.cR.. __ -1
#
#     ___ on_category_change  t__
#         __ t__ __ 'New…'
#             dialog _ CW..
#             ?.s__.c.. a_c..
#             e_c_.sCI.. 0
#
#     ___ add_category  category
#         e_c_.aI.. ?
#         e_c_.sCT.. ?
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
