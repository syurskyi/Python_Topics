# %%
'''
### Accessors - Application
'''

# %%
'''
Another useful application of `__getattr__` and `__setattr__` is dealing with objects where we may not know 
the attributes in advance.
'''

# %%
'''
Consider this scenario where we have a database with various tables and fields. We want to create a class that allows 
us to retrieve data from these tables.
'''

# %%
'''
We could certainly write a class for each specific table, and hardcode the fields as properties in the class - 
but that's going to create repetitive code, and anytime there is a new table or the schema of an existing table changes 
we'll have to revise our code.
'''

# %%
'''
I'm going to simulate a database here by using dictionaries. The outer dictionary will contain tables (as keys), 
and each table will contain records with a numeric key for each record.
'''

# %%
DB = {
    'Person': {
        1: {'first_name': 'Isaac', 'last_name': 'Newton', 'born': 1642, 'country_id': 1},
        2: {'first_name': 'Gottfried', 'last_name': 'von Leibniz', 'born': 1646, 'country_id': 5},
        3: {'first_name': 'Joseph', 'last_name': 'Fourier', 'born': 1768, 'country_id': 3},
        4: {'first_name': 'Bernhard', 'last_name': 'Riemann', 'born': 1826, 'country_id': 5},
        5: {'first_name': 'David', 'last_name': 'Hilbert', 'born': 1862 , 'country_id': 5},
        6: {'first_name': 'Srinivasa', 'last_name': 'Ramanujan', 'born': 1887, 'country_id': 4},
        7: {'first_name': 'John', 'last_name': 'von Neumann', 'born': 1903, 'country_id': 2},
        8: {'first_name': 'Andrew', 'last_name': 'Wiles', 'born': 1928, 'country_id': 6}
    },
    'Country': {
        1: {'name': 'United Kingdom', 'capital': 'London', 'continent': 'Europe'},
        2 :{'name': 'Hungary', 'capital': 'Budapest', 'continent': 'Europe'},
        3: {'name': 'France', 'capital': 'Paris', 'continent': 'Europe'},
        4: {'name': 'India', 'capital': 'New Delhi', 'continent': 'Asia'},
        5: {'name': 'Germany', 'capital': 'Berlin', 'continent': 'Europe'},
        6: {'name': 'USA', 'capital': 'Washington DC', 'continent': 'North America'}
        }
}

# %%
'''
Now we could certainly do something like this for each table:
'''

# %%
class Country:
    def __init__(self, id_):
        if _id in DB['Country']:
            self._db_record = DB['Country'][id_]
        else:
            raise ValueError(f'Record not found (Country.id={id_})')

    @property
    def name(self):
        return self._db_record['name']
    
    @property
    def capital(self):
        return self._db_record['capital']
    
    @property
    def continent(self):
        return self._db_record['continent']

# %%
'''
And we would have to do the same thing with the `Person` table, and any other table we want from our database. Tedious 
and repetitive code!!
'''

# %%
'''
We could create a metaclass that inspects the table structure and creates the appropriate fields, that would work well 
with code completion for example. 
But if we don't want to get too fancy, we can instead just use `__getattr__`. We'll implement the `__setattr__` as well, 
but of course in a real database situation you would need to implement some mechanism to persist the changes back to 
the database.
'''

# %%
'''
We are going to create a `DBTable` class that will be used to represent a table in the database, and we'll make 
it callable so we can pass the record id to the instance, which will return a `DBRecord` object that we can then use to 
access the fields in the table.
'''

# %%
'''
Let's write the `DBRecord` class first. This class will be passed a database record (so a dictionary in this example), 
and will be tasked with looking up "fields" (keys in this example) in the table (dictionary).
'''

