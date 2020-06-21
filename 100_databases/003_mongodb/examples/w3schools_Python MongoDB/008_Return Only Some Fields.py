# Return Only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result.
# This parameter is optional, and if omitted, all fields will be included in the result.
# Example
# Return only the names and addresses, not the _ids:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)