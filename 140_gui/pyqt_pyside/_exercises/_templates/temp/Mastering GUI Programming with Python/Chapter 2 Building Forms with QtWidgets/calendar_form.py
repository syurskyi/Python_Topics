# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?C.. __ qtc
#
# c_ MainWindow ?.?W..
#
#     ___  -
#         """MainWindow constructor."""
#         s_. -
#
#         # Configure the window
#         sWT.. My Calendar App
#         r.. 800, 600
#
#         # Create our widgets
#         calendar _ ?.?CW..
#         event_list _ ?.?LW..
#         event_title _ ?.?LE..
#         event_category _ ?.?CB..
#         event_time _ ?.?TE.. ?.?T..8, 0
#         allday_check _ ?.?CB.. All Day
#         event_detail _ ?.?TE..)
#         add_button _ ?.?PB.. Add/Update
#         del_button _ ?.?PB..Delete
#
#         # Configure some widgets
#
#         # Add event categories
#         e_c__.aI..(
#             ['Select category…', 'New…', 'Work',
#              'Meeting', 'Doctor', 'Family']
#             )
#         # disable the first category item
#         e_c__.m__.i.. 0 .sE.. F..
#
#         # Arrange the widgets
#         main_layout _ ?.?HBL..
#         sL.. ?
#         ?.aW.. c..
#         # Calendar expands to fill the window
#         c__.sSP..
#             ?.?SP...E..
#             ?.?SP...E..
#
#         right_layout _ ?.?VBL..
#         m__.aL.. ?
#         r__.aW.. ?.?L.. 'Events on Date'
#         r__.aW.. e_l..
#         # Event list expands to fill the right area
#         e_l__.sSP..
#             ?.?SP...E..
#             ?.?SP...E..
#
#
#         # Create a sub-layout for the event view/add form
#         event_form _ ?.?GB.. Event
#         rt_l_.aW.. ?
#         event_form_layout _ ?.?GL..
#         event_form.sL.. ?
#
#         ?.aW.. e_t.. 1, 1, 1, 3
#         ?.aW.. e_c.. 2, 1
#         ?.aW.. e_t.. 2, 2
#         ?.aW.. a_c.. 2, 3
#         ?.aW.. e_d.. 3, 1, 1, 3
#         ?.aW.. a_b.. 4, 2
#         ?.aW.. d_b.. 4, 3
#
#         s..
#
#
# __ ______ __ ______
#     app _ ?.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
