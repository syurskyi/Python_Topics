____ n__.plugins.attrib ______ attr

# nosetests -a '!slow'   <= You won't execute this test case
# nosetests -a 'slow'    <= Execute the test cases with the attribute 'slow'
@attr('slow')
___ test_slow_test(
    p..

# To be more specific, you can do...
# nosetests -a speed=slow_test
@attr(speed_'slow_test')
___ test_attr_name(
    p..
