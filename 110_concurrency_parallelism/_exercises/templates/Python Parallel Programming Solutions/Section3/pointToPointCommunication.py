# ____ mpi4py ______ MPI
#
# comm_MPI.COMM_WORLD
# rank _ comm.rank
# print("my rank is : " , rank)
#
# __ rank__0:
#     data_ 10000000
#     destination_process _ 4
#     comm.send(data,dest_destination_process)
#     print ("sending data @ " @data +\
#            "to process @d" @destination_process)
#
# __ rank__1:
#     destination_process _ 8
#     data_ "hello"
#     comm.send(data,dest_destination_process)
#     print ("sending data @ :" @data + \
#            "to process @d" @destination_process)
#
#
# __ rank__4:
#     data_comm.recv(source_0)
#     print ("data received is = @" @data)
#
#
# __ rank__8:
#     data1_comm.recv(source_1)
#     print ("data1 received is = @" @data1)
