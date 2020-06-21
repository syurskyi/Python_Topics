# # -*- coding: utf-8 -*-

def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")

    return wrapper


def sandwich(food="--ветчина--"):
    print(food)


sandwich()
# выведет: --ветчина--
sandwich = bread(ingredients(sandwich))
sandwich()
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)


sandwich()
# выведет:
# </------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>