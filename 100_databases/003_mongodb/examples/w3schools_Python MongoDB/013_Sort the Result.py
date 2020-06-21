# Use the sort() method to sort the result in ascending or descending order.
#
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
# Example
#
# Sort the result alphabetically by name:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)