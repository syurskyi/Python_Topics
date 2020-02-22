# ____ e.. ______ E..
# ____ ma.. ______ *
#
#
# c_ CoordinateSystem E..
#     CARTESIAN = 1
#     POLAR = 2
#
#
# c_ Point
#     # ___ __init__(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     ___ -s
#         r_ _*x: |.x , y: |.y '
#
#     # redeclaration won't work
#     # ___ __init__(self, rho, theta):
#
#     ___ - a b system_C__.C..
#         __ ? __ C___.C..
#             ?x _ a
#             ?y _ b
#         ____ system __ c___.P..
#             ?x _ a * sin(b)
#             ?y _ a * cos(b)
#
#         # steps to add a new system
#         # 1. augment CoordinateSystem
#         # 2. change init method
#
#     ??
#     ___ new_cartesian_point x y
#         r_ P.. x y
#
#     ??
#     ___ new_polar_point rho theta
#         r_ P.. ? * sin(t..  ? * cos(t..
#
#     c_ F..
#         ??
#         ___ new_cartesian_point x y)
#             r_ P.. x y
#
#     factory = F..
#
# # take out factory methods to a separate c_
# c_ PointFactory
#     ??
#     ___ new_cartesian_point x y
#         r_ P... x y
#
#     ??
#     ___ new_polar_point rho theta)
#         r_ P__ ? * sin(t.. ? * cos(t..
#
#
# __ _______ __ _____
#     p1 = P.. 2 3 C__.C..
#     p2 = PF_.n_c_p.. 1 2
#     # or you can expose factory through the type
#     p3 = P__.F__.n.. 5 6
#     p4 = P__.f__.n.. 7 8
#     print(p1, p2, p3, p4)
