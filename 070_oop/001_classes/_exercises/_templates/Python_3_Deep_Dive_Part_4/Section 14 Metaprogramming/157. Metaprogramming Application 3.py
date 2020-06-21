# %%
'''
### Metaprogramming - Application 3
'''

# %%
'''
Let's say we have some `.ini` files that hold various application configurations. We want to read those `.ini` files 
into an object structure so that we can access the data in our config files using dot notation.
'''

# %%
'''
Let's start by creating some `.ini` files:
'''

# %%
with open('prod.ini', 'w') as prod, open('dev.ini', 'w') as dev:
    prod.write('[Database]\n')
    prod.write('db_host=prod.mynetwork.com\n')
    prod.write('db_name=my_database\n')
    prod.write('\n[Server]\n')
    prod.write('port=8080\n')
    
    dev.write('[Database]\n')
    dev.write('db_host=dev.mynetwork.com\n')
    dev.write('db_name=my_database\n')
    dev.write('\n[Server]\n')
    dev.write('port=3000\n')

# %%
'''
Note: I could have used the `configparser` module to write out these ini files, but we don't have to - generally these 
config files are created and edited manually. We will use `configparser` to load up the config files though.
'''

# %%
'''
When we start our program, we want to load up one of these files into a config object of some sort.
We could certainly do it this way:
'''

# %%
import configparser

class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file...')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        self.db_host = config['Database']['db_host']
        self.db_name = config['Database']['db_name']
        self.port = config['Server']['port']

# %%
config = Config('dev')

# %%
print(config.__dict__)

# %%
'''
but whenever we need access to this config object again, we either have to store the object somewhere in a global
variable (common, and extremely simple!), or we need to re-create it:
'''

# %%
config = Config('dev')

# %%
'''
Which means we end up parsing the `ini` file over and over again.
'''

# %%
print(config.db_name)

# %%
help(config)

# %%
'''
Furthermore, `help` is not very useful to us here.
'''

# %%
'''
The other thing is that we had to "hardcode" each config value in our `Config` class. 
That's a bit of a pain. 
Could we maybe create instance attributes from inspecting what's inside the `ini` files instead?
'''

# %%
class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file...')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            for key, value in config[section_name].items():
                setattr(self, key, value)

# %%
config = Config('prod')

# %%
print(config.__dict__)

# %%
'''
So this is good, we can access our config values using dot notation:
'''

# %%
print(config.port)

# %%
'''
The next issue we need to deal with is that our config files are organized into sections, and here we've essentially 
ignored this and create just a "flat" data structure.
'''

# %%
'''
So let's deal with that next.
'''

# %%
'''
Let's write a custom class for representing sections:
'''

# %%
class Section:
    def __init__(self, name, item_dict):
        """
        name: str
            name of section
        item_dict : dictionary
            dictionary of named (key) config values (value)
        """
        self.name = name
        for key, value in item_dict.items():
            setattr(self, key, value)

# %%
'''
And now we can rewrite our `Config` class this way:
'''

# %%
class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file...')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            section = Section(section_name, config[section_name])
            setattr(self, section_name.lower(), section)

# %%
config = Config()

# %%
'''
Now we have sections:
'''

# %%
vars(config)

# %%
'''
And each section has its config values:
'''

# %%
vars(config.database)

# %%
'''
But that still does not solve our documentation issue:
'''

# %%
help(Config)

# %%
'''
Most modern IDE's will still be able to provide us some auto-completion on the attributes though, using some form of 
introspection.
'''

# %%
'''
But let's assume we really want `help` to give us some useful information, or we're working with an IDE that isn't 
sophisticated enough.
'''

# %%
'''
To do that, we are going to switch to metaclasses.
'''

# %%
'''
Our custom metaclass will load up the `ini` file and use it to create class attributes instead:
'''

# %%
'''
And we'll need to do this for both the sections and the overall config.
'''

# %%
'''
To keep things a little simpler, we're going to create two distinct metaclasses. One for the sections in the config 
file, and one that combines the sections together - very similar to what we did with our original `Config` class.
'''

# %%
'''
One key difference, is that each `Section` class instance, will be a brand new class, created via its metaclass.
'''

# %%
'''
Let's write the `Section` metaclass first.
'''

# %%
class SectionType(type):
    def __new__(cls, name, bases, cls_dict, section_name, items_dict):
        cls_dict['__doc__'] = f'Configs for {section_name} section'
        cls_dict['section_name'] = section_name
        for key, value in items_dict.items():
            cls_dict[key] = value
        return super().__new__(cls, name, bases, cls_dict)

# %%
'''
We can now create `Section` classes for different sections in our configs, passing the metaclass the section name, 
and a dictionary of the values it should create as class attributes.
'''

# %%
class DatabaseSection(metaclass=SectionType, section_name='database', items_dict={'db_name': 'my_database', 'host': 'myhost.com'}):
    pass

# %%
vars(DatabaseSection)

# %%
'''
As you can see, our items `db_name` and `host` are in the class.
'''

# %%
print(DatabaseSection.db_name)

# %%
'''
And the `help` function introspection will work too:
'''

# %%
help(DatabaseSection)

# %%
'''
And we can now create any section we want using this metaclass, for example:
'''

# %%
class PasswordsSection(metaclass=SectionType, section_name='passwords', items_dict={'db': 'secret', 'site': 'super secret'}):
    pass

# %%
vars(PasswordsSection)

# %%
'''
Just like we can create classes programmatically by calling the `type` metaclass:
'''

# %%
MyClass = type('MyClass', (object,), {})

# %%
print(MyClass)

# %%
'''
We can also create `Section` **classes** by calling the `SectionType` metaclass:
'''

# %%
MySection = SectionType('DBSection', (object,), {}, section_name='databases', items_dict={'db_name': 'my_db', 'port': 8000})

# %%
print(MySection)

# %%
vars(MySection)

# %%
'''
Now that we have a metaclass to create section classes, we can build our main config metaclass to build the `Config` 
class.
'''

# %%
class ConfigType(type):
    def __new__(cls, name, bases, cls_dict, env):
        """
        env : str
            The environment we are loading the config for (e.g. dev, prod)
        """
        cls_dict['__doc__'] = f'Configurations for {env}.'
        cls_dict['env'] = env
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            class_name = section_name.capitalize()
            class_attribute_name = section_name.casefold()
            section_items = config[section_name]
            bases = (object, )
            section_cls_dict = {}
            # create a new Section class for this section
            Section = SectionType(
                class_name, bases, section_cls_dict, section_name=section_name, items_dict=section_items
            )
            # And assign it to an attribute in the main config class
            cls_dict[class_attribute_name] = Section
        return super().__new__(cls, name, bases, cls_dict)

# %%
'''
Now we can create config classes for each of our environments:
'''

# %%
class DevConfig(metaclass=ConfigType, env='dev'):
    pass

class ProdConfig(metaclass=ConfigType, env='prod'):
    pass

# %%
vars(DevConfig)

# %%
help(DevConfig)

# %%
vars(DevConfig.database)

# %%
help(DevConfig.database)

# %%
print(DevConfig.database.db_host, ProdConfig.database.db_host)