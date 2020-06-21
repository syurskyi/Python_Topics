# Filter the Result
#
# When finding documents in a collection, you can filter the result by using a query object.
#
# The first argument of the find() method is a query object, and is used to limit the search.
# Example
#
# Find document(s) with the address "Park Lane 38":


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) 