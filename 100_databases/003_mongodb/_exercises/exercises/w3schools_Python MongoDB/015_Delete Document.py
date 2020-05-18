# # To delete one document, we use the delete_one() method.
# #
# # The first parameter of the delete_one() method is a query object defining which document to delete.
# #
# # Note: If the query finds more than one document, only the first occurrence is deleted.
# # Example
# #
# # Delete the document with the address "Mountain 21":
#
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _  "address" "Mountain 21"
#
# ?.d_o_ ?