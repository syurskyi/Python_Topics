from pymongo import Connection
import datetime
server = Connection()
db = server["test"]
country_collection = db["country"]
country_collection.drop()

canada = dict()
canada['name'] = "canada"
canada['population'] = 35000000
canada['fondation'] = datetime.datetime(1867,07,01)
country_collection.save(canada)

usa = dict()
usa['name'] = "usa"
usa['population'] = 316000000
usa['fondation'] = datetime.datetime(1776,07,04)
country_collection.save(usa)

#update document
usa = country_collection.find_one({"name": "usa"})
usa['population'] = 320000000
country_collection.save(usa)

#save multiple documents
country_collection.insert([canada,usa])







