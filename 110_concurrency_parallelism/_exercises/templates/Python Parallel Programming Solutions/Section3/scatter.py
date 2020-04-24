# #scatter communication – Section 3: Process Based Parallelism
# ____ mpi4py ______ MPI
#
# comm _ MPI.COMM_WORLD
# rank _ comm.Get_rank()
#
# __ rank __ 0:
#    array_to_share _ [1, 2, 3, 4 ,5 ,6 ,7, 8 ,9 ,10]
#
# ____
#    array_to_share _ N..
#
# recvbuf _ comm.scatter(array_to_share, root_0)
# print("process = @d" @rank + " variable shared  = @d " @recvbuf )
