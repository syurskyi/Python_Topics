# To delete more than one document, use the delete_many() method.
#
# The first parameter of the delete_many() method is a query object defining which documents to delete.
# Example
#
# Delete all documents were the address starts with the letter S:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")