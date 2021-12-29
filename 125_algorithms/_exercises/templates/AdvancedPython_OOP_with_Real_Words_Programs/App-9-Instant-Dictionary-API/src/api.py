_____ justpy as jp
_____ definition
_____ json

c_ Api:
    """Handles requests at /api?w=word
    """
    @classmethod
    ___ serve(cls, req):
        wp  jp.WebPage()
        word  req.query_params.get('w')

        defined  definition.Definition(word).get()

        response  {
            "word":word,
            "definition":defined
        }

        wp.html  json.dumps(response)
        r_ wp


