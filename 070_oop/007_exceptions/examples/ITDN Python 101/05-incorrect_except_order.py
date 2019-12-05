class MyException(Exception):
    pass

try:
    raise MyException("error")
except Exception:
    print('some exception')
except MyException as e:
    print(e)
