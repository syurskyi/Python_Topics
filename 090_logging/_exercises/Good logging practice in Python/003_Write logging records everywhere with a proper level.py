# # With the flexibility of the logging module, its a good practice to write logging record everywhere with appropriate
# # level and configure them later. What is the appropriate level to use, you may ask. Let me share my experience here.
# #
# # In most cases, you dont want to flood your log file with too many trivial information. And as the name implies,
# # the DEBUG level is for debugging. Therefore, the DEBUG level should only be enabled when you are debugging.
# # I use the DEBUG level only for logging verbose details. Especially when the data is huge, or the frequency is high,
# # such as records of algorithm internal state changes in a for-loop.
# #
# ___ complex_algorithm items
#     ___ i, item i_ en.. ?
#         # do some complex algorithm computation
#         ?.d... '@ iteration, item=@', ?, i..
# 
# # I use INFO level for routines. For example, handling requests or server state changed.
# 
# ___ handle_request request
#     ?.i.. 'Handling request @', ?
#     # handle request here
#     result = 'result'
#     ?.i.. 'Return result: @', ?
# 
# ___ start_service
#     ?.i.. 'Starting service at port %s ...', port
#     service.st..
#     ?.i.. 'Service is started')
# 
# # I use WARNING when something needs your attention, but not an error. For example, when a user attempts to log in
# # with a wrong password, or, the connection is slow.
# #
# ___ authenticate user_name, password, ip_address
#     i_ user_name !_ USER_NAME and password != PASSWORD
#         ?.w... 'Login attempt to %s from IP %s', u.., i..
#         r_ F..
#     # do authentication here
# 
# # I use ERROR level when something is wrong. For example, an exception is thrown, IO operation failure or connectivity
# # issue.
# #
# # ___ get_user_by_id(user_id):
# #     user = db.read_user(user_id)
# #     if user is None:
# #         logger.error('Cannot find user with user_id=%s', user_id)
# #         return user
# #     return user
# # I never use CRITICAL, you can use it when something horrible happens. For example, out of memory, the disk is full
# # or a nuclear meltdown (Hopefully that will not actually happen ).
