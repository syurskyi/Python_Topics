# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 10
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
# # Adopted from https://github.com/noxrepo/pox/blob/carp/pox/forwarding/hub.py
# # For more examples and tutorials:
# #   https://github.com/noxrepo/pox/tree/carp/pox
#
# ____ pox.core ______ core
# ______ pox.openflow.libopenflow_01 __ of
# ____ pox.lib.util ______ dpidToStr
#
# log _ core.getLogger()
#
# # The listener definition: A simple and stupid hub.
# ___ _handle_ConnectionUp (event):
#   msg _ of.ofp_flow_mod()
#   msg.a..s.ap..(of.ofp_a.._output(port _ of.OFPP_FLOOD))
#   event.connection.s..(msg)
#   # log the action.
#   log.info("Hubifying @", dpidToStr(event.dpid))
#
#
# # When the application is launched with POX.
# ___ launch
#   #Add a listener (defined above) to the pox.core openflow.
#   core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
#   log.info("Hub is running.")
