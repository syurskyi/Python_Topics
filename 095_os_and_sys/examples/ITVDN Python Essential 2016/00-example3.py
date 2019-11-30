class MyManager(object):
    def __init__(self):
        self.resource = 42

    def __enter__(self):
        print('Entered context')
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Left context')
        if exc_type:
            print('(Exeption occured: {})'.format(exc_type))

with MyManager() as resource:
    print('Some actions with resource:', resource)
    # raise ValueError