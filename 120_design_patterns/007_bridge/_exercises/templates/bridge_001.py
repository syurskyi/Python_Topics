# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# # Example of `bridge' design pattern
# # This code is part of http://wp.me/p1Fz60-8y
# # Copyright (C) 2011 Radek Pazdera
#
# # This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# # the Free Software Foundation, either version 3 of the License, or
# # (at your option) any later version.
#
# # This program is distributed in the hope that it will be useful,
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# # GNU General Public License for more details.
#
# # You should have received a copy of the GNU General Public License
# # along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#
# c_ AbstractInterface
#     """ Target interface.
#     This is the target interface, that clients use.
#     """
#
#     ___ someFunctionality
#         r_ N..
#
#
# c_ Bridge AI..
#     """ Bridge class.
#
#     This class forms a bridge between the target
#     interface and background implementation.
#     """
#
#     ___ -
#         __implementation _ N..
#
#
# c_ UseCase1 B..
#     """ Variant of the target interface.
#     This is a variant of the target Abstract interface.
#     It can do something little differently and it can
#     also use various background implementations through
#     the bridge.
#     """
#
#     ___ - implementation
#         __?  ?
#
#     ___ someFunctionality
#         print("UseCase1: ", __?.aF..
#
#
# c_ UseCase2 B..
#     ___ - implementation
#         __?  ?
#
#     ___ someFunctionality
#         print("UseCase2: ", __?.aF..
#
#
# c_ ImplementationInterface
#     """ Interface for the background implementation.
#     This class defines how the Bridge communicates
#     with various background implementations.
#     """
#
#     ___ anotherFunctionality
#         r_ N...
#
#
# c_ Linux(II..
#     """ Concrete background implementation.
#     A variant of background implementation, in this
#     case for Linux!
#     """
#
#     ___ anotherFunctionality
#         print("Linux!")
#
#
# c_ Windows II..
#     ___ anotherFunctionality
#         print("Windows.")
#
#
# ___ main
#     linux _ L..
#     windows _ W..
#
#     # Couple of variants under a couple
#     # of operating systems.
#     useCase _ U_1 l..
#     ?.sF...
#
#     useCase _ UseCase1 w..
#     ?.sF...
#
#     useCase _ UseCase2 l..
#     ?.sF...
#
#     useCase _ UseCase2 w..
#     ?.sF...
#
#
# __ ______ __ ______
#     ?