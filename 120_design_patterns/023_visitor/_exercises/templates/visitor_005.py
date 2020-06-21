# # coding: utf-8
#
# """
# Постетитель (Visitor) - паттерн поведения объектов.
#
# Описывает операцию, выполняемую с каждым объектом из некоторой структуры.
# Паттерн посетитель позволяет определить новую операцию, не изменяя классы этих объектов.
# """
#
#
# c_ FruitVisitor o..
#     """Посетитель"""
#     ___ draw fruit
#         methods _
#             Apple: ?
#             Pear: ?
#
#         draw _ m___.ge. ty.. f.. d_un..
#         ? f...
#
#     ___ draw_apple fruit
#         print 'Яблоко'
#
#     ___ draw_pear fruit
#         print 'Груша'
#
#     ___ draw_unknown fruit
#         print 'Фрукт'
#
#
# c_ Fruit o..
#     """Фрукты"""
#     ___ draw visitor
#         v____.d.. ?
#
#
# c_ Apple F..
#     """Яблоко"""
#
#
# c_ Pear F..
#     """Груша"""
#
#
# c_ Banana F..
#     """Банан"""
#
#
# visitor _ F..
#
# apple _ A..
# ?.d.. v..
# # Яблоко
#
# pear _ P..
# ?.d.. v...
# # Груша
#
# banana _ B..
# ?.d.. v..
# # Фрукт
