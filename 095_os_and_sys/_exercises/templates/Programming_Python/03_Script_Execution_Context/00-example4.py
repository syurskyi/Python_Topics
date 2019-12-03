import sys
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

# with MyManager() as resource:
#     print('Some actions with resource:', resource)
#     raise ValueError

def my_with(manager, context_body):
    resource = manager.__enter__()
    exc_type, exc_value, exc_treaceback = None, None, None
    error = None
    try:
        context_body(resource)
    except Exception as e:
        exc_type, exc_value, exc_treaceback = sys.exc_info()
        error = e
    finally:
        manager.__exit__(exc_type, exc_value, exc_treaceback)
        if error:
            raise error

def context_body(resource):
    print("Some action with resource")
    # raise ValueError

my_with(MyManager(), context_body)

"""
class FileIO:
    def __enter__(self):
        return self
    
    def __exit__(self):
        self.close()
"""
