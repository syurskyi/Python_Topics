____ python_news _______ get_top_titles, Entry

homepage ("https://bites-data.s3.us-east-2.amazonaws.com/"
            "news.python.sc/index.html")
page2 ("https://bites-data.s3.us-east-2.amazonaws.com/"
         "news.python.sc/index2.html")


___ test_homepage
    a.. get_top_titles(homepage)
    e.. [
        Entry(title='How do you set up your Python development environment?',
              points=15, comments=8),
        Entry(title='Python alternative to Docker (www.mattlayman.com)',
              points=9, comments=4),
        Entry(title='Debugging Python programs (stribny.name)',
              points=9, comments=3),
        Entry(title='New features planned for Python 4.0 (charlesleifer.com)',
              points=9, comments=2),
        Entry(title='Python 3.8 is out (www.python.org)',
              points=9, comments=0),
    ]
    ... a.. __ e..


___ test_page2
    a.. get_top_titles(page2, top=2)
    e.. [
        Entry(title='Django REST Framework - Typed Views (github.com)',
              points=4, comments=0),
        Entry(title=('Show 🐍: A news aggregator for the Python community '
                     'written in Python/Django (github.com)'),
              points=3, comments=1),
    ]
    ... a.. __ e..
