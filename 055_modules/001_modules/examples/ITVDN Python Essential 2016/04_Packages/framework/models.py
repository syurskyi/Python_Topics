"""Модуль эмуляции ORM"""

class Model(object):
    @classmethod
    def get_objects(cls):
        print('Retrieving ' + cls.__name__ + ' objects from DB')