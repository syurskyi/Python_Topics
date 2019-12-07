# # -*- coding: utf-8 -*-
#
# """
# isi.... obj, cls) проверяет, является ли obj экземпляром класса cls
# или класса, который является наследником класса cls
# """
#
# print isi.... 8, in.   # True
# print isi.... 'str', in.   # False
# print isi.... T..., bo..   # True
# print isi.... T..., in.   # True, так как bool -- подкласс int
# print isi.... 'a string', ob..   # True, всё является объектами
# print isi.... N... ob..   # True, даже None
# print isi.... F... st.  # False
# print isi.... in., ty..   # True, любой класс -- объект-экземпляр метакласса type
# print isi.... 42, ty..   # False, 42 -- это не тип данных
