# # To delete more than one document, use the delete_many() method.
# #
# # The first parameter of the delete_many() method is a query object defining which documents to delete.
# # Example
# #
# # Delete all documents were the address starts with the letter S:
#
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _ "address" |"$regex" "^S"
#
# x _ ?.d_m.. ?
#
# print ?.d_c.. " documents deleted."