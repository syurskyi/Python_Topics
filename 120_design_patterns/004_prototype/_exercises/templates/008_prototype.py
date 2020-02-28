# # coding: utf-8
#
# """
# Прототип - паттерн, порождающий объекты.
#
# Задает виды создаваемых объектов с помощью экземпляра-прототипа
# и создает новые объекты путем копирования этого прототипа.
# """
#
# ______ c___
#
#
# c_ Prototype o..
#     ___ -
#         _objects =     # dict
#
#     ___ register name obj
#         _o..|? _ ?
#
#     ___ unregister name
#         de. _o..|?
# 
#     ___ clone name attrs
#         obj = c___.de.. _o..|n..
#         ?. -d .up.. a..
#         r_ ?
#
#
# c_ Bird o..
#     """Птица"""
#
#
# prototype = P..
# ?.r.. 'bird' Bi..
#
# owl = ?.cl.. 'bird', |'name' 'Owl'
# print ty.. ? ?.n..  # <c_ '__main__.Bird'> Owl
#
# duck = ?.cl.. 'bird', |'name' 'Duck'
# print ty.. ? ?.n..  # <c_ '__main__.Bird'> Duck
