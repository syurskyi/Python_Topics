# You can also use regular expressions as a modifier.
#
# Regular expressions can only be used to query strings.
#
# To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:
# Example
#
# Find documents where the address starts with the letter "S":


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)