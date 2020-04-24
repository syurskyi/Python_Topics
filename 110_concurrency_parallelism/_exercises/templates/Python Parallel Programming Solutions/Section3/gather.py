# #gather communication – Section 3: Process Based Parallelism
# ____ mpi4py ______ MPI
#
# comm _ MPI.COMM_WORLD
# size _ comm.Get_size()
# rank _ comm.Get_rank()
# data _ (rank+1)**2
#
# data _ comm.gather(data, root_0)
# __ rank __ 0:
#    print ("rank = @ " @rank +\
#           "...receiving data to other process")
#    ___ i __ ra..(1,size):
#       data[i] _ (i+1)**2
#       value _ data[i]
#       print(" process @ receiving @ from process @"\
#             @(rank , value , i))
