# """
# Dependency Inversion Principle
#
# Dependency should be on abstractions not concretions A. High-level modules
# should not depend upon low-level modules. Both should depend upon abstractions.
# B. Abstractions should not depend on details. Details should depend upon
# abstractions.
#
# There comes a point in software development where our app will be largely
# composed of modules.  When this happens, we have to clear things up by using
# dependency injection.  High-level components depending on low-level components
# to function.
# """
#
# c_ XMLHttpService X..
#     p..
#
# c_ Http
#     ___ - xml_http_service XMLHt..
#         ??  ?
#
#     ___ get  url st. options di..
#         ??.re.. ? 'G..
#
#     ___ post url options di..
#         ??.re.. ? 'P..
#
# """
# Here, Http is the high-level component whereas XMLHttpService is the low-level
# component.  This design violates DIP A: High-level modules should not depend on
# low-level level modules. It should depend upon its abstraction.
#
# Ths Http class is forced to depend upon the XMLHttpService class.  If we were to
# change the Http connection service, maybe we want to connect to the internet
# through cURL or even Mock the http service.  We will painstakingly have to move
# through all the instances of Http to edit the code and this violates the OCP
# principle.
#
# The Http class should care less the type of Http service you are using. We make
# a Connection interface:
# """
#
# c_ Connection
#     ___ request url st. options di..
#         r_ N..
#
# """
# The Connection interface has a request method. With this, we pass in an argument
# of type Connection to our Http class:
# """
#
# c_ Http
#     ___ - http_connection Co..
#         ??  ?
#
#     ___ get url st. options di..
#         ??.re.. ? 'G..
#
#     ___ post  url options di..
#         ??.re.. ? 'P..
#
# """
# So now, no matter the type of Http connection service passed to Http it can
# easily connect to a network without bothering to know the type of network
# connection.
#
# We can now re-implement our XMLHttpService class to implement the Connection
# interface:
# """
#
# c_ XMLHttpService C..
#     xhr = X___R..
#
#     ___ request url st. options di..
#         ?x__.o..
#         ?x__.s..
#
# """
# We can create many Http Connection types and pass it to our Http class without
# any fuss about errors.
# """
# c_ NodeHttpService C..
#     ___ request url st. options di..
#         p..
#
# c_ MockHttpService C..
#     ___ request url st. options di..
#         p..
#
# """
# Now, we can see that both high-level modules and low-level modules depend on
# abstractions.  Http class(high level module) depends on the Connection
# interface(abstraction) and the Http service types(low level modules) in turn,
# depends on the Connection interface(abstraction).
#
# Also, this DIP will force us not to violate the Liskov Substitution Principle:
# The Connection types Node-XML-MockHttpService are substitutable for their parent
# type Connection.
# """
