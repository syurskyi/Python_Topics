# #Virtual Topology– Section 3: Process Based Parallelism
# ____ mpi4py ______ MPI
# ______ numpy as np
#
# UP _ 0
# DOWN _ 1
# LEFT _ 2
# RIGHT _ 3
# neighbour_processes _ [0,0,0,0]
# __ _______ __ "__main__":
#     comm _ MPI.COMM_WORLD
#     rank _ comm.rank
#     size _ comm.size
#
#     grid_rows _ in.(np.floor(np.sqrt(comm.size)))
#     grid_column _ comm.size // grid_rows
#
#
#     __ grid_rows*grid_column > size:
#         grid_column -_ 1
#     __ grid_rows*grid_column > size:
#         grid_rows -_ 1
#
#     __ (rank __ 0) :
#         print("Building a @d x @d grid topology:"\
#               @ (grid_rows, grid_column) )
#
#
# #Bidimensional MxN Mesh
# ##    cartesian_communicator = comm.Create_cart( (grid_rows, grid_column), periods=(False, False), reorder=True)
# ##    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords( cartesian_communicator.rank )
#
#    # print ("rank = @s grid row = @s grid column =@s" @(rank, my_mpi_row, my_mpi_col))
#
#
#     #Thorus MxN
#     cartesian_communicator _ \
#                            comm.Create_cart( \
#                                (grid_rows, grid_column), \
#                                periods_(T.., T..), reorder_True)
#     my_mpi_row, my_mpi_col _ \
#                 cartesian_communicator.Get_coords\
#                 ( cartesian_communicator.rank )
# ##    print ("rank = @s grid row = @s grid column =@s" @(rank, my_mpi_row, my_mpi_col))
# ##
#
#
#     neighbour_processes[UP], neighbour_processes[DOWN]\
#                              _ cartesian_communicator.Shift(0, 1)
#     neighbour_processes[LEFT],  \
#                                neighbour_processes[RIGHT]  _ \
#                                cartesian_communicator.Shift(1, 1)
#     print ("Process = @ \
# row = @ \
# column = @ ----> neighbour_processes[UP] = @ \
# neighbour_processes[DOWN] = @ \
# neighbour_processes[LEFT] =@ neighbour_processes[RIGHT]=@" \
#            @(rank, my_mpi_row, \
#              my_mpi_col,neighbour_processes[UP], \
#              neighbour_processes[DOWN], \
#              neighbour_processes[LEFT] , \
#              neighbour_processes[RIGHT]))
