# Use the value -1 as the second parameter to sort descending.
#
# sort("name", 1) #ascending
# sort("name", -1) #descending
# Example
#
# Sort the result reverse alphabetically by name:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)