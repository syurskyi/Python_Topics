# # Filter the Result
# #
# # When finding documents in a collection, you can filter the result by using a query object.
# #
# # The first argument of the find() method is a query object, and is used to limit the search.
# # Example
# #
# # Find document(s) with the address "Park Lane 38":
#
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _  "address" "Park Lane 38"
#
# mydoc _ ?.f.. ?
#
# ___ x __ ?
#   print ?