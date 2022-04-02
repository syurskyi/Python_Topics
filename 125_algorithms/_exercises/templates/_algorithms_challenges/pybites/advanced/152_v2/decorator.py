DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


___ strip_range(start, end
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """

    ___ wrap(func
        ___ wrapped(text, *args, **kwargs
            _start = m..(start, 0)
            _end = m..(l..(text), end) __ end > 0 ____ 0
            result = (text[:_start], text[_start:_end], text[_end:])
            r.. func _*{result[0]}{DOT * l..(result[1])}{result[2]}')

        r.. wrapped

    r.. wrap
