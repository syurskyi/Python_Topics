# # Return Only Some Fields
# # The second parameter of the find() method is an object describing which fields to include in the result.
# # This parameter is optional, and if omitted, all fields will be included in the result.
# # Example
# # Return only the names and addresses, not the _ids:
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# ___ x __ ?.f.. ||  |"_id" 0, "name" 1, "address" 1
#   print ?