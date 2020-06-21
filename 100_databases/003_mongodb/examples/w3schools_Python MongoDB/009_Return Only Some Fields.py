# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field).
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)


# ou get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
#
# for x in mycol.find({},{ "name": 1, "address": 0 }):
#   print(x)