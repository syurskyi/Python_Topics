import common
import common.validators as validators
import common.models as models
# from common.models import *
import common.helpers as helpers



validators.is_boolean('true')
validators.is_json('{}')
validators.is_numeric(10)
validators.is_date('2018-0101')

john_post = models.Post()
john_posts = models.Posts()
john = models.User()


print('\n\n***** self *****')
# for k in globals().keys():
#     print(k)                     # doesn't work. RuntimeError: dictionary changed size during iteration

for k in dict(globals()).keys():
    print(k)


print('\n\n***** common *****')
for k in common.__dict__.keys():
    print(k)

print('\n\n***** helpers *****')
for k in common.helpers.__dict__.keys():
    print(k)


print('\n\n***** models *****')
for k in common.models.__dict__.keys():
    print(k)

print('\n\n***** validators *****')
for k in common.validators.__dict__.keys():
    print(k)

print('#' * 52 + ' in helpers ')

print(helpers.say_hello('Python'))
print(helpers.factorial(5))

