#!/usr/bin/env python3

______ json
______ unicodedata

from bottle ______ route, request, run, static_file

from charindex ______ InvertedIndex

index = {}

@route('/')
___ form():
    r_ static_file('form.html', root='static/')


@route('/search')
___ search():
    query = request.query['q']
    chars = index.search(query)
    results   # list
    ___ char __ chars:
        name = unicodedata.name(char)
        results.a.. ({'char': char, 'name': name})
    r_ json.dumps(results).encode('UTF-8')


___ main(port):
    global index
    index = InvertedIndex()
    run(host='localhost', port=port, debug=True)


__ _____ __ ______
    main(8000)
