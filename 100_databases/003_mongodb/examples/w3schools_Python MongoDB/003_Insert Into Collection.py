# To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
#
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field
# in the document you want to insert.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

print(x)

# Return the _id Field
#
# The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds
# the id of the inserted document.
# Example
#
# Insert another record in the "customers" collection, and return the value of the _id field:

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)

