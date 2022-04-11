____ flask _______ Flask, jsonify, abort, request

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


___ _get_quote(qid
    """Recommended helper"""
    r.. [q ___ q __ quotes __ q 'id'  __ qid]


___ _quote_exists(existing_quote
    """Recommended helper"""
    r.. any(q 'quote'  __ existing_quote 'quote'  a.. q 'movie'  __ existing_quote 'movie'  ___ q __ quotes)


___ _new_id
    r.. m..(q 'id'  ___ q __ quotes) + 1


@app.route('/api/quotes', methods= 'GET' )
___ get_quotes
    r.. jsonify(quotes=quotes)


@app.route('/api/quotes/<int:qid>', methods= 'GET' )
___ get_quote(qid
    q = _get_quote(qid)
    __ l..(q) __ 0:
        abort(404)
    r.. jsonify(quotes=q)


@app.route('/api/quotes', methods= 'POST' )
___ create_quote
    quote_str = request.j__.g.. 'quote')
    movie_str = request.j__.g.. 'movie')
    __ n.. quote_str o. n.. movie_str:
        abort(400)
    quote = {'quote': quote_str, 'movie': movie_str}
    __ _quote_exists(quote
        abort(400)
    quote 'id'  = _new_id()
    quotes.a..(quote)
    r.. jsonify(quote=quote), 201, {'Location': f'/api/quotes/{quote["id"]}'}


@app.route('/api/quotes/<int:qid>', methods= 'PUT' )
___ update_quote(qid
    q = _get_quote(qid)
    __ l..(q) __ 0:
        abort(404)
    q = q[0]
    dirty = F..
    quote_str = request.j__.g.. 'quote')
    __ quote_str:
        q 'quote'  = quote_str
        dirty = T..
    movie_str = request.j__.g.. 'movie')
    __ movie_str:
        q 'movie'  = movie_str
        dirty = T..
    __ n.. dirty:
        abort(400)
    r.. jsonify(quote=q), 200


@app.route('/api/quotes/<int:qid>', methods= 'DELETE' )
___ delete_quote(qid
    q = _get_quote(qid)
    __ l..(q) __ 0:
        abort(404)
    q = q[0]
    quotes.remove(q)
    r.. jsonify(quotes=q), 204
