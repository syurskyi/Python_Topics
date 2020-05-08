from nose.plugins.attrib import attr

# nosetests -a '!slow'   <= You won't execute this test case
# nosetests -a 'slow'    <= Execute the test cases with the attribute 'slow'
@attr('slow')
def test_slow_test():
    pass

# To be more specific, you can do...
# nosetests -a speed=slow_test
@attr(speed='slow_test')
def test_attr_name():
    pass
