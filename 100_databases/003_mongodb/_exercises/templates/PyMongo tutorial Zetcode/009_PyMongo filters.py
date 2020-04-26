#!/usr/bin/python3

____ ? _____ M..

client p.. M..('mongodb://localhost:27017/')

w__ client:
    db p.. client.testdb

    expensive_cars p.. db.cars.f..({'price': {'$gt': 50000}})

    ___ ecar __ expensive_cars:
        print(ecar['name'])
        
