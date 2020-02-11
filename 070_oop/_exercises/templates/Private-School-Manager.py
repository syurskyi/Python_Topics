# from getpass import getpass
#
#
# c_ Person
#     ___ - ____ f_name l_name age password m_name
#         ____.__f_ _ ?.t..
#         ____.__m_ _ ?.u..
#         ____.__l_ _ ?.u..
#         ____.__a.. _ ?
#         ____.__email _ ____.g_f.. 0 +____.g_l... +'@psu.com' .l..
#         ____.__password _ password
#
#     ??
#     ___ string_has_number string
#         r_ an. char.isd.. ___ ? __ ?
#
#     ___ get_first_name ____
#         r_ ____.__f_n..
#
#     ___ set_first_name ____ f_name
#         __ ____.s_h_n.. f_n..
#             print('The first name that you entered contains a number!')
#         ____
#             ____.__f_n.. _ f_n__.t..
#
#     ___ get_last_name ____
#         r_ ____.__l_.
#
#     ___ set_last_name ____ l_name
#         __ ____.s_h_n.. l_n..
#             print('The last name that you entered contains a number!')
#         ____
#             ____.__l_ _ l_.u..
#
#     ___ get_middle_name ____
#         r_ ____.__m_
#
#     ___ set_middle_name ____ m_name
#         __ ____.s_h_n m_
#             print('The middle name that you entered contains a number')
#         ____
#             ____.__m_ _ m_.u..
#
#     ___ get_age ____
#         r_ ____.__a..
#
#     ___ set_age ____ age
#         __  5 <_ ? < 130
#             ____.__a.. _ ?
#         ____
#             print('Age out of ra..')
#
#     ___ get_email ____
#             r_ ____.__e..
#
#     ___ set_email ____ new_email
#             ____.__e.. _ ?
#
#     ___ get_password ____
#             r_ ____.__p..
#
#     ___ set_password ____
#         old_password _ g.. ('Please enter your password: ')
#         ___ tries __ ra.. 4
#             __ o.. !_ ____.__p..
#                 o.. _ g...('Worong password! please enter your password again: ')
#             ____
#                 b..
#             __ tries __ 3
#                 print('\nYou had 5 tries! Logging out!')
#                 r_ ex..
#         new_password _ g.. ('Please enter a new password: ')
#         w___ le. ? < 6
#             ? _ g..('Password should contains 6 or more characters! '
#                                  'please enter a new password: ')
#         ____.__p.. _ ?
#
#     ___ administrator_set_password ____ password
#         w___ le. ? < 6
#             ? _ g... ('Passord should contains 6 or more characters!'
#                                    ' please enter a new passwor: ')
#         ____.__p.. _ ?
#
#
# c_ Student P..
#     number_of_students _ 0
#
#     ___ - ____ f_name l_name age password grade speciality group_number m_name_''
#         s__.- f_name l_name age password m_name
#         ____.__g.. _ ?.u..
#         ____.__s.. _ ?.u..
#         ____.__g.. _ ?
#         ____.__id _ 'STD'+'_'+____.__g.. 0 3 +'_'+____.__s.. 0 3 +'_'+\
#                     st. ____.__g.. +'_'+st. ____.nu..
#         ____.__maths _ N..
#         ____.__informatics _ N..
#         ____.__electronics _ N..
#
#     ___ get_id ____
#         r_ ____.__id
#
#     ___ set_id ____
#         ____.__id _ ____.__g.. 0 3 + '_' + ____.__s.. 0 3 + \
#                     '_' + st. ____.__g.. + '_' + st. ____.nu..
#
#     ___ get_grade ____
#         r_ ____.__g..
#
#     ___ set_grade ____ grade
#         __ ?.u.. no. __ 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH'
#             print('Wrong grade!')
#         ____
#             ____.__g.. _ ?.u..
#             ____.s_i.
#
#     ___ get_speciality ____
#         r_ ____.__s..
#
#     ___ set_speciality ____ speciality
#         __ ?.u.. no. __ 'PYTHON', 'JAVA', 'PHP'
#             print('Wrong speciality!')
#         ____
#             ____.__s.. _ ?.u..
#             ____.s_i.
#
#     ___ get_group_number ____
#         r_ ____.__g..
#
#     ___ set_group_number ____ group_number
#         __ ? no. __ ra.. 1 30
#             print('Group number out of ra..!')
#         ____
#             ____.__g.. _ ?
#             ____.s_i..
#
#
#     ___ get_maths ____
#         r_ ____.__ma..
#
#     ___ set_maths ____ maths
#         __ 20 >_ ? >_ 0
#             ____.__m.. _ ?
#         ____
#             r_ 'The marks is out of ra..!'
#
#     ___ get_informatics ____
#         r_ ____.__i..
#
#     ___ set_informatics____ informatics
#         __ 20 >_ ? >_ 0
#             ____.__i.. _ ?
#         ____
#             r_ 'The marks is out of ra..'
#
#     ___ g_e.. ____
#         r_ ____.__e..
#
#     ___ set_electronics ____ electronics
#         __ 20 >_ ? >_ 0
#             ____.__e.. _ ?
#         ____
#             r_ 'The mark is out of ra..'
#
#     ___ get_average ____
#         __ ____.__m.. an. ____.__i.. an. ____.__e..
#             print(____.g_f_n ____.g_l_n en._': ')
#             r_ ro.. ____.__m.. + ____.__i.. + ____.__e..) / 3, 2)
#         ____
#             print('Maths: ', ____.g_m.
#             print('Informatics: ', ____.g_i.
#             print('Electronics: ', ____.g_e.
#             r_ "Student doesn't have all the marks!"
#
#     ___ define ____
#         __ ____.g_m_n.
#             print('Student',____.g_f_n. ____.g_l_n. ____.g_m_n. '- his ID is:'____.__id
#         ____
#             print('Student', ____.g_f_n. ____.g_l_n. '- his ID is:' ____.__id
#
#
# c_ Professor P..
#     number_of_professors _ 0
#
#     ___ - ____ f_name l_name age password grade speciality teaching_hours m_name_''
#         s__.- f_name l_name age password m_name
#         ____.__g.. _ g..
#         ____.__s.. _ s__.u..
#         ____.__id _ 'PRO' + '_' + st. ____.__g.. + '_' + ____.__s.. \
#                     + '_' + st. ____.nu..
#         ____.__t.. _ t..
#
#     ___ get_id ____
#         r_ ____.__i.
#
#     ___ set_id ____
#         ____.__id _ 'PRO' + '_' + st. ____.__g.. + '_' + ____.__s.. 0 3 + '_' + st. (
#             ____.nu..
#
#     ___ get_grade ____
#         r_ ____.__g..
#
#     ___ set_grade ____ grade
#         __ ? no. __ ra..1 6
#             print('Wrong grade!')
#         ____
#             ____.__g.. _ ?
#             ____.s_i.
#
#     ___ get_speciality ____
#         r_ ____.__s..
#
#     ___ set_speciality ____ speciality
#         __ ?.u.. no. __ 'MATHS', 'INFORMATICS', 'ELECTRONICS'
#             print('Wrong speciality!')
#         ____
#             ____.__s.. _ ?.u..
#             ____.s_i.
#
#     ___ get_teaching_hours ____
#         r_ ____.__te..
#
#     ___ set_teaching_hours ____ teaching_hours
#         __ 5 <_ ? <_ 25
#             ____.__t.. _ ?
#         ____
#             print('Teaching hours out of ra..!')
#
#     ___ get_salary ____
#         basic_salary _ 2000
#         print('The salary of the professor', ____.g_f_n.. ____.g_l_n.. 'is: ', en._''
#         salary _ st. ro.. b.. + ____.g_g. / 100 * |? +
#                             ____.__t.. * 20), 2)) + '$'
#         r_ ?
#
#     ___ define ____
#         __ ____.g_m_n.
#             print('Professor', ____.g_f_n.. ____.g_l_n.. ____.g_m_n..
#                   '- his ID is:',____.__id
#         ____
#             print('Professor', ____.g_f_n. ____.g_l_n. '- his ID is:', ____.__id
#
#
# c_ Administrator P..
#     number_of_administrators _ 0
#
#     ___ - ____ f_name l_name age password grade speciality m_name_''
#         s__.- f_name l_name age password m_name
#         ____.__g.. _ g..
#         ____.__s.. _ s...u..
#         ____.__id _ 'ADM' + '_' + st. ____.__g.. + '_' + ____.__s.. 0 3 + '_' + st. (
#             ____.nu..
#
#     ___ get_id ____
#         r_ ____.__i.
#
#     ___ set_id ____
#         ____.__id _ 'ADM' + '_' + st. ____.__g.. + '_' + ____.__s.. 0 3 + '_' + st.(
#             ____.nu..
#
#     ___ get_grade____
#         r_ ____.__g..
#
#     ___ set_grade ____ grade
#         __ ? no. __ ra..(1, 6
#             print('Wrong grade!')
#         ____
#             ____.__g.. _ ?
#             ____.s_i.
#
#     ___ get_speciality____
#         r_ ____.__s..
#
#     ___ set_speciality ____ speciality
#         __ ?.u.. no. __ ('STUDENTS', 'PROFESSORS', 'ADMINS'):
#             print('Wrong speciality!')
#         ____
#             ____.__s.. _ ?.u..
#             ____.s_i.
#
#     ___ get_salary ____
#         basic_salary _ 3000
#         print('The salary of the administrator', ____.g_f_n.. ____.g_l_n.. 'is:', en._' ')
#         salary _ st. ro.. b.. + ____.g_g. / 100) *
#                             (b.. 2|| + '$'
#         r_ ?
#
#     ___ define ____
#         __ ____.g_m_n.
#             print('Administrator', ____.g_f_n.. ____.g_l_n..
#                   ____.g_m_n.. '- his ID is:' ____.__i.
#         ____
#             print('Administrator', ____.g_f_n.. ____.g_l_n..
#                   '- his ID is:', ____.__i.
#
#
# ___ student_menu logged_member: S..
#     print('Please select an operation:'
#           '\n\t1)Change your password'
#           '\n\t2)Check your mark'
#           '\n\t3)Check your average')
#     operation _ in. in..
#     w___ ? no. __ ra.. 1 4
#         ? _ in.. ('Wrong operation! please an operation again: ')
#     __ ? __ 1
#         l__.set..
#     ____ ? __ 2
#         print('Maths mark:', l__.g_m..,
#               '\nInformatics mark:', l__.g_i..
#               '\nElectronics mark:', l__.g_e..
#     ____
#         l__.get_average
#     r_ student_menu l__
#
#
# ___ professor_menu(l__: P..
#     print('Please select an operation:'
#           '\n\t1)Change your password'
#           '\n\t2)Check students list'
#           '\n\t3)Set students marks'
#           '\n\t4)Get students marks')
#     operation _ in. in..
#     w___ ? no. __ ra.. 1 5
#         ? _ in.. ('Wrong operation! please eneter an operation again: ')
#     __ ? __ 1
#         l__.s_p..
#     ____ ? __ 2
#         g_m_l.. me.. 0
#     ____ ? __ 3
#         student_number _ g_m_n.. me.. 0
#         mark _ in. in..('Please enter the mark: '))
#         w___ ? no. __ ra..0, 21
#             ? _ in. in..'Mark out of ra..! please enter the mark again: '))
#         {
#             'MATHS': m.. 0 s_n.|.s_m.
#             'INFORMATICS': m.. 0| s_n.|.s_i.
#             'ELECTRONICS': m..[0][s_n.].s_i.
#         }[l__.g_s.. m..
#     ____
#         i _ 1
#         __ l__.g_s. __ 'MATHS':
#             ___ student __ m.. 0
#                     print(st. i + ')' + s__.g_f_n. s__.g_l_n.
#                           s__.g_m_n. '\t\t', s__.g_m.
#                     i +_ 1
#         ____ l__.g_s. __ 'INFORMATICS':
#             ___ student __ m.. 0
#                     print(st. i + ')' + s__.g_f_n. s__.g_l_n.
#                           s__.g_m_n. '\t\t', s__.g_i..
#                     i +_ 1
#         ____
#             ___ student __ m.. 0
#                 print(st. i + ')' + s__.g_f_n. s__.g_l_n.
#                       s__.g_m_n. '\t\t' s__.g_e..
#                 i +_ 1
#     r_ professor_menu l__
#
#
# ___ g_m_l.. members_list
#     i _ 1
#     ___ member __ ?
#         print(st. i +')'+ m__.g_f_n.
#               m__.g_l_n. m___.g_m_n.
#         i +_ 1
#
#
# ___ get_members_details members_list
#     i _ 1
#     ___ member __ ?
#         print(st. i + ')', en._ '')
#         m___.de..
#         i +_ 1
#
#
# ___ set_person_data keyword person: P.. data
#     __ k.. __ 'first_name'
#         p__.s_f_n. d..
#     ____ k.. __ 'last_name'
#         p__.s_l_n. d..
#     ____ k.. __ 'middle_name'
#         p__.s_m_n. d..
#     ____ k.. __ 'age'
#         p__.s_a. in. d..
#     ____ k.. __ 'email'
#         p__.s_e. d..
#     ____ k.. __ 'password'
#         p__.a_s_p. d..
#
#
# ___ get_member_number members_list
#     print('Please enter the number of the @: ' @
#           ('student' __ m_l.. __ m.. 0 ____
#             'professor' __ m_l. __ m.. 1 ____
#             'administrator'), en._''
#     member_number _ in. in..)) - 1
#     w___ ? no. __ ra..(0, le. m_l.
#         member_number _ in. in..'Number out of ra..! '
#                                   'please enter the number again: ')) - 1
#     r_ ?
#
#
# ___ add_member members_list
#     print('Please enter the data of the @: ' @
#           ('student' __ m_l. __ m.. 0 ____
#            'professor' __ m_l. __ m.. 1 ____
#            'administrator'))
#     __ m_l. __ m.. 0
#         member _ S.. 'a', 'a', 7, 'a', 'a', 'a', 11
#         ?.s_g_n.. in. in..'Enter group number: '
#     ____ m_l. __ m.. 1
#         member _ P.. 'a', 'a', 7, 'a', 'a', 'a', 11
#         ?.s_t_h.. in. in..'Enter teaching hours: '
#     ____
#         member _ A.. 'a', 'a', 7, 'a', 'a', 'a'
#     ?.s_f_n. in. 'First_name: '
#     ?.s_l_n. in. 'Last_name: '
#     ?.s_a. in. in..'Age: '
#     ?.a_s_p. in. 'Enter password: '))
#     ?.s_g. in. 'Enter grade: ') __ m_l. __ m.. 0
#                      ____ in. in..'Enter grade: '
#     ?.s_s. in. 'Enter speciality: '
#     m_l..ap.. ?
#
#
# ___ student_administrator_menu(l__: A..
#     print('Please select an operation:'
#           '\n\t1)Change your password'
#           '\n\t2)Check students list'
#           '\n\t3)Set student first name'
#           '\n\t4)Set student last name'
#           '\n\t5)Set student middle name'
#           '\n\t6)Set student age'
#           '\n\t7)Set student email'
#           '\n\t8)Set student password'
#           '\n\t9)Set student grade'
#           '\n\t10)Set student speciality'
#           '\n\t11)Set student group number'
#           '\n\t12)Get students averages'
#           '\n\t13)Get students details'
#           '\n\t14)Add a new student'
#           '\n\t@' @ '15)Back to the admin menu' __ l__.g_s. __ 'ADMINS' ____ '')
#     operation _ in. in..'> '
#     w___ ? no. __ ra.. 1 16
#         ? _ in. in..'Wrong operation! please enter an operation again: '))
#     __ ? __ 1
#         l__.s_p..
#     ____ ? __ 2:
#         g_m_l.. m.. 0
#     ____ ? __ ra.. 3 9
#         s_n. _ g_m_n.. m.. 0
#         data _ in.. 'Please enter the data that you want to set: '
#         s_p_d.('first_name' __ ? __ 3
#                         ____ 'last_name' __ ? __ 4
#         ____ 'last_middle' __ ? __ 5
#         ____ 'age' __ ? __ 6
#         ____ 'email' __ ? __ 7
#         ____ 'password', m.. 0 |s_n. ,
#                         d..)
#     ____ ? __ ra.. 9 12
#         s_n. _ g_m_n.. m.. 0
#         data _ in.. ('Please enter the data that you want to set: ')
#         {
#             9: m.. 0 |s_n.|.s_g..
#             10: m.. 0 |s_n.|.s_s..
#             11: m.. 0 |s_n.|.s_g_n..
#         }|?| in. d.. __ ? __ 11 ____ d..
#     ____ ? __ 12
#         s_n. _ g_m_n.. m.. 0
#         print(m.. 0 |s_n.| .g_a..
#     ____ ? __ 13
#         g_m_d.. m.. 0
#     ____ ? __ 14
#         a_m. m.. 0
#     ____
#         __ l__.g_s. __ 'ADMINS':
#             a_m. l__
#         ____
#             print('Wrong operation! please enter an operation again: ')
#     r_ s_a_m.. l__
#
#
# ___ professor_administrator_menu l__
#     print('Please select an operation:'
#           '\n\t1)Change your password'
#           '\n\t2)Check professors list'
#           '\n\t3)Change professor first name'
#           '\n\t4)Change professor last name'
#           '\n\t5)Change professor middle name'
#           '\n\t6)Change professor age'
#           '\n\t7)Change professor email'
#           '\n\t8)Change professor password'
#           '\n\t9)Change professor grade'
#           '\n\t10)Change professor speciality'
#           '\n\t11)Change professor teaching hours'
#           '\n\t12)Check professor salary'
#           '\n\t13)Check professors details'
#           '\n\t14)Add a new professor'
#           '\n\t%s' % '15)Back to the admin menu'
#           __ l__.g_s. __ 'ADMINS' ____ '')
#     operation _ in. in..'> '
#     w___ ? no. __ ra.. 1 15
#         ? _ in. in..'Wrong operation! please enter an operation again: '
#     __ ? __ 1
#         l__.s_p..
#     ____ ? __ 2
#         g_m_l.. m.. 1
#     ____ ? __ ra.. 3 9
#         professor_number _ g_m_n.. m.. 1
#         data _ in.. ('Please enter the data that you want to set: ')
#         s_p_d..('first_name' __ ? __ 3
#                         ____ 'last_name' __ ? __ 4
#                         ____ 'middle_name' __ ? __ 5
#                         ____ 'age' __ ? __ 6
#                         ____ 'email' __ ? __ 7
#                         ____ 'password', m.. 1 |p_n. ,
#                         d..)
#     ____ ? __ ra.. 9 12
#         professor_number _ g_m_n.. m.. 1
#         data _ in..('Please enter the data that you want to set: ')
#         {
#             9: m.. 1 |p_n..|.s_g..
#             10: m.. 1 |p_n..|.s_s..,
#             11: m.. 1 |p_n..|.s_t_h..,
#         }|?| d.. __ ? __ 10 ____ in. d..
#     ____ ? __ 12
#         professor_number _ g_m_n.. m.. 1
#         print(m.. 1 |?|.g_s.
#     ____ ? __ 13
#         g_m_d.. m.. 1
#     ____ ? __ 14
#         a_m.. m.. 1
#     ____
#         __ l__.g_s. __ 'ADMINS'
#             a.._m.. l__
#         ____
#             print('Wrong operation! please enter an operation again: ')
#     r_ p_a_m.. l_
#
#
# ___ admins_menu logged_member: A..
#     print('Please select what you want to manage:'
#           '\n\t1)Manage Administrators'
#           '\n\t2)Manage Professors'
#           '\n\t3)Manage Students')
#     manage _ in. in..'> '
#     w___ ? no. __ 1, 2, 3
#         ? _ in. in..'Wrong choice! Please select what you want to manege an other time: '))
#     ___ a_a_m.. l__: A..
#         print('Please select an operation:'
#               '\n\t1)Change your password'
#               '\n\t2)Check administrators list'
#               '\n\t3)Change administrator first name'
#               '\n\t4)Change administrator last name'
#               '\n\t5)Change administrator middle name'
#               '\n\t6)Change administrator age'
#               '\n\t7)Change administrator email'
#               '\n\t8)Change administrator password'
#               '\n\t9)Change administrator grade'
#               '\n\t10)Change administrator speciality'
#               '\n\t11)Check administrator salary'
#               '\n\t12)Check administrators details'
#               '\n\t13)Add a new administrator'
#               '\n\t@' @ '14)Back to the admin menu' __ l__.g_s. __ 'ADMINS'
#               ____ '')
#         operation _ in. in..'> '
#         w___ ? no. __ ra.. 1 15
#             ? _ in. in..'Wrong operation! please enter an operation again: '))
#         __ ? __ 1
#             l__.s_p..
#         ____ ? __ 2
#             g_m_l.. m.. 2
#         ____ ? __ ra.. 3 9
#             administrator_number _ g_m_n.. m.. 2
#             data _ in.. 'Please enter the data that you want to set: ')
#             s_p_d..('first_name' __ ? __ 3
#                             ____ 'last_name' __ ? __ 4
#                             ____ 'middle_name' __ ? __ 5
#                             ____ 'age' __ ? __ 6
#                             ____ 'email' __ ? __ 7
#                             ____ 'password', m.. 2 |a_n..,
#                                             d..)
#         ____ ? __ ra.. 9 11
#             a_n.. _ g_m_n..(m.. 2
#             data _ in..('Please enter the data that you want to set: ')
#             {
#                 9: m.. 2 |a_n.|.s_g..,
#                 10: m.. 2 |a_n.|.s_s..,
#             }|?| d.. __ ? __ 10 ____ in. d..
#         ____ ? __ 11
#             administrator_number _ g_m_n.. m.. 2
#             print(m.. 2|a_n.|.g_s..
#         ____ ? __ 12
#             g_m_d.. m.. 2
#         ____ ? __ 13
#             a_m.. m..2
#         ____
#             __ l__.g_s. __ 'ADMINS'
#                 a_m. l__
#             ____
#                 print('Wrong operation! please enter an operation again: ')
#         r_ a_a_m.. l__
#     {
#         1: a_a_m..
#         2: p_a_m
#         3: s_a_m
#     }|m..|l__
#
#
# members _ S..('jalil', 'benharkat', 22, 'hhhhhh', 'first', 'python', 10
#             P..('Taher', 'Mayssoum', 30, '123456789', 5, 'MATHS', 25
#             A..('Moussa', 'Lhaj', 35, '1234', 5, 'admins'
# print("\t\t\t\t\t\t\t\t**Welcome to our School System**\n\nPlease enter your profession:\n\t1)Student"
#       "\n\t2)Professor\n\t3)Administrator")
# profession _ in. in..)) - 1
# w___ ?+1 no. __ ra..(1, 4):
#     ? _ in..('Wrong choice! Please enter your profession again: ')
# l__ _ N..
# w___ no. l__
#     email _ in..('Please enter your Email aderess: ')
#     ___ member __ m..|?
#         __ ?.g_e. __ e..
#             password _ ge.. ('Please your password: ')
#             ___ i __ ra.. 4
#                 __ p... __ m___.g_p..
#                     print('Hello',m__.g_f_n. m__.g_l_n..
#                     l__ _ m..
#                     b..
#                 ____
#                     p.. _ ge..('Wrong password! Enter your password again: ')
#             b..
#     __ no. l__
#         print('Incorrect information')
# __ p.. __ 0
#     s_m.. l_
# ____ p.. __ 1
#     p_m. l__
# ____
#     __ l__.g_s.  __ 'STUDENTS'
#         s_a_m.. l__
#     ____ l__.g_s. __ 'PROFESSORS'
#         p_a_m.. l__
#     ____ l__.g_s. __ 'ADMINS':
#         a_m.. l__
#     ____
#         print('Administrator with a wrong specialit!')
#
# #on the administrators menu __ the w___ loop in. in..))
# #line 256 grade no. grade.upper///add to all the classes the
# # last choice and change the ra..-loop
# #and add the ____ statement at the end///
#
# ___ admins_menu logged_member: A...
#     print('Please select what you want to manage:'
#           '\n\t1)Manage Administrators'
#           '\n\t2)Manage Professors'
#           '\n\t3)Manage Students')
#     manage _ in. in..'> '
#     w___ ? no. __ 1, 2, 3
#         m.. _ in. in..'Wrong choice! Please select what you want to manege an other time: '))
#     ___ a_a_m.. l__: A..
#         print('Please select an operation:'
#               '\n\t1)Change your password'
#               '\n\t2)Check administrators list'
#               '\n\t3)Change administrator first name'
#               '\n\t4)Change administrator last name'
#               '\n\t5)Change administrator middle name'
#               '\n\t6)Change administrator age'
#               '\n\t7)Change administrator email'
#               '\n\t8)Change administrator password'
#               '\n\t9)Change administrator grade'
#               '\n\t10)Change administrator speciality'
#               '\n\t11)Check administrator salary'
#               '\n\t12)Check administrators details'
#               '\n\t13)Add a new administrator'
#               '\n\t14)Back to the professions menu')
#         operation _ in. in..'> '
#         w___ ? no. __ ra.. 1, 15
#             ? _ in. in..'Wrong operation! please enter an operation again: '))
#         __ ? __ 1
#             l__.s_p..
#         ____ ? __ 2
#             g_m_l..(m.. 2
#         ____ ? __ ra.. 3 9
#             administrator_number _ g_m_n.. m.. 2
#             data _ in.. ('Please enter the data that you want to set: ')
#             s_p_d..('first_name' __ ? __ 3
#                             ____ 'last_name' __ ? __ 4
#                             ____ 'middle_name' __ ? __ 5
#                             ____ 'age' __ ? __ 6
#                             ____ 'email' __ ? __ 7
#                             ____ 'password', m.. 2 |a_n.|,
#                                             d..)
#         ____ ? __ ra.. 9 11
#             a_n.. _ g_m_n.. m.. 2
#             data _ in..('Please enter the data that you want to set: ')
#             {
#                 9: m.. 2 |a_n.|.s_g..
#                 10: m.. 2 |a_n.|.s_s..
#             }|?| d.. __ ? __ 10 ____ in. d..
#         ____ ? __ 11
#             a_n.. _ g_m_n.. m.. 2
#             print(m.. 2 |a_n.|.g_s..
#         ____ ? __ 12
#             get_members_details m.. 2
#         ____ ? __ 13
#             a_m.. m.. 2
#         ____
#             admins_menu l__
#         r_ a_a_m.. l__
#     {
#         1: a_a_m..
#         2: p_a_m..
#         3: s_a_m..
#     } m..|  l_m..
