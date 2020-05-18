# # Exploring business review data
#
#
# ____ ? _____ M..
# # Connect to the MongoDB, change the connection string per your MongoDB environment
# client _ M.. p.._27017
# # Set the db object to point to the business database
# db _ ?.b..
# # Showcasing the count() method of find, count the total number of 5 ratings
# print('The number of 5 star reviews:')
# fivestarcount _ db.r__.f.. 'rating' 5 .c..
# print ?
# # Now let's use the aggregation framework to sum the occurrence of each rating across the entire data set
# print('\nThe sum of each rating occurance across all data grouped by rating ')
# stargroup _ ?.r__.ag..(
# # The Aggregation Pipeline is defined as an array of different operations
# [
# # The first stage in this pipe is to group data
# { '$group':
#     { '_id': "$rating",
#      "count" :
#                  { '$sum' :1 }
#     }
# },
# # The second stage in this pipe is to sort the data
# {"$sort":  { "_id":1}
# }
# # Close the array with the ] tag
# ] )
# # Print the result
# ___ group __ ?
#     print ?
