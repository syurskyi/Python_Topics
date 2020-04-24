# #reduction operation – Section 3: Process Based Parallelism
# ______ numpy
# ______ numpy as np
# ____ mpi4py ______ MPI
# comm _ MPI.COMM_WORLD
# size _ comm.size
# rank _ comm.rank
#
#
# a_size _ 3
# recvdata _ numpy.zeros(a_size,dtype_numpy.in.)
# senddata _ (rank+1)*numpy.arange(a_size,dtype_numpy.in.)
#
# print(" process @ sending @ " @(rank , senddata))
#
#
# comm.Reduce(senddata,recvdata,root_0,op_MPI.SUM)
# print ('on task',rank,'after Reduce:    data = ',recvdata)
