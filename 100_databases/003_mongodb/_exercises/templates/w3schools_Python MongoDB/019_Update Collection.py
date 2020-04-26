# # You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# # The first parameter of the update_one() method is a query object defining which document to update.
# # Note: If the query finds more than one record, only the first occurrence is updated.
# # The second parameter is an object defining the new values of the document.
# # Example
# # Change the address from "Valley 345" to "Canyon 123":
#
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _ "address" "Valley 345"
# newvalues _  "$set" | "address" "Canyon 123"
#
# ?.u_o.. ? ?
#
# #print "customers" after the update:
# ___ x __ ?.f..
#   print ?