# In this example we have some dictionaries we use to configure our application. One dictionary specifies
# some configuration defaults for every configuration parameter our application will need.
# Another dictionary is used to configure some global configuration, and another set of dictionaries is used
# to define environment specific configurations, maybe dev and prod.
conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_defaults)

conf_global = {
    'port': 5432,
    'database': 'deepdive'}

conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod'
}

# Now we can generate a full configuration for our dev environment this way:

config_dev = {**conf_defaults, **conf_global, **conf_dev}
print(config_dev)

# and a config for our prod environment:

config_prod = {**conf_defaults, **conf_global, **conf_prod}
print(config_prod)
