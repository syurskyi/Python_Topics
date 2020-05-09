# ______ datetime
# ______ u___
# ______ u___.m..
#
#
# ___ sum_two_values a b
#     r_ a + b
#
#
# ___ power x n
#     r_ x ** n
#
#
# ___ concat_values $
#     result = ''
#     ___ item i_ args
#         r.. +_ st. ?
#     r_ r..
#
#
# ___ desc x y
#     i_ x __ 0
#         r____ V....('`x` should not be equeal 0')
#     r_ y / x
#
#
# c_ User
#     ___ test_method
#         r_ NotImplementedError
#
#
# c_ UserTestCase ?.?
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_sum_two_values_uncalled____ mocked_sum
#         a.F. m__.ca..
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_sum_two_values_called ____ mocked_sum
#         s_t_v(10, 20)
#         a.T.  m._s..c...
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_sum_two_values_called_with ____ mocked_sum
#         s_t_v(10, 20)
#         a.T.  m._s..c...
#         a..E.  m._s..call_count, 1
#         m._s..a_c_w (10, 20)
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_reset_mock  mocked_sum)
#         s_t_v 10, 20
#         s_t_v 10, 20
#         a.T. (m._s..c...)
#         a..E. (m._s..call_count, 2)
#         m._s.. a_c
#         m._s..a_c_w (10, 20)
#
#         m._s..r._m..
#
#         a..E. (m._s..call_count, 0)
#         a.F.(m._s..c...)
#         m._s..a_n_c
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_mock_call mocked_sum
#         s_t_v 10, 40
#         s_t_v 20, 50
#         s_t_v 30, 60
#         m._s..a_a_c 10, 40
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_mock_call_with mocked_sum
#         s_t_v 10, 40
#         m._s..a_c_w 10, 40
#
#         s_t_v 20, 50
#         m._s..a_c_w 20, 50
#
#         s_t_v 30, 60
#         m._s..a_a_c 30, 60
#
#     _u___.m_.p.. _5_m.s_t_v r.._v.._20
#     ___ test_mock_return_value_in_dec mocked_sum
#         result1 _ s_t_v 10, 40
#         result2 _ s_t_v 110, 140
#         result3 _ s_t_v 1110, 1140
#         a..E. _1, 20
#         a..E. _2, 20
#         a..E. _3, 20
#
#     _u___.m_.p.. _5_m.s_t_v
#     ___ test_mock_return_value_in_body  m._s.
#         m._s..return_value _ 20
#
#         result1 = s_t_v 10, 40
#         result2 = s_t_v 110, 140
#         result3 = s_t_v 1110, 1140
#         a..E. _1, 20
#         a..E. _2, 20
#         a..E. _3, 20
#
#     _u___.m_.p.. '_5_m.s_t_v'
#     ___ test_mock_side_effect mocked_sum
#         result _ 0
#
#         ___ res_func(x, y)
#             r_ r...
#
#         m._s..side_effect _ r._f.
#
#         a..E. s_t_v 110, 140), r..
#         a..E. s_t_v 10, 0), r..
#         a..E. s_t_v 300, 400), r..
#
#         raise_text _ 'Test exception'
#         m._s..side_effect _ V.... r...
#         w___ a.R. V....
#             s_t_v(10, 30)
#
#         m._s..side_effect _ V...., R..., Z
#
#         w__ a.R. V....
#             s_t_v 10, 30
#         w__ a.R. R...
#             s_t_v 10, 30
#         w__ a.R. Z...
#             s_t_v 10, 30
#
#         ___ res_func2(x, y)
#             print('Hey')
#             r_ u___.mo__.DE..
#
#         m._s..return_value _ 300
#         m._s..side_effect _ res_func2
#         a..E. (s_t_v(1, 2), 300)
#
#     ___ test_mock_return_value_in_body_with
#         w__ u___.m_.p..('_5_m.s_t_v') as m._s.
#             m._s..return_value _ 20
#             result1 _ s_t_v 10, 40
#             result2 _ s_t_v 110, 140
#             result3 _ s_t_v 1110, 1140
#             a..E. _1, 20
#             a..E. _2, 20
#             a..E. _3, 20
#
#     ___ test_mock_builtin
#         w__ u___.m_.p..('datetime.datetime') as mocked_datetime
#             actual_date _ d.t_.d.t.(2019, 1, 1, 23, 8, 6)
#
#             mocked_datetime.now.return_value = actual_date
#             result1 = d.t_.d.t_.n..
#             ____.a..E. _1 ac._d.
#
#     _u___.m_.p...object U.. 'test_method')
#     ___ test_user mo._me.
#         mock_method.return_value _ 10
#         user _ ?
#         ?.t_m..
#         ____.a.T. mock_method.c...
#         m_m_.a_c_o..
