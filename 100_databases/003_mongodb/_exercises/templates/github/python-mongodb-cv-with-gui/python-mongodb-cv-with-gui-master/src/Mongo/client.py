____ _______ _______ _______
____ random _______ randint
# from Mongo.sample_data import SampleData
____ ? _______ Qt
____ pathlib _______ Path
_______ time
_______ secrets

# to run the database type: sudo mongod


c_ Client():
    ___  -
        s__(). - ()
        ConnectToServer()
        print('client initialized successfully!')

    ___ ConnectToServer
        # will attempt to connect to local host
        client = _______("mongodb://localhost:27017/")
        # connect to database
        db = client["myDatabase"]
        print('db=\n', db, '\n')
        myCollection = db["users"]

    ___ InsertUser(self,
                   userName: st.,
                   userDescription: st.,
                   imageID:st.):
        aUser = {"name": userName,
                 "description": userDescription,
                 "image_id": imageID}
        # insert user into the database in the users collection
        result = myCollection.insert_one(aUser)

    ___ FindUser(self,
                 userName: st.,
                 description: st.):
        print('found the following users named:', userName)
        myList = li..()

        ___ i __ myCollection.f..(
            {
                '$and': 
                [
                    {'name': userName}, {'description': description}
                ]
            }
        ):
            myList.append(i)
            print('added to the list: ', i)
        print('counted numbers in list=', le.(myList))
        length = le.(myList)
        ___ i __ ra..(length):
            print(myList[i]['description'], '\n', myList[i]['image_id'])

    ___ FinderImageID(self, userName: st., description: st.):
        '''
        returns an image id of the user
        '''
        print(__name__,' passing user= <',userName,'> description= <',description,'>\n')
        myList = li..()
        ___ i __ myCollection.f..(
            {
                '$and': 
                [
                    {'name': userName}, {'description': description}
                ]
            },
            {'_id': 0, 'image_id': 1}
        ):
            myList.append(i)
            print('found user ',i)
        # if len(myList) > 0:
        print('image id= ', myList[0]['image_id'])
        value=myList[0]['image_id']
        return value

    ___ GetAllUsers
        '''
        returns a list of all users of the database
        '''
        print('found the following users')
        myList = li..()
        ___ i __ myCollection.f..({}, {'_id': 0,'name':1, 'description': 1, 'image_id': 1}):
            myList.append(i)
        # print('counted numbers in list=', len(myList))
        # for i in range(len(myList)):
        #     print(myList[i]['name'],myList[i]['description'],myList[i]['image_id'])
        return myList
    ___ DeleteAllUsers
        myCollection.delete_many({})

    ___ DeleteUser(self, name: st., description: st.):
        tmpQuery = {"name": name, "description": description}
        result = myCollection.delete_one(tmpQuery)
        # print('deleted user: ', result)

    ___ GetRandomID
        '''
        generate a secret id and return it
        '''
        return secrets.token_hex(16)


__ __name__ __ "__main__":
    client = Client()
    
    client.InsertUser('John', 'this is my description1')
    client.InsertUser('Jack', 'this is my description2')
    client.InsertUser('Jason', 'this is my description3')
    client.InsertUser('Jason', 'this is my description3')

    # client.FindAllUsers()
    # client.FindUser('asd', 'asdasd')
    # tmp=client.FinderImageID('asd','asdasd')
    tmpList=client.GetAllUsers()
    print('counted numbers in list=', le.(tmpList))
    ___ i __ ra..(le.(tmpList)):
        print(tmpList[i]['name'],tmpList[i]['description'],tmpList[i]['image_id'])
    # client.DeleteAllUsers()
