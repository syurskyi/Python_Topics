class MyException(Exception):
    pass

try:
    raise MyException("error")
except MyException as e:
    print(e)
except Exception:
    print('some exception')
