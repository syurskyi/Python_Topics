# ____ mpi4py ______ MPI
#
# comm_MPI.COMM_WORLD
# rank _ comm.rank
# print("my rank is : " , rank)
#
# __ rank__1:
#     data_send_ "a"
#     destination_process _ 5
#     source_process _ 5
#
#     data_received_comm.sendrecv(data_send,dest_destination_process,source_source_process)
#
#
#     print ("sending data @ " data_send + \
#        "to process @d" destination_process)
#     print ("data received is = @" data_received)
#
#
#
# __ rank__5:
#     data_send_ "b"
#     destination_process _ 1
#     source_process _ 1
#
#
#     data_received_comm.sendrecv(data_send,dest_destination_process,source_source_process)
#
#
#     print ("sending data @ :" data_send + \
#             "to process @d" destination_process)
#     print ("data received is = @" data_received)
