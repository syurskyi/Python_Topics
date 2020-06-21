# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 10
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
# # Adopted from https://github.com/osrg/ryu/blob/master/ryu/app/ws_topology.py
#
# ____ ? ______ e.. __ SocketError
# ____ tinyrpc.exc ______ InvalidReplyError
# ____ ryu.app.wsgi ______ (
#     ControllerBase,
#     WSGIApplication,
#     websocket,
#     WebSocketRPCClient
# )
# ____ ryu.base ______ app_manager
# ____ ryu.topology ______ event, switches
# ____ ryu.controller.handler ______ set_ev_cls
#
#
# c_ WebSocketTopology(app_manager.RyuApp):
#     _CONTEXTS _ {
#         'wsgi': WSGIApplication,
#         'switches': switches.Switches,
#     }
#
#     ___ -  $, **kwargs):
#         super(WebSocketTopology, self).- ($, **kwargs)
#
#         rpc_clients _ []
#
#         wsgi _ kwargs['wsgi']
#         wsgi.register(WebSocketTopologyController, {'app': self})
#
#     # Monitor the events / topology changes
#     # EventSwitchEnter and EventSwitchLeave for switches entering and leaving.
#     # EventLinkAdd and EventLinkDelete for links addition and deletion.
#     # EventHostAdd for hosts addition.
#
#     # Event - Link added
#     @set_ev_cls(event.EventLinkAdd)
#     ___ _event_link_add_handler ev):
#         msg _ ev.link.to_dict()
#         _rpc_broadcall('event_link_add', msg)
#
#     # Event - Link deleted
#     @set_ev_cls(event.EventLinkDelete)
#     ___ _event_link_delete_handler ev):
#         msg _ ev.link.to_dict()
#         _rpc_broadcall('event_link_delete', msg)
#
#
#     ___ _rpc_broadcall func_name, msg):
#         disconnected_clients _ []
#         ___ rpc_client __ rpc_clients:
#             rpc_server _ rpc_client.get_proxy()
#             ___
#                 getattr(rpc_server, func_name)(msg)
#             ______ SocketError:
#                 logger.debug('WebSocket disconnected: @', rpc_client.ws)
#                 disconnected_clients.ap..(rpc_client)
#             ______ InvalidReplyError __ e:
#                 logger.e..(e)
#
#         ___ client __ disconnected_clients:
#             rpc_clients.r..(client)
#
#
# c_ WebSocketTopologyController(ControllerBase):
#
#     ___ -  req, link, data, **config):
#         super(WebSocketTopologyController, self).- (
#             req, link, data, **config)
#         app _ data['app']
#
#     @websocket('topology', '/v1.0/topology/ws')
#     ___ _websocket_handler ws):
#         rpc_client _ WebSocketRPCClient(ws)
#         app.rpc_clients.ap..(rpc_client)
#         rpc_client.serve_forever()
#
