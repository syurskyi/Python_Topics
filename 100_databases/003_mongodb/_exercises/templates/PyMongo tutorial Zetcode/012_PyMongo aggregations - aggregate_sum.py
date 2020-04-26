#!/usr/bin/python3

____ ? _____ M..

client _ M..('mongodb://localhost:27017/')

w__ client:
    db _ client.testdb

    agr _ [{'$group': {'_id': 1, 'all': {'$sum': '$price'}}}]

    val _ list(db.cars.aggregate(agr))

    print('The sum of prices is {}'.f..(val[0]['all']))
