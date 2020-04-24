# #alltoall communication – Section 3: Process Based Parallelism
# ____ mpi4py ______ MPI
# ______ numpy
#
# comm _ MPI.COMM_WORLD
# size _ comm.Get_size()
# rank _ comm.Get_rank()
#
# a_size _ 1
# senddata _ (rank+1)*numpy.arange(size,dtype_int)
# recvdata _ numpy.empty(size*a_size,dtype_int)
# comm.Alltoall(senddata,recvdata)
#
#
# print(" process @ sending @ receiving @"\
#       @(rank , senddata , recvdata))
