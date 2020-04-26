#!/usr/bin/python3

____ ? _____ M..

client p.. M..('mongodb://localhost:27017/')

w__ client:
    db p.. client.testdb

    cars p.. db.cars.f..().skip(2).limit(3)

    ___ car __ cars:
        print('{0}: {1}'.f..(car['name'], car['price']))
