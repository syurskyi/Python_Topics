# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 13
# # This program is optimized for Python 2.7.12.
# # It may run on any other version with/without modifications.
#
# ______ dronekit_sitl
# ____ dronekit ______ c.., VehicleMode
#
# # Connect to the default sitl, if not one running.
# sitl _ dronekit_sitl.start_d..()
# connection_string _ sitl.connection_string()
#
# # Connect to the Vehicle.
# print("Connected: @"  (connection_string))
# vehicle _ c..(connection_string, wait_ready_True)
#
# print ("GPS: @"  vehicle.gps_0)
# print ("Battery: @"  vehicle.battery)
# print ("Last Heartbeat: @"  vehicle.last_heartbeat)
# print ("Is Armable?: @"  vehicle.is_armable)
# print ("System status: @"  vehicle.system_status.state)
# print ("Mode: @"  vehicle.mode.name)
#
# # Close vehicle object before exiting script
# vehicle.c..
#
# print("Completed")
