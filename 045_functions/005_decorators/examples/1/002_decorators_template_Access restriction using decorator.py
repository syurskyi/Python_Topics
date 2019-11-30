# # -*- coding: utf-8 -*-

passw = input("Введите пароль: ")

def test_passw(p):
    def deco(f):
        if p == "10":  # Сравниваем пароли
            return f
        else:
            return lambda: "Доступ закрыт"

    return deco  # Возвращаем функцию-декоратор


@test_passw(passw)
def func():
    return "Доступ открыт"


print(func())  # Вызываем функцию