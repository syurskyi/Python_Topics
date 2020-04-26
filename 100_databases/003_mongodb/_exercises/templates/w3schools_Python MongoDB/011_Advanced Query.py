# # Advanced Query
# #
# # To make advanced queries you can use modifiers as values in the query object.
# #
# # E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
# # Example
# #
# # Find documents where the address starts with the letter "S" or higher:
#
# _____ ?
#
# myclient _?.M..("mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _ "address" | "$gt" "S"
#
# mydoc _?.f.. ?
#
# ___ x __ ?
#   print ?