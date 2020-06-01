# ______ ___
# ____ ? ______ ?W.. __ qtw
# ____ ? ______ ?C.. __ qtc
#
#
# c_ FormWindow ?.?W..
#
#     submitted _ ?.pS.. st. |in. st.
#
#     ___  -
#         s_. -
#         sL.. ?.?VBL..
#
#         edit _ ?.?LE..
#         submit _ ?.?PB..('Submit', c___self.oS..)
#
#         la__ .aW..(edit)
#         la__ .aW..(submit)
#
#     ___ oS..
#         __ edit.t__ .i_d..
#             t__ _ e__.t__
#             s.. in. st. .e.. in. t__ t__
#         ____
#             s.. st.. .e.. e__.t__
#         c..
#
# c_ MainWindow ?.?W..
#
#     ___  -
#         s_. -
#         sL.. ?.?VBL..
#
#         label _ ?.?L..('Click "change" to change this text.')
#         change _ ?.?PB..("Change", c___s.oC..
#         la__ .aW.. ?
#         la__ .aW.. ?
#         s..
#
#     ??.?
#     ___ onChange
#         formwindow _ ?
#         #self.formwindow.submitted.connect(self.label.setText)
#         ?.s..|st. .c.. oSS..
#         ?.s..|in. st. .c.. oSIS..
#         ?.s..
#
#     ??.? st.
#     ___ onSubmittedStr  string
#         l__.sT.. ?
#
#     ??.? in. st.
#     ___ onSubmittedIntStr  integer, string
#         t__ _ _*The string ? becomes the number ?'
#         l__.sT.. t__
#
#
# __ ______ __ ______
#     app _ qtw.?A.. ___.a..
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw _ ?
#     ___.e.. ?.e..
