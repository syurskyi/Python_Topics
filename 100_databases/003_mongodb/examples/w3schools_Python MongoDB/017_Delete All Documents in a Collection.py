# To delete all documents in a collection, pass an empty query object to the delete_many() method:
# Example
#
# Delete all documents in the "customers" collection:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")