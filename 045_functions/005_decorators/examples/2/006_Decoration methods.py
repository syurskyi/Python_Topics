# # -*- coding: utf-8 -*-

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)

    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))


l = Lucy()
l.sayYourAge(-3)
# выведет: Мне 26, а ты бы сколько дал?