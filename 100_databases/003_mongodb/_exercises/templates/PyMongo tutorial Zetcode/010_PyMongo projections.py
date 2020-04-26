#!/usr/bin/python3

____ ? _____ M..

client p.. M..('mongodb://localhost:27017/')

w__ client:
    db p.. client.testdb

    cars p.. db.cars.f..({}, {'_id': 1, 'name': 1})

    ___ car __ cars:
        print(car)
