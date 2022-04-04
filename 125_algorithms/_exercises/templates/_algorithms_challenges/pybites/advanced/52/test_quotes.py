_______ json

____ quotes _______ app

API_ENDPOINT = 'http://127.0.0.1:5000/api/quotes'

client = app.test_client()
client.testing = T..


___ test_get_quotes
    response = client.g.. API_ENDPOINT)
    ... response.status_code __ 200

    data = json.loads(response.get_data
    print(data)
    quotes = data 'quotes'
    ... l..(quotes) __ 3

    e.. = {'id': 1, 'movie': 'The Godfather',
                'quote': "I'm gonna make him an offer he can't refuse."}
    ... quotes[0] __ e..


___ test_get_existing_quote
    response = client.g.. API_ENDPOINT + '/2')
    ... response.status_code __ 200

    data = json.loads(response.get_data
    quotes = data 'quotes'
    ... l..(quotes) __ 1

    e.. = {'id': 2, 'movie': 'Predator', 'quote': "Get to the choppa!"}
    ... quotes[0] __ e..


___ test_get_not_existing_quote
    response = client.g.. API_ENDPOINT + '/4')
    ... response.status_code __ 404


___ test_create_quote
    new_quote = d..(quote='You talking to me?',
                     movie='Taxi driver')
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    ... response.status_code __ 201
    data = json.loads(response.get_data
    new_quote = data 'quote'
    ... new_quote 'id'  __ 4
    ... new_quote 'quote'  __ 'You talking to me?'
    ... new_quote 'movie'  __ 'Taxi driver'


___ test_create_quote_missing_data
    new_quote    # dict
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    ... response.status_code __ 400


___ test_create_quote_incomplete_data
    new_quote = d..(quote='You talking to me?')
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    ... response.status_code __ 400


___ test_create_existing_quote
    new_quote = d..(quote='You talking to me?',
                     movie='Taxi driver')
    response = client.post(API_ENDPOINT,
                           data=json.dumps(new_quote),
                           content_type='application/json')
    ... response.status_code __ 400


___ test_update_quote
    update_quote = d..(quote='You talking to me?!',
                        movie='Taxi driver (1976)')
    response = client.put(API_ENDPOINT + '/4',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    ... response.status_code __ 200

    data = json.loads(response.get_data
    updated_quote = data 'quote'
    ... updated_quote 'id'  __ 4
    ... updated_quote 'quote'  __ 'You talking to me?!'
    ... updated_quote 'movie'  __ 'Taxi driver (1976)'


___ test_update_no_data
    update_quote    # dict
    response = client.put(API_ENDPOINT + '/4',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    ... response.status_code __ 400


___ test_update_not_existing_quote
    update_quote = d..(quote='You talking to me?!')
    response = client.put(API_ENDPOINT + '/5',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    ... response.status_code __ 404


___ test_update_no_changes
    update_quote = d..(quote='Get to the choppa!',
                        movie='Predator')
    response = client.put(API_ENDPOINT + '/2',
                          data=json.dumps(update_quote),
                          content_type='application/json')
    ... response.status_code __ 200

    data = json.loads(response.get_data
    updated_quote = data 'quote'
    ... updated_quote 'id'  __ 2
    ... updated_quote 'quote'  __ 'Get to the choppa!'
    ... updated_quote 'movie'  __ 'Predator'


___ test_delete_existing_quote
    response = client.delete(API_ENDPOINT + '/2')
    ... response.status_code __ 204

    # number quotes from 4 to 3
    response = client.g.. API_ENDPOINT)
    data = json.loads(response.get_data
    quotes = data 'quotes'
    ... l..(quotes) __ 3


___ test_delete_not_existing_quote
    response = client.delete(API_ENDPOINT + '/5')
    ... response.status_code __ 404
