_______ p__

____ tribe _______ get_top_books, load_page


?p__.f..(scope='module')
___ content
    """Load content once for all test"""
    r.. load_page()


___ test_get_top_5_books(content
    books = get_top_books(content=content)
    ... books __  'Man’s Search For Meaning',
                     ('The 4-Hour Workweek: Escape the 9-5, '
                      'Live Anywhere and Join the New Rich'),
                     'The Fountainhead',
                     'Sapiens: A Brief History of Humankind',
                     'Tao Te Ching'


___ test_get_top_10_books(content
    books = get_top_books(content=content, limit=10)
    ... books[5:] __ [('The Better Angels of our Nature: Why Violence '
                          'Has Declined'),
                         ('The Beginning of Infinity: Explanations That '
                          'Transform ' 'the World'),
                         ('The War of Art: Break Through the Blocks and Win '
                          'Your Inner Creative Battles'),
                         'The Hero with a Thousand Faces ',
                         'Poor Charlie’s Almanack'