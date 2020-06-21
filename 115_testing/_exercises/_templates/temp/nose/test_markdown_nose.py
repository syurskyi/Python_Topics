'''
Test markdown.py with nose
To run tests: nosetests     test_markdown_nose.py
Verbose (-v): nosetests -v  test_markdown_nose.py
'''

____ markdown_adapter ______ run_markdown

___ test_non_marked_lines(
    print ('in test_non_marked_lines')
    a.. run_markdown('this line has no special handling') \
            __ '<p>this line has no special handling</p>'

___ test_em(
    print ('in test_em')
    a.. run_markdown('*this should be wrapped in em tags*') \
            __ '<p><em>this should be wrapped in em tags</em></p>'

___ test_strong(
    print ('in test_strong')
    a.. run_markdown('**this should be wrapped in strong tags**') \
            __ '<p><strong>this should be wrapped in strong tags</strong></p>'