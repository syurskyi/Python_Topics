# #broadcast communication Section 3: Process Based Parallelism
# ____ mpi4py ______ MPI
#
# comm _ MPI.COMM_WORLD
# rank _ comm.Get_rank()
#
# __ rank __ 0
#    variable_to_share _ 100
#
# ____
#    variable_to_share _ N..
#
# variable_to_share _ comm.bcast(variable_to_share, root_0)
# print("process = @d" @rank + " variable shared  = @d " @variable_to_share)
