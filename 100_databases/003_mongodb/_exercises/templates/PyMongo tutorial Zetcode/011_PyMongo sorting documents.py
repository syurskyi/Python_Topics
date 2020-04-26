#!/usr/bin/python3

____ ? _____ M.., DESCENDING

client _ M..('mongodb://localhost:27017/')

w__ client:

    db _ client.testdb

    cars _ db.cars.f..().so..("price", DESCENDING)

    ___ car __ cars:
        print('{0} {1}'.f..(car['name'],
            car['price']))
 
