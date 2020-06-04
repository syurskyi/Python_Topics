# ____ ?.?C.. ______ _
# ____ ?.?W.. ______ _
# ____ ?.?G.. ______ _
# ____ ?.?WEW.. ______ ?WEV..
# ____ ?.?PS.. ______ _
# ______ ___
# ______ _3
# ______ t__
# ______ __
#
#
# c_ InsertDialog ?D..
#     ___  -   $ $$
#         s__ ? ? - $ $$
#
#         QBtn _ ?PB..
#         QBtn.sT.. Register
#
#         sWT.. Add Student
#         sFW.. 300
#         sFH.. 300
#
#         sWT.. Insert Student Data
#         sFW.. 300
#         sFH.. 300
#
#         QBtn.c__.c__ a..
#
#         layout _ ?VBL..
#
#         nameinput _ ?LE..
#         ?.sPT.. Name
#         l__.aW.. ?
#
#         branchinput _ ?CB..
#         ?.aI.. Chemical Engg
#         ?.aI.. Civil
#         ?.aI.. Electrical
#         ?.aI.. Electronics and Communication
#         ?.aI.. Computer Engineering
#         ?.aI.. Information Technology
#         l__.aW.. ?
#
#         seminput _ ?CB..
#         ?.aI.. 1
#         ?.aI.. 2
#         ?.aI.. 3
#         ?.aI.. 4
#         ?.aI.. 5
#         ?.aI.. 6
#         ?.aI.. 7
#         ?.aI.. 8
#         l__.aW.. ?
#
#         mobileinput _ ?LE..
#         ?.sPT.. Mobile No.
#         l__.aW.. ?
#
#         addressinput _ ?LE..
#         ?.sPT.. Address
#         l__.aW.. ?
#
#         layout.aW.. ?B..
#         sL.. ?
#
#     ___ addstudent
#
#         name _ ""
#         branch _ ""
#         sem _ -1
#         mobile _ ""
#         address _ ""
#
#         name _ n__.t..
#         branch _ b__.iT.. b__.cI..
#         sem _ s__.iT.. s__.cI..
#         mobile _ m__.t..
#         address _ a__.t..
#         ___
#             conn _ _3.c__ database.db
#             c _ ?.c__
#             c.e.. I.. I.. students n.. b.. s.. M.. a.. V.. _ _ _ _ _ , n.. b.. s.. m.. a..
#             ?.c__
#             c.c__
#             ?.c__
#             ?MB...i.. ?MB.. 'Successful','Student is added successfully to the database.'
#             c__
#         ______ E..
#             ?MB...w.. ?MB.. 'Error', 'Could not add student to the database.'
#
# c_ SearchDialog ?D..
#     ___  -   $ $$
#         s__ ? ? -  $ $$
#
#         QBtn _ ?PB..
#         ?.sT.. earch
#
#         sWT.. Search user
#         sFW.. 300
#         sFH.. 100
#         ?.c__.c__ s_s..
#         layout _ ?VBL..
#
#         searchinput _ ?LE..
#         onlyInt _ ?IV..
#         s__.sV.. ?
#         s__.sPT.. Roll No.
#         l__.aW.. s__
#         l__.aW.. ?B..
#         sL.. l..
#
#     ___ searchstudent
#
#         searchrol _ ""
#         searchrol _ s__.t..
#         ___
#             ? _ _3.c__ database.db
#             c _ ?.c__
#             result _ c.e.. S.. _ f.. students W.. roll= +st. s_r..
#             row _ ?.f_o_
#             serachresult _ "Rollno : "+st. r.. 0 +'\n'+"Name : "+st. r.. 1 +'\n'+"Branch : "+st. r.. 2 +'\n'+"Sem : "+st. r.. 3 +'\n'+"Address : "+st. r.. 4
#             ?MB...i.. ?MB.. 'Successful' ?
#             ?.c__
#             c.c__
#             ?.c__
#         ______ E..
#             ?MB...w.. ?MB.. 'Error', 'Could not Find student from the database.'
#
# c_ DeleteDialog ?D..
#     ___  -   $ $$
#         s__ ? ? - $ $$
#
#         QBtn _ ?PB..
#         ?.sT.. Delete
#
#         sWT.. Delete Student
#         sFW.. 300
#         sFH.. 100
#         ?.c__.c__ d..
#         layout _ ?VBL..
#
#         deleteinput _ ?LE..
#         onlyInt _ ?IV..
#         d__.sV.. oI..
#         d__.sPT.. Roll No.
#         l__.aW.. d..
#         l__.aW.. ?B..
#         sL.. l..
#
#     ___ deletestudent
#
#         delrol _ ""
#         delrol _ d__.t..
#         ___
#             conn _ _3.c__ database.db
#             c _ ?.c__
#             c.e.. D.. f.. st.. W.. roll= +st. ?
#             ?.c__
#             c.c__
#             ?.c__
#             ?MB...i.. ?MB.. 'Successful','Deleted From Table Successful')
#             c__
#         ______ E..
#             ?MB...w.. ?MB.. 'Error' 'Could not Delete student from the database.'
#
#
#
#
#
#
# c_ AboutDialog ?D..
#     ___  -   $ $$
#         s__ ? ? - $ $$
#
#         sFW.. 500
#         sFH.. 250
#
#         QBtn _ ?DBB....O.
#         buttonBox _ ?DBB... ?
#         ?.a___.c__ a..
#         ?.r___.c__ r..
#
#         layout _ ?VBL..
#
#         sWT.. About
#         title _ ?L.. Student Record Maintainer In PyQt5
#         font _ ?.f..
#         ?.sPS.. 20
#         t__.sF.. ?
#
#         labelpic _ ?L..
#         pixmap _ ?P.. icon/dexter.jpg
#         pixmap _ ?.sTW.. 275
#         la__.sP.. ?
#         la__.sFH.. 150
#
#         l__.aW.. t..
#
#         l__.aW.. ?L.. "v2.0"
#         l__.aW.. ?L.. "Copyright Okay Dexter 2019"
#         l__.aW.. l_p..
#
#
#         l__.aW.. bB..
#
#         sL.. l__
#
#
# c_ MainWindow ?MW..
#     ___  -   $ $$
#         s__ ? ? -  $ $$
#         sWI..(?I.. icon/g2.png  #window icon
#
#         ? _ _3.c__ database.db
#         c _ ?.c__
#         c.e.. C.. T.. I. N.. E.. st.. roll I.. P.. K.. A.. name T.. branch T.. sem I.. mobile I.. address T..
#         c.c__
#
#         file_menu _ mB...aM.. &File
#
#         help_menu _ mB...aM.. &About
#         sWT.. Student Record Maintainer In PyQT5
#         sMS.. 800, 600
#
#         tableWidget _ ?TW..
#         setCentralWidget ?
#         ?.sARC.. T..
#         ?.sCC.. 6
#         ?.hH.. .sCSR.. F..
#         ?.hH.. .sSIS.. F..
#         ?.hH.. .sSLS.. T..
#         ?.vH.. .sV.. F..
#         ?.vH.. .sCSR.. F..
#         ?.vH.. .sSLS.. F..
#         ?.sHHL.. "Roll No.", "Name", "Branch", "Sem", "Mobile","Address"
#
#         toolbar _ ?TB..
#         ?.sM.. F..
#         aTB.. ?
#
#         statusbar _ ?SB..
#         sSB.. ?
#
#         btn_ac_adduser _ ?A.. ?I.."icon/add1.jpg" "Add Student"   #add student icon
#         ?.t___.c__ i..
#         ?.sST.. Add Student
#         t__.aA.. ?
#
#         btn_ac_refresh _ ?A.. ?I.. "icon/r3.png"  "Refresh"   #refresh icon
#         ?.t___.c__ l..
#         ?.sST.. Refresh Table
#         t__.aA.. ?
#
#         btn_ac_search _ ?A.. ?I.. "icon/s1.png" "Search"   #search icon
#         ?.t___.c__ s..
#         ?.sST.. Search User
#         t__.aA.. ?
#
#         btn_ac_delete _ ?A.. ?I.. "icon/d1.png" "Delete"
#         ?.t___.c__ d..
#         ?.sST.. Delete User
#         t__.aA.. ?
#
#         adduser_action _ ?A.. ?I.. "icon/add1.jpg" "Insert Student"
#         ?.t___.c__ i..
#         f_m_.aA.. ?
#
#         searchuser_action _ ?A.. ?I.. "icon/s1.png" "Search Student"
#         ?.t___.c__ s..
#         f_m_.aA.. ?
#
#         deluser_action _ ?A.. ?I.. "icon/d1.png" "Delete"
#         ?.t___.c__ d..
#         f_m_.aA.. ?
#
#
#         about_action _ ?A.. ?I.. "icon/i1.png"  "Developer" #info icon
#         ?.t___.c__ a..
#         h_m_.aA.. ?
#
#     ___ loaddata
#         connection _ _3.c__ database.db
#         query _ "S.. _ F.. st..
#         result _ ?.e.. ?
#         tW__.sRC.. 0
#         ___ row_number row_data __ en.. r..
#             tW__.iR.. ?
#             ___ column_number data __ en.. ?
#                 tW__.sI.. r_n.. c_n.. ?TWI.. st. d..
#         c__.c__
#
#     ___ handlePaintRequest  printer
#         document _ ?TD..
#         cursor _ ?TC.. ?
#         model _ t__.m..
#         table _ c__.iT..
#             m__.rC.. m__.cC..
#         ___ row __ ra.. t__.r..
#             ___ column __ ra.. t__.c..
#                 cu__.iT.. m__.i.. r.., c.. .t..
#                 cu__.mP.. ?TC__.NC..
#         d__.print_ p..
#
#     ___ insert
#         dlg _ ID..
#         ?.e..
#
#     ___ delete
#         dlg _ DD..
#         ?.e..
#
#     ___ search
#         dlg _ SD..
#         ?.e..
#
#     ___ about
#         dlg _ AD..
#         ?.e..
#
#
# app _ ?A.. ___.____
# __ ?D...A.. __ T..
#     window _ ?
#     ?.s..
#     ?.l..
# ___.e.. ?.e..
