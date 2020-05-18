# # To establish a connection we’ll use the MongoClient object.
# # The first thing that we need to do in order to establish a connection is import the MongoClient class.
# # We’ll use this to communicate with the running database instance. Use the following code to do so:
#
# ____ ? _____ M..
# client _ M..
#
# # Using the snippet above, the connection will be established to the default host (localhost) and port (27017).
# # You can also specify the host and/or port using:
#
# client _ M.. 'localhost' 27017
#
# # Or just use the Mongo URI format:
#
# client _ M.. 'mongodb://localhost:27017'
#
# # All of these calls to MongoClient will do the same thing; it just depends on how explicit you want to be in your code.
#
# # Accessing Databases
# #
# # Once you have a connected instance of MongoClient, you can access any of the databases within that Mongo server.
# # To specify which database you actually want to use, you can access it as an attribute:
#
# db _ ?.pymongo_test
#
# # Or you can also use the dictionary-style access:
#
# db _ ? 'pymongo_test'
#
# # It doesn’t actually matter if your specified database has been created yet. By specifying this database
# # name and saving data to it, you create the database automatically.
# # Inserting Documents
# #
# # Storing data in your database is as easy as calling just two lines of code. The first line specifies
# # which collection you’ll be using (posts in the example below). In MongoDB terminology, a collection is a group
# # of documents that are stored together within the database. Collections and documents are akin to SQL tables and rows,
# # respectively. Retrieving a collection is as easy as getting a database.
# #
# # The second line is where you actually insert the data in to the collection using the insert_one() method:
#
# posts _ ?.p..
# post_data _ {
#     'title': 'Python and MongoDB'
#     'content': 'PyMongo is fun, you guys'
#     'author': 'Scott'
# }
# result _ ?.i_o.. ?
# print 'One post: @'.f.. result.i_i..
#
# # We can even insert many documents at a time, which is much faster than using insert_one()
# # if you have many documents to add to the database. The method to use here is insert_many().
# # This method takes an array of document data:
#
# post_1 _ {
#     'title': 'Python and MongoDB'
#     'content': 'PyMongo is fun, you guys'
#     'author': 'Scott'
# }
# post_2 _ {
#     'title': 'Virtual Environments'
#     'content': 'Use virtual environments, you guys'
#     'author': 'Scott'
# }
# post_3 _ {
#     'title': 'Learning Python'
#     'content': 'Learn Python, it is easy'
#     'author': 'Bill'
# }
# new_result _ ?.i_m.. _1 _2 _3
# print 'Multiple posts: @'.f.. ?.i_id.
#
# # When ran, you should see something like:
# #
# # One post: 584d947dea542a13e9ec7ae6
# # Multiple posts: [
# #     ObjectId('584d947dea542a13e9ec7ae7'),
# #     ObjectId('584d947dea542a13e9ec7ae8'),
# #     ObjectId('584d947dea542a13e9ec7ae9')
# # ]
# #
# #     NOTE: Don’t worry that your ObjectIds don’t match those shown above. They are dynamically generated
# #     when you insert data and consist of a Unix epoch, machine identifier, and other unique data.
# #
# # Retrieving Documents
# #
# # To retrieve a document, we’ll use the find_one() method. The lone argument that we’ll use here
# # (although it supports many more) is a dictionary that contains fields to match. In our example below,
# # we want to retrieve the post that was written by Bill:
#
# bills_post _ ?.f_o.. 'author' 'Bill'
# print ?
#
# # Run this:
# #
# # {
# #     'author': 'Bill',
# #     'title': 'Learning Python',
# #     'content': 'Learn Python, it is easy',
# #     '_id': ObjectId('584c4afdea542a766d254241')
# # }
# #
# # You may have noticed that the post’s ObjectId is set under the _id key, which we can later use to uniquely identify
# # it if needed. If we want to find more than one document, we can use the find() method. This time,
# # let’s find all of the posts written by Scott:
#
# scotts_posts _ ?.f.. author' 'Scott'
# print ?
#
# # Run:
# #
# # <pymongo.cursor.Cursor object at 0x109852f98>
# #
# # The main difference here is that the document data isn’t returned directly to us as an array. Instead we get an
# # instance of the Cursor object. This Cursor is an iterable object that contains quite a few helper methods
# # to help you work with the data. To get each document, just iterate over the result:
#
# ___ post __ ?
#     print ?
