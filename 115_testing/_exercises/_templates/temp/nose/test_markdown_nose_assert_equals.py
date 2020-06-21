'''
Test markdown.py with nose
To run tests: nosetests     test_markdown_nose.py
Verbose (-v): nosetests -v  test_markdown_nose.py
'''

____ n__.tools ______ assert_equals
____ markdown_adapter ______ run_markdown

___ test_non_marked_lines(
    print ('in test_non_marked_lines')
    assert_equals(run_markdown('this line has no special handling'),
    	'<p>this line has no special handling</p>')

___ test_em(
    print ('in test_em')
    assert_equals( run_markdown('*this should be wrapped in em tags*'),
    	'<p><em>this should be wrapped in em tags</em></p>')

___ test_strong(
    print ('in test_strong')
    assert_equals( run_markdown('**this should be wrapped in strong tags**'),
    	'<p><strong>this should be wrapped in strong tags</strong></p>')