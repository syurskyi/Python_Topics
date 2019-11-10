# Specifying multiple decorators

# ___ deco1 f
#     print("Вызвана функция deco1()")
#     r_ f
# ___ deco2 f
#     print("Вызвана функция deco2()")
#     r_ f
# _deco1
# _deco2
# ___ func x
#     r_  x = _0_.f_ x
# print(f_(10))
#
# print()
# ######################################################################################################################
# Access restriction using decorator

# passw i_ Введите пароль:
#
# ___ test_passw
#     ___ deco f
#         i_ p == "10":  # Сравниваем пароли
#             r_ f
#         e_
#             r_ l_ "Доступ закрыт"
#
#     r_ d_  # Возвращаем функцию-декоратор
#
# _test_passw passw
# ___ func
#     ___ "Доступ открыт"
#
# print(f_())  # Вызываем функцию
#
# print()

# ######################################################################################################################
# decorator
#
# ___ decorator fn
#     """Пример декоратора"""
#
#     ___ decorated_fn _args __kwargs
#         """Модифицированная функция"""
#
#         print Decorated function says:
#         fn _args __kwargs  # вызов изначальной функции
#         print()
#
#     r_ decorated_fn
#
# _d
# ___ hello
#     print Hello!
#
# # Вызов декорированной функции
# hello()
#
# print()
# ######################################################################################################################
# Пример создания декоратора с параметром

# ___ cast_result type_
#     """Пример создания декоратора с параметром"""
#
#     ___ cast_decorator function
#         """Сам декоратор"""
#
#         ___ decorated_function _args __kwargs
#             result _ function _args __kwargs
#             r_ type_ result
#
#         r_ decorated_function
#
#     r_ cast_decorator
#
# _cast_result float
# ___ add x y
#     r_ x + y
#
# print add(2, 3)
#
# import decimal
#
# _cast_result repr
# _cast_result d_.D_
# ___ div x y
#     r_ x / y
#
# print div(3, 2)
#
# print()

# ######################################################################################################################
# call that counter function a decorator.

# ___ counter fn
#     count _ 0
#
#     ___ inner _args __kwargs
#         no__
#         co__
#         co__ += 1
#         print('Function |0| was called |1| times'.f_fn.__n_ co__
#         r_ fn _args __kwargs
#
#     r_ inner
#
# _counter
# ___ mult a| float b| float _ 1 c| float _ 1) __ float
#     """
#     returns the product of a, b, and c
#     """
#     r_ a * b * c
#
# mult 1 2 3
# mult 2 2 2
#
# # Let's do a little bit of introspection on our two decorated functions:
#
# add.__n_
# mult.__n_
#
# print()
# ######################################################################################################################
# We can use a special function in the functools module, called wraps. In fact, that function is a decorator itself!

# f_ f_ i_ w_
#
# ___ counter fn
#     count _ 0
#
#     _wraps fn
#     ___ inner _args __kwargs
#         no__
#         co__
#         co__ += 1
#         print("|0| was called |1| times".f_ fn.__n_ co__
#
#     r_ inner
#
# _counter
# ___ add a| int__ b| int _ 10 __ int
#     """
#     returns sum of two integers
#     """
#     r_ a + b
#
# i_.g_ add
# i_.s_ add
# i_.s_ add.p_
#
# print()

# ######################################################################################################################
# Simulating a simple Switch in Python

# ___ dow_switch_fn dow
#     __ dow __ 1
#         fn _ l_: print Monday
#     e__ dow __ 2
#         fn _ l_: print Tuesday
#     e__ dow __ 3
#         fn _ l_: print Wednesday
#     e__ dow __ 4:
#         fn _ l_: print Thursday
#     e___ dow __ 5:
#         fn _ l_: print Friday
#     e___ dow __ 6:
#         fn _ l_: print Saturday
#     e___ dow == 7:
#         fn = l_: print Sunday
#     e___
#         fn = l_: print Invalid day of week
#
#     r_ fn()
#
# dow_switch_fn 1
# dow_switch_fn 100
#
# print()
# ######################################################################################################################
# Simulating a simple Switch in Python
# dictionaries could also be used quite effectively here:

# ___ dow_switch_dict dow
#     dow_dict _ {
#         1: l_: print Monday
#         2: l_: print Tuesday
#         3: l_: print Wednesday
#         4: l_: print Thursday
#         5: l_: print Friday
#         6: l_: print Saturday
#         7: l_: print Sunday
#         'default': l_: print Invalid day of week
#     }
#
#     r_ dow_dict.g_ dow dow_d_|_default_|
#
# dow_switch_dict 1
# dow_switch_dict 100
#
# print()
# ######################################################################################################################
# Simulating a simple Switch in Python
# recall our own implementation of the @singledispatch decorator:
#
# ___ switcher fn
#     registry _ d_
#     registry|_default_| _ fn
#
#     ___ register case
#         ___ inner fn
#             registry|case| _ fn
#             r_ fn  # we do this so we can stack register decorators!
#
#         r_ inner
#
#     ___ decorator case
#         fn _ registry.g_ case registry|_default_|
#         r_ fn()
#
#     decorator.register _ register
#     r_ decorator
#
# _switcher
# ___ dow
#     print Invalid day of week
#
# _dow.register 1
# ___ dow_1(
#     print Monday
#
# dow.r_(2)(l_| print Tuesday
# dow.r_(3)(l_| print Wednesday
# dow.r_(4)(l_| print Thursday
# dow.r_(5)(l_| print Friday
# dow.r_(6)(l_| print Saturday
# dow.r_(7)(l_| print Sunday
#
# dow(1)
# dow(2)
# dow(100)
#
# print()

# ######################################################################################################################
# Introduction to Decorators
# be_polite

# ___ be_politefn
#     ___ wrapper
#         print "What a pleasure to meet you!"
#         fn()
#         print Have a great day!
#     r_ wr__
#
# ___ greet
#     print My name is Colt.
#
# ___ rage
#     print I HATE YOU!
#
# # we are decorating our function
# # with politeness!
#
# greet _ be_polite greet
#
# polite_rage _ be_polite rage
# polite_rage()
#
# print()
# ######################################################################################################################
# Introduction to Decorators_decorate-syntax - be polite

# ___ be_polite fn
#     ___ wrapper
#         print What a pleasure to meet you!
#         fn()
#         print Have a great day!
#     r_ wr___
#
# _be_polite
# ___ greet
#     print My name is Colt.
#
# _be_polite
# ___ rage
#     print I HATE YOU!
#
# greet()
# rage()
#
# print()
# # ######################################################################################################################
#  Decorators With Different Signatures
# shout example

# ___ shout fn
#     ___ wrapper _args __kwargs
#         r_ fn _args __kwargs.u_
#     r_ wr__
#
# _shout
# ___ greet name
#     r_ f"Hi, I'm |name|."
#
# _shout
# ___ order main side
#     r_ _"Hi, I'd like the |main|, with a side of |side|, please."
#
# _shout
# ___ lol
#     r_ "lol"
#
# print greet("todd")
# print(order(side_"burger" main_"fries"))
# print(lol())
#
# print()
# # ######################################################################################################################
# Using Wraps To Preserve Metadata

# f_ f_ i_ w_
#
# ___ log_function_data fn
#     _wraps fn
#     ___ wrapper _args __kwargs
#         """I AM WRAPPER FUNCTION"""
#         print _"you are about to call |fn.__n_|"
#         print _"Here's the documentation: |fn.__d_|")
#         r_ fn _args __kwargs
#     r_ wr_
#
# _log_function_data
# ___ add x y
#     """Adds two numbers together."""
#     r_ x + y
#
# print add.__d_
# print(add.__n_
# help add
#
# print()
# ######################################################################################################################
# Building A Speed-Test Decorator

# f_ f_ i_ w_
# f_ t_ i_ t_
#
# ___ speed_test fn
#     _wraps fn
#     ___ wrapper _args __kwargs
#         start_time _ time
#         result _ fn _args __kwargs
#         end_time _ time
#         print _"Executing |fn.__n_|"
#         print _"Time Elapsed: |end_time - start_time|")
#         r_ res___
#     r_ wra___
#
# _speed_test
# ___ sum_nums_gen
#     r_ s_(x ___ x __ r_(90000000))
#
# _speed_test
# ___ sum_nums_list
#     r_ s_([x ___ x __ r_(90000000)])
#
# print sum_nums_gen
# print sum_nums_list
#
# print()
# ######################################################################################################################
# Another Example Ensuring Args With A Decorator
# f_ f_ i_ w_
#
# ___ ensure_no_kwargs fn
#     _wraps fn
#     ___ wrapper _args __kwargs
#         __ kwargs
#             ra___ V_E_ No kwargs allowed! sorry :(")
#         r_ fn _args __kwargs
#     r_ wra___
#
# _ensure_no_kwargs
# ___ greet name
#     print _"hi there |name|"
#
# greet name_"Tony"
#
# print()
# # ######################################################################################################################
# 290. Writing an ensure_first_arg_is Decorator_ensure-first-arg

