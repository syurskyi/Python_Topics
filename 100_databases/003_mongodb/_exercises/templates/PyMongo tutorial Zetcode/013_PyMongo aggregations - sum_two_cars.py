#!/usr/bin/python3

____ ? _____ M..

client _ M..('mongodb://localhost:27017/')

w__ client:
    db _ client.testdb

    agr _ [{'$match': {'$or': [{'name': "Audi"}, {'name': "Volvo"}]}},
           {'$group': {'_id': 1, 'sum2cars': {'$sum': "$price"}}}]

    val _ list(db.cars.aggregate(agr))

    print('The sum of prices of two cars is {}'.f..(val[0]['sum2cars']))
