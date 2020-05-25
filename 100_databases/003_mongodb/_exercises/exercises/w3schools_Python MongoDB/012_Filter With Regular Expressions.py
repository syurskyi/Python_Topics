# # You can also use regular expressions as a modifier.
# #
# # Regular expressions can only be used to query strings.
# #
# # To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:
# # Example
# #
# # Find documents where the address starts with the letter "S":
#
#
# _____ ?
#
# myclient _ ?.M.. "mongodb://localhost:27017/"
# mydb _ ? "mydatabase"
# mycol _ ? "customers"
#
# myquery _ "address": | "$regex" "^S"
#
# mydoc _ ?.f.. ?
#
# ___ x __ ?
#   print ?