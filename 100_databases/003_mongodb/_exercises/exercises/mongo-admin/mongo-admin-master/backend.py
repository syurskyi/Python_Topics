from pymongo import MongoClient

client = MongoClient()

def insert(dbname, collection, data):
	try:
		db = client[dbname]
		collection = db[collection]
		collection.insert(data)
	except:
		return {"code": 2, "message": "Insert failed"}

	return {"code": 1, "message": "Successfully inserted"}


def find(dbname, collection, query):
	try:
		db = client[dbname]
		collection = db[collection]
		result = collection.find(query)
	except:
		return {"code": 2, "message": "Find error"}

	return {"code": 1, "message": list(result)}

def getDbs():
	try:
		result = client.database_names()
	except:
		return {"code": 2, "message": "Find error"}

	return {"code": 1, "message": result}

def getCollections(dbname):
	try:
		db = client[dbname]
		result = db.collection_names()
	except:
		return {"code": 2, "message": "Find error"}

	return {"code": 1, "message": result}

def delete(dbname, collection, query):
	try:
		db = client[dbname]
		collection = db[collection]
		collection.remove(query)
	except:
		return {"code": 2, "message": "Delete error"}

	return {"code": 1, "message": "Successfully Deleted"}

def login(user, password):
	try:
		db = client['_config']
		collection = db['_users']
		if len(list(collection.find({}))) == 0:
			if(user == 'root' and password == 'root'):
				return {"code": 1, "message": [{"user": "root", "password": "root"}]}
		result = collection.find({"user": user, "password": password})
	except:
		return {"code": 2, "message": "Login error"}

	return {"code": 1, "message": list(result)}

def signup(user, password):
	try:
		db = client['_config']
		collection = db['_users']
		collection.insert({"user": user, "password": password})
	except:
		return {"code": 2, "message": "Signup error"}

	return {"code": 1, "message": "Signed up sucessfully"}
