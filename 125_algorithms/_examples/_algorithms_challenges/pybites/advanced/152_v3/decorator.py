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
    def decorator_replace(fun):
        @wraps(fun)
        def wrapper_replace(*args, **kwargs):
            output = list(fun(*args, **kwargs))
            this_end = end if end < len(output) else len(output)
            this_end = this_end if this_end > 0 else 0
            this_start = start if start >= 0 else 0

            for k in range(this_start, this_end):
                output[k] = '.'
            return ''.join(output)
        return wrapper_replace
    return decorator_replace
