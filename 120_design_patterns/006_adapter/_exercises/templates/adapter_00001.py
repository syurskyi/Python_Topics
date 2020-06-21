# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# # Example of `adapter' design pattern
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
# # along with this program. __ not, see <http://www.gnu.org/licenses/>.
#
#
# # Adaptee (source) interface
# c_ EuropeanSocketInterface
#     ___ voltage p..
#
#     ___ live p..
#
#     ___ neutral p..
#
#     ___ earth p..
#
#
# # Adaptee
# c_ Socket E..
#     ___ voltage
#         r_ 230
#
#     ___ live
#         r_ 1
#
#     ___ neutral
#         r_ -1
#
#     ___ earth
#         r_ 0
#
#
# # Target interface
# c_ USASocketInterface
#     ___ voltage p..
#
#     ___ live p..
#
#     ___ neutral p..
#
#
# # The Adapter
# c_ Adapter U..
#     __socket _ N...
#
#     ___  - socket
#         __?  ?
#
#     ___ voltage
#         r_ 110
#
#     ___ live
#         r_ __s__.l..
#
#     ___ neutral
#         r_ __s___.n..
#
#
# # Client
# c_ ElectricKettle
#     __power _ N..
#
#     ___ - power
#         __?  ?
#
#     ___ boil
#         __ __p__.v.. > 110
#             print "Kettle on fire!"
#         ____
#             __ __p...l.. __ 1 an. \
#                     __p__.n.. __ -1:
#                 print "Coffee time!"
#             ____
#                 print "No power."
#
#
# ___ main
#     # Plug in
#     socket = S..
#     adapter = A.. ?
#     kettle = E.. ?
#
#     # Make coffee
#     ?.b..
#
#     r_ 0
#
#
# __ __name__ == "__main__":
#     main()
