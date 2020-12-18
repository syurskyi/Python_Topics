import sqlite3
from collections import OrderedDict


class ObjectDoesNotExist(Exception):
    pass


class Storage:
    __SELECT_PATTER = 'SELECT * FROM {table_name} WHERE {fields}'
    __DELETE_PATTER = 'DELETE FROM {table_name} WHERE {fields}'
    __INSERT_PATTER = 'INSERT INTO {table_name} ({fields}) ' \
                      'VALUES({values})'
    _connection = None

    def __init__(self, cls):
        self.cls = cls

    @classmethod
    def bind_connection(cls, connection):
        cls._connection = connection

    def get_by_field(self, single=False, **kwargs):
        values = list(kwargs.values())
        params = [
            '{field} = ?'.format(field=field)
            for field in kwargs.keys()
        ]
        fields_part = ' AND '.join(params)
        sql_row = self.__SELECT_PATTER.format(
            table_name=self.cls._metadata._table_name,
            fields=fields_part
        )
        if single:
            row = self.execute_sql(sql_row, values).fetchone()
            if row is None:
                raise ObjectDoesNotExist(
                    'Object does not exist: {name} ({fields})'.format(
                        name=self.cls, fields=list(kwargs.items())
                    )
                )
            else:
                return self.cls(**dict(row))
        result = []
        for row in self.execute_sql(sql_row, values).fetchall():
            result.append(self.cls(**dict(row)))
        return result

    def insert(self, **values):
        fields = ', '.join(values.keys())
        values = list(values.values())
        values_ = ', '.join(map(lambda x: '?', values))
        sql_row = self.__INSERT_PATTER.format(
            table_name=self.cls._metadata._table_name,
            fields=fields,
            values=values_
        )
        cursor = self.execute_sql(sql_row, values)
        instance = self.get_by_field(id=cursor.lastrowid)[0]
        return instance

    def delete(self, **fields):
        values = list(fields.values())
        params = [
            '{field} = ?'.format(field=field)
            for field in fields.keys()
        ]
        fields_part = ' AND '.join(params)
        sql_raw = self.__DELETE_PATTER.format(
            table_name=self.cls._metadata._table_name,
            fields=fields_part
        )
        return self.execute_sql(sql_raw, values).rowcount

    @classmethod
    def execute_sql(cls, sql_text, params=None):
        params = params or ()
        print('SQL: {sql_text} with params: {params}'.format(
            sql_text=sql_text, params=params
        ))
        return cls._connection.execute(sql_text, params)


class Metadata(object):

    def __init__(self, fields, cls):
        self._fields = fields
        table_name = cls.__name__.lower()
        if table_name.endswith('y'):
            table_name = cls.__name__.lower()[:-1]
            suffix = 'ies'
        else:
            table_name = cls.__name__.lower()
            suffix = 's'
        self._table_name = '{old_name}{suffix}'.format(old_name=table_name,
                                                       suffix=suffix)

    def get_fields(self):
        return self._fields.items()

    def get_field(self, field_name):
        result = '{field_name} {field_type}'.format(
            field_name=field_name, field_type=self._fields[field_name].type
        )
        return result

    def has_field(self, field_name):
        return field_name in self._fields

    def generate_create_table_sql(self):
        fields_data = ', '.join([
            self.get_field(field)
            for field in self._fields.keys()
        ])
        sql = 'CREATE TABLE {table_name} ({fields})'
        return sql.format(table_name=self._table_name, fields=fields_data)


class Field(object):

    def __init__(self, field_type, default=None):
        self.type = field_type
        self.default = default


class BaseMeta(type):

    # @classmethod
    # def __prepare__(mcs, name, bases, **kwargs):
    #     print('Prepared', name, bases, kwargs)
    #     return OrderedDict()

    @staticmethod
    def __new__(mcs, name, bases, attrs):
        print('mcs', mcs)
        new_attrs = OrderedDict()
        fields = OrderedDict()
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields.setdefault(key, value)
            else:
                new_attrs[key] = value
        print(fields)
        new_cls = super().__new__(mcs, name, bases, new_attrs)
        new_cls.storage = Storage(new_cls)
        new_cls._metadata = Metadata(fields=fields, cls=new_cls)
        return new_cls


class BaseModel(metaclass=BaseMeta):

    def __init__(self, **kwargs):

        for item in kwargs:
            assert self._metadata.has_field(item), \
                'Field "{}" does not exist'.format(item)
            setattr(self, item, kwargs.get(item))
            # self.age = 10
            # self.first_name = "Dmitry"

        for item in self._metadata._fields:
            if not hasattr(self, item):
                value = self._metadata._fields[item].default
                if callable(value):
                    value = value()
                setattr(self, item, value)


class User(BaseModel):
    id = Field('INTEGER PRIMARY KEY AUTOINCREMENT')
    age = Field('INTEGER')
    first_name = Field('VARCHAR(30)', default='')
    last_name = Field('VARCHAR(30)', default='')


class Country(BaseModel):
    name = Field('VARCHAR(30)')


# preparing
DATABASE = ':memory:'
connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row

Storage.bind_connection(connection)
Storage.execute_sql(User._metadata.generate_create_table_sql())
Storage.execute_sql(Country._metadata.generate_create_table_sql())

# executing select/insert/delete
user = User.storage.insert(
    first_name='John',
    last_name='Test',
    age=10
)
print('ID', user.id)

user = User.storage.insert(
    first_name='John',
    last_name='Test',
    age=10
)
print('ID', user.id)

print(User.storage.get_by_field(first_name='John'))
print(User.storage.delete(first_name='John'))
print(User.storage.get_by_field(first_name='John'))

try:
    print(User.storage.get_by_field(first_name='John', single=True))
except ObjectDoesNotExist as e:
    print(e)
