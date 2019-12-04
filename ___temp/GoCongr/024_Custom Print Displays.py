# Custom Print Displays
#
# class with __str__
#
# class with __repr__

class MyBad(Exception): pass

try:
    raise MyBad('Sorry--my mistake!')
except MyBad as X:
    print(X)

raise MyBad('Sorry--my mistake!')

class MyBad(Exception):
    def __str__(self):
        return 'Always look on the bright side of life...'

try:
    raise MyBad()
except MyBad as X:
    print(X)

raise MyBad()

class E(Exception):
  def __repr__(self): return 'Not called!'
raise E('spam')

class E(Exception):
  def __str__(self): return 'Called!'

raise E('spam')
