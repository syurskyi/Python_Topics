# User-defined exception
# class AlreadyGotOne
class AlreadyGotOne(Exception):
    pass  # User-defined exception


def grail():
	raise AlreadyGotOne() # Raise an instance

try:
    grail()
except AlreadyGotOne:     # Catch class name
	print('got exception')