# -*- coding: utf-8 -*-

# В этом примере показано использование функции __getattribute__
# для сокрытия данных


class MyClass:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        """
        Метод __getattribute__ вызывается при получении атрибутов
        """

        # Если запрошено поле secret_field и пароль верный
        if item == 'secret_field' and self.password == '9ea)fc':
            # то возвращаем значение
            return 'secret value'
        else:
            # иначе вызываем метод __getattribute__ класса object
            return object.__getattribute__(self, item)


# Создание экземпляра класса
obj = MyClass()

# Разблокирование секретного поля
# obj.password = '9ea)fc'

# Вывод значения secret field.
# Значение будет получено, если раскомментировать предыдущую
# строку программного кода, иначе будет получена ошибка.
print(obj.secret_field)