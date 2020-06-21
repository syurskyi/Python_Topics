# Creating a Collection
# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
# MongoDB will create the collection if it does not exist.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]


# Important: In MongoDB, a collection is not created until it gets content!
#
# MongoDB waits until you have inserted a document before it actually creates the collection.
# Check if Collection Exists
#
# Remember: In MongoDB, a collection is not created until it gets content, so if this is your first time creating
# a collection, you should complete the next chapter (create document) before you check if the collection exists!
#
# You can check if a collection exist in a database by listing all collections:

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")