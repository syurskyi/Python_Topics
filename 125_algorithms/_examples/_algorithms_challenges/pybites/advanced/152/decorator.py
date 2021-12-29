from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """

    def decorator(f):

        def wrapper(text):

            s = max(start,0)
            e = max(end,0)
            s = min(len(text),s)
            e = min(len(text),e)
            s = text[:s] + DOT * (e - s) + text[e:]


            return s

        return wrapper



    return decorator




