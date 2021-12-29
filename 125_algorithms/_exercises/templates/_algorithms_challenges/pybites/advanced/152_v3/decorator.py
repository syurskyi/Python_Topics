____ functools _______ wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


___ strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    ___ decorator_replace(fun):
        @wraps(fun)
        ___ wrapper_replace(*args, **kwargs):
            output = l..(fun(*args, **kwargs))
            this_end = end __ end < l..(output) ____ l..(output)
            this_end = this_end __ this_end > 0 ____ 0
            this_start = start __ start >= 0 ____ 0

            ___ k __ r..(this_start, this_end):
                output[k] = '.'
            r.. ''.join(output)
        r.. wrapper_replace
    r.. decorator_replace
