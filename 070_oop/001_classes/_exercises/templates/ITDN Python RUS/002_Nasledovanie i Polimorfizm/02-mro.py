# # -*- coding: utf-8 -*-
#
# """
# Порядок разрешения методов при ромбовидном множественном наследовании
# """
#
# c_ A o...
#     ___ method ____
#         print('A method')
#
#
# c_ B ?
#     p_
#
#
# c_ C ?
#     ___ method ____
#         print('C method')
#
#
# c_ D B C
#     p_
#
#
# obj = D
# ?.m..  # 'C method'
