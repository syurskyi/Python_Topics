# # Limit the Result
# #
# # To limit the result in MongoDB, we use the limit() method.
# #
# # The limit() method takes one parameter, a number defining how many documents to return.
# #
# # Consider you have a "customers" collection:
#
# # Limit the result to only return 5 documents:
#
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myresult _ ?.f..().l.. 5
#
# #print the result:
# ___ x __ ?
#   print ?