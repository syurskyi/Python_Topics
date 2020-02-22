# """
# Dependency Inversion Principle
#
# Bad
# Http is the high-level component, which is dependent on HttpService, the low-level component.
# """
#
#
# class XMLHttpRequestService:
#     pass
#
#
# class XMLHttpService(XMLHttpRequestService):
#     pass
#
#
# class Http:
#     ___ __init__(self, xml_http_service: XMLHttpService):
#         self.xml_http_service = xml_http_service
#
#     ___ get(self, url: str, options: dict):
#         self.xml_http_service.request(url, 'GET')
#
#     ___ post(self, url, options: dict):
#         self.xml_http_service.request(url, 'POST')
#
#
# """
# better
#
# Now, we are not dependent on the type of Http connection service passed to Http. it can easily connect to a network
# without bothering to know the type of network connection.
# """
#
#
# c_ Connection
#     ___ request url st. options: di..
#         r_ N..
#
#
# c_ Http
#     ___ - http_connection C..
#         ??  ?
#
#     ___ get url st. options di..
#         ??.re.. ? 'G..
#
#     ___ post url options di..
#         ??.re.. ? 'P..
#
#
# c_ XMLHttpService C..
#     xhr _ XMLHttpR..
#
#     ___ request url st. options: di..
#         ?x__.o..
#         ?x__.s..
#
# """
# other types of connection:
# """
#
# c_ NodeHttpService C..
#     ___ request url st. options di..
#         p..
#
#
# c_ MockHttpService C..
#     ___ request url st. options di..
#         pa..
