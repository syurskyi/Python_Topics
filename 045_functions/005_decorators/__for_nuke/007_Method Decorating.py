# # -*- coding: utf-8 -*-

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        # Теперь мы распакуем *args и **kwargs
        # Если вы не слишком хорошо знакомы с распаковкой, можете прочесть следующую статью:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here." ) # оставлено без перевода, хорошая игра слов:)


function_with_no_argument()


# выведет:
# Передали ли мне что-нибудь?:
# ()
# {}
# Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


# выведет:
# Передали ли мне что-нибудь?:
# (1, 2, 3)
# {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
    print("Любят ли %s, %s и %s утконосов? %s" % (a, b, c, platypus))


function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")


# выведет:
# Передали ли мне что-нибудь?:
# ('Билл', 'Линус', 'Стив')
# {'platypus': 'Определенно!'}
# Любят ли Билл, Линус и Стив утконосов? Определенно!

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):  # Теперь мы можем указать значение по умолчанию
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))


m = Mary()
m.sayYourAge()
# выведет:
# Передали ли мне что-нибудь?:
# (<__main__ .Mary object at 0xb7d303ac>,)
# {}
# Мне 28, а ты бы сколько дал?