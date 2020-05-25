# # To update all documents that meets the criteria of the query, use the update_many() method.
# # Example
# #
# # Update all documents where the address starts with the letter "S":
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _ "address" | "$regex" "^S"
# newvalues _  "$set" | "name" "Minnie"
#
# x _ ?.u_m.. ? ?
#
# print ?.m_c.., "documents updated.")