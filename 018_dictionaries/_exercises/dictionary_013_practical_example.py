# # -*- coding: utf-8 -*-
#
# # In this example we have some dictionaries we use to configure our application. One dictionary specifies
# # some configuration defaults for every configuration parameter our application will need.
# # Another dictionary is used to configure some global configuration, and another set of dictionaries is used
# # to define environment specific configurations, maybe dev and prod.
# conf_defaults _ di__.fr... 'host' 'port' 'user' 'pwd' 'database' N..
# print c.._d..
#
# conf_global _
#     'port': 5432,
#     'database': 'deepdive'
#
# conf_dev _
#     'host': 'localhost',
#     'user': 'test',
#     'pwd': 'test'
#
#
# conf_prod _
#     'host': 'prodpg.deepdive.com',
#     'user': '$prod_user',
#     'pwd': '$prod_pwd',
#     'database': 'deepdive_prod'
#
#
# # Now we can generate a full configuration for our dev environment this way:
#
# config_dev _ |00c.._d.. 00c.._g.. 00c.._d..|
# print c.._d..
#
# # and a config for our prod environment:
#
# config_prod _ |00c.._d.. 00c.._g.. 00c.._p..
# print c.._p..
