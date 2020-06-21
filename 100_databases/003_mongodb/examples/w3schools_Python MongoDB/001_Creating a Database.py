import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

#
# Important: In MongoDB, a database is not created until it gets content!
#
# MongoDB waits until you have created a collection (table), with at least one document (record) before
# it actually creates the database (and collection).
# Check if Database Exists
# Remember: In MongoDB, a database is not created until it gets content, so if this is your first time creating
# a database, you should complete the next two chapters (create collection and create document) before you check
# if the database exists!
# You can check if a database exist by listing all databases in you system:

print(myclient.list_database_names())

# Or you can check a specific database by name:

dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("The database exists.")