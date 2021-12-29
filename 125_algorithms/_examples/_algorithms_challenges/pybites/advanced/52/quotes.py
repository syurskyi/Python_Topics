from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""

    for quote in quotes:
        if quote["id"] == qid:
            return quote


def _quote_exists(existing_quote):
    """Recommended helper"""


    for quote in quotes:
        if quote['quote'] == existing_quote['quote'] and quote['movie'] == existing_quote['movie']:
            return True

    return False

    


def _get_max_id():
    

    return max(quote['id'] for quote in quotes)

@app.route('/api/quotes', methods=['GET'])
def get_quotes():

    return jsonify({'quotes': quotes})


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):

        
    quote = _get_quote(qid)
    if not quote:
        return "Quote not found",404

    return jsonify({'quotes': [quote]})


@app.route('/api/quotes', methods=['POST'])
def create_quote():

    data = request.json

    if not (('quote' in data) and  ('movie' in data)):
        return "Incomplete data",400
    

    exists = _quote_exists(data)

    if exists:
        return "Already exists",400
    
    _id = _get_max_id() + 1



    quote = {'id': _id,'quote': data['quote'],'movie': data['movie']}

    quotes.append(quote)


    return jsonify({'quote': quote}),201







@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    


    data = request.json
    print(data)
    if not (('quote' in data) or  ('movie' in data)):
        return "Incomplete data",400
    quote = _get_quote(qid)

    if not quote:
        return "Quote not found",404
    

    
    quote['quote'] = data['quote']
    quote['movie'] = data['movie']


    return jsonify({'quote': quote})

@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):

    quote = _get_quote(qid)

    if not quote:
        return "Quote not found",404


    for i,quote in enumerate(quotes):
        if quote['id'] == qid:
            quotes.pop(i)
            break


    
    return "Deleted successfully",204