# %%
class DBRecord:
    def __init__(self, db_record_dict):
        # again, careful how you set a property on instances of this class
        # because we are overriding __setattr__ we cannot just use 
        # self._record = db_record_dict
        # this will call OUR version of `__setattr__`, which attempts to 
        # see if name is in _record - but _record does not exist yet, so it will
        # call __getattr__, which in turn tries to check if that is contained in _record
        # so, infinite recursion.
        # What we want to here is BYPASS our custom __setattr__ - so we'll use
        # the one in the superclass.
        super().__setattr__('_record', db_record_dict)    
        
    def __getattr__(self, name):
        # here we could write
        #     if name in self._record 
        # since this method should not get called
        # before _record as been created.
        # But just to be on the safe side, I'm still going to use super
        if name in super().__getattribute__('_record'):
            return self._record[name]
        else:
            raise AttributeError(f'Field name {name} does not exist.')

    def __setattr__(self, name, value):
        # and again here, we could write
        # if name in self._record, but I'm still going to use super
        if name in super().__getattribute__('_record'):
            # super().__setattr__(name, value)
            self._record[name] = value
        else:
            raise AttributeError(f'Field name {name} does not exist.')

# %%
'''
Next, we define the `DBTable` class. It will be initialized with the name of the table we want to use in our instance. 
Furthermore we'll make it callable (passing in the record id) and that shoudl return an instance of `DBRecord` for 
the particular record.
'''

# %%
class DBTable:
    def __init__(self, db, table_name):
        if table_name not in db:
            raise ValueError(f'The table {table_name} does not exist in the database.')
        self._table_name = table_name
        self._table = db[table_name]
        
    @property
    def table_name(self):
        return self._table_name
    
    def __call__(self, record_id):
        if record_id not in self._table:
            raise ValueError(f'Specified id ({record_id}) does not exist '
                             f'in table {self._table_name}')
        return DBRecord(self._table[record_id])

# %%
'''
And now we can use our classes this way:
'''

# %%
tbl_person = DBTable(DB, 'Person')
tbl_country = DBTable(DB, 'Country')

# %%
person_1 = tbl_person(1)

# %%
print(person_1.first_name, person_1.last_name, person_1.born, person_1.country_id)

# %%
country_1 = tbl_country(person_1.country_id)

# %%
print(country_1.name, country_1.capital)

# %%
'''
There's quite a bit more functionality we might want to add - maybe a way to determine all the fields available in
a record for example:
'''

# %%
class DBRecord:
    def __init__(self, db_record_dict):
        # again, careful how you set a property on instances of this class
        # because we are overriding __setattr__ we cannot just use 
        # self._record = db_record_dict
        # this will call OUR version of `__setattr__`, which attempts to 
        # see if name is in _record - but _record does not exist yet, so it will
        # call __getattr__, which in turn tries to check if that is contained in _record
        # so, infinite recursion.
        # What we want to here is BYPASS our custom __setattr__ - so we'll use
        # the one in the superclass.
        super().__setattr__('_record', db_record_dict)    
        
    def __getattr__(self, name):
        # here we could write
        #     if name in self._record 
        # since this method should not get called
        # before _record as been created.
        # But just to be on the safe side, I'm still going to use super
        if name in super().__getattribute__('_record'):
            return self._record[name]
        else:
            raise AttributeError(f'Field name {name} does not exist.')

    def __setattr__(self, name, value):
        # and again here, we could write
        # if name in self._record, but I'm still going to use super
        if name in super().__getattribute__('_record'):
            self._record[name] = value
        else:
            raise AttributeError(f'Field name {name} does not exist.')
            
    @property
    def fields(self):
        return tuple(self._record.keys())

# %%
tbl_person = DBTable(DB, 'Person')

# %%
person_1 = tbl_person(2)

# %%
print(person_1.fields)

# %%
'''
We can of course set the field values, via the `__setattr__`:
'''

# %%
print(person_1.last_name)

# %%
person_1.last_name = 'Leibniz'

# %%
print(person_1.last_name)

# %%
print(person_1.__dict__)

# %%
'''
There are many more improvements we could make, but this is good enough to show how we can use `__getattr__` 
and `__setattr__`.
'''

# %%
'''
The main difficulty with using `__getattr__` and, especially, `__setattr__` is to make sure we do not accidentally 
create recursive calls.
'''