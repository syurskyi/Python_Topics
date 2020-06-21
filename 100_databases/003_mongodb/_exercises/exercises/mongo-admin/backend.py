from pymongo import MongoClient

client = MongoClient()

def insert(dbname, collection, data):
    try:
        db = client[dbname]
        collection = db[collection]
        collection.insert(data)
    except:
        return {"code": 2, "message": "Insert failed"}


def find(dbname, collection, query):
    try:
        db = client[dbname]
        collection = db[collection]
        result = collection.find(query)
    except:
        return {'code': 2, 'message': 'Find error'}

    return {'code': 1, 'message': list(result)}


def getDbs():
    try:
        result = client.database_names()
    except:
        return {"code": 2, "message:": "Find error"}

	return {'code': 1, 'message': result}


# ___ getCollections dbname
# 	___
# 		db _ ? ?
# 		result _ ?.c_n..
# 	______
# 		r_ *c.. 2, *m.. *Find error
#
# 	r_ *c.. 1, *m.. result
#
#
# ___ delete dbname, collection, query)
# 	___
# 		db _ ?
# 		collection _ ?
# 		collection.r.. ?
# 	______
# 		r_ *c.. 2, *m.. *Delete error
#
# 	r_ *c.. 1, *m.. *Successfully Deleted
#
#
# ___ login user password
# 	___
# 		db _ ? _co..
# 		collection _ ? _us..
# 		__ le. li.. ?.f.. __ 0
# 			__ u.. __ *r.. an. p.. __ *r..
# 				r_ *c.. 1, *m.. |*u.. *r.. *p.. *r..
# 		result _ ?.f.. *u.. u.. *p.. p..
# 	______
# 		r_ *c.. 2 *m.. *Login error
#
# 	r_ *c.. 1, *m.. li.. ?
#
#
# ___ signup user password
# 	___
# 		db _ ? _c..
# 		collection _ ? '_u..
# 		?.i.. *u.. u.. *p.. p..
# 	______
# 		r_ *c.. 2 *m.. *Signup error
#
# 	r_ *c.. 1, *m.. *Signed up sucessfully