# f_ f_ i_ w_
#
# ___ ensure_first_arg_is val
#     ___ inner fn
#         _wraps fn
#         ___ wrapper _args __kwargs
#             __ args a_ args|0| |- val
#                 r_ _ First arg needs to be |val|
#             r_ fn _args __kwargs
#         r_ wra___
#     r_ inn__
#
# _ensure_first_arg_is _burrito_
# ___ fav_foods _foods
#     print foods
#
# print fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
# print fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'
#
# _ensure_first_arg_is 10
# ___ add_to_ten num1 num2
#     r_ num1 + num2
#
# print(add_to_ten(10, 12))  # 12
# print(add_to_ten(1, 2))  # 'Invalid! First argument must be 10'
#
# print()
# ######################################################################################################################
# Enforcing Argument Types With A Decorator

# ___ enforce types
#     ___ decorator f
#         ___ new_func _args __kwargs
#             # convert args into something mutable
#             newargs _ ||
#             ___  a t __ z_ args types
#                newargs.a_(t(a))  # feel free to have more elaborated convertion
#             r_ f(_newargs __kwargs
#         r_ new_fu__
#     r_ dec__
#
# _enforce st in
# ___ repeat_msg msg times
#     ___ time __ r_ times
#         print msg
#
# _enforce fl_ fl_
# ___ divide a b
#     print a/b
# # repeat_msg("hello", '5')
#
# divide '1' '4'
#
# print()
# # ######################################################################################################################
# Using a @syntax
# user_has_permission

# user = {'username': 'jose123', 'access_level': 'guest'}
#
# ___ user_has_permission func
#     ___ secure_func
#         __ user.g_ 'access_level' __ 'admin'
#             r_ func
#     r_ se__f_
#
# _user_has_permission
# ___ my_function
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ 'Password for admin panel is 1234.'
#
# _user_has_permission
# ___ another
#     pass
#
# print my_function.__n_
# print another.__n_
#
# print()
# ######################################################################################################################
# Functools wraps in Python
# user_has_permission

# i_ f_
#
# user = {'username': 'jose123', 'access_level': 'guest'}
#
# ___ user_has_permission func
#     _fun___.w_ func
#     ___ secure_func
#         __ user.g_('access_level') __ 'admin'
#             r_ func
#     r_ se__fu_
#
# _user_has_permission
# ___ my_function
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ 'Password for admin panel is 1234.'
#
# _user_has_permission
# ___ another
#     pass
#
# print my_fu_.__n_
# print ano__.__n_
#
# print()
# ######################################################################################################################
# Decorating functions with parameters
# user_has_permission

# i_ f_
#
# user = {'username': 'jose123', 'access_level': 'admin'}
#
# ___ user_has_permission func
#     _func___.wr_ func
#     ___ secure_func panel
#         __ user.g__ 'access_level') __ 'admin'
#             r_ func panel
#     r_ sec__fu_
#
# _user_has_permission
# ___ my_function panel
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ _'Password for |panel| panel is 1234.'
#
# print my_fun_.__n_
#
# print my_fun__ movies
#
# print()
# ######################################################################################################################
# Decorators with parameters
# user_has_permission

# i_ f_
#
# user = {'username': 'jose123', 'access_level': 'user'}
#
# ___ user_has_permission access_level
#     ___ my_decorator func
#         func__.wr__ func
#         ___ secure_func panel
#             __ user.g__('access_level') __ access_level
#                 r_ func panel
#         r_ secure_func
#     r_ my_decorator
#
# _user_has_permission 'user'
# ___ my_function panel
#     """
#     Allows us to retrieve the password for the admin panel.
#     """
#     r_ _'Password for |panel| panel is 1234.'
#
# print(my_function.__n_
# print(my_function('movies'))
#
# print()
# ######################################################################################################################
# #  Generic decorators for any function
# # user_has_permission
#
# # i_ f_
# #
# # user = {'username': 'jose123', 'access_level': 'admin'}
# #
# # ___ user_has_permission func
# #     _fun___.wr__ func
# #     ___ secure_func _args __kwargs
# #         __ user.g_('access_level') __ 'admin'
# #             r_ func _args __kwargs
# #     r_ secure_func
# #
# # _user_has_permission
# # ___ my_function panel
# #     """
# #     Allows us to retrieve the password for the admin panel.
# #     """
# #     r_ _'Password for |panel| panel is 1234.'
# #
# # _user_has_permission
# # ___ another
# #     pass
# #
# # print(my_function.__n_
# #
# # print(my_function('movies'))
# # print(another())
# #
# # print()