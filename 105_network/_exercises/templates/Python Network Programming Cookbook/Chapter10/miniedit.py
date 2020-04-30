# #!/usr/bin/python
#
# """
# MiniEdit: a simple network editor for Mininet
#
# This is a simple demonstration of how one might build a
# GUI application using Mininet as the network model.
#
# Bob Lantz, April 2010
# Gregory Gee, July 2013
#
# Controller icon from http://semlabs.co.uk/
# OpenFlow icon from https://www.opennetworking.org/
# """
#
# # Miniedit needs some work in order to pass pylint...
# # pylint: disable=line-too-long,too-many-branches
# # pylint: disable=too-many-statements,attribute-defined-outside-init
# # pylint: disable=missing-docstring
#
# MINIEDIT_VERSION _ '2.2.0.1'
#
# ____ optparse ______ OptionParser
# # from Tkinter import *
# ____ Tkinter ______ ( Frame, Label, LabelFrame, Entry, OptionMenu, Checkbutton,
#                       Menu, Toplevel, Button, BitmapImage, PhotoImage, Canvas,
#                       Scrollbar, Wm, TclError, StringVar, IntVar,
#                       E, W, EW, NW, Y, VERTICAL, SOLID, CENTER,
#                       RIGHT, LEFT, BOTH, TRUE, FALSE )
# ____ ttk ______ Notebook
# ____ tkMessageBox ______ showerror
# ____ subprocess ______ call
# ______ tkFont
# ______ tkFileDialog
# ______ tkSimpleDialog
# ______ re
# ______ j..
# ____ distutils.version ______ StrictVersion
# ______ __
# ______ ___
# ____ functools ______ partial
#
# __ 'PYTHONPATH' __ __.environ:
#     ___.pa__ _ __.environ[ 'PYTHONPATH' ].s..( ':' ) + ___.pa__
#
# # someday: from ttk import *
#
# ____ mininet.log ______ info, debug, warn, setLogLevel
# ____ mininet.net ______ Mininet, VERSION
# ____ mininet.util ______ netParse, ipAdd, quietRun
# ____ mininet.util ______ buildTopo
# ____ mininet.util ______ custom, customClass
# ____ mininet.term ______ makeTerm, cleanUpScreens
# ____ mininet.node ______ Controller, RemoteController, NOX, OVSController
# ____ mininet.node ______ CPULimitedHost, Host, Node
# ____ mininet.node ______ OVSSwitch, UserSwitch
# ____ mininet.link ______ TCLink, Intf, Link
# ____ mininet.cli ______ CLI
# ____ mininet.moduledeps ______ moduleDeps
# ____ mininet.topo ______ SingleSwitchTopo, LinearTopo, SingleSwitchReversedTopo
# ____ mininet.topolib ______ TreeTopo
#
# info( 'MiniEdit running against Mininet '+VERSION, '\n' )
# MININET_VERSION _ re.sub(r'[^\d\.]', '', VERSION)
# __ StrictVersion(MININET_VERSION) > StrictVersion('2.0'):
#     ____ mininet.node ______ IVSSwitch
#
# TOPODEF _ 'none'
# TOPOS _ { 'minimal': lambda: SingleSwitchTopo( k_2 ),
#           'linear': LinearTopo,
#           'reversed': SingleSwitchReversedTopo,
#           'single': SingleSwitchTopo,
#           'none': N..,
#           'tree': TreeTopo }
# CONTROLLERDEF _ 'ref'
# CONTROLLERS _ { 'ref': Controller,
#                 'ovsc': OVSController,
#                 'nox': NOX,
#                 'remote': RemoteController,
#                 'none': lambda name: N.. }
# LINKDEF _ 'default'
# LINKS _ { 'default': Link,
#           'tc': TCLink }
# HOSTDEF _ 'proc'
# HOSTS _ { 'proc': Host,
#           'rt': custom( CPULimitedHost, sched_'rt' ),
#           'cfs': custom( CPULimitedHost, sched_'cfs' ) }
#
#
# c_ InbandController( RemoteController ):
#     "RemoteController that ignores checkListening"
#     ___ checkListening( self ):
#         "Overridden to do nothing."
#         r_
#
# c_ CustomUserSwitch(UserSwitch):
#     "Customized UserSwitch"
#     ___ - ( self, name, dpopts_'--no-slicing', **kwargs ):
#         UserSwitch.- ( self, name, **kwargs )
#         switchIP _ N..
#
#     ___ getSwitchIP
#         "Return management IP address"
#         r_ switchIP
#
#     ___ setSwitchIP ip):
#         "Set management IP address"
#         switchIP _ ip
#
#     ___ start( self, controllers ):
#         "Start and set management IP address"
#         # Call superclass constructor
#         UserSwitch.start( self, controllers )
#         # Set Switch IP address
#         __ switchIP is no. N..:
#             __ no. inNamespace:
#                 cmd( 'ifconfig', self, switchIP )
#             ____
#                 cmd( 'ifconfig lo', switchIP )
#
# c_ LegacyRouter( Node ):
#     "Simple IP router"
#     ___ - ( self, name, inNamespace_True, **params ):
#         Node.- ( self, name, inNamespace, **params )
#
#     ___ config( self, **_params ):
#         __ intfs:
#             setParam( _params, 'setIP', ip_'0.0.0.0' )
#         r _ Node.config( self, **_params )
#         cmd('sysctl -w net.ipv4.ip_forward=1')
#         r_ r
#
# c_ LegacySwitch(OVSSwitch):
#     "OVS switch in standalone/bridge mode"
#     ___ - ( self, name, **params ):
#         OVSSwitch.- ( self, name, failMode_'standalone', **params )
#         switchIP _ N..
#
# c_ customOvs(OVSSwitch):
#     "Customized OVS switch"
#
#     ___ - ( self, name, failMode_'secure', datapath_'kernel', **params ):
#         OVSSwitch.- ( self, name, failMode_failMode, datapath_datapath,**params )
#         switchIP _ N..
#
#     ___ getSwitchIP
#         "Return management IP address"
#         r_ switchIP
#
#     ___ setSwitchIP ip):
#         "Set management IP address"
#         switchIP _ ip
#
#     ___ start( self, controllers ):
#         "Start and set management IP address"
#         # Call superclass constructor
#         OVSSwitch.start( self, controllers )
#         # Set Switch IP address
#         __ switchIP is no. N..:
#             cmd( 'ifconfig', self, switchIP )
#
# c_ PrefsDialog(tkSimpleDialog.Dialog):
#     "Preferences dialog"
#
#     ___ -  parent, title, prefDefaults):
#
#         prefValues _ prefDefaults
#
#         tkSimpleDialog.Dialog.-  parent, title)
#
#     ___ body master):
#         "Create dialog body"
#         rootFrame _ master
#         leftfieldFrame _ Frame(rootFrame, padx_5, pady_5)
#         leftfieldFrame.grid(row_0, column_0, sticky_'nswe', columnspan_2)
#         rightfieldFrame _ Frame(rootFrame, padx_5, pady_5)
#         rightfieldFrame.grid(row_0, column_2, sticky_'nswe', columnspan_2)
#
#         # Field for Base IP
#         Label(leftfieldFrame, text_"IP Base:").grid(row_0, sticky_E)
#         ipEntry _ Entry(leftfieldFrame)
#         ipEntry.grid(row_0, column_1)
#         ipBase _  prefValues['ipBase']
#         ipEntry.insert(0, ipBase)
#
#         # Selection of terminal type
#         Label(leftfieldFrame, text_"Default Terminal:").grid(row_1, sticky_E)
#         terminalVar _ StringVar(leftfieldFrame)
#         terminalOption _ OptionMenu(leftfieldFrame, terminalVar, "xterm", "gterm")
#         terminalOption.grid(row_1, column_1, sticky_W)
#         terminalType _ prefValues['terminalType']
#         terminalVar.set(terminalType)
#
#         # Field for CLI
#         Label(leftfieldFrame, text_"Start CLI:").grid(row_2, sticky_E)
#         cliStart _ IntVar()
#         cliButton _ Checkbutton(leftfieldFrame, variable_self.cliStart)
#         cliButton.grid(row_2, column_1, sticky_W)
#         __ prefValues['startCLI'] __ '0':
#             cliButton.deselect()
#         ____
#             cliButton.se__()
#
#         # Selection of switch type
#         Label(leftfieldFrame, text_"Default Switch:").grid(row_3, sticky_E)
#         switchType _ StringVar(leftfieldFrame)
#         switchTypeMenu _ OptionMenu(leftfieldFrame, switchType, "Open vSwitch Kernel Mode", "Indigo Virtual Switch", "Userspace Switch", "Userspace Switch inNamespace")
#         switchTypeMenu.grid(row_3, column_1, sticky_W)
#         switchTypePref _ prefValues['switchType']
#         __ switchTypePref __ 'ivs':
#             switchType.set("Indigo Virtual Switch")
#         ____ switchTypePref __ 'userns':
#             switchType.set("Userspace Switch inNamespace")
#         ____ switchTypePref __ 'user':
#             switchType.set("Userspace Switch")
#         ____
#             switchType.set("Open vSwitch Kernel Mode")
#
#
#         # Fields for OVS OpenFlow version
#         ovsFrame_ LabelFrame(leftfieldFrame, text_'Open vSwitch', padx_5, pady_5)
#         ovsFrame.grid(row_4, column_0, columnspan_2, sticky_EW)
#         Label(ovsFrame, text_"OpenFlow 1.0:").grid(row_0, sticky_E)
#         Label(ovsFrame, text_"OpenFlow 1.1:").grid(row_1, sticky_E)
#         Label(ovsFrame, text_"OpenFlow 1.2:").grid(row_2, sticky_E)
#         Label(ovsFrame, text_"OpenFlow 1.3:").grid(row_3, sticky_E)
#
#         ovsOf10 _ IntVar()
#         covsOf10 _ Checkbutton(ovsFrame, variable_self.ovsOf10)
#         covsOf10.grid(row_0, column_1, sticky_W)
#         __ prefValues['openFlowVersions']['ovsOf10'] __ '0':
#             covsOf10.deselect()
#         ____
#             covsOf10.se__()
#
#         ovsOf11 _ IntVar()
#         covsOf11 _ Checkbutton(ovsFrame, variable_self.ovsOf11)
#         covsOf11.grid(row_1, column_1, sticky_W)
#         __ prefValues['openFlowVersions']['ovsOf11'] __ '0':
#             covsOf11.deselect()
#         ____
#             covsOf11.se__()
#
#         ovsOf12 _ IntVar()
#         covsOf12 _ Checkbutton(ovsFrame, variable_self.ovsOf12)
#         covsOf12.grid(row_2, column_1, sticky_W)
#         __ prefValues['openFlowVersions']['ovsOf12'] __ '0':
#             covsOf12.deselect()
#         ____
#             covsOf12.se__()
#
#         ovsOf13 _ IntVar()
#         covsOf13 _ Checkbutton(ovsFrame, variable_self.ovsOf13)
#         covsOf13.grid(row_3, column_1, sticky_W)
#         __ prefValues['openFlowVersions']['ovsOf13'] __ '0':
#             covsOf13.deselect()
#         ____
#             covsOf13.se__()
#
#         # Field for DPCTL listen port
#         Label(leftfieldFrame, text_"dpctl port:").grid(row_5, sticky_E)
#         dpctlEntry _ Entry(leftfieldFrame)
#         dpctlEntry.grid(row_5, column_1)
#         __ 'dpctl' __ prefValues:
#             dpctlEntry.insert(0, prefValues['dpctl'])
#
#         # sFlow
#         sflowValues _ prefValues['sflow']
#         sflowFrame_ LabelFrame(rightfieldFrame, text_'sFlow Profile for Open vSwitch', padx_5, pady_5)
#         sflowFrame.grid(row_0, column_0, columnspan_2, sticky_EW)
#
#         Label(sflowFrame, text_"Target:").grid(row_0, sticky_E)
#         sflowTarget _ Entry(sflowFrame)
#         sflowTarget.grid(row_0, column_1)
#         sflowTarget.insert(0, sflowValues['sflowTarget'])
#
#         Label(sflowFrame, text_"Sampling:").grid(row_1, sticky_E)
#         sflowSampling _ Entry(sflowFrame)
#         sflowSampling.grid(row_1, column_1)
#         sflowSampling.insert(0, sflowValues['sflowSampling'])
#
#         Label(sflowFrame, text_"Header:").grid(row_2, sticky_E)
#         sflowHeader _ Entry(sflowFrame)
#         sflowHeader.grid(row_2, column_1)
#         sflowHeader.insert(0, sflowValues['sflowHeader'])
#
#         Label(sflowFrame, text_"Polling:").grid(row_3, sticky_E)
#         sflowPolling _ Entry(sflowFrame)
#         sflowPolling.grid(row_3, column_1)
#         sflowPolling.insert(0, sflowValues['sflowPolling'])
#
#         # NetFlow
#         nflowValues _ prefValues['netflow']
#         nFrame_ LabelFrame(rightfieldFrame, text_'NetFlow Profile for Open vSwitch', padx_5, pady_5)
#         nFrame.grid(row_1, column_0, columnspan_2, sticky_EW)
#
#         Label(nFrame, text_"Target:").grid(row_0, sticky_E)
#         nflowTarget _ Entry(nFrame)
#         nflowTarget.grid(row_0, column_1)
#         nflowTarget.insert(0, nflowValues['nflowTarget'])
#
#         Label(nFrame, text_"Active Timeout:").grid(row_1, sticky_E)
#         nflowTimeout _ Entry(nFrame)
#         nflowTimeout.grid(row_1, column_1)
#         nflowTimeout.insert(0, nflowValues['nflowTimeout'])
#
#         Label(nFrame, text_"Add ID to Interface:").grid(row_2, sticky_E)
#         nflowAddId _ IntVar()
#         nflowAddIdButton _ Checkbutton(nFrame, variable_self.nflowAddId)
#         nflowAddIdButton.grid(row_2, column_1, sticky_W)
#         __ nflowValues['nflowAddId'] __ '0':
#             nflowAddIdButton.deselect()
#         ____
#             nflowAddIdButton.se__()
#
#         # initial focus
#         r_ ipEntry
#
#     ___ apply
#         ipBase _ ipEntry.get()
#         terminalType _ terminalVar.get()
#         startCLI _ st..(cliStart.get())
#         sw _ switchType.get()
#         dpctl _ dpctlEntry.get()
#
#         ovsOf10 _ st..(ovsOf10.get())
#         ovsOf11 _ st..(ovsOf11.get())
#         ovsOf12 _ st..(ovsOf12.get())
#         ovsOf13 _ st..(ovsOf13.get())
#
#         sflowValues _ {'sflowTarget':sflowTarget.get(),
#                        'sflowSampling':sflowSampling.get(),
#                        'sflowHeader':sflowHeader.get(),
#                        'sflowPolling':sflowPolling.get()}
#         nflowvalues _ {'nflowTarget':nflowTarget.get(),
#                        'nflowTimeout':nflowTimeout.get(),
#                        'nflowAddId':st..(nflowAddId.get())}
#         result _ {'ipBase':ipBase,
#                        'terminalType':terminalType,
#                        'dpctl':dpctl,
#                        'sflow':sflowValues,
#                        'netflow':nflowvalues,
#                        'startCLI':startCLI}
#         __ sw __ 'Indigo Virtual Switch':
#             result['switchType'] _ 'ivs'
#             __ StrictVersion(MININET_VERSION) < StrictVersion('2.1'):
#                 ovsOk _ F..
#                 showerror(title_"Error",
#                           message_'MiniNet version 2.1+ required. You have '+VERSION+'.')
#         ____ sw __ 'Userspace Switch':
#             result['switchType'] _ 'user'
#         ____ sw __ 'Userspace Switch inNamespace':
#             result['switchType'] _ 'userns'
#         ____
#             result['switchType'] _ 'ovs'
#
#         ovsOk _ T..
#         __ ovsOf11 __ "1":
#             ovsVer _ getOvsVersion()
#             __ StrictVersion(ovsVer) < StrictVersion('2.0'):
#                 ovsOk _ F..
#                 showerror(title_"Error",
#                           message_'Open vSwitch version 2.0+ required. You have '+ovsVer+'.')
#         __ ovsOf12 __ "1" or ovsOf13 __ "1":
#             ovsVer _ getOvsVersion()
#             __ StrictVersion(ovsVer) < StrictVersion('1.10'):
#                 ovsOk _ F..
#                 showerror(title_"Error",
#                           message_'Open vSwitch version 1.10+ required. You have '+ovsVer+'.')
#
#         __ ovsOk:
#             result['openFlowVersions']_{'ovsOf10':ovsOf10,
#                                              'ovsOf11':ovsOf11,
#                                              'ovsOf12':ovsOf12,
#                                              'ovsOf13':ovsOf13}
#         ____
#             result _ N..
#
#     @staticmethod
#     ___ getOvsVersion
#         "Return OVS version"
#         outp _ quietRun("ovs-vsctl --version")
#         r _ r'ovs-vsctl \(Open vSwitch\) (.*)'
#         m _ re.search(r, outp)
#         __ m is N..:
#             warn( 'Version check failed' )
#             r_ N..
#         ____
#             info( 'Open vSwitch version is '+m.group(1), '\n' )
#             r_ m.group(1)
#
#
# c_ CustomDialog(o..):
#
#     # TODO: Fix button placement and Title and window focus lock
#     ___ -  master, _title):
#         top_Toplevel(master)
#
#         bodyFrame _ Frame(top)
#         bodyFrame.grid(row_0, column_0, sticky_'nswe')
#         body(bodyFrame)
#
#         #return self.b # initial focus
#         buttonFrame _ Frame(top, relief_'ridge', bd_3, bg_'lightgrey')
#         buttonFrame.grid(row_1 , column_0, sticky_'nswe')
#
#         okButton _ Button(buttonFrame, width_8, text_'OK', relief_'groove',
#                    bd_4, command_self.okAction)
#         okButton.grid(row_0, column_0, sticky_E)
#
#         canlceButton _ Button(buttonFrame, width_8, text_'Cancel', relief_'groove',
#                     bd_4, command_self.cancelAction)
#         canlceButton.grid(row_0, column_1, sticky_W)
#
#     ___ body master):
#         rootFrame _ master
#
#     ___ apply
#         top.d..roy()
#
#     ___ cancelAction
#         top.d..roy()
#
#     ___ okAction
#         apply()
#         top.d..roy()
#
# c_ HostDialog(CustomDialog):
#
#     ___ -  master, title, prefDefaults):
#
#         prefValues _ prefDefaults
#         result _ N..
#
#         CustomDialog.-  master, title)
#
#     ___ body master):
#         rootFrame _ master
#         n _ Notebook(rootFrame)
#         propFrame _ Frame(n)
#         vlanFrame _ Frame(n)
#         interfaceFrame _ Frame(n)
#         mountFrame _ Frame(n)
#         n.add(propFrame, text_'Properties')
#         n.add(vlanFrame, text_'VLAN Interfaces')
#         n.add(interfaceFrame, text_'External Interfaces')
#         n.add(mountFrame, text_'Private Directories')
#         n.pack()
#
#         ### TAB 1
#         # Field for Hostname
#         Label(propFrame, text_"Hostname:").grid(row_0, sticky_E)
#         hostnameEntry _ Entry(propFrame)
#         hostnameEntry.grid(row_0, column_1)
#         __ 'hostname' __ prefValues:
#             hostnameEntry.insert(0, prefValues['hostname'])
#
#         # Field for Switch IP
#         Label(propFrame, text_"IP Address:").grid(row_1, sticky_E)
#         ipEntry _ Entry(propFrame)
#         ipEntry.grid(row_1, column_1)
#         __ 'ip' __ prefValues:
#             ipEntry.insert(0, prefValues['ip'])
#
#         # Field for default route
#         Label(propFrame, text_"Default Route:").grid(row_2, sticky_E)
#         routeEntry _ Entry(propFrame)
#         routeEntry.grid(row_2, column_1)
#         __ 'defaultRoute' __ prefValues:
#             routeEntry.insert(0, prefValues['defaultRoute'])
#
#         # Field for CPU
#         Label(propFrame, text_"Amount CPU:").grid(row_3, sticky_E)
#         cpuEntry _ Entry(propFrame)
#         cpuEntry.grid(row_3, column_1)
#         __ 'cpu' __ prefValues:
#             cpuEntry.insert(0, st..(prefValues['cpu']))
#         # Selection of Scheduler
#         __ 'sched' __ prefValues:
#             sched _  prefValues['sched']
#         ____
#             sched _ 'host'
#         schedVar _ StringVar(propFrame)
#         schedOption _ OptionMenu(propFrame, schedVar, "host", "cfs", "rt")
#         schedOption.grid(row_3, column_2, sticky_W)
#         schedVar.set(sched)
#
#         # Selection of Cores
#         Label(propFrame, text_"Cores:").grid(row_4, sticky_E)
#         coreEntry _ Entry(propFrame)
#         coreEntry.grid(row_4, column_1)
#         __ 'cores' __ prefValues:
#             coreEntry.insert(1, prefValues['cores'])
#
#         # Start command
#         Label(propFrame, text_"Start Command:").grid(row_5, sticky_E)
#         startEntry _ Entry(propFrame)
#         startEntry.grid(row_5, column_1, sticky_'nswe', columnspan_3)
#         __ 'startCommand' __ prefValues:
#             startEntry.insert(0, st..(prefValues['startCommand']))
#         # Stop command
#         Label(propFrame, text_"Stop Command:").grid(row_6, sticky_E)
#         stopEntry _ Entry(propFrame)
#         stopEntry.grid(row_6, column_1, sticky_'nswe', columnspan_3)
#         __ 'stopCommand' __ prefValues:
#             stopEntry.insert(0, st..(prefValues['stopCommand']))
#
#         ### TAB 2
#         # External Interfaces
#         externalInterfaces _ 0
#         Label(interfaceFrame, text_"External Interface:").grid(row_0, column_0, sticky_E)
#         b _ Button( interfaceFrame, text_'Add', command_self.addInterface)
#         b.grid(row_0, column_1)
#
#         interfaceFrame _ VerticalScrolledTable(interfaceFrame, rows_0, columns_1, title_'External Interfaces')
#         interfaceFrame.grid(row_1, column_0, sticky_'nswe', columnspan_2)
#         tableFrame _ interfaceFrame.interior
#         tableFrame.addRow(value_['Interface Name'], readonly_True)
#
#         # Add defined interfaces
#         externalInterfaces _ []
#         __ 'externalInterfaces' __ prefValues:
#             externalInterfaces _ prefValues['externalInterfaces']
#
#         ___ externalInterface __ externalInterfaces:
#             tableFrame.addRow(value_[externalInterface])
#
#         ### TAB 3
#         # VLAN Interfaces
#         vlanInterfaces _ 0
#         Label(vlanFrame, text_"VLAN Interface:").grid(row_0, column_0, sticky_E)
#         vlanButton _ Button( vlanFrame, text_'Add', command_self.addVlanInterface)
#         vlanButton.grid(row_0, column_1)
#
#         vlanFrame _ VerticalScrolledTable(vlanFrame, rows_0, columns_2, title_'VLAN Interfaces')
#         vlanFrame.grid(row_1, column_0, sticky_'nswe', columnspan_2)
#         vlanTableFrame _ vlanFrame.interior
#         vlanTableFrame.addRow(value_['IP Address','VLAN ID'], readonly_True)
#
#         vlanInterfaces _ []
#         __ 'vlanInterfaces' __ prefValues:
#             vlanInterfaces _ prefValues['vlanInterfaces']
#         ___ vlanInterface __ vlanInterfaces:
#             vlanTableFrame.addRow(value_vlanInterface)
#
#         ### TAB 4
#         # Private Directories
#         privateDirectories _ 0
#         Label(mountFrame, text_"Private Directory:").grid(row_0, column_0, sticky_E)
#         mountButton _ Button( mountFrame, text_'Add', command_self.addDirectory)
#         mountButton.grid(row_0, column_1)
#
#         mountFrame _ VerticalScrolledTable(mountFrame, rows_0, columns_2, title_'Directories')
#         mountFrame.grid(row_1, column_0, sticky_'nswe', columnspan_2)
#         mountTableFrame _ mountFrame.interior
#         mountTableFrame.addRow(value_['Mount','Persistent Directory'], readonly_True)
#
#         directoryList _ []
#         __ 'privateDirectory' __ prefValues:
#             directoryList _ prefValues['privateDirectory']
#         ___ privateDir __ directoryList:
#             __ isinstance( privateDir, tuple ):
#                 mountTableFrame.addRow(value_privateDir)
#             ____
#                 mountTableFrame.addRow(value_[privateDir,''])
#
#
#     ___ addDirectory( self ):
#         mountTableFrame.addRow()
#
#     ___ addVlanInterface( self ):
#         vlanTableFrame.addRow()
#
#     ___ addInterface( self ):
#         tableFrame.addRow()
#
#     ___ apply
#         externalInterfaces _ []
#         ___ row __ ra..(tableFrame.rows):
#             __ (le.(tableFrame.get(row, 0)) > 0 and
#                 row > 0):
#                 externalInterfaces.ap..(tableFrame.get(row, 0))
#         vlanInterfaces _ []
#         ___ row __ ra..(vlanTableFrame.rows):
#             __ (le.(vlanTableFrame.get(row, 0)) > 0 and
#                 le.(vlanTableFrame.get(row, 1)) > 0 and
#                 row > 0):
#                 vlanInterfaces.ap..([vlanTableFrame.get(row, 0), vlanTableFrame.get(row, 1)])
#         privateDirectories _ []
#         ___ row __ ra..(mountTableFrame.rows):
#             __ le.(mountTableFrame.get(row, 0)) > 0 and row > 0:
#                 __ le.(mountTableFrame.get(row, 1)) > 0:
#                     privateDirectories.ap..((mountTableFrame.get(row, 0), mountTableFrame.get(row, 1)))
#                 ____
#                     privateDirectories.ap..(mountTableFrame.get(row, 0))
#
#         results _ {'cpu': cpuEntry.get(),
#                    'cores':coreEntry.get(),
#                    'sched':schedVar.get(),
#                    'hostname':hostnameEntry.get(),
#                    'ip':ipEntry.get(),
#                    'defaultRoute':routeEntry.get(),
#                    'startCommand':startEntry.get(),
#                    'stopCommand':stopEntry.get(),
#                    'privateDirectory':privateDirectories,
#                    'externalInterfaces':externalInterfaces,
#                    'vlanInterfaces':vlanInterfaces}
#         result _ results
#
# c_ SwitchDialog(CustomDialog):
#
#     ___ -  master, title, prefDefaults):
#
#         prefValues _ prefDefaults
#         result _ N..
#         CustomDialog.-  master, title)
#
#     ___ body master):
#         rootFrame _ master
#         leftfieldFrame _ Frame(rootFrame)
#         rightfieldFrame _ Frame(rootFrame)
#         leftfieldFrame.grid(row_0, column_0, sticky_'nswe')
#         rightfieldFrame.grid(row_0, column_1, sticky_'nswe')
#
#         rowCount _ 0
#         externalInterfaces _ []
#         __ 'externalInterfaces' __ prefValues:
#             externalInterfaces _ prefValues['externalInterfaces']
#
#         # Field for Hostname
#         Label(leftfieldFrame, text_"Hostname:").grid(row_rowCount, sticky_E)
#         hostnameEntry _ Entry(leftfieldFrame)
#         hostnameEntry.grid(row_rowCount, column_1)
#         hostnameEntry.insert(0, prefValues['hostname'])
#         rowCount+_1
#
#         # Field for DPID
#         Label(leftfieldFrame, text_"DPID:").grid(row_rowCount, sticky_E)
#         dpidEntry _ Entry(leftfieldFrame)
#         dpidEntry.grid(row_rowCount, column_1)
#         __ 'dpid' __ prefValues:
#             dpidEntry.insert(0, prefValues['dpid'])
#         rowCount+_1
#
#         # Field for Netflow
#         Label(leftfieldFrame, text_"Enable NetFlow:").grid(row_rowCount, sticky_E)
#         nflow _ IntVar()
#         nflowButton _ Checkbutton(leftfieldFrame, variable_self.nflow)
#         nflowButton.grid(row_rowCount, column_1, sticky_W)
#         __ 'netflow' __ prefValues:
#             __ prefValues['netflow'] __ '0':
#                 nflowButton.deselect()
#             ____
#                 nflowButton.se__()
#         ____
#             nflowButton.deselect()
#         rowCount+_1
#
#         # Field for sflow
#         Label(leftfieldFrame, text_"Enable sFlow:").grid(row_rowCount, sticky_E)
#         sflow _ IntVar()
#         sflowButton _ Checkbutton(leftfieldFrame, variable_self.sflow)
#         sflowButton.grid(row_rowCount, column_1, sticky_W)
#         __ 'sflow' __ prefValues:
#             __ prefValues['sflow'] __ '0':
#                 sflowButton.deselect()
#             ____
#                 sflowButton.se__()
#         ____
#             sflowButton.deselect()
#         rowCount+_1
#
#         # Selection of switch type
#         Label(leftfieldFrame, text_"Switch Type:").grid(row_rowCount, sticky_E)
#         switchType _ StringVar(leftfieldFrame)
#         switchTypeMenu _ OptionMenu(leftfieldFrame, switchType, "Default", "Open vSwitch Kernel Mode", "Indigo Virtual Switch", "Userspace Switch", "Userspace Switch inNamespace")
#         switchTypeMenu.grid(row_rowCount, column_1, sticky_W)
#         __ 'switchType' __ prefValues:
#             switchTypePref _ prefValues['switchType']
#             __ switchTypePref __ 'ivs':
#                 switchType.set("Indigo Virtual Switch")
#             ____ switchTypePref __ 'userns':
#                 switchType.set("Userspace Switch inNamespace")
#             ____ switchTypePref __ 'user':
#                 switchType.set("Userspace Switch")
#             ____ switchTypePref __ 'ovs':
#                 switchType.set("Open vSwitch Kernel Mode")
#             ____
#                 switchType.set("Default")
#         ____
#             switchType.set("Default")
#         rowCount+_1
#
#         # Field for Switch IP
#         Label(leftfieldFrame, text_"IP Address:").grid(row_rowCount, sticky_E)
#         ipEntry _ Entry(leftfieldFrame)
#         ipEntry.grid(row_rowCount, column_1)
#         __ 'switchIP' __ prefValues:
#             ipEntry.insert(0, prefValues['switchIP'])
#         rowCount+_1
#
#         # Field for DPCTL port
#         Label(leftfieldFrame, text_"DPCTL port:").grid(row_rowCount, sticky_E)
#         dpctlEntry _ Entry(leftfieldFrame)
#         dpctlEntry.grid(row_rowCount, column_1)
#         __ 'dpctl' __ prefValues:
#             dpctlEntry.insert(0, prefValues['dpctl'])
#         rowCount+_1
#
#         # External Interfaces
#         Label(rightfieldFrame, text_"External Interface:").grid(row_0, sticky_E)
#         b _ Button( rightfieldFrame, text_'Add', command_self.addInterface)
#         b.grid(row_0, column_1)
#
#         interfaceFrame _ VerticalScrolledTable(rightfieldFrame, rows_0, columns_1, title_'External Interfaces')
#         interfaceFrame.grid(row_1, column_0, sticky_'nswe', columnspan_2)
#         tableFrame _ interfaceFrame.interior
#
#         # Add defined interfaces
#         ___ externalInterface __ externalInterfaces:
#             tableFrame.addRow(value_[externalInterface])
#
#         commandFrame _ Frame(rootFrame)
#         commandFrame.grid(row_1, column_0, sticky_'nswe', columnspan_2)
#         commandFrame.columnconfigure(1, weight_1)
#         # Start command
#         Label(commandFrame, text_"Start Command:").grid(row_0, column_0, sticky_W)
#         startEntry _ Entry(commandFrame)
#         startEntry.grid(row_0, column_1,  sticky_'nsew')
#         __ 'startCommand' __ prefValues:
#             startEntry.insert(0, st..(prefValues['startCommand']))
#         # Stop command
#         Label(commandFrame, text_"Stop Command:").grid(row_1, column_0, sticky_W)
#         stopEntry _ Entry(commandFrame)
#         stopEntry.grid(row_1, column_1, sticky_'nsew')
#         __ 'stopCommand' __ prefValues:
#             stopEntry.insert(0, st..(prefValues['stopCommand']))
#
#     ___ addInterface( self ):
#         tableFrame.addRow()
#
#     ___ d..Dpid( self, name):
#         "Derive dpid from switch name, s1 -> 1"
#         assert self  # satisfy pylint and allow contextual override
#         ___
#             dpid _ int( re.findall( r'\d+', name )[ 0 ] )
#             dpid _ hex( dpid )[ 2: ]
#             r_ dpid
#         ______ IndexError:
#             r_ N..
#             #raise Exception( 'Unable to derive default datapath ID - '
#             #                 'please either specify a dpid or use a '
#             #                 'canonical switch name such as s23.' )
#
#     ___ apply
#         externalInterfaces _ []
#         ___ row __ ra..(tableFrame.rows):
#             # debug( 'Interface is ' + self.tableFrame.get(row, 0), '\n' )
#             __ le.(tableFrame.get(row, 0)) > 0:
#                 externalInterfaces.ap..(tableFrame.get(row, 0))
#
#         dpid _ dpidEntry.get()
#         __ (d..Dpid(hostnameEntry.get()) is N..
#            and le.(dpid) __ 0):
#             showerror(title_"Error",
#                           message_ 'Unable to derive default datapath ID - '
#                              'please either specify a DPID or use a '
#                              'canonical switch name such as s23.' )
#
#
#         results _ {'externalInterfaces':externalInterfaces,
#                    'hostname':hostnameEntry.get(),
#                    'dpid':dpid,
#                    'startCommand':startEntry.get(),
#                    'stopCommand':stopEntry.get(),
#                    'sflow':st..(sflow.get()),
#                    'netflow':st..(nflow.get()),
#                    'dpctl':dpctlEntry.get(),
#                    'switchIP':ipEntry.get()}
#         sw _ switchType.get()
#         __ sw __ 'Indigo Virtual Switch':
#             results['switchType'] _ 'ivs'
#             __ StrictVersion(MININET_VERSION) < StrictVersion('2.1'):
#                 ovsOk _ F..
#                 showerror(title_"Error",
#                           message_'MiniNet version 2.1+ required. You have '+VERSION+'.')
#         ____ sw __ 'Userspace Switch inNamespace':
#             results['switchType'] _ 'userns'
#         ____ sw __ 'Userspace Switch':
#             results['switchType'] _ 'user'
#         ____ sw __ 'Open vSwitch Kernel Mode':
#             results['switchType'] _ 'ovs'
#         ____
#             results['switchType'] _ 'default'
#         result _ results
#
#
# c_ VerticalScrolledTable(LabelFrame):
#     """A pure Tkinter scrollable frame that actually works!
#
#     * Use the 'interior' attribute to place widgets inside the scrollable frame
#     * Construct and pack/place/grid normally
#     * This frame only allows vertical scrolling
#
#     """
#     ___ -  parent, rows_2, columns_2, title_None, $, **kw):
#         LabelFrame.-  parent, text_title, padx_5, pady_5, $, **kw)
#
#         # create a canvas object and a vertical scrollbar for scrolling it
#         vscrollbar _ Scrollbar orient_VERTICAL)
#         vscrollbar.pack(fill_Y, side_RIGHT, expand_FALSE)
#         canvas _ Canvas bd_0, highlightthickness_0,
#                         yscrollcommand_vscrollbar.set)
#         canvas.pack(side_LEFT, fill_BOTH, expand_TRUE)
#         vscrollbar.config(command_canvas.yview)
#
#         # reset the view
#         canvas.xview_moveto(0)
#         canvas.yview_moveto(0)
#
#         # create a frame inside the canvas which will be scrolled with it
#         interior _ interior _ TableFrame(canvas, rows_rows, columns_columns)
#         interior_id _ canvas.create_window(0, 0, window_interior,
#                                            anchor_NW)
#
#         # track changes to the canvas and frame width and sync them,
#         # also updating the scrollbar
#         ___ _configure_interior(_event):
#         # update the scrollbars to match the size of the inner frame
#             size _ (interior.winfo_reqwidth(), interior.winfo_reqheight())
#             canvas.config(scrollregion_"0 0 @ @"  size)
#             __ interior.winfo_reqwidth() !_ canvas.winfo_width
#             # update the canvas's width to fit the inner frame
#                 canvas.config(width_interior.winfo_reqwidth())
#         interior.b..('<Configure>', _configure_interior)
#
#         ___ _configure_canvas(_event):
#             __ interior.winfo_reqwidth() !_ canvas.winfo_width
#                 # update the inner frame's width to fill the canvas
#                 canvas.itemconfigure(interior_id, width_canvas.winfo_width())
#         canvas.b..('<Configure>', _configure_canvas)
#
#         r_
#
# c_ TableFrame(Frame):
#     ___ -  parent, rows_2, columns_2):
#
#         Frame.-  parent, background_"black")
#         _widgets _ []
#         rows _ rows
#         columns _ columns
#         ___ row __ ra..(rows):
#             current_row _ []
#             ___ column __ ra..(columns):
#                 label _ Entry borderwidth_0)
#                 label.grid(row_row, column_column, sticky_"wens", padx_1, pady_1)
#                 current_row.ap..(label)
#             _widgets.ap..(current_row)
#
#     ___ set row, column, value):
#         widget _ _widgets[row][column]
#         widget.insert(0, value)
#
#     ___ get row, column):
#         widget _ _widgets[row][column]
#         r_ widget.get()
#
#     ___ addRow( self, value_None, readonly_False ):
#         # debug( "Adding row " + st..(self.rows +1), '\n' )
#         current_row _ []
#         ___ column __ ra..(columns):
#             label _ Entry borderwidth_0)
#             label.grid(row_self.rows, column_column, sticky_"wens", padx_1, pady_1)
#             __ value is no. N..:
#                 label.insert(0, value[column])
#             __ readonly __ T..:
#                 label.configure(state_'readonly')
#             current_row.ap..(label)
#         _widgets.ap..(current_row)
#         update_idletasks()
#         rows +_ 1
#
# c_ LinkDialog(tkSimpleDialog.Dialog):
#
#     ___ -  parent, title, linkDefaults):
#
#         linkValues _ linkDefaults
#
#         tkSimpleDialog.Dialog.-  parent, title)
#
#     ___ body master):
#
#         var _ StringVar(master)
#         Label(master, text_"Bandwidth:").grid(row_0, sticky_E)
#         e1 _ Entry(master)
#         e1.grid(row_0, column_1)
#         Label(master, text_"Mbit").grid(row_0, column_2, sticky_W)
#         __ 'bw' __ linkValues:
#             e1.insert(0,st..(linkValues['bw']))
#
#         Label(master, text_"Delay:").grid(row_1, sticky_E)
#         e2 _ Entry(master)
#         e2.grid(row_1, column_1)
#         __ 'delay' __ linkValues:
#             e2.insert(0, linkValues['delay'])
#
#         Label(master, text_"Loss:").grid(row_2, sticky_E)
#         e3 _ Entry(master)
#         e3.grid(row_2, column_1)
#         Label(master, text_"").grid(row_2, column_2, sticky_W)
#         __ 'loss' __ linkValues:
#             e3.insert(0, st..(linkValues['loss']))
#
#         Label(master, text_"Max Queue size:").grid(row_3, sticky_E)
#         e4 _ Entry(master)
#         e4.grid(row_3, column_1)
#         __ 'max_queue_size' __ linkValues:
#             e4.insert(0, st..(linkValues['max_queue_size']))
#
#         Label(master, text_"Jitter:").grid(row_4, sticky_E)
#         e5 _ Entry(master)
#         e5.grid(row_4, column_1)
#         __ 'jitter' __ linkValues:
#             e5.insert(0, linkValues['jitter'])
#
#         Label(master, text_"Speedup:").grid(row_5, sticky_E)
#         e6 _ Entry(master)
#         e6.grid(row_5, column_1)
#         __ 'speedup' __ linkValues:
#             e6.insert(0, st..(linkValues['speedup']))
#
#         r_ e1 # initial focus
#
#     ___ apply
#         result _ {}
#         __ le.(e1.get()) > 0:
#             result['bw'] _ int(e1.get())
#         __ le.(e2.get()) > 0:
#             result['delay'] _ e2.get()
#         __ le.(e3.get()) > 0:
#             result['loss'] _ int(e3.get())
#         __ le.(e4.get()) > 0:
#             result['max_queue_size'] _ int(e4.get())
#         __ le.(e5.get()) > 0:
#             result['jitter'] _ e5.get()
#         __ le.(e6.get()) > 0:
#             result['speedup'] _ int(e6.get())
#
# c_ ControllerDialog(tkSimpleDialog.Dialog):
#
#     ___ -  parent, title, ctrlrDefaults_None):
#
#         __ ctrlrDefaults:
#             ctrlrValues _ ctrlrDefaults
#
#         tkSimpleDialog.Dialog.-  parent, title)
#
#     ___ body master):
#
#         var _ StringVar(master)
#         protcolvar _ StringVar(master)
#
#         rowCount_0
#         # Field for Hostname
#         Label(master, text_"Name:").grid(row_rowCount, sticky_E)
#         hostnameEntry _ Entry(master)
#         hostnameEntry.grid(row_rowCount, column_1)
#         hostnameEntry.insert(0, ctrlrValues['hostname'])
#         rowCount+_1
#
#         # Field for Remove Controller Port
#         Label(master, text_"Controller Port:").grid(row_rowCount, sticky_E)
#         e2 _ Entry(master)
#         e2.grid(row_rowCount, column_1)
#         e2.insert(0, ctrlrValues['remotePort'])
#         rowCount+_1
#
#         # Field for Controller Type
#         Label(master, text_"Controller Type:").grid(row_rowCount, sticky_E)
#         controllerType _ ctrlrValues['controllerType']
#         o1 _ OptionMenu(master, var, "Remote Controller", "In-Band Controller", "OpenFlow Reference", "OVS Controller")
#         o1.grid(row_rowCount, column_1, sticky_W)
#         __ controllerType __ 'ref':
#             var.set("OpenFlow Reference")
#         ____ controllerType __ 'inband':
#             var.set("In-Band Controller")
#         ____ controllerType __ 'remote':
#             var.set("Remote Controller")
#         ____
#             var.set("OVS Controller")
#         rowCount+_1
#
#         # Field for Controller Protcol
#         Label(master, text_"Protocol:").grid(row_rowCount, sticky_E)
#         __ 'controllerProtocol' __ ctrlrValues:
#             controllerProtocol _ ctrlrValues['controllerProtocol']
#         ____
#             controllerProtocol _ 'tcp'
#         protcol _ OptionMenu(master, protcolvar, "TCP", "SSL")
#         protcol.grid(row_rowCount, column_1, sticky_W)
#         __ controllerProtocol __ 'ssl':
#             protcolvar.set("SSL")
#         ____
#             protcolvar.set("TCP")
#         rowCount+_1
#
#         # Field for Remove Controller IP
#         remoteFrame_ LabelFrame(master, text_'Remote/In-Band Controller', padx_5, pady_5)
#         remoteFrame.grid(row_rowCount, column_0, columnspan_2, sticky_W)
#
#         Label(remoteFrame, text_"IP Address:").grid(row_0, sticky_E)
#         e1 _ Entry(remoteFrame)
#         e1.grid(row_0, column_1)
#         e1.insert(0, ctrlrValues['remoteIP'])
#         rowCount+_1
#
#         r_ hostnameEntry # initial focus
#
#     ___ apply
#         result _ { 'hostname': hostnameEntry.get(),
#                         'remoteIP': e1.get(),
#                         'remotePort': int(e2.get())}
#
#         controllerType _ var.get()
#         __ controllerType __ 'Remote Controller':
#             result['controllerType'] _ 'remote'
#         ____ controllerType __ 'In-Band Controller':
#             result['controllerType'] _ 'inband'
#         ____ controllerType __ 'OpenFlow Reference':
#             result['controllerType'] _ 'ref'
#         ____
#             result['controllerType'] _ 'ovsc'
#         controllerProtocol _ protcolvar.get()
#         __ controllerProtocol __ 'SSL':
#             result['controllerProtocol'] _ 'ssl'
#         ____
#             result['controllerProtocol'] _ 'tcp'
#
# c_ ToolTip(o..):
#
#     ___ -  widget):
#         widget _ widget
#         tipwindow _ N..
#         id _ N..
#         x _ y _ 0
#
#     ___ showtip text):
#         "Display text in tooltip window"
#         text _ text
#         __ tipwindow or no. text:
#             r_
#         x, y, _cx, cy _ widget.bbox("insert")
#         x _ x + widget.winfo_rootx() + 27
#         y _ y + cy + widget.winfo_rooty() +27
#         tipwindow _ tw _ Toplevel(widget)
#         tw.wm_overrideredirect(1)
#         tw.wm_geometry("+d+d"  (x, y))
#         ___
#             # For Mac OS
#             # pylint: disable=protected-access
#             tw.tk.call("::tk::unsupported::MacWindowStyle",
#                        "style", tw._w,
#                        "help", "noActivates")
#             # pylint: enable=protected-access
#         ______ TclError:
#             p..
#         label _ Label(tw, text_self.text, justify_LEFT,
#                       background_"#ffffe0", relief_SOLID, borderwidth_1,
#                       font_("tahoma", "8", "normal"))
#         label.pack(ipadx_1)
#
#     ___ hidetip
#         tw _ tipwindow
#         tipwindow _ N..
#         __ tw:
#             tw.d..roy()
#
# c_ MiniEdit( Frame ):
#
#     "A simple network editor for Mininet."
#
#     ___ - ( self, parent_None, cheight_600, cwidth_1000 ):
#
#         d..IpBase_'10.0.0.0/8'
#
#         nflowDefaults _ {'nflowTarget':'',
#                               'nflowTimeout':'600',
#                               'nflowAddId':'0'}
#         sflowDefaults _ {'sflowTarget':'',
#                               'sflowSampling':'400',
#                               'sflowHeader':'128',
#                               'sflowPolling':'30'}
#
#         appPrefs_{
#             "ipBase": d..IpBase,
#             "startCLI": "0",
#             "terminalType": 'xterm',
#             "switchType": 'ovs',
#             "dpctl": '',
#             'sflow':sflowDefaults,
#             'netflow':nflowDefaults,
#             'openFlowVersions':{'ovsOf10':'1',
#                                 'ovsOf11':'0',
#                                 'ovsOf12':'0',
#                                 'ovsOf13':'0'}
#
#         }
#
#
#         Frame.- ( self, parent )
#         a.. _ N..
#         appName _ 'MiniEdit'
#         fixedFont _ tkFont.Font ( family_"DejaVu Sans Mono", size_"14" )
#
#         # Style
#         font _ ( 'Geneva', 9 )
#         smallFont _ ( 'Geneva', 7 )
#         bg _ 'white'
#
#         # Title
#         top _ winfo_toplevel()
#         top.title( appName )
#
#         # Menu bar
#         createMenubar()
#
#         # Editing canvas
#         cheight, cwidth _ cheight, cwidth
#         cframe, canvas _ createCanvas()
#
#         # Toolbar
#         controllers _ {}
#
#         # Toolbar
#         images _ miniEditImages()
#         buttons _ {}
#         active _ N..
#         tools _ ( 'Select', 'Host', 'Switch', 'LegacySwitch', 'LegacyRouter', 'NetLink', 'Controller' )
#         customColors _ { 'Switch': 'darkGreen', 'Host': 'blue' }
#         toolbar _ createToolbar()
#
#         # Layout
#         toolbar.grid( column_0, row_0, sticky_'nsew')
#         cframe.grid( column_1, row_0 )
#         columnconfigure( 1, weight_1 )
#         rowconfigure( 0, weight_1 )
#         pack( expand_True, fill_'both' )
#
#         # About box
#         aboutBox _ N..
#
#         # Initialize node data
#         nodeBindings _ createNodeBindings()
#         nodePrefixes _ { 'LegacyRouter': 'r', 'LegacySwitch': 's', 'Switch': 's', 'Host': 'h' , 'Controller': 'c'}
#         widgetToItem _ {}
#         itemToWidget _ {}
#
#         # Initialize link tool
#         link _ linkWidget _ N..
#
#         # Selection support
#         selection _ N..
#
#         # Keyboard bindings
#         b..( '<Control-q>', lambda event: q.. )
#         b..( '<KeyPress-Delete>', deleteSelection )
#         b..( '<KeyPress-BackSpace>', deleteSelection )
#         focus()
#
#         hostPopup _ Menu(top, tearoff_0)
#         hostPopup.add_command(label_'Host Options', font_self.font)
#         hostPopup.add_separator()
#         hostPopup.add_command(label_'Properties', font_self.font, command_self.hostDetails )
#
#         hostRunPopup _ Menu(top, tearoff_0)
#         hostRunPopup.add_command(label_'Host Options', font_self.font)
#         hostRunPopup.add_separator()
#         hostRunPopup.add_command(label_'Terminal', font_self.font, command_self.xterm )
#
#         legacyRouterRunPopup _ Menu(top, tearoff_0)
#         legacyRouterRunPopup.add_command(label_'Router Options', font_self.font)
#         legacyRouterRunPopup.add_separator()
#         legacyRouterRunPopup.add_command(label_'Terminal', font_self.font, command_self.xterm )
#
#         switchPopup _ Menu(top, tearoff_0)
#         switchPopup.add_command(label_'Switch Options', font_self.font)
#         switchPopup.add_separator()
#         switchPopup.add_command(label_'Properties', font_self.font, command_self.switchDetails )
#
#         switchRunPopup _ Menu(top, tearoff_0)
#         switchRunPopup.add_command(label_'Switch Options', font_self.font)
#         switchRunPopup.add_separator()
#         switchRunPopup.add_command(label_'List bridge details', font_self.font, command_self.listBridge )
#
#         linkPopup _ Menu(top, tearoff_0)
#         linkPopup.add_command(label_'Link Options', font_self.font)
#         linkPopup.add_separator()
#         linkPopup.add_command(label_'Properties', font_self.font, command_self.linkDetails )
#
#         linkRunPopup _ Menu(top, tearoff_0)
#         linkRunPopup.add_command(label_'Link Options', font_self.font)
#         linkRunPopup.add_separator()
#         linkRunPopup.add_command(label_'Link Up', font_self.font, command_self.linkUp )
#         linkRunPopup.add_command(label_'Link Down', font_self.font, command_self.linkDown )
#
#         controllerPopup _ Menu(top, tearoff_0)
#         controllerPopup.add_command(label_'Controller Options', font_self.font)
#         controllerPopup.add_separator()
#         controllerPopup.add_command(label_'Properties', font_self.font, command_self.controllerDetails )
#
#
#         # Event handling initalization
#         linkx _ linky _ linkItem _ N..
#         lastSelection _ N..
#
#         # Model initialization
#         links _ {}
#         hostOpts _ {}
#         switchOpts _ {}
#         hostCount _ 0
#         switchCount _ 0
#         controllerCount _ 0
#         net _ N..
#
#         # Close window gracefully
#         Wm.wm_protocol( top, name_'WM_DELETE_WINDOW', func_self.quit )
#
#     ___ quit( self ):
#         "Stop our network, if any, then quit."
#         stop()
#         Frame.quit( self )
#
#     ___ createMenubar( self ):
#         "Create our menu bar."
#
#         font _ font
#
#         mbar _ Menu( top, font_font )
#         top.configure( menu_mbar )
#
#
#         fileMenu _ Menu( mbar, tearoff_False )
#         mbar.add_cascade( label_"File", font_font, menu_fileMenu )
#         fileMenu.add_command( label_"New", font_font, command_self.newTopology )
#         fileMenu.add_command( label_"Open", font_font, command_self.loadTopology )
#         fileMenu.add_command( label_"Save", font_font, command_self.saveTopology )
#         fileMenu.add_command( label_"Export Level 2 Script", font_font, command_self.exportScript )
#         fileMenu.add_separator()
#         fileMenu.add_command( label_'Quit', command_self.quit, font_font )
#
#         editMenu _ Menu( mbar, tearoff_False )
#         mbar.add_cascade( label_"Edit", font_font, menu_editMenu )
#         editMenu.add_command( label_"Cut", font_font,
#                               command_lambda: deleteSelection( N.. ) )
#         editMenu.add_command( label_"Preferences", font_font, command_self.prefDetails)
#
#         runMenu _ Menu( mbar, tearoff_False )
#         mbar.add_cascade( label_"Run", font_font, menu_runMenu )
#         runMenu.add_command( label_"Run", font_font, command_self.doRun )
#         runMenu.add_command( label_"Stop", font_font, command_self.doStop )
#         fileMenu.add_separator()
#         runMenu.add_command( label_'Show OVS Summary', font_font, command_self.ovsShow )
#         runMenu.add_command( label_'Root Terminal', font_font, command_self.rootTerminal )
#
#         # Application menu
#         appMenu _ Menu( mbar, tearoff_False )
#         mbar.add_cascade( label_"Help", font_font, menu_appMenu )
#         appMenu.add_command( label_'About MiniEdit', command_self.about,
#                              font_font)
#     # Canvas
#
#     ___ createCanvas( self ):
#         "Create and return our scrolling canvas frame."
#         f _ Frame( self )
#
#         canvas _ Canvas( f, width_self.cwidth, height_self.cheight,
#                          bg_self.bg )
#
#         # Scroll bars
#         xbar _ Scrollbar( f, orient_'horizontal', command_canvas.xview )
#         ybar _ Scrollbar( f, orient_'vertical', command_canvas.yview )
#         canvas.configure( xscrollcommand_xbar.set, yscrollcommand_ybar.set )
#
#         # Resize box
#         resize _ Label( f, bg_'white' )
#
#         # Layout
#         canvas.grid( row_0, column_1, sticky_'nsew')
#         ybar.grid( row_0, column_2, sticky_'ns')
#         xbar.grid( row_1, column_1, sticky_'ew' )
#         resize.grid( row_1, column_2, sticky_'nsew' )
#
#         # Resize behavior
#         f.rowconfigure( 0, weight_1 )
#         f.columnconfigure( 1, weight_1 )
#         f.grid( row_0, column_0, sticky_'nsew' )
#         f.b..( '<Configure>', lambda event: updateScrollRegion() )
#
#         # Mouse bindings
#         canvas.b..( '<ButtonPress-1>', clickCanvas )
#         canvas.b..( '<B1-Motion>', dragCanvas )
#         canvas.b..( '<ButtonRelease-1>', releaseCanvas )
#
#         r_ f, canvas
#
#     ___ updateScrollRegion( self ):
#         "Update canvas scroll region to hold everything."
#         bbox _ canvas.bbox( 'all' )
#         __ bbox is no. N..:
#             canvas.configure( scrollregion_( 0, 0, bbox[ 2 ],
#                                    bbox[ 3 ] ) )
#
#     ___ canvasx( self, x_root ):
#         "Convert root x coordinate to canvas coordinate."
#         c _ canvas
#         r_ c.canvasx( x_root ) - c.winfo_rootx()
#
#     ___ canvasy( self, y_root ):
#         "Convert root y coordinate to canvas coordinate."
#         c _ canvas
#         r_ c.canvasy( y_root ) - c.winfo_rooty()
#
#     # Toolbar
#
#     ___ activate( self, toolName ):
#         "Activate a tool and press its button."
#         # Adjust button appearance
#         __ active:
#             buttons[ active ].configure( relief_'raised' )
#         buttons[ toolName ].configure( relief_'sunken' )
#         # Activate dynamic bindings
#         active _ toolName
#
#
#     @staticmethod
#     ___ createToolTip(widget, text):
#         toolTip _ ToolTip(widget)
#         ___ enter(_event):
#             toolTip.showtip(text)
#         ___ leave(_event):
#             toolTip.hidetip()
#         widget.b..('<Enter>', enter)
#         widget.b..('<Leave>', leave)
#
#     ___ createToolbar( self ):
#         "Create and return our toolbar frame."
#
#         toolbar _ Frame( self )
#
#         # Tools
#         ___ tool __ tools:
#             cmd _ ( lambda t_tool: activate( t ) )
#             b _ Button( toolbar, text_tool, font_self.smallFont, command_cmd)
#             __ tool __ images:
#                 b.config( height_35, image_self.images[ tool ] )
#                 createToolTip(b, st..(tool))
#                 # b.config( compound='top' )
#             b.pack( fill_'x' )
#             buttons[ tool ] _ b
#         activate( tools[ 0 ] )
#
#         # Spacer
#         Label( toolbar, text_'' ).pack()
#
#         # Commands
#         ___ cmd, color __ [ ( 'Stop', 'darkRed' ), ( 'Run', 'darkGreen' ) ]:
#             doCmd _ getattr( self, 'do' + cmd )
#             b _ Button( toolbar, text_cmd, font_self.smallFont,
#                         fg_color, command_doCmd )
#             b.pack( fill_'x', side_'bottom' )
#
#         r_ toolbar
#
#     ___ doRun( self ):
#         "Run command."
#         activate( 'Select' )
#         ___ tool __ tools:
#             buttons[ tool ].config( state_'disabled' )
#         s..
#
#     ___ doStop( self ):
#         "Stop command."
#         stop()
#         ___ tool __ tools:
#             buttons[ tool ].config( state_'normal' )
#
#     ___ addNode( self, node, nodeNum, x, y, name_None):
#         "Add a new node to our canvas."
#         __ 'Switch' __ node:
#             switchCount +_ 1
#         __ 'Host' __ node:
#             hostCount +_ 1
#         __ 'Controller' __ node:
#             controllerCount +_ 1
#         __ name is N..:
#             name _ nodePrefixes[ node ] + nodeNum
#         addNamedNode(node, name, x, y)
#
#     ___ addNamedNode( self, node, name, x, y):
#         "Add a new node to our canvas."
#         icon _ nodeIcon( node, name )
#         item _ canvas.create_window( x, y, anchor_'c', window_icon,
#                                           tags_node )
#         widgetToItem[ icon ] _ item
#         itemToWidget[ item ] _ icon
#         icon.links _ {}
#
#     ___ convertJsonUnicode text):
#         "Some part of Mininet don't like Unicode"
#         __ isinstance(text, dict):
#             r_ {convertJsonUnicode(key): convertJsonUnicode(value) ___ key, value __ text.iteritems()}
#         ____ isinstance(text, list):
#             r_ [convertJsonUnicode(element) ___ element __ text]
#         ____ isinstance(text, unicode):
#             r_ text.e..('utf-8')
#         ____
#             r_ text
#
#     ___ loadTopology( self ):
#         "Load command."
#         c _ canvas
#
#         myFormats _ [
#             ('Mininet Topology','*.mn'),
#             ('All Files','*'),
#         ]
#         f _ tkFileDialog.askopenfile(filetypes_myFormats, mode_'rb')
#         __ f __ N..:
#             r_
#         newTopology()
#         loadedTopology _ convertJsonUnicode(?.load(f))
#
#         # Load application preferences
#         __ 'application' __ loadedTopology:
#             appPrefs _ dict(appPrefs.items() + loadedTopology['application'].items())
#             __ "ovsOf10" no. __ appPrefs["openFlowVersions"]:
#                 appPrefs["openFlowVersions"]["ovsOf10"] _ '0'
#             __ "ovsOf11" no. __ appPrefs["openFlowVersions"]:
#                 appPrefs["openFlowVersions"]["ovsOf11"] _ '0'
#             __ "ovsOf12" no. __ appPrefs["openFlowVersions"]:
#                 appPrefs["openFlowVersions"]["ovsOf12"] _ '0'
#             __ "ovsOf13" no. __ appPrefs["openFlowVersions"]:
#                 appPrefs["openFlowVersions"]["ovsOf13"] _ '0'
#             __ "sflow" no. __ appPrefs:
#                 appPrefs["sflow"] _ sflowDefaults
#             __ "netflow" no. __ appPrefs:
#                 appPrefs["netflow"] _ nflowDefaults
#
#         # Load controllers
#         __ 'controllers' __ loadedTopology:
#             __ loadedTopology['version'] __ '1':
#                 # This is old location of controller info
#                 hostname _ 'c0'
#                 controllers _ {}
#                 controllers[hostname] _ loadedTopology['controllers']['c0']
#                 controllers[hostname]['hostname'] _ hostname
#                 addNode('Controller', 0, float(30), float(30), name_hostname)
#                 icon _ findWidgetByName(hostname)
#                 icon.b..('<Button-3>', do_controllerPopup )
#             ____
#                 controllers _ loadedTopology['controllers']
#                 ___ controller __ controllers:
#                     hostname _ controller['opts']['hostname']
#                     x _ controller['x']
#                     y _ controller['y']
#                     addNode('Controller', 0, float(x), float(y), name_hostname)
#                     controllers[hostname] _ controller['opts']
#                     icon _ findWidgetByName(hostname)
#                     icon.b..('<Button-3>', do_controllerPopup )
#
#
#         # Load hosts
#         hosts _ loadedTopology['hosts']
#         ___ host __ hosts:
#             nodeNum _ host['number']
#             hostname _ 'h'+nodeNum
#             __ 'hostname' __ host['opts']:
#                 hostname _ host['opts']['hostname']
#             ____
#                 host['opts']['hostname'] _ hostname
#             __ 'nodeNum' no. __ host['opts']:
#                 host['opts']['nodeNum'] _ int(nodeNum)
#             x _ host['x']
#             y _ host['y']
#             addNode('Host', nodeNum, float(x), float(y), name_hostname)
#
#             # Fix JSON converting tuple to list when saving
#             __ 'privateDirectory' __ host['opts']:
#                 newDirList _ []
#                 ___ privateDir __ host['opts']['privateDirectory']:
#                     __ isinstance( privateDir, list ):
#                         newDirList.ap..((privateDir[0],privateDir[1]))
#                     ____
#                         newDirList.ap..(privateDir)
#                 host['opts']['privateDirectory'] _ newDirList
#             hostOpts[hostname] _ host['opts']
#             icon _ findWidgetByName(hostname)
#             icon.b..('<Button-3>', do_hostPopup )
#
#         # Load switches
#         switches _ loadedTopology['switches']
#         ___ switch __ switches:
#             nodeNum _ switch['number']
#             hostname _ 's'+nodeNum
#             __ 'controllers' no. __ switch['opts']:
#                 switch['opts']['controllers'] _ []
#             __ 'switchType' no. __ switch['opts']:
#                 switch['opts']['switchType'] _ 'default'
#             __ 'hostname' __ switch['opts']:
#                 hostname _ switch['opts']['hostname']
#             ____
#                 switch['opts']['hostname'] _ hostname
#             __ 'nodeNum' no. __ switch['opts']:
#                 switch['opts']['nodeNum'] _ int(nodeNum)
#             x _ switch['x']
#             y _ switch['y']
#             __ switch['opts']['switchType'] __ "legacyRouter":
#                 addNode('LegacyRouter', nodeNum, float(x), float(y), name_hostname)
#                 icon _ findWidgetByName(hostname)
#                 icon.b..('<Button-3>', do_legacyRouterPopup )
#             ____ switch['opts']['switchType'] __ "legacySwitch":
#                 addNode('LegacySwitch', nodeNum, float(x), float(y), name_hostname)
#                 icon _ findWidgetByName(hostname)
#                 icon.b..('<Button-3>', do_legacySwitchPopup )
#             ____
#                 addNode('Switch', nodeNum, float(x), float(y), name_hostname)
#                 icon _ findWidgetByName(hostname)
#                 icon.b..('<Button-3>', do_switchPopup )
#             switchOpts[hostname] _ switch['opts']
#
#             # create links to controllers
#             __ int(loadedTopology['version']) > 1:
#                 controllers _ switchOpts[hostname]['controllers']
#                 ___ controller __ controllers:
#                     d.. _ findWidgetByName(controller)
#                     dx, dy _ canvas.coords( widgetToItem[ d.. ] )
#                     link _ canvas.create_line(float(x),
#                                                         float(y),
#                                                         dx,
#                                                         dy,
#                                                         width_4,
#                                                         fill_'red',
#                                                         dash_(6, 4, 2, 4),
#                                                         tag_'link' )
#                     c.itemconfig(link, tags_c.gettags(link)+('control',))
#                     addLink( icon, d.., linktype_'control' )
#                     createControlLinkBindings()
#                     link _ linkWidget _ N..
#             ____
#                 d.. _ findWidgetByName('c0')
#                 dx, dy _ canvas.coords( widgetToItem[ d.. ] )
#                 link _ canvas.create_line(float(x),
#                                                     float(y),
#                                                     dx,
#                                                     dy,
#                                                     width_4,
#                                                     fill_'red',
#                                                     dash_(6, 4, 2, 4),
#                                                     tag_'link' )
#                 c.itemconfig(link, tags_c.gettags(link)+('control',))
#                 addLink( icon, d.., linktype_'control' )
#                 createControlLinkBindings()
#                 link _ linkWidget _ N..
#
#         # Load links
#         links _ loadedTopology['links']
#         ___ link __ links:
#             srcNode _ link['src']
#             src _ findWidgetByName(srcNode)
#             sx, sy _ canvas.coords( widgetToItem[ src ] )
#
#             d..Node _ link['dest']
#             d.. _ findWidgetByName(d..Node)
#             dx, dy _ canvas.coords( widgetToItem[ d..]  )
#
#             link _ canvas.create_line( sx, sy, dx, dy, width_4,
#                                              fill_'blue', tag_'link' )
#             c.itemconfig(link, tags_c.gettags(link)+('data',))
#             addLink( src, d.., linkopts_link['opts'] )
#             createDataLinkBindings()
#             link _ linkWidget _ N..
#
#         f.c..
#
#     ___ findWidgetByName( self, name ):
#         ___ widget __ widgetToItem:
#             __ name __  widget[ 'text' ]:
#                 r_ widget
#
#     ___ newTopology( self ):
#         "New command."
#         ___ widget __ widgetToItem.keys
#             deleteItem( widgetToItem[ widget ] )
#         hostCount _ 0
#         switchCount _ 0
#         controllerCount _ 0
#         links _ {}
#         hostOpts _ {}
#         switchOpts _ {}
#         controllers _ {}
#         appPrefs["ipBase"]_ d..IpBase
#
#     ___ saveTopology( self ):
#         "Save command."
#         myFormats _ [
#             ('Mininet Topology','*.mn'),
#             ('All Files','*'),
#         ]
#
#         savingDictionary _ {}
#         fileName _ tkFileDialog.asksaveasfilename(filetypes_myFormats ,title_"Save the topology as...")
#         __ le.(fileName ) > 0:
#             # Save Application preferences
#             savingDictionary['version'] _ '2'
#
#             # Save Switches and Hosts
#             hostsToSave _ []
#             switchesToSave _ []
#             controllersToSave _ []
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 x1, y1 _ canvas.coords( widgetToItem[ widget ] )
#                 __ 'Switch' __ tags or 'LegacySwitch' __ tags or 'LegacyRouter' __ tags:
#                     nodeNum _ switchOpts[name]['nodeNum']
#                     nodeToSave _ {'number':st..(nodeNum),
#                                   'x':st..(x1),
#                                   'y':st..(y1),
#                                   'opts':switchOpts[name] }
#                     switchesToSave.ap..(nodeToSave)
#                 ____ 'Host' __ tags:
#                     nodeNum _ hostOpts[name]['nodeNum']
#                     nodeToSave _ {'number':st..(nodeNum),
#                                   'x':st..(x1),
#                                   'y':st..(y1),
#                                   'opts':hostOpts[name] }
#                     hostsToSave.ap..(nodeToSave)
#                 ____ 'Controller' __ tags:
#                     nodeToSave _ {'x':st..(x1),
#                                   'y':st..(y1),
#                                   'opts':controllers[name] }
#                     controllersToSave.ap..(nodeToSave)
#                 ____
#                     r_ E..( "Cannot create mystery node: " + name )
#             savingDictionary['hosts'] _ hostsToSave
#             savingDictionary['switches'] _ switchesToSave
#             savingDictionary['controllers'] _ controllersToSave
#
#             # Save Links
#             linksToSave _ []
#             ___ link __ links.values
#                 src _ link['src']
#                 dst _ link['dest']
#                 linkopts _ link['linkOpts']
#
#                 srcName, dstName _ src[ 'text' ], dst[ 'text' ]
#                 linkToSave _ {'src':srcName,
#                               'dest':dstName,
#                               'opts':linkopts}
#                 __ link['type'] __ 'data':
#                     linksToSave.ap..(linkToSave)
#             savingDictionary['links'] _ linksToSave
#
#             # Save Application preferences
#             savingDictionary['application'] _ appPrefs
#
#             ___
#                 f _ o..(fileName, 'wb')
#                 f.w..(?.d..(savingDictionary, sort_keys_True, indent_4, separators_(',', ': ')))
#             # pylint: disable=broad-except
#             ______ E.. __ er:
#                 warn( er, '\n' )
#             # pylint: enable=broad-except
#             f..
#                 f.c..
#
#     ___ exportScript( self ):
#         "Export command."
#         myFormats _ [
#             ('Mininet Custom Topology','*.py'),
#             ('All Files','*'),
#         ]
#
#         fileName _ tkFileDialog.asksaveasfilename(filetypes_myFormats ,title_"Export the topology as...")
#         __ le.(fileName ) > 0:
#             # debug( "Now saving under @\n"  fileName )
#             f _ o..(fileName, 'wb')
#
#             f.w..("#!/usr/bin/python\n")
#             f.w..("\n")
#             f.w..("from mininet.net import Mininet\n")
#             f.w..("from mininet.node import Controller, RemoteController, OVSController\n")
#             f.w..("from mininet.node import CPULimitedHost, Host, Node\n")
#             f.w..("from mininet.node import OVSKernelSwitch, UserSwitch\n")
#             __ StrictVersion(MININET_VERSION) > StrictVersion('2.0'):
#                 f.w..("from mininet.node import IVSSwitch\n")
#             f.w..("from mininet.cli import CLI\n")
#             f.w..("from mininet.log import setLogLevel, info\n")
#             f.w..("from mininet.link import TCLink, Intf\n")
#             f.w..("from subprocess import call\n")
#
#             inBandCtrl _ F..
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#
#                 __ 'Controller' __ tags:
#                     opts _ controllers[name]
#                     controllerType _ opts['controllerType']
#                     __ controllerType __ 'inband':
#                         inBandCtrl _ T..
#
#             __ inBandCtrl __ T..:
#                 f.w..("\n")
#                 f.w..("class InbandController( RemoteController ):\n")
#                 f.w..("\n")
#                 f.w..("    def checkListening( self ):\n")
#                 f.w..("        \"Overridden to do nothing.\"\n")
#                 f.w..("        return\n")
#
#             f.w..("\n")
#             f.w..("def myNetwork():\n")
#             f.w..("\n")
#             f.w..("    net = Mininet( topo=None,\n")
#             __ le.(appPrefs['dpctl']) > 0:
#                 f.w..("                   listenPort="+appPrefs['dpctl']+",\n")
#             f.w..("                   build=False,\n")
#             f.w..("                   ipBase='"+appPrefs['ipBase']+"')\n")
#             f.w..("\n")
#             f.w..("    info( '*** Adding controller\\n' )\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#
#                 __ 'Controller' __ tags:
#                     opts _ controllers[name]
#                     controllerType _ opts['controllerType']
#                     __ 'controllerProtocol' __ opts:
#                         controllerProtocol _ opts['controllerProtocol']
#                     ____
#                         controllerProtocol _ 'tcp'
#                     controllerIP _ opts['remoteIP']
#                     controllerPort _ opts['remotePort']
#
#
#                     f.w..("    "+name+"=net.addController(name='"+name+"',\n")
#
#                     __ controllerType __ 'remote':
#                         f.w..("                      controller=RemoteController,\n")
#                         f.w..("                      ip='"+controllerIP+"',\n")
#                     ____ controllerType __ 'inband':
#                         f.w..("                      controller=InbandController,\n")
#                         f.w..("                      ip='"+controllerIP+"',\n")
#                     ____ controllerType __ 'ovsc':
#                         f.w..("                      controller=OVSController,\n")
#                     ____
#                         f.w..("                      controller=Controller,\n")
#
#                     f.w..("                      protocol='"+controllerProtocol+"',\n")
#                     f.w..("                      port="+st..(controllerPort)+")\n")
#                     f.w..("\n")
#
#             # Save Switches and Hosts
#             f.w..("    info( '*** Add switches\\n')\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'LegacyRouter' __ tags:
#                     f.w..("    "+name+" = net.addHost('"+name+"', cls=Node, ip='0.0.0.0')\n")
#                     f.w..("    "+name+".cmd('sysctl -w net.ipv4.ip_forward=1')\n")
#                 __ 'LegacySwitch' __ tags:
#                     f.w..("    "+name+" = net.addSwitch('"+name+"', cls=OVSKernelSwitch, failMode='standalone')\n")
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     nodeNum _ opts['nodeNum']
#                     f.w..("    "+name+" = net.addSwitch('"+name+"'")
#                     __ opts['switchType'] __ 'default':
#                         __ appPrefs['switchType'] __ 'ivs':
#                             f.w..(", cls=IVSSwitch")
#                         ____ appPrefs['switchType'] __ 'user':
#                             f.w..(", cls=UserSwitch")
#                         ____ appPrefs['switchType'] __ 'userns':
#                             f.w..(", cls=UserSwitch, inNamespace=True")
#                         ____
#                             f.w..(", cls=OVSKernelSwitch")
#                     ____ opts['switchType'] __ 'ivs':
#                         f.w..(", cls=IVSSwitch")
#                     ____ opts['switchType'] __ 'user':
#                         f.w..(", cls=UserSwitch")
#                     ____ opts['switchType'] __ 'userns':
#                         f.w..(", cls=UserSwitch, inNamespace=True")
#                     ____
#                         f.w..(", cls=OVSKernelSwitch")
#                     __ 'dpctl' __ opts:
#                         f.w..(", listenPort="+opts['dpctl'])
#                     __ 'dpid' __ opts:
#                         f.w..(", dpid='"+opts['dpid']+"'")
#                     f.w..(")\n")
#                     __ 'externalInterfaces' __ opts:
#                         ___ extInterface __ opts['externalInterfaces']:
#                             f.w..("    Intf( '"+extInterface+"', node="+name+" )\n")
#
#             f.w..("\n")
#             f.w..("    info( '*** Add hosts\\n')\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Host' __ tags:
#                     opts _ hostOpts[name]
#                     ip _ N..
#                     d..Route _ N..
#                     __ 'defaultRoute' __ opts and le.(opts['defaultRoute']) > 0:
#                         d..Route _ "'via "+opts['defaultRoute']+"'"
#                     ____
#                         d..Route _ 'None'
#                     __ 'ip' __ opts and le.(opts['ip']) > 0:
#                         ip _ opts['ip']
#                     ____
#                         nodeNum _ hostOpts[name]['nodeNum']
#                         ipBaseNum, prefixLen _ netParse( appPrefs['ipBase'] )
#                         ip _ ipAdd(i_nodeNum, prefixLen_prefixLen, ipBaseNum_ipBaseNum)
#
#                     __ 'cores' __ opts or 'cpu' __ opts:
#                         f.w..("    "+name+" = net.addHost('"+name+"', cls=CPULimitedHost, ip='"+ip+"', defaultRoute="+d..Route+")\n")
#                         __ 'cores' __ opts:
#                             f.w..("    "+name+".setCPUs(cores='"+opts['cores']+"')\n")
#                         __ 'cpu' __ opts:
#                             f.w..("    "+name+".setCPUFrac(f="+st..(opts['cpu'])+", sched='"+opts['sched']+"')\n")
#                     ____
#                         f.w..("    "+name+" = net.addHost('"+name+"', cls=Host, ip='"+ip+"', defaultRoute="+d..Route+")\n")
#                     __ 'externalInterfaces' __ opts:
#                         ___ extInterface __ opts['externalInterfaces']:
#                             f.w..("    Intf( '"+extInterface+"', node="+name+" )\n")
#             f.w..("\n")
#
#             # Save Links
#             f.w..("    info( '*** Add links\\n')\n")
#             ___ key,linkDetail __ links.iteritems
#                 tags _ canvas.gettags(key)
#                 __ 'data' __ tags:
#                     optsExist _ F..
#                     src _ linkDetail['src']
#                     dst _ linkDetail['dest']
#                     linkopts _ linkDetail['linkOpts']
#                     srcName, dstName _ src[ 'text' ], dst[ 'text' ]
#                     bw _ ''
#                     # delay = ''
#                     # loss = ''
#                     # max_queue_size = ''
#                     linkOpts _ "{"
#                     __ 'bw' __ linkopts:
#                         bw _  linkopts['bw']
#                         linkOpts _ linkOpts + "'bw':"+st..(bw)
#                         optsExist _ T..
#                     __ 'delay' __ linkopts:
#                         # delay =  linkopts['delay']
#                         __ optsExist:
#                             linkOpts _ linkOpts + ","
#                         linkOpts _ linkOpts + "'delay':'"+linkopts['delay']+"'"
#                         optsExist _ T..
#                     __ 'loss' __ linkopts:
#                         __ optsExist:
#                             linkOpts _ linkOpts + ","
#                         linkOpts _ linkOpts + "'loss':"+st..(linkopts['loss'])
#                         optsExist _ T..
#                     __ 'max_queue_size' __ linkopts:
#                         __ optsExist:
#                             linkOpts _ linkOpts + ","
#                         linkOpts _ linkOpts + "'max_queue_size':"+st..(linkopts['max_queue_size'])
#                         optsExist _ T..
#                     __ 'jitter' __ linkopts:
#                         __ optsExist:
#                             linkOpts _ linkOpts + ","
#                         linkOpts _ linkOpts + "'jitter':'"+linkopts['jitter']+"'"
#                         optsExist _ T..
#                     __ 'speedup' __ linkopts:
#                         __ optsExist:
#                             linkOpts _ linkOpts + ","
#                         linkOpts _ linkOpts + "'speedup':"+st..(linkopts['speedup'])
#                         optsExist _ T..
#
#                     linkOpts _ linkOpts + "}"
#                     __ optsExist:
#                         f.w..("    "+srcName+dstName+" = "+linkOpts+"\n")
#                     f.w..("    net.addLink("+srcName+", "+dstName)
#                     __ optsExist:
#                         f.w..(", cls=TCLink , **"+srcName+dstName)
#                     f.w..(")\n")
#
#             f.w..("\n")
#             f.w..("    info( '*** Starting network\\n')\n")
#             f.w..("    net.build()\n")
#
#             f.w..("    info( '*** Starting controllers\\n')\n")
#             f.w..("    for controller in net.controllers:\n")
#             f.w..("        controller.start()\n")
#             f.w..("\n")
#
#             f.w..("    info( '*** Starting switches\\n')\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Switch' __ tags or 'LegacySwitch' __ tags:
#                     opts _ switchOpts[name]
#                     ctrlList _ ",".j..(opts['controllers'])
#                     f.w..("    net.get('"+name+"').start(["+ctrlList+"])\n")
#
#             f.w..("\n")
#
#             f.w..("    info( '*** Post configure switches and hosts\\n')\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     __ opts['switchType'] __ 'default':
#                         __ appPrefs['switchType'] __ 'user':
#                             __ 'switchIP' __ opts:
#                                 __ le.(opts['switchIP']) > 0:
#                                     f.w..("    "+name+".cmd('ifconfig "+name+" "+opts['switchIP']+"')\n")
#                         ____ appPrefs['switchType'] __ 'userns':
#                             __ 'switchIP' __ opts:
#                                 __ le.(opts['switchIP']) > 0:
#                                     f.w..("    "+name+".cmd('ifconfig lo "+opts['switchIP']+"')\n")
#                         ____ appPrefs['switchType'] __ 'ovs':
#                             __ 'switchIP' __ opts:
#                                 __ le.(opts['switchIP']) > 0:
#                                     f.w..("    "+name+".cmd('ifconfig "+name+" "+opts['switchIP']+"')\n")
#                     ____ opts['switchType'] __ 'user':
#                         __ 'switchIP' __ opts:
#                             __ le.(opts['switchIP']) > 0:
#                                 f.w..("    "+name+".cmd('ifconfig "+name+" "+opts['switchIP']+"')\n")
#                     ____ opts['switchType'] __ 'userns':
#                         __ 'switchIP' __ opts:
#                             __ le.(opts['switchIP']) > 0:
#                                 f.w..("    "+name+".cmd('ifconfig lo "+opts['switchIP']+"')\n")
#                     ____ opts['switchType'] __ 'ovs':
#                         __ 'switchIP' __ opts:
#                             __ le.(opts['switchIP']) > 0:
#                                 f.w..("    "+name+".cmd('ifconfig "+name+" "+opts['switchIP']+"')\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Host' __ tags:
#                     opts _ hostOpts[name]
#                     # Attach vlan interfaces
#                     __ 'vlanInterfaces' __ opts:
#                         ___ vlanInterface __ opts['vlanInterfaces']:
#                             f.w..("    "+name+".cmd('vconfig add "+name+"-eth0 "+vlanInterface[1]+"')\n")
#                             f.w..("    "+name+".cmd('ifconfig "+name+"-eth0."+vlanInterface[1]+" "+vlanInterface[0]+"')\n")
#                     # Run User Defined Start Command
#                     __ 'startCommand' __ opts:
#                         f.w..("    "+name+".cmdPrint('"+opts['startCommand']+"')\n")
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     # Run User Defined Start Command
#                     __ 'startCommand' __ opts:
#                         f.w..("    "+name+".cmdPrint('"+opts['startCommand']+"')\n")
#
#             # Configure NetFlow
#             nflowValues _ appPrefs['netflow']
#             __ le.(nflowValues['nflowTarget']) > 0:
#                 nflowEnabled _ F..
#                 nflowSwitches _ ''
#                 ___ widget __ widgetToItem:
#                     name _ widget[ 'text' ]
#                     tags _ canvas.gettags( widgetToItem[ widget ] )
#
#                     __ 'Switch' __ tags:
#                         opts _ switchOpts[name]
#                         __ 'netflow' __ opts:
#                             __ opts['netflow'] __ '1':
#                                 nflowSwitches _ nflowSwitches+' -- set Bridge '+name+' netflow=@MiniEditNF'
#                                 nflowEnabled_True
#                 __ nflowEnabled:
#                     nflowCmd _ 'ovs-vsctl -- --id=@MiniEditNF create NetFlow '+ 'target=\\\"'+nflowValues['nflowTarget']+'\\\" '+ 'active-timeout='+nflowValues['nflowTimeout']
#                     __ nflowValues['nflowAddId'] __ '1':
#                         nflowCmd _ nflowCmd + ' add_id_to_interface=true'
#                     ____
#                         nflowCmd _ nflowCmd + ' add_id_to_interface=false'
#                     f.w..("    \n")
#                     f.w..("    call('"+nflowCmd+nflowSwitches+"', shell=True)\n")
#
#             # Configure sFlow
#             sflowValues _ appPrefs['sflow']
#             __ le.(sflowValues['sflowTarget']) > 0:
#                 sflowEnabled _ F..
#                 sflowSwitches _ ''
#                 ___ widget __ widgetToItem:
#                     name _ widget[ 'text' ]
#                     tags _ canvas.gettags( widgetToItem[ widget ] )
#
#                     __ 'Switch' __ tags:
#                         opts _ switchOpts[name]
#                         __ 'sflow' __ opts:
#                             __ opts['sflow'] __ '1':
#                                 sflowSwitches _ sflowSwitches+' -- set Bridge '+name+' sflow=@MiniEditSF'
#                                 sflowEnabled_True
#                 __ sflowEnabled:
#                     sflowCmd _ 'ovs-vsctl -- --id=@MiniEditSF create sFlow '+ 'target=\\\"'+sflowValues['sflowTarget']+'\\\" '+ 'header='+sflowValues['sflowHeader']+' '+ 'sampling='+sflowValues['sflowSampling']+' '+ 'polling='+sflowValues['sflowPolling']
#                     f.w..("    \n")
#                     f.w..("    call('"+sflowCmd+sflowSwitches+"', shell=True)\n")
#
#             f.w..("\n")
#             f.w..("    CLI(net)\n")
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Host' __ tags:
#                     opts _ hostOpts[name]
#                     # Run User Defined Stop Command
#                     __ 'stopCommand' __ opts:
#                         f.w..("    "+name+".cmdPrint('"+opts['stopCommand']+"')\n")
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     # Run User Defined Stop Command
#                     __ 'stopCommand' __ opts:
#                         f.w..("    "+name+".cmdPrint('"+opts['stopCommand']+"')\n")
#
#             f.w..("    net.stop()\n")
#             f.w..("\n")
#             f.w..("if __name__ == '__main__':\n")
#             f.w..("    setLogLevel( 'info' )\n")
#             f.w..("    myNetwork()\n")
#             f.w..("\n")
#
#
#             f.c..
#
#
#     # Generic canvas handler
#     #
#     # We could have used bindtags, as in nodeIcon, but
#     # the dynamic approach used here
#     # may actually require less code. In any case, it's an
#     # interesting introspection-based alternative to bindtags.
#
#     ___ canvasHandle( self, eventName, event ):
#         "Generic canvas event handler"
#         __ active is N..:
#             r_
#         toolName _ active
#         handler _ getattr( self, eventName + toolName, N.. )
#         __ handler is no. N..:
#             handler( event )
#
#     ___ clickCanvas( self, event ):
#         "Canvas click handler."
#         canvasHandle( 'click', event )
#
#     ___ dragCanvas( self, event ):
#         "Canvas drag handler."
#         canvasHandle( 'drag', event )
#
#     ___ releaseCanvas( self, event ):
#         "Canvas mouse up handler."
#         canvasHandle( 'release', event )
#
#     # Currently the only items we can select directly are
#     # links. Nodes are handled by bindings in the node icon.
#
#     ___ findItem( self, x, y ):
#         "Find items at a location in our canvas."
#         items _ canvas.find_overlapping( x, y, x, y )
#         __ le.( items ) __ 0:
#             r_ N..
#         ____
#             r_ items[ 0 ]
#
#     # Canvas bindings for Select, Host, Switch and Link tools
#
#     ___ clickSelect( self, event ):
#         "Select an item."
#         selectItem( findItem( event.x, event.y ) )
#
#     ___ deleteItem( self, item ):
#         "Delete an item."
#         # Don't delete w__ network is running
#         __ buttons[ 'Select' ][ 'state' ] __ 'disabled':
#             r_
#         # Delete from model
#         __ item __ links:
#             deleteLink( item )
#         __ item __ itemToWidget:
#             deleteNode( item )
#         # Delete from view
#         canvas.delete( item )
#
#     ___ deleteSelection( self, _event ):
#         "Delete the selected item."
#         __ selection is no. N..:
#             deleteItem( selection )
#         selectItem( N.. )
#
#     ___ nodeIcon( self, node, name ):
#         "Create a new node icon."
#         icon _ Button( canvas, image_self.images[ node ],
#                        text_name, compound_'top' )
#         # Unfortunately bindtags wants a tuple
#         bindtags _ [ st..( nodeBindings ) ]
#         bindtags +_ list( icon.bindtags() )
#         icon.bindtags( tuple( bindtags ) )
#         r_ icon
#
#     ___ newNode( self, node, event ):
#         "Add a new node to our canvas."
#         c _ canvas
#         x, y _ c.canvasx( event.x ), c.canvasy( event.y )
#         name _ nodePrefixes[ node ]
#         __ 'Switch' __ node:
#             switchCount +_ 1
#             name _ nodePrefixes[ node ] + st..( switchCount )
#             switchOpts[name] _ {}
#             switchOpts[name]['nodeNum']_self.switchCount
#             switchOpts[name]['hostname']_name
#             switchOpts[name]['switchType']_'default'
#             switchOpts[name]['controllers']_[]
#         __ 'LegacyRouter' __ node:
#             switchCount +_ 1
#             name _ nodePrefixes[ node ] + st..( switchCount )
#             switchOpts[name] _ {}
#             switchOpts[name]['nodeNum']_self.switchCount
#             switchOpts[name]['hostname']_name
#             switchOpts[name]['switchType']_'legacyRouter'
#         __ 'LegacySwitch' __ node:
#             switchCount +_ 1
#             name _ nodePrefixes[ node ] + st..( switchCount )
#             switchOpts[name] _ {}
#             switchOpts[name]['nodeNum']_self.switchCount
#             switchOpts[name]['hostname']_name
#             switchOpts[name]['switchType']_'legacySwitch'
#             switchOpts[name]['controllers']_[]
#         __ 'Host' __ node:
#             hostCount +_ 1
#             name _ nodePrefixes[ node ] + st..( hostCount )
#             hostOpts[name] _ {'sched':'host'}
#             hostOpts[name]['nodeNum']_self.hostCount
#             hostOpts[name]['hostname']_name
#         __ 'Controller' __ node:
#             name _ nodePrefixes[ node ] + st..( controllerCount )
#             ctrlr _ { 'controllerType': 'ref',
#                       'hostname': name,
#                       'controllerProtocol': 'tcp',
#                       'remoteIP': '127.0.0.1',
#                       'remotePort': 6633}
#             controllers[name] _ ctrlr
#             # We want to start controller count at 0
#             controllerCount +_ 1
#
#         icon _ nodeIcon( node, name )
#         item _ canvas.create_window( x, y, anchor_'c', window_icon,
#                                           tags_node )
#         widgetToItem[ icon ] _ item
#         itemToWidget[ item ] _ icon
#         selectItem( item )
#         icon.links _ {}
#         __ 'Switch' __ node:
#             icon.b..('<Button-3>', do_switchPopup )
#         __ 'LegacyRouter' __ node:
#             icon.b..('<Button-3>', do_legacyRouterPopup )
#         __ 'LegacySwitch' __ node:
#             icon.b..('<Button-3>', do_legacySwitchPopup )
#         __ 'Host' __ node:
#             icon.b..('<Button-3>', do_hostPopup )
#         __ 'Controller' __ node:
#             icon.b..('<Button-3>', do_controllerPopup )
#
#     ___ clickController( self, event ):
#         "Add a new Controller to our canvas."
#         newNode( 'Controller', event )
#
#     ___ clickHost( self, event ):
#         "Add a new host to our canvas."
#         newNode( 'Host', event )
#
#     ___ clickLegacyRouter( self, event ):
#         "Add a new switch to our canvas."
#         newNode( 'LegacyRouter', event )
#
#     ___ clickLegacySwitch( self, event ):
#         "Add a new switch to our canvas."
#         newNode( 'LegacySwitch', event )
#
#     ___ clickSwitch( self, event ):
#         "Add a new switch to our canvas."
#         newNode( 'Switch', event )
#
#     ___ dragNetLink( self, event ):
#         "Drag a link's endpoint to another node."
#         __ link is N..:
#             r_
#         # Since drag starts in widget, we use root coords
#         x _ canvasx( event.x_root )
#         y _ canvasy( event.y_root )
#         c _ canvas
#         c.coords( link, linkx, linky, x, y )
#
#     ___ releaseNetLink( self, _event ):
#         "Give up on the current link."
#         __ link is no. N..:
#             canvas.delete( link )
#         linkWidget _ linkItem _ link _ N..
#
#     # Generic node handlers
#
#     ___ createNodeBindings( self ):
#         "Create a set of bindings for nodes."
#         bindings _ {
#             '<ButtonPress-1>': clickNode,
#             '<B1-Motion>': dragNode,
#             '<ButtonRelease-1>': releaseNode,
#             '<Enter>': enterNode,
#             '<Leave>': leaveNode
#         }
#         l _ Label()  # lightweight-ish owner for bindings
#         ___ event, binding __ bindings.items
#             l.b..( event, binding )
#         r_ l
#
#     ___ selectItem( self, item ):
#         "Select an item and remember old selection."
#         lastSelection _ selection
#         selection _ item
#
#     ___ enterNode( self, event ):
#         "Select node on entry."
#         selectNode( event )
#
#     ___ leaveNode( self, _event ):
#         "Restore old selection on exit."
#         selectItem( lastSelection )
#
#     ___ clickNode( self, event ):
#         "Node click handler."
#         __ active is 'NetLink':
#             startLink( event )
#         ____
#             selectNode( event )
#         r_ 'break'
#
#     ___ dragNode( self, event ):
#         "Node drag handler."
#         __ active is 'NetLink':
#             dragNetLink( event )
#         ____
#             dragNodeAround( event )
#
#     ___ releaseNode( self, event ):
#         "Node release handler."
#         __ active is 'NetLink':
#             finishLink( event )
#
#     # Specific node handlers
#
#     ___ selectNode( self, event ):
#         "Select the node that was clicked on."
#         item _ widgetToItem.get( event.widget, N.. )
#         selectItem( item )
#
#     ___ dragNodeAround( self, event ):
#         "Drag a node around on the canvas."
#         c _ canvas
#         # Convert global to local coordinates;
#         # Necessary since x, y are widget-relative
#         x _ canvasx( event.x_root )
#         y _ canvasy( event.y_root )
#         w _ event.widget
#         # Adjust node position
#         item _ widgetToItem[ w ]
#         c.coords( item, x, y )
#         # Adjust link positions
#         ___ d.. __ w.links:
#             link _ w.links[ d.. ]
#             item _ widgetToItem[ d.. ]
#             x1, y1 _ c.coords( item )
#             c.coords( link, x, y, x1, y1 )
#         updateScrollRegion()
#
#     ___ createControlLinkBindings( self ):
#         "Create a set of bindings for nodes."
#         # Link bindings
#         # Selection still needs a bit of work overall
#         # Callbacks ignore event
#
#         ___ se__( _event, link_self.link ):
#             "Select item on mouse entry."
#             selectItem( link )
#
#         ___ highlight( _event, link_self.link ):
#             "Highlight item on mouse entry."
#             selectItem( link )
#             canvas.itemconfig( link, fill_'green' )
#
#         ___ unhighlight( _event, link_self.link ):
#             "Unhighlight item on mouse exit."
#             canvas.itemconfig( link, fill_'red' )
#             #self.selectItem( None )
#
#         canvas.tag_bind( link, '<Enter>', highlight )
#         canvas.tag_bind( link, '<Leave>', unhighlight )
#         canvas.tag_bind( link, '<ButtonPress-1>', se__ )
#
#     ___ createDataLinkBindings( self ):
#         "Create a set of bindings for nodes."
#         # Link bindings
#         # Selection still needs a bit of work overall
#         # Callbacks ignore event
#
#         ___ se__( _event, link_self.link ):
#             "Select item on mouse entry."
#             selectItem( link )
#
#         ___ highlight( _event, link_self.link ):
#             "Highlight item on mouse entry."
#             selectItem( link )
#             canvas.itemconfig( link, fill_'green' )
#
#         ___ unhighlight( _event, link_self.link ):
#             "Unhighlight item on mouse exit."
#             canvas.itemconfig( link, fill_'blue' )
#             #self.selectItem( None )
#
#         canvas.tag_bind( link, '<Enter>', highlight )
#         canvas.tag_bind( link, '<Leave>', unhighlight )
#         canvas.tag_bind( link, '<ButtonPress-1>', se__ )
#         canvas.tag_bind( link, '<Button-3>', do_linkPopup )
#
#
#     ___ startLink( self, event ):
#         "Start a new link."
#         __ event.widget no. __ widgetToItem:
#             # Didn't click on a node
#             r_
#
#         w _ event.widget
#         item _ widgetToItem[ w ]
#         x, y _ canvas.coords( item )
#         link _ canvas.create_line( x, y, x, y, width_4,
#                                              fill_'blue', tag_'link' )
#         linkx, linky _ x, y
#         linkWidget _ w
#         linkItem _ item
#
#
#     ___ finishLink( self, event ):
#         "Finish creating a link"
#         __ link is N..:
#             r_
#         source _ linkWidget
#         c _ canvas
#         # Since we dragged from the widget, use root coords
#         x, y _ canvasx( event.x_root ), canvasy( event.y_root )
#         target _ findItem( x, y )
#         d.. _ itemToWidget.get( target, N.. )
#         __ ( source is N.. or d.. is N.. or source __ d..
#                 or d.. __ source.links or source __ d...links ):
#             releaseNetLink( event )
#             r_
#         # For now, don't allow hosts to be directly linked
#         stags _ canvas.gettags( widgetToItem[ source ] )
#         dtags _ canvas.gettags( target )
#         __ (('Host' __ stags and 'Host' __ dtags) or
#            ('Controller' __ dtags and 'LegacyRouter' __ stags) or
#            ('Controller' __ stags and 'LegacyRouter' __ dtags) or
#            ('Controller' __ dtags and 'LegacySwitch' __ stags) or
#            ('Controller' __ stags and 'LegacySwitch' __ dtags) or
#            ('Controller' __ dtags and 'Host' __ stags) or
#            ('Controller' __ stags and 'Host' __ dtags) or
#            ('Controller' __ stags and 'Controller' __ dtags)):
#             releaseNetLink( event )
#             r_
#
#         # Set link type
#         linkType_'data'
#         __ 'Controller' __ stags or 'Controller' __ dtags:
#             linkType_'control'
#             c.itemconfig(link, dash_(6, 4, 2, 4), fill_'red')
#             createControlLinkBindings()
#         ____
#             linkType_'data'
#             createDataLinkBindings()
#         c.itemconfig(link, tags_c.gettags(link)+(linkType,))
#
#         x, y _ c.coords( target )
#         c.coords( link, linkx, linky, x, y )
#         addLink( source, d.., linktype_linkType )
#         __ linkType __ 'control':
#             controllerName _ ''
#             switchName _ ''
#             __ 'Controller' __ stags:
#                 controllerName _ source[ 'text' ]
#                 switchName _ d..[ 'text' ]
#             ____
#                 controllerName _ d..[ 'text' ]
#                 switchName _ source[ 'text' ]
#
#             switchOpts[switchName]['controllers'].ap..(controllerName)
#
#         # We're done
#         link _ linkWidget _ N..
#
#     # Menu handlers
#
#     ___ about( self ):
#         "Display about box."
#         about _ aboutBox
#         __ about is N..:
#             bg _ 'white'
#             about _ Toplevel( bg_'white' )
#             about.title( 'About' )
#             desc _ appName + ': a simple network editor for MiniNet'
#             version _ 'MiniEdit '+MINIEDIT_VERSION
#             author _ 'Originally by: Bob Lantz <rlantz@cs>, April 2010'
#             enhancements _ 'Enhancements by: Gregory Gee, Since July 2013'
#             www _ 'http://gregorygee.wordpress.com/category/miniedit/'
#             line1 _ Label( about, text_desc, font_'Helvetica 10 bold', bg_bg )
#             line2 _ Label( about, text_version, font_'Helvetica 9', bg_bg )
#             line3 _ Label( about, text_author, font_'Helvetica 9', bg_bg )
#             line4 _ Label( about, text_enhancements, font_'Helvetica 9', bg_bg )
#             line5 _ Entry( about, font_'Helvetica 9', bg_bg, width_len(www), justify_CENTER )
#             line5.insert(0, www)
#             line5.configure(state_'readonly')
#             line1.pack( padx_20, pady_10 )
#             line2.pack(pady_10 )
#             line3.pack(pady_10 )
#             line4.pack(pady_10 )
#             line5.pack(pady_10 )
#             hide _ ( lambda about_about: about.withdraw() )
#             aboutBox _ about
#             # Hide on close rather than destroying window
#             Wm.wm_protocol( about, name_'WM_DELETE_WINDOW', func_hide )
#         # Show (existing) window
#         about.deiconify()
#
#     ___ createToolImages( self ):
#         "Create toolbar (and icon) images."
#
#     @staticmethod
#     ___ checkIntf( intf ):
#         "Make sure intf exists and is not configured."
#         __ ( ' @:'  intf ) no. __ quietRun( 'ip link show' ):
#             showerror(title_"Error",
#                       message_'External interface ' +intf + ' does not exist! Skipping.')
#             r_ F..
#         ips _ re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun( 'ifconfig ' + intf ) )
#         __ ips:
#             showerror(title_"Error",
#                       message_ intf + ' has an IP address and is probably in use! Skipping.' )
#             r_ F..
#         r_ T..
#
#     ___ hostDetails( self, _ignore_None ):
#         __ ( selection is N.. or
#              net is no. N.. or
#              selection no. __ itemToWidget ):
#             r_
#         widget _ itemToWidget[ selection ]
#         name _ widget[ 'text' ]
#         tags _ canvas.gettags( selection )
#         __ 'Host' no. __ tags:
#             r_
#
#         prefDefaults _ hostOpts[name]
#         hostBox _ HostDialog title_'Host Details', prefDefaults_prefDefaults)
#         master.wait_window(hostBox.top)
#         __ hostBox.result:
#             newHostOpts _ {'nodeNum':hostOpts[name]['nodeNum']}
#             newHostOpts['sched'] _ hostBox.result['sched']
#             __ le.(hostBox.result['startCommand']) > 0:
#                 newHostOpts['startCommand'] _ hostBox.result['startCommand']
#             __ le.(hostBox.result['stopCommand']) > 0:
#                 newHostOpts['stopCommand'] _ hostBox.result['stopCommand']
#             __ le.(hostBox.result['cpu']) > 0:
#                 newHostOpts['cpu'] _ float(hostBox.result['cpu'])
#             __ le.(hostBox.result['cores']) > 0:
#                 newHostOpts['cores'] _ hostBox.result['cores']
#             __ le.(hostBox.result['hostname']) > 0:
#                 newHostOpts['hostname'] _ hostBox.result['hostname']
#                 name _ hostBox.result['hostname']
#                 widget[ 'text' ] _ name
#             __ le.(hostBox.result['defaultRoute']) > 0:
#                 newHostOpts['defaultRoute'] _ hostBox.result['defaultRoute']
#             __ le.(hostBox.result['ip']) > 0:
#                 newHostOpts['ip'] _ hostBox.result['ip']
#             __ le.(hostBox.result['externalInterfaces']) > 0:
#                 newHostOpts['externalInterfaces'] _ hostBox.result['externalInterfaces']
#             __ le.(hostBox.result['vlanInterfaces']) > 0:
#                 newHostOpts['vlanInterfaces'] _ hostBox.result['vlanInterfaces']
#             __ le.(hostBox.result['privateDirectory']) > 0:
#                 newHostOpts['privateDirectory'] _ hostBox.result['privateDirectory']
#             hostOpts[name] _ newHostOpts
#             info( 'New host details for ' + name + ' = ' + st..(newHostOpts), '\n' )
#
#     ___ switchDetails( self, _ignore_None ):
#         __ ( selection is N.. or
#              net is no. N.. or
#              selection no. __ itemToWidget ):
#             r_
#         widget _ itemToWidget[ selection ]
#         name _ widget[ 'text' ]
#         tags _ canvas.gettags( selection )
#         __ 'Switch' no. __ tags:
#             r_
#
#         prefDefaults _ switchOpts[name]
#         switchBox _ SwitchDialog title_'Switch Details', prefDefaults_prefDefaults)
#         master.wait_window(switchBox.top)
#         __ switchBox.result:
#             newSwitchOpts _ {'nodeNum':switchOpts[name]['nodeNum']}
#             newSwitchOpts['switchType'] _ switchBox.result['switchType']
#             newSwitchOpts['controllers'] _ switchOpts[name]['controllers']
#             __ le.(switchBox.result['startCommand']) > 0:
#                 newSwitchOpts['startCommand'] _ switchBox.result['startCommand']
#             __ le.(switchBox.result['stopCommand']) > 0:
#                 newSwitchOpts['stopCommand'] _ switchBox.result['stopCommand']
#             __ le.(switchBox.result['dpctl']) > 0:
#                 newSwitchOpts['dpctl'] _ switchBox.result['dpctl']
#             __ le.(switchBox.result['dpid']) > 0:
#                 newSwitchOpts['dpid'] _ switchBox.result['dpid']
#             __ le.(switchBox.result['hostname']) > 0:
#                 newSwitchOpts['hostname'] _ switchBox.result['hostname']
#                 name _ switchBox.result['hostname']
#                 widget[ 'text' ] _ name
#             __ le.(switchBox.result['externalInterfaces']) > 0:
#                 newSwitchOpts['externalInterfaces'] _ switchBox.result['externalInterfaces']
#             newSwitchOpts['switchIP'] _ switchBox.result['switchIP']
#             newSwitchOpts['sflow'] _ switchBox.result['sflow']
#             newSwitchOpts['netflow'] _ switchBox.result['netflow']
#             switchOpts[name] _ newSwitchOpts
#             info( 'New switch details for ' + name + ' = ' + st..(newSwitchOpts), '\n' )
#
#     ___ linkUp( self ):
#         __ ( selection is N.. or
#              net is N..):
#             r_
#         link _ selection
#         linkDetail _  links[link]
#         src _ linkDetail['src']
#         dst _ linkDetail['dest']
#         srcName, dstName _ src[ 'text' ], dst[ 'text' ]
#         net.configLinkStatus(srcName, dstName, 'up')
#         canvas.itemconfig(link, dash_())
#
#     ___ linkDown( self ):
#         __ ( selection is N.. or
#              net is N..):
#             r_
#         link _ selection
#         linkDetail _  links[link]
#         src _ linkDetail['src']
#         dst _ linkDetail['dest']
#         srcName, dstName _ src[ 'text' ], dst[ 'text' ]
#         net.configLinkStatus(srcName, dstName, 'down')
#         canvas.itemconfig(link, dash_(4, 4))
#
#     ___ linkDetails( self, _ignore_None ):
#         __ ( selection is N.. or
#              net is no. N..):
#             r_
#         link _ selection
#
#         linkDetail _  links[link]
#         # src = linkDetail['src']
#         # dest = linkDetail['dest']
#         linkopts _ linkDetail['linkOpts']
#         linkBox _ LinkDialog title_'Link Details', linkDefaults_linkopts)
#         __ linkBox.result is no. N..:
#             linkDetail['linkOpts'] _ linkBox.result
#             info( 'New link details = ' + st..(linkBox.result), '\n' )
#
#     ___ prefDetails( self ):
#         prefDefaults _ appPrefs
#         prefBox _ PrefsDialog title_'Preferences', prefDefaults_prefDefaults)
#         info( 'New Prefs = ' + st..(prefBox.result), '\n' )
#         __ prefBox.result:
#             appPrefs _ prefBox.result
#
#
#     ___ controllerDetails( self ):
#         __ ( selection is N.. or
#              net is no. N.. or
#              selection no. __ itemToWidget ):
#             r_
#         widget _ itemToWidget[ selection ]
#         name _ widget[ 'text' ]
#         tags _ canvas.gettags( selection )
#         oldName _ name
#         __ 'Controller' no. __ tags:
#             r_
#
#         ctrlrBox _ ControllerDialog title_'Controller Details', ctrlrDefaults_self.controllers[name])
#         __ ctrlrBox.result:
#             # debug( 'Controller is ' + ctrlrBox.result[0], '\n' )
#             __ le.(ctrlrBox.result['hostname']) > 0:
#                 name _ ctrlrBox.result['hostname']
#                 widget[ 'text' ] _ name
#             ____
#                 ctrlrBox.result['hostname'] _ name
#             controllers[name] _ ctrlrBox.result
#             info( 'New controller details for ' + name + ' = ' + st..(controllers[name]), '\n' )
#             # Find references to controller and change name
#             __ oldName !_ name:
#                 ___ widget __ widgetToItem:
#                     switchName _ widget[ 'text' ]
#                     tags _ canvas.gettags( widgetToItem[ widget ] )
#                     __ 'Switch' __ tags:
#                         switch _ switchOpts[switchName]
#                         __ oldName __ switch['controllers']:
#                             switch['controllers'].r..(oldName)
#                             switch['controllers'].ap..(name)
#
#
#     ___ listBridge( self, _ignore_None ):
#         __ ( selection is N.. or
#              net is N.. or
#              selection no. __ itemToWidget ):
#             r_
#         name _ itemToWidget[ selection ][ 'text' ]
#         tags _ canvas.gettags( selection )
#
#         __ name no. __ net.nameToNode:
#             r_
#         __ 'Switch' __ tags or 'LegacySwitch' __ tags:
#             call(["xterm -T 'Bridge Details' -sb -sl 2000 -e 'ovs-vsctl list bridge " + name + "; read -p \"Press Enter to close\"' &"], shell_True)
#
#     @staticmethod
#     ___ ovsShow( _ignore_None ):
#         call(["xterm -T 'OVS Summary' -sb -sl 2000 -e 'ovs-vsctl show; read -p \"Press Enter to close\"' &"], shell_True)
#
#     @staticmethod
#     ___ rootTerminal( _ignore_None ):
#         call(["xterm -T 'Root Terminal' -sb -sl 2000 &"], shell_True)
#
#     # Model interface
#     #
#     # Ultimately we will either want to use a topo or
#     # mininet object here, probably.
#
#     ___ addLink( self, source, d.., linktype_'data', linkopts_None ):
#         "Add link to model."
#         __ linkopts is N..:
#             linkopts _ {}
#         source.links[ d.. ] _ link
#         d...links[ source ] _ link
#         links[ link ] _ {'type' :linktype,
#                                    'src':source,
#                                    'dest':d..,
#                                    'linkOpts':linkopts}
#
#     ___ deleteLink( self, link ):
#         "Delete link from model."
#         pair _ links.get( link, N.. )
#         __ pair is no. N..:
#             source_pair['src']
#             d.._pair['dest']
#             del source.links[ d.. ]
#             del d...links[ source ]
#             stags _ canvas.gettags( widgetToItem[ source ] )
#             # dtags = self.canvas.gettags( self.widgetToItem[ dest ] )
#             ltags _ canvas.gettags( link )
#
#             __ 'control' __ ltags:
#                 controllerName _ ''
#                 switchName _ ''
#                 __ 'Controller' __ stags:
#                     controllerName _ source[ 'text' ]
#                     switchName _ d..[ 'text' ]
#                 ____
#                     controllerName _ d..[ 'text' ]
#                     switchName _ source[ 'text' ]
#
#                 __ controllerName __ switchOpts[switchName]['controllers']:
#                     switchOpts[switchName]['controllers'].r..(controllerName)
#
#
#         __ link is no. N..:
#             del links[ link ]
#
#     ___ deleteNode( self, item ):
#         "Delete node (and its links) from model."
#
#         widget _ itemToWidget[ item ]
#         tags _ canvas.gettags(item)
#         __ 'Controller' __ tags:
#             # remove from switch controller lists
#             ___ serachwidget __ widgetToItem:
#                 name _ serachwidget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ serachwidget ] )
#                 __ 'Switch' __ tags:
#                     __ widget['text'] __ switchOpts[name]['controllers']:
#                         switchOpts[name]['controllers'].r..(widget['text'])
#
#         ___ link __ widget.links.values
#             # Delete from view and model
#             deleteItem( link )
#         del itemToWidget[ item ]
#         del widgetToItem[ widget ]
#
#     ___ buildNodes( self, net):
#         # Make nodes
#         info( "Getting Hosts and Switches.\n" )
#         ___ widget __ widgetToItem:
#             name _ widget[ 'text' ]
#             tags _ canvas.gettags( widgetToItem[ widget ] )
#             # debug( name+' has '+st..(tags), '\n' )
#
#             __ 'Switch' __ tags:
#                 opts _ switchOpts[name]
#                 # debug( st..(opts), '\n' )
#
#                 # Create the correct switch class
#                 switchClass _ customOvs
#                 switchParms_{}
#                 __ 'dpctl' __ opts:
#                     switchParms['listenPort']_int(opts['dpctl'])
#                 __ 'dpid' __ opts:
#                     switchParms['dpid']_opts['dpid']
#                 __ opts['switchType'] __ 'default':
#                     __ appPrefs['switchType'] __ 'ivs':
#                         switchClass _ IVSSwitch
#                     ____ appPrefs['switchType'] __ 'user':
#                         switchClass _ CustomUserSwitch
#                     ____ appPrefs['switchType'] __ 'userns':
#                         switchParms['inNamespace'] _ T..
#                         switchClass _ CustomUserSwitch
#                     ____
#                         switchClass _ customOvs
#                 ____ opts['switchType'] __ 'user':
#                     switchClass _ CustomUserSwitch
#                 ____ opts['switchType'] __ 'userns':
#                     switchClass _ CustomUserSwitch
#                     switchParms['inNamespace'] _ T..
#                 ____ opts['switchType'] __ 'ivs':
#                     switchClass _ IVSSwitch
#                 ____
#                     switchClass _ customOvs
#
#                 __ switchClass __ customOvs:
#                     # Set OpenFlow versions
#                     openFlowVersions _ []
#                     __ appPrefs['openFlowVersions']['ovsOf10'] __ '1':
#                         openFlowVersions.ap..('OpenFlow10')
#                     __ appPrefs['openFlowVersions']['ovsOf11'] __ '1':
#                         openFlowVersions.ap..('OpenFlow11')
#                     __ appPrefs['openFlowVersions']['ovsOf12'] __ '1':
#                         openFlowVersions.ap..('OpenFlow12')
#                     __ appPrefs['openFlowVersions']['ovsOf13'] __ '1':
#                         openFlowVersions.ap..('OpenFlow13')
#                     protoList _ ",".j..(openFlowVersions)
#                     switchParms['protocols'] _ protoList
#                 newSwitch _ net.addSwitch( name , cls_switchClass, **switchParms)
#
#                 # Some post startup config
#                 __ switchClass __ CustomUserSwitch:
#                     __ 'switchIP' __ opts:
#                         __ le.(opts['switchIP']) > 0:
#                             newSwitch.setSwitchIP(opts['switchIP'])
#                 __ switchClass __ customOvs:
#                     __ 'switchIP' __ opts:
#                         __ le.(opts['switchIP']) > 0:
#                             newSwitch.setSwitchIP(opts['switchIP'])
#
#                 # Attach external interfaces
#                 __ 'externalInterfaces' __ opts:
#                     ___ extInterface __ opts['externalInterfaces']:
#                         __ checkIntf(extInterface):
#                             Intf( extInterface, node_newSwitch )
#
#             ____ 'LegacySwitch' __ tags:
#                 newSwitch _ net.addSwitch( name , cls_LegacySwitch)
#             ____ 'LegacyRouter' __ tags:
#                 newSwitch _ net.addHost( name , cls_LegacyRouter)
#             ____ 'Host' __ tags:
#                 opts _ hostOpts[name]
#                 # debug( st..(opts), '\n' )
#                 ip _ N..
#                 d..Route _ N..
#                 __ 'defaultRoute' __ opts and le.(opts['defaultRoute']) > 0:
#                     d..Route _ 'via '+opts['defaultRoute']
#                 __ 'ip' __ opts and le.(opts['ip']) > 0:
#                     ip _ opts['ip']
#                 ____
#                     nodeNum _ hostOpts[name]['nodeNum']
#                     ipBaseNum, prefixLen _ netParse( appPrefs['ipBase'] )
#                     ip _ ipAdd(i_nodeNum, prefixLen_prefixLen, ipBaseNum_ipBaseNum)
#
#                 # Create the correct host class
#                 __ 'cores' __ opts or 'cpu' __ opts:
#                     __ 'privateDirectory' __ opts:
#                         hostCls _ partial( CPULimitedHost,
#                                            privateDirs_opts['privateDirectory'] )
#                     ____
#                         hostCls_CPULimitedHost
#                 ____
#                     __ 'privateDirectory' __ opts:
#                         hostCls _ partial( Host,
#                                            privateDirs_opts['privateDirectory'] )
#                     ____
#                         hostCls_Host
#                 debug( hostCls, '\n' )
#                 newHost _ net.addHost( name,
#                                        cls_hostCls,
#                                        ip_ip,
#                                        d..Route_d..Route
#                                       )
#
#                 # Set the CPULimitedHost specific options
#                 __ 'cores' __ opts:
#                     newHost.setCPUs(cores _ opts['cores'])
#                 __ 'cpu' __ opts:
#                     newHost.setCPUFrac(f_opts['cpu'], sched_opts['sched'])
#
#                 # Attach external interfaces
#                 __ 'externalInterfaces' __ opts:
#                     ___ extInterface __ opts['externalInterfaces']:
#                         __ checkIntf(extInterface):
#                             Intf( extInterface, node_newHost )
#                 __ 'vlanInterfaces' __ opts:
#                     __ le.(opts['vlanInterfaces']) > 0:
#                         info( 'Checking that OS is VLAN prepared\n' )
#                         pathCheck('vconfig', moduleName_'vlan package')
#                         moduleDeps( add_'8021q' )
#             ____ 'Controller' __ tags:
#                 opts _ controllers[name]
#
#                 # Get controller info from panel
#                 controllerType _ opts['controllerType']
#                 __ 'controllerProtocol' __ opts:
#                     controllerProtocol _ opts['controllerProtocol']
#                 ____
#                     controllerProtocol _ 'tcp'
#                     opts['controllerProtocol'] _ 'tcp'
#                 controllerIP _ opts['remoteIP']
#                 controllerPort _ opts['remotePort']
#
#                 # Make controller
#                 info( 'Getting controller selection:'+controllerType, '\n' )
#                 __ controllerType __ 'remote':
#                     net.addController(name_name,
#                                       controller_RemoteController,
#                                       ip_controllerIP,
#                                       protocol_controllerProtocol,
#                                       port_controllerPort)
#                 ____ controllerType __ 'inband':
#                     net.addController(name_name,
#                                       controller_InbandController,
#                                       ip_controllerIP,
#                                       protocol_controllerProtocol,
#                                       port_controllerPort)
#                 ____ controllerType __ 'ovsc':
#                     net.addController(name_name,
#                                       controller_OVSController,
#                                       protocol_controllerProtocol,
#                                       port_controllerPort)
#                 ____
#                     net.addController(name_name,
#                                       controller_Controller,
#                                       protocol_controllerProtocol,
#                                       port_controllerPort)
#
#             ____
#                 r_ E..( "Cannot create mystery node: " + name )
#
#     @staticmethod
#     ___ pathCheck( $, **kwargs ):
#         "Make sure each program in *args can be found in $PATH."
#         moduleName _ kwargs.get( 'moduleName', 'it' )
#         ___ arg __ args:
#             __ no. quietRun( 'which ' + arg ):
#                 showerror(title_"Error",
#                       message_ 'Cannot find required executable @.\n'  arg +
#                        'Please make sure that @ is installed '  moduleName +
#                        'and available in your $PATH.' )
#
#     ___ buildLinks( self, net):
#         # Make links
#         info( "Getting Links.\n" )
#         ___ key,link __ links.iteritems
#             tags _ canvas.gettags(key)
#             __ 'data' __ tags:
#                 src_link['src']
#                 dst_link['dest']
#                 linkopts_link['linkOpts']
#                 srcName, dstName _ src[ 'text' ], dst[ 'text' ]
#                 srcNode, dstNode _ net.nameToNode[ srcName ], net.nameToNode[ dstName ]
#                 __ linkopts:
#                     net.addLink(srcNode, dstNode, cls_TCLink, **linkopts)
#                 ____
#                     # debug( st..(srcNode) )
#                     # debug( st..(dstNode), '\n' )
#                     net.addLink(srcNode, dstNode)
#                 canvas.itemconfig(key, dash_())
#
#
#     ___ build( self ):
#         "Build network based on our topology."
#
#         dpctl _ N..
#         __ le.(appPrefs['dpctl']) > 0:
#             dpctl _ int(appPrefs['dpctl'])
#         net _ Mininet( topo_None,
#                        listenPort_dpctl,
#                        build_False,
#                        ipBase_self.appPrefs['ipBase'] )
#
#         buildNodes(net)
#         buildLinks(net)
#
#         # Build network (we have to do this separately at the moment )
#         net.build()
#
#         r_ net
#
#
#     ___ postStartSetup( self ):
#
#         # Setup host details
#         ___ widget __ widgetToItem:
#             name _ widget[ 'text' ]
#             tags _ canvas.gettags( widgetToItem[ widget ] )
#             __ 'Host' __ tags:
#                 newHost _ net.get(name)
#                 opts _ hostOpts[name]
#                 # Attach vlan interfaces
#                 __ 'vlanInterfaces' __ opts:
#                     ___ vlanInterface __ opts['vlanInterfaces']:
#                         info( 'adding vlan interface '+vlanInterface[1], '\n' )
#                         newHost.cmdPrint('ifconfig '+name+'-eth0.'+vlanInterface[1]+' '+vlanInterface[0])
#                 # Run User Defined Start Command
#                 __ 'startCommand' __ opts:
#                     newHost.cmdPrint(opts['startCommand'])
#             __ 'Switch' __ tags:
#                 newNode _ net.get(name)
#                 opts _ switchOpts[name]
#                 # Run User Defined Start Command
#                 __ 'startCommand' __ opts:
#                     newNode.cmdPrint(opts['startCommand'])
#
#
#         # Configure NetFlow
#         nflowValues _ appPrefs['netflow']
#         __ le.(nflowValues['nflowTarget']) > 0:
#             nflowEnabled _ F..
#             nflowSwitches _ ''
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     __ 'netflow' __ opts:
#                         __ opts['netflow'] __ '1':
#                             info( name+' has Netflow enabled\n' )
#                             nflowSwitches _ nflowSwitches+' -- set Bridge '+name+' netflow=@MiniEditNF'
#                             nflowEnabled_True
#             __ nflowEnabled:
#                 nflowCmd _ 'ovs-vsctl -- --id=@MiniEditNF create NetFlow '+ 'target=\\\"'+nflowValues['nflowTarget']+'\\\" '+ 'active-timeout='+nflowValues['nflowTimeout']
#                 __ nflowValues['nflowAddId'] __ '1':
#                     nflowCmd _ nflowCmd + ' add_id_to_interface=true'
#                 ____
#                     nflowCmd _ nflowCmd + ' add_id_to_interface=false'
#                 info( 'cmd = '+nflowCmd+nflowSwitches, '\n' )
#                 call(nflowCmd+nflowSwitches, shell_True)
#
#             ____
#                 info( 'No switches with Netflow\n' )
#         ____
#             info( 'No NetFlow targets specified.\n' )
#
#         # Configure sFlow
#         sflowValues _ appPrefs['sflow']
#         __ le.(sflowValues['sflowTarget']) > 0:
#             sflowEnabled _ F..
#             sflowSwitches _ ''
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     __ 'sflow' __ opts:
#                         __ opts['sflow'] __ '1':
#                             info( name+' has sflow enabled\n' )
#                             sflowSwitches _ sflowSwitches+' -- set Bridge '+name+' sflow=@MiniEditSF'
#                             sflowEnabled_True
#             __ sflowEnabled:
#                 sflowCmd _ 'ovs-vsctl -- --id=@MiniEditSF create sFlow '+ 'target=\\\"'+sflowValues['sflowTarget']+'\\\" '+ 'header='+sflowValues['sflowHeader']+' '+ 'sampling='+sflowValues['sflowSampling']+' '+ 'polling='+sflowValues['sflowPolling']
#                 info( 'cmd = '+sflowCmd+sflowSwitches, '\n' )
#                 call(sflowCmd+sflowSwitches, shell_True)
#
#             ____
#                 info( 'No switches with sflow\n' )
#         ____
#             info( 'No sFlow targets specified.\n' )
#
#         ## NOTE: MAKE SURE THIS IS LAST THING CALLED
#         # Start the CLI if enabled
#         __ appPrefs['startCLI'] __ '1':
#             info( "\n\n NOTE: PLEASE REMEMBER TO EXIT THE CLI BEFORE YOU PRESS THE STOP BUTTON. Not exiting will prevent MiniEdit from quitting and will prevent you from starting the network again during this sessoin.\n\n")
#             CLI(net)
#
#     ___ start( self ):
#         "Start network."
#         __ net is N..:
#             net _ build()
#
#             # Since I am going to inject per switch controllers.
#             # I can't call net.start().  I have to replicate what it
#             # does and add the controller options.
#             #self.net.start()
#             info( '**** Starting @ controllers\n'  le.( net.controllers ) )
#             ___ controller __ net.controllers:
#                 info( st..(controller) + ' ')
#                 controller.s..
#             info('\n')
#             info( '**** Starting @ switches\n'  le.( net.switches ) )
#             #for switch in self.net.switches:
#             #    info( switch.name + ' ')
#             #    switch.start( self.net.controllers )
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Switch' __ tags:
#                     opts _ switchOpts[name]
#                     switchControllers _ []
#                     ___ ctrl __ opts['controllers']:
#                         switchControllers.ap..(net.get(ctrl))
#                     info( name + ' ')
#                     # Figure out what controllers will manage this switch
#                     net.get(name).start( switchControllers )
#                 __ 'LegacySwitch' __ tags:
#                     net.get(name).start( [] )
#                     info( name + ' ')
#             info('\n')
#
#             postStartSetup()
#
#     ___ stop( self ):
#         "Stop network."
#         __ net is no. N..:
#             # Stop host details
#             ___ widget __ widgetToItem:
#                 name _ widget[ 'text' ]
#                 tags _ canvas.gettags( widgetToItem[ widget ] )
#                 __ 'Host' __ tags:
#                     newHost _ net.get(name)
#                     opts _ hostOpts[name]
#                     # Run User Defined Stop Command
#                     __ 'stopCommand' __ opts:
#                         newHost.cmdPrint(opts['stopCommand'])
#                 __ 'Switch' __ tags:
#                     newNode _ net.get(name)
#                     opts _ switchOpts[name]
#                     # Run User Defined Stop Command
#                     __ 'stopCommand' __ opts:
#                         newNode.cmdPrint(opts['stopCommand'])
#
#             net.stop()
#         cleanUpScreens()
#         net _ N..
#
#     ___ do_linkPopup event):
#         # display the popup menu
#         __ net is N..:
#             ___
#                 linkPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 linkPopup.grab_release()
#         ____
#             ___
#                 linkRunPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 linkRunPopup.grab_release()
#
#     ___ do_controllerPopup event):
#         # display the popup menu
#         __ net is N..:
#             ___
#                 controllerPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 controllerPopup.grab_release()
#
#     ___ do_legacyRouterPopup event):
#         # display the popup menu
#         __ net is no. N..:
#             ___
#                 legacyRouterRunPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 legacyRouterRunPopup.grab_release()
#
#     ___ do_hostPopup event):
#         # display the popup menu
#         __ net is N..:
#             ___
#                 hostPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 hostPopup.grab_release()
#         ____
#             ___
#                 hostRunPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 hostRunPopup.grab_release()
#
#     ___ do_legacySwitchPopup event):
#         # display the popup menu
#         __ net is no. N..:
#             ___
#                 switchRunPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 switchRunPopup.grab_release()
#
#     ___ do_switchPopup event):
#         # display the popup menu
#         __ net is N..:
#             ___
#                 switchPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 switchPopup.grab_release()
#         ____
#             ___
#                 switchRunPopup.tk_popup(event.x_root, event.y_root, 0)
#             f..
#                 # make sure to release the grab (Tk 8.0a1 only)
#                 switchRunPopup.grab_release()
#
#     ___ xterm( self, _ignore_None ):
#         "Make an xterm when a button is pressed."
#         __ ( selection is N.. or
#              net is N.. or
#              selection no. __ itemToWidget ):
#             r_
#         name _ itemToWidget[ selection ][ 'text' ]
#         __ name no. __ net.nameToNode:
#             r_
#         term _ makeTerm( net.nameToNode[ name ], 'Host', term_self.appPrefs['terminalType'] )
#         __ StrictVersion(MININET_VERSION) > StrictVersion('2.0'):
#             net.terms +_ term
#         ____
#             net.terms.ap..(term)
#
#     ___ iperf( self, _ignore_None ):
#         "Make an xterm when a button is pressed."
#         __ ( selection is N.. or
#              net is N.. or
#              selection no. __ itemToWidget ):
#             r_
#         name _ itemToWidget[ selection ][ 'text' ]
#         __ name no. __ net.nameToNode:
#             r_
#         net.nameToNode[ name ].cmd( 'iperf -s -p 5001 &' )
#
#     ### BELOW HERE IS THE TOPOLOGY IMPORT CODE ###
#
#     ___ parseArgs( self ):
#         """Parse command-line args and return options object.
#            returns: opts parse options dict"""
#
#         __ '--custom' __ ___.argv:
#             index _ ___.argv.index( '--custom' )
#             __ le.( ___.argv ) > index + 1:
#                 filename _ ___.argv[ index + 1 ]
#                 parseCustomFile( filename )
#             ____
#                 r_ E..( 'Custom file name not found' )
#
#         desc _ ( "The prog utility creates Mininet network from the\n"
#                  "command line. It can create parametrized topologies,\n"
#                  "invoke the Mininet CLI, and run tests." )
#
#         usage _ ( 'prog [options]\n'
#                   '(type prog -h for details)' )
#
#         opts _ OptionParser( d.._desc, usage_usage )
#
#         addDictOption( opts, TOPOS, TOPODEF, 'topo' )
#         addDictOption( opts, LINKS, LINKDEF, 'link' )
#
#         opts.add_option( '--custom', type_'string', d.._None,
#                          help_'read custom topo and node params from .py' +
#                          'file' )
#
#         options, args _ opts.p_a..
#         # We don't accept extra arguments after the options
#         __ args:
#             opts.print_help()
#             e..()
#
#     ___ setCustom( self, name, value ):
#         "Set custom parameters for MininetRunner."
#         __ name __ ( 'topos', 'switches', 'hosts', 'controllers' ):
#             # Update dictionaries
#             param _ name.upper()
#             globals()[ param ].update( value )
#         ____ name __ 'validate':
#             # Add custom validate function
#             validate _ value
#         ____
#             # Add or modify global variable or class
#             globals()[ name ] _ value
#
#     ___ parseCustomFile( self, fileName ):
#         "Parse custom file and add params before parsing cmd-line options."
#         customs _ {}
#         __ __.pa__.isfile( fileName ):
#             execfile( fileName, customs, customs )
#             ___ name, val __ customs.iteritems
#                 setCustom( name, val )
#         ____
#             r_ E..( 'could not find custom file: @'  fileName )
#
#     ___ importTopo( self ):
#         info( 'topo='+options.topo, '\n' )
#         __ options.topo __ 'none':
#             r_
#         newTopology()
#         topo _ buildTopo( TOPOS, options.topo )
#         link _ customClass( LINKS, options.link )
#         importNet _ Mininet(topo_topo, build_False, link_link)
#         importNet.build()
#
#         c _ canvas
#         rowIncrement _ 100
#         currentY _ 100
#
#         # Add Controllers
#         info( 'controllers:'+st..(le.(importNet.controllers)), '\n' )
#         ___ controller __ importNet.controllers:
#             name _ controller.name
#             x _ controllerCount*100+100
#             addNode('Controller', controllerCount,
#                  float(x), float(currentY), name_name)
#             icon _ findWidgetByName(name)
#             icon.b..('<Button-3>', do_controllerPopup )
#             ctrlr _ { 'controllerType': 'ref',
#                       'hostname': name,
#                       'controllerProtocol': controller.protocol,
#                       'remoteIP': controller.ip,
#                       'remotePort': controller.port}
#             controllers[name] _ ctrlr
#
#
#
#         currentY _ currentY + rowIncrement
#
#         # Add switches
#         info( 'switches:'+st..(le.(importNet.switches)), '\n' )
#         columnCount _ 0
#         ___ switch __ importNet.switches:
#             name _ switch.name
#             switchOpts[name] _ {}
#             switchOpts[name]['nodeNum']_self.switchCount
#             switchOpts[name]['hostname']_name
#             switchOpts[name]['switchType']_'default'
#             switchOpts[name]['controllers']_[]
#
#             x _ columnCount*100+100
#             addNode('Switch', switchCount,
#                  float(x), float(currentY), name_name)
#             icon _ findWidgetByName(name)
#             icon.b..('<Button-3>', do_switchPopup )
#             # Now link to controllers
#             ___ controller __ importNet.controllers:
#                 switchOpts[name]['controllers'].ap..(controller.name)
#                 d.. _ findWidgetByName(controller.name)
#                 dx, dy _ c.coords( widgetToItem[ d.. ] )
#                 link _ c.create_line(float(x),
#                                           float(currentY),
#                                           dx,
#                                           dy,
#                                           width_4,
#                                           fill_'red',
#                                           dash_(6, 4, 2, 4),
#                                           tag_'link' )
#                 c.itemconfig(link, tags_c.gettags(link)+('control',))
#                 addLink( icon, d.., linktype_'control' )
#                 createControlLinkBindings()
#                 link _ linkWidget _ N..
#             __ columnCount __ 9:
#                 columnCount _ 0
#                 currentY _ currentY + rowIncrement
#             ____
#                 columnCount _columnCount+1
#
#
#         currentY _ currentY + rowIncrement
#         # Add hosts
#         info( 'hosts:'+st..(le.(importNet.hosts)), '\n' )
#         columnCount _ 0
#         ___ host __ importNet.hosts:
#             name _ host.name
#             hostOpts[name] _ {'sched':'host'}
#             hostOpts[name]['nodeNum']_self.hostCount
#             hostOpts[name]['hostname']_name
#             hostOpts[name]['ip']_host.IP()
#
#             x _ columnCount*100+100
#             addNode('Host', hostCount,
#                  float(x), float(currentY), name_name)
#             icon _ findWidgetByName(name)
#             icon.b..('<Button-3>', do_hostPopup )
#             __ columnCount __ 9:
#                 columnCount _ 0
#                 currentY _ currentY + rowIncrement
#             ____
#                 columnCount _columnCount+1
#
#         info( 'links:'+st..(le.(topo.links())), '\n' )
#         #[('h1', 's3'), ('h2', 's4'), ('s3', 's4')]
#         ___ link __ topo.links
#             info( st..(link), '\n' )
#             srcNode _ link[0]
#             src _ findWidgetByName(srcNode)
#             sx, sy _ canvas.coords( widgetToItem[ src ] )
#
#             d..Node _ link[1]
#             d.. _ findWidgetByName(d..Node)
#             dx, dy _ canvas.coords( widgetToItem[ d..]  )
#
#             params _ topo.linkInfo( srcNode, d..Node )
#             info( 'Link Parameters='+st..(params), '\n' )
#
#             link _ canvas.create_line( sx, sy, dx, dy, width_4,
#                                              fill_'blue', tag_'link' )
#             c.itemconfig(link, tags_c.gettags(link)+('data',))
#             addLink( src, d.., linkopts_params )
#             createDataLinkBindings()
#             link _ linkWidget _ N..
#
#         importNet.stop()
#
# ___ miniEditImages
#     "Create and return images for MiniEdit."
#
#     # Image data. Git will be unhappy. However, the alternative
#     # is to keep track of separate binary files, which is also
#     # unappealing.
#
#     r_ {
#         'Select': BitmapImage(
#             file_'/usr/include/X11/bitmaps/left_ptr' ),
#
#         'Switch': PhotoImage( data_r"""
# R0lGODlhLgAgAPcAAB2ZxGq61imex4zH3RWWwmK41tzd3vn9/jCiyfX7/Q6SwFay0gBlmtnZ2snJ
# yr+2tAuMu6rY6D6kyfHx8XO/2Uqszjmly6DU5uXz+JLN4uz3+kSrzlKx0ZeZm2K21BuYw67a6QB9
# r+Xl5rW2uHW61On1+UGpzbrf6xiXwny9166vsMLCwgBdlAmHt8TFxgBwpNTs9C2hyO7t7ZnR5L/B
# w0yv0NXV1gBimKGjpABtoQBuoqKkpiaUvqWmqHbB2/j4+Pf39729vgB/sN7w9obH3hSMugCAsonJ
# 4M/q8wBglgB6rCCaxLO0tX7C2wBqniGMuABzpuPl5f3+/v39/fr6+r7i7vP6/ABonV621LLc6zWk
# yrq6uq6wskGlyUaszp6gohmYw8HDxKaoqn3E3LGztWGuzcnLzKmrrOnp6gB1qCaex1q001ewz+Dg
# 4QB3qrCxstHS09LR0dHR0s7Oz8zNzsfIyQaJuQB0pozL4YzI3re4uAGFtYDG3hOUwb+/wQB5rOvr
# 6wB2qdju9TWfxgBpniOcxeLj48vn8dvc3VKuzwB2qp6fos/Q0aXV6D+jxwB7rsXHyLu8vb27vCSc
# xSGZwxyZxH3A2RuUv0+uzz+ozCedxgCDtABnnABroKutr/7+/n2/2LTd6wBvo9bX2OLo6lGv0C6d
# xS6avjmmzLTR2uzr6m651RuXw4jF3CqfxySaxSadyAuRv9bd4cPExRiMuDKjyUWevNPS0sXl8BeY
# xKytr8G/wABypXvC23vD3O73+3vE3cvU2PH5+7S1t7q7vCGVwO/v8JfM3zymyyyZwrWys+Hy90Ki
# xK6qqg+TwBKXxMvMzaWtsK7U4jemzLXEygBxpW++2aCho97Z18bP0/T09fX29vb19ViuzdDR0crf
# 51qz01y00ujo6Onq6hCDs2Gpw3i71CqWv3S71nO92M/h52m207bJ0AN6rPPz9Nrh5Nvo7K/b6oTI
# 37Td7ABqneHi4yScxo/M4RiWwRqVwcro8n3B2lGoylStzszMzAAAACH5BAEAAP8ALAAAAAAuACAA
# Bwj/AP8JHEjw3wEkEY74WOjrQhUNBSNKnCjRSoYKCOwJcKWpEAACBFBRGEKxZMkDjRAg2OBlQyYL
# WhDEcOWxDwofv0zqHIhhDYIFC2p4MYFMS62ZaiYVWlJJAYIqO00KMlEjABYOQokaRbp0CYBKffpE
# iDpxSKYC1gqswToUmYVaCFyp6QrgwwcCscaSJZhgQYBeAdRyqFBhgwWkGyct8WoXRZ8Ph/YOxMOB
# CIUAHsBxwGQBAII1YwpMI5Brcd0PKFA4Q2ZFMgYteZqkwxyu1KQNJzQc+CdFCrxypyqdRoEPX6x7
# ki/n2TfbAxtNRHYTVCWpWTRbuRoX7yMgZ9QSFQa0/7LU/BXygjIWXVOBTR2sxp7BxGpENgKbY+PR
# reqyIOKnOh0M445AjTjDCgrPSBNFKt9w8wMVU5g0Bg8kDAAKOutQAkNEQNBwDRAEeVEcAV6w84Ay
# KowQSRhmzNGAASIAYow2IP6DySPk8ANKCv1wINE2cpjxCUEgOIOPAKicQMMbKnhyhhg97HDNF4vs
# IEYkNkzwjwSP/PHIE2VIgIdEnxjAiBwNGIKGDKS8I0sw2VAzApNOQimGLlyMAIkDw2yhZTF/KKGE
# lxCEMtEPBtDhACQurLDCLkFIsoUeZLyRpx8OmEGHN3AEcU0HkFAhUDFulDroJvOU5M44iDjgDTQO
# 1P/hzRw2IFJPGw3AAY0LI/SAwxc7jEKQI2mkEUipRoxp0g821AMIGlG0McockMzihx5c1LkDDmSg
# UVAiafACRbGPVKDTFG3MYUYdLoThRxDE6DEMGUww8eQONGwTER9piFINFOPasaFJVIjTwC1xzOGP
# A3HUKoIMDTwJR4QRgdBOJzq8UM0Lj5QihU5ZdGMOCSSYUwYzAwwkDhNtUKTBOZ10koMOoohihDwm
# HZKPEDwb4fMe9An0g5Yl+SDKFTHnkMMLLQAjXUTxUCLEIyH0bIQAwuxVQhEMcEIIIUmHUEsWGCQg
# xQEaIFGAHV0+QnUIIWwyg2T/3MPLDQwwcAUhTjiswYsQl1SAxQKmbBJCIMe6ISjVmXwsWQKJEJJE
# 3l1/TY8O4wZyh8ZQ3IF4qX9cggTdAmEwCAMs3IB311fsDfbMGv97BxSBQBAP6QMN0QUhLCSRhOp5
# e923zDpk/EIaRdyO+0C/eHBHEiz0vjrrfMfciSKD4LJ8RBEk88IN0ff+O/CEVEPLGK1tH1ECM7Dx
# RDWdcMLJFTpUQ44jfCyjvlShZNDE/0QAgT6ypr6AAAA7
#             """),
#
#         'LegacySwitch': PhotoImage( data_r"""
# R0lGODlhMgAYAPcAAAEBAXmDjbe4uAE5cjF7xwFWq2Sa0S9biSlrrdTW1k2Ly02a5xUvSQFHjmep
# 6bfI2Q5SlQIYLwFfvj6M3Jaan8fHyDuFzwFp0Vah60uU3AEiRhFgrgFRogFr10N9uTFrpytHYQFM
# mGWt9wIwX+bm5kaT4gtFgR1cnJPF9yt80CF0yAIMGHmp2c/P0AEoUb/P4Fei7qK4zgpLjgFkyQlf
# t1mf5jKD1WWJrQ86ZwFAgBhYmVOa4MPV52uv8y+A0iR3ywFbtUyX5ECI0Q1UmwIcOUGQ3RBXoQI0
# aRJbpr3BxVeJvQUJDafH5wIlS2aq7xBmv52lr7fH12el5Wml3097ph1ru7vM3HCz91Ke6lid40KQ
# 4GSQvgQGClFnfwVJjszMzVCX3hljrdPT1AFLlBRnutPf6yd5zjeI2QE9eRBdrBNVl+3v70mV4ydf
# lwMVKwErVlul8AFChTGB1QE3bsTFxQImTVmAp0FjiUSM1k+b6QQvWQ1SlxMgLgFixEqU3xJhsgFT
# pn2Xs5OluZ+1yz1Xb6HN+Td9wy1zuYClykV5r0x2oeDh4qmvt8LDwxhuxRlLfyRioo2124mft9bi
# 71mDr7fT79nl8Z2hpQs9b7vN4QMQIOPj5XOPrU2Jx32z6xtvwzeBywFFikFnjwcPFa29yxJjuFmP
# xQFv3qGxwRc/Z8vb6wsRGBNqwqmpqTdvqQIbNQFPngMzZAEfP0mQ13mHlQFYsAFnznOXu2mPtQxj
# vQ1Vn4Ot1+/x8my0/CJgnxNNh8DT5CdJaWyx+AELFWmt8QxPkxBZpwMFB015pgFduGCNuyx7zdnZ
# 2WKm6h1xyOPp8aW70QtPkUmM0LrCyr/FyztljwFPm0OJzwFny7/L1xFjswE/e12i50iR2VR8o2Gf
# 3xszS2eTvz2BxSlloQdJiwMHDzF3u7bJ3T2I1WCp8+Xt80FokQFJklef6mORw2ap7SJ1y77Q47nN
# 3wFfu1Kb5cXJyxdhrdDR0wlNkTSF11Oa4yp4yQEuW0WQ3QIDBQI7dSH5BAEAAAAALAAAAAAyABgA
# Bwj/AAEIHDjKF6SDvhImPMHwhA6HOiLqUENRDYSLEIplxBcNHz4Z5GTI8BLKS5OBA1Ply2fDhxwf
# PlLITGFmmRkzP+DlVKHCmU9nnz45csSqKKsn9gileZKrVC4aRFACOGZu5UobNuRohRkzhc2b+36o
# qCaqrFmzZEV1ERBg3BOmMl5JZTBhwhm7ZyycYZnvJdeuNl21qkCHTiPDhxspTtKoQgUKCJ6wehMV
# 5QctWupeo6TkjOd8e1lmdQkTGbTTMaDFiDGINeskX6YhEicUiQa5A/kUKaFFwQ0oXzjZ8Tbcm3Hj
# irwpMtTSgg9QMJf5WEZ9375AiED19ImpSQSUB4Kw/8HFSMyiRWJaqG/xhf2X91+oCbmq1e/MFD/2
# EcApVkWVJhp8J9AqsywQxDfAbLJJPAy+kMkL8shjxTkUnhOJZ5+JVp8cKfhwxwdf4fQLgG4MFAwW
# KOZRAxM81EAPPQvoE0QQfrDhx4399OMBMjz2yCMVivCoCAWXKLKMTPvoUYcsKwi0RCcwYCAlFjU0
# A6OBM4pXAhsl8FYELYWFWZhiZCbRQgIC2AGTLy408coxAoEDx5wwtGPALTVg0E4NKC7gp4FsBKoA
# Ki8U+oIVmVih6DnZPMBMAlGwIARWOLiggSYC+ZNIOulwY4AkSZCyxaikbqHMqaeaIp4+rAaxQxBg
# 2P+IozuRzvLZIS4syYVAfMAhwhSC1EPCGoskIIYY9yS7Hny75OFnEIAGyiVvWkjjRxF11fXIG3WU
# KNA6wghDTCW88PKMJZOkm24Z7LarSjPtoIjFn1lKyyVmmBVhwRtvaDDMgFL0Eu4VhaiDwhXCXNFD
# D8QQw7ATEDsBw8RSxotFHs7CKJ60XWrRBj91EOGPQCA48c7J7zTjSTPctOzynjVkkYU+O9S8Axg4
# Z6BzBt30003Ps+AhNB5C4PCGC5gKJMMTZJBRytOl/CH1HxvQkMbVVxujtdZGGKGL17rsEfYQe+xR
# zNnFcGQCv7LsKlAtp8R9Sgd0032BLXjPoPcMffTd3YcEgAMOxOBA1GJ4AYgXAMjiHDTgggveCgRI
# 3RfcnffefgcOeDKEG3444osDwgEspMNiTQhx5FoOShxcrrfff0uQjOycD+554qFzMHrpp4cwBju/
# 5+CmVNbArnntndeCO+O689777+w0IH0o1P/TRJMohRA4EJwn47nyiocOSOmkn/57COxE3wD11Mfh
# fg45zCGyVF4Ufvvyze8ewv5jQK9++6FwXxzglwM0GPAfR8AeSo4gwAHCbxsQNCAa/kHBAVhwAHPI
# 4BE2eIRYeHAEIBwBP0Y4Qn41YWRSCQgAOw==
#             """),
#
#         'LegacyRouter': PhotoImage( data_r"""
# R0lGODlhMgAYAPcAAAEBAXZ8gQNAgL29vQNctjl/xVSa4j1dfCF+3QFq1DmL3wJMmAMzZZW11dnZ
# 2SFrtyNdmTSO6gIZMUKa8gJVqEOHzR9Pf5W74wFjxgFx4jltn+np6Eyi+DuT6qKiohdtwwUPGWiq
# 6ymF4LHH3Rh11CV81kKT5AMoUA9dq1ap/mV0gxdXlytRdR1ptRNPjTt9vwNgvwJZsX+69gsXJQFH
# jTtjizF0tvHx8VOm9z2V736Dhz2N3QM2acPZ70qe8gFo0HS19wVRnTiR6hMpP0eP1i6J5iNlqAtg
# tktjfQFu3TNxryx4xAMTIzOE1XqAh1uf5SWC4AcfNy1XgQJny93n8a2trRh312Gt+VGm/AQIDTmB
# yAF37QJasydzvxM/ayF3zhdLf8zLywFdu4i56gFlyi2J4yV/1w8wUo2/8j+X8D2Q5Eee9jeR7Uia
# 7DpeggFt2QNPm97e3jRong9bpziH2DuT7aipqQoVICmG45vI9R5720eT4Q1hs1er/yVVhwJJktPh
# 70tfdbHP7Xev5xs5V7W1sz9jhz11rUVZcQ9WoCVVhQk7cRdtwWuw9QYOFyFHbSBnr0dznxtWkS18
# zKfP9wwcLAMHCwFFiS5UeqGtuRNNiwMfPS1hlQMtWRE5XzGM5yhxusLCwCljnwMdOFWh7cve8pG/
# 7Tlxp+Tr8g9bpXF3f0lheStrrYu13QEXLS1ppTV3uUuR1RMjNTF3vU2X4TZupwRSolNne4nB+T+L
# 2YGz4zJ/zYe99YGHjRdDcT95sx09XQldsgMLEwMrVc/X3yN3yQ1JhTRbggsdMQNfu9HPz6WlpW2t
# 7RctQ0GFyeHh4dvl8SBZklCb5kOO2kWR3Vmt/zdjkQIQHi90uvPz8wIVKBp42SV5zbfT7wtXpStV
# fwFWrBVvyTt3swFz5kGBv2+1/QlbrVFjdQM7d1+j54i67UmX51qn9i1vsy+D2TuR5zddhQsjOR1t
# u0GV6ghbsDVZf4+76RRisent8Xd9hQFBgwFNmwJLlcPDwwFr1z2T5yH5BAEAAAAALAAAAAAyABgA
# Bwj/AAEIHEiQYJY7Qwg9UsTplRIbENuxEiXJgpcz8e5YKsixY8Essh7JcbbOBwcOa1JOmJAmTY4c
# HeoIabJrCShI0XyB8YRso0eOjoAdWpciBZajJ1GuWcnSZY46Ed5N8hPATqEBoRB9gVJsxRlhPwHI
# 0kDkVywcRpGe9LF0adOnMpt8CxDnxg1o9lphKoEACoIvmlxxvHOKVg0n/Tzku2WoVoU2J1P6WNkS
# rtwADuxCG/MOjwgRUEIjGG3FhaOBzaThiDSCil27G8Isc3LLjZwXsA6YYJmDjhTMmseoKQIFDx7R
# oxHo2abnwygAlUj1mV6tWjlelEpRwfd6gzI7VeJQ/2vZoVaDUqigqftXpH0R46H9Kl++zUo4JnKq
# 9dGvv09RHFhcIUMe0NiFDyql0OJUHWywMc87TXRhhCRGiHAccvNZUR8JxpDTH38p9HEUFhxgMSAv
# jbBjQge8PSXEC6uo0IsHA6gAAShmgCbffNtsQwIJifhRHX/TpUUiSijlUk8AqgQixSwdNBjCa7CF
# oVggmEgCyRf01WcFCYvYUgB104k4YlK5HONEXXfpokYdMrXRAzMhmNINNNzB9p0T57AgyZckpKKP
# GFNgw06ZWKR10jTw6MAmFWj4AJcQQkQQwSefvFeGCemMIQggeaJywSQ/wgHOAmJskQEfWqBlFBEH
# 1P/QaGY3QOpDZXA2+A6m7hl3IRQKGDCIAj6iwE8yGKC6xbJv8IHNHgACQQybN2QiTi5NwdlBpZdi
# isd7vyanByOJ7CMGGRhgwE+qyy47DhnBPLDLEzLIAEQjBtChRmVPNWgpr+Be+Nc9icARww9TkIEu
# DAsQ0O7DzGIQzD2QdDEJHTsIAROc3F7qWQncyHPPHN5QQAAG/vjzw8oKp8sPPxDH3O44/kwBQzLB
# xBCMOTzzHEMMBMBARgJvZJBBEm/4k0ACKydMBgwYoKNNEjJXbTXE42Q9jtFIp8z0Dy1jQMA1AGzi
# z9VoW7310V0znYDTGMQgwUDXLDBO2nhvoTXbbyRk/XXL+pxWkAT8UJ331WsbnbTSK8MggDZhCTOM
# LQkcjvXeSPedAAw0nABWWARZIgEDfyTzxt15Z53BG1PEcEknrvgEelhZMDHKCTwI8EcQFHBBAAFc
# gGPLHwLwcMIo12Qxu0ABAQA7
#             """),
#
#         'Controller': PhotoImage( data_r"""
#             R0lGODlhMAAwAPcAAAEBAWfNAYWFhcfHx+3t6/f390lJUaWlpfPz8/Hx72lpaZGRke/v77m5uc0B
#             AeHh4e/v7WNjY3t7e5eXlyMjI4mJidPT0+3t7f///09PT7Ozs/X19fHx8ZWTk8HBwX9/fwAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAAALAAAAAAwADAA
#             Bwj/AAEIHEiwoMGDCBMqXMiwocOHECNKnEixosWLGAEIeMCxo8ePHwVkBGABg8mTKFOmtDByAIYN
#             MGPCRCCzQIENNzEMGOkBAwIKQIMKpYCgKAIHCDB4GNkAA4OnUJ9++CDhQ1QGFzA0GKkBA4GvYMOK
#             BYtBA1cNaNOqXcuWq8q3b81m7Cqzbk2bMMu6/Tl0qFEEAZLKxdj1KlSqVA3rnet1rOOwiwmznUzZ
#             LdzLJgdfpIv3pmebN2Pm1GyRbocNp1PLNMDaAM3Im1/alQk4gO28pCt2RdCBt+/eRg8IP1AUdmmf
#             f5MrL56bYlcOvaP7Xo6Ag3HdGDho3869u/YE1507t+3AgLz58ujPMwg/sTBUCAzgy49PH0LW5u0x
#             XFiwvz////5dcJ9bjxVIAHsSdUXAAgs2yOCDDn6FYEQaFGDgYxNCpEFfHHKIX4IDhCjiiCSS+CGF
#             FlCmogYpcnVABTDGKGOMAlRQYwUHnKjhAjX2aOOPN8LImgAL6PiQBhLMqCSNAThQgQRGOqRBBD1W
#             aaOVAggnQARRNqRBBxmEKeaYZIrZQZcMKbDiigqM5OabcMYp55x01ilnQAA7
#             """),
#
#         'Host': PhotoImage( data_r"""
#             R0lGODlhIAAYAPcAMf//////zP//mf//Zv//M///AP/M///MzP/M
#             mf/MZv/MM//MAP+Z//+ZzP+Zmf+ZZv+ZM/+ZAP9m//9mzP9mmf9m
#             Zv9mM/9mAP8z//8zzP8zmf8zZv8zM/8zAP8A//8AzP8Amf8AZv8A
#             M/8AAMz//8z/zMz/mcz/Zsz/M8z/AMzM/8zMzMzMmczMZszMM8zM
#             AMyZ/8yZzMyZmcyZZsyZM8yZAMxm/8xmzMxmmcxmZsxmM8xmAMwz
#             /8wzzMwzmcwzZswzM8wzAMwA/8wAzMwAmcwAZswAM8wAAJn//5n/
#             zJn/mZn/Zpn/M5n/AJnM/5nMzJnMmZnMZpnMM5nMAJmZ/5mZzJmZ
#             mZmZZpmZM5mZAJlm/5lmzJlmmZlmZplmM5lmAJkz/5kzzJkzmZkz
#             ZpkzM5kzAJkA/5kAzJkAmZkAZpkAM5kAAGb//2b/zGb/mWb/Zmb/
#             M2b/AGbM/2bMzGbMmWbMZmbMM2bMAGaZ/2aZzGaZmWaZZmaZM2aZ
#             AGZm/2ZmzGZmmWZmZmZmM2ZmAGYz/2YzzGYzmWYzZmYzM2YzAGYA
#             /2YAzGYAmWYAZmYAM2YAADP//zP/zDP/mTP/ZjP/MzP/ADPM/zPM
#             zDPMmTPMZjPMMzPMADOZ/zOZzDOZmTOZZjOZMzOZADNm/zNmzDNm
#             mTNmZjNmMzNmADMz/zMzzDMzmTMzZjMzMzMzADMA/zMAzDMAmTMA
#             ZjMAMzMAAAD//wD/zAD/mQD/ZgD/MwD/AADM/wDMzADMmQDMZgDM
#             MwDMAACZ/wCZzACZmQCZZgCZMwCZAABm/wBmzABmmQBmZgBmMwBm
#             AAAz/wAzzAAzmQAzZgAzMwAzAAAA/wAAzAAAmQAAZgAAM+4AAN0A
#             ALsAAKoAAIgAAHcAAFUAAEQAACIAABEAAADuAADdAAC7AACqAACI
#             AAB3AABVAABEAAAiAAARAAAA7gAA3QAAuwAAqgAAiAAAdwAAVQAA
#             RAAAIgAAEe7u7t3d3bu7u6qqqoiIiHd3d1VVVURERCIiIhEREQAA
#             ACH5BAEAAAAALAAAAAAgABgAAAiNAAH8G0iwoMGDCAcKTMiw4UBw
#             BPXVm0ixosWLFvVBHFjPoUeC9Tb+6/jRY0iQ/8iVbHiS40CVKxG2
#             HEkQZsyCM0mmvGkw50uePUV2tEnOZkyfQA8iTYpTKNOgKJ+C3AhO
#             p9SWVaVOfWj1KdauTL9q5UgVbFKsEjGqXVtP40NwcBnCjXtw7tx/
#             C8cSBBAQADs=
#         """ ),
#
#         'OldSwitch': PhotoImage( data_r"""
#             R0lGODlhIAAYAPcAMf//////zP//mf//Zv//M///AP/M///MzP/M
#             mf/MZv/MM//MAP+Z//+ZzP+Zmf+ZZv+ZM/+ZAP9m//9mzP9mmf9m
#             Zv9mM/9mAP8z//8zzP8zmf8zZv8zM/8zAP8A//8AzP8Amf8AZv8A
#             M/8AAMz//8z/zMz/mcz/Zsz/M8z/AMzM/8zMzMzMmczMZszMM8zM
#             AMyZ/8yZzMyZmcyZZsyZM8yZAMxm/8xmzMxmmcxmZsxmM8xmAMwz
#             /8wzzMwzmcwzZswzM8wzAMwA/8wAzMwAmcwAZswAM8wAAJn//5n/
#             zJn/mZn/Zpn/M5n/AJnM/5nMzJnMmZnMZpnMM5nMAJmZ/5mZzJmZ
#             mZmZZpmZM5mZAJlm/5lmzJlmmZlmZplmM5lmAJkz/5kzzJkzmZkz
#             ZpkzM5kzAJkA/5kAzJkAmZkAZpkAM5kAAGb//2b/zGb/mWb/Zmb/
#             M2b/AGbM/2bMzGbMmWbMZmbMM2bMAGaZ/2aZzGaZmWaZZmaZM2aZ
#             AGZm/2ZmzGZmmWZmZmZmM2ZmAGYz/2YzzGYzmWYzZmYzM2YzAGYA
#             /2YAzGYAmWYAZmYAM2YAADP//zP/zDP/mTP/ZjP/MzP/ADPM/zPM
#             zDPMmTPMZjPMMzPMADOZ/zOZzDOZmTOZZjOZMzOZADNm/zNmzDNm
#             mTNmZjNmMzNmADMz/zMzzDMzmTMzZjMzMzMzADMA/zMAzDMAmTMA
#             ZjMAMzMAAAD//wD/zAD/mQD/ZgD/MwD/AADM/wDMzADMmQDMZgDM
#             MwDMAACZ/wCZzACZmQCZZgCZMwCZAABm/wBmzABmmQBmZgBmMwBm
#             AAAz/wAzzAAzmQAzZgAzMwAzAAAA/wAAzAAAmQAAZgAAM+4AAN0A
#             ALsAAKoAAIgAAHcAAFUAAEQAACIAABEAAADuAADdAAC7AACqAACI
#             AAB3AABVAABEAAAiAAARAAAA7gAA3QAAuwAAqgAAiAAAdwAAVQAA
#             RAAAIgAAEe7u7t3d3bu7u6qqqoiIiHd3d1VVVURERCIiIhEREQAA
#             ACH5BAEAAAAALAAAAAAgABgAAAhwAAEIHEiwoMGDCBMqXMiwocOH
#             ECNKnEixosWB3zJq3Mixo0eNAL7xG0mypMmTKPl9Cznyn8uWL/m5
#             /AeTpsyYI1eKlBnO5r+eLYHy9Ck0J8ubPmPOrMmUpM6UUKMa/Ui1
#             6saLWLNq3cq1q9evYB0GBAA7
#         """ ),
#
#         'NetLink': PhotoImage( data_r"""
#             R0lGODlhFgAWAPcAMf//////zP//mf//Zv//M///AP/M///MzP/M
#             mf/MZv/MM//MAP+Z//+ZzP+Zmf+ZZv+ZM/+ZAP9m//9mzP9mmf9m
#             Zv9mM/9mAP8z//8zzP8zmf8zZv8zM/8zAP8A//8AzP8Amf8AZv8A
#             M/8AAMz//8z/zMz/mcz/Zsz/M8z/AMzM/8zMzMzMmczMZszMM8zM
#             AMyZ/8yZzMyZmcyZZsyZM8yZAMxm/8xmzMxmmcxmZsxmM8xmAMwz
#             /8wzzMwzmcwzZswzM8wzAMwA/8wAzMwAmcwAZswAM8wAAJn//5n/
#             zJn/mZn/Zpn/M5n/AJnM/5nMzJnMmZnMZpnMM5nMAJmZ/5mZzJmZ
#             mZmZZpmZM5mZAJlm/5lmzJlmmZlmZplmM5lmAJkz/5kzzJkzmZkz
#             ZpkzM5kzAJkA/5kAzJkAmZkAZpkAM5kAAGb//2b/zGb/mWb/Zmb/
#             M2b/AGbM/2bMzGbMmWbMZmbMM2bMAGaZ/2aZzGaZmWaZZmaZM2aZ
#             AGZm/2ZmzGZmmWZmZmZmM2ZmAGYz/2YzzGYzmWYzZmYzM2YzAGYA
#             /2YAzGYAmWYAZmYAM2YAADP//zP/zDP/mTP/ZjP/MzP/ADPM/zPM
#             zDPMmTPMZjPMMzPMADOZ/zOZzDOZmTOZZjOZMzOZADNm/zNmzDNm
#             mTNmZjNmMzNmADMz/zMzzDMzmTMzZjMzMzMzADMA/zMAzDMAmTMA
#             ZjMAMzMAAAD//wD/zAD/mQD/ZgD/MwD/AADM/wDMzADMmQDMZgDM
#             MwDMAACZ/wCZzACZmQCZZgCZMwCZAABm/wBmzABmmQBmZgBmMwBm
#             AAAz/wAzzAAzmQAzZgAzMwAzAAAA/wAAzAAAmQAAZgAAM+4AAN0A
#             ALsAAKoAAIgAAHcAAFUAAEQAACIAABEAAADuAADdAAC7AACqAACI
#             AAB3AABVAABEAAAiAAARAAAA7gAA3QAAuwAAqgAAiAAAdwAAVQAA
#             RAAAIgAAEe7u7t3d3bu7u6qqqoiIiHd3d1VVVURERCIiIhEREQAA
#             ACH5BAEAAAAALAAAAAAWABYAAAhIAAEIHEiwoEGBrhIeXEgwoUKG
#             Cx0+hGhQoiuKBy1irChxY0GNHgeCDAlgZEiTHlFuVImRJUWXEGEy
#             lBmxI8mSNknm1Dnx5sCAADs=
#         """ )
#     }
#
# ___ addDictOption( opts, choicesDict, d.., name, helpStr_None ):
#     """Convenience function to add choices dicts to OptionParser.
#        opts: OptionParser instance
#        choicesDict: dictionary of valid choices, must include default
#        default: default choice key
#        name: long option name
#        help: string"""
#     __ d.. no. __ choicesDict:
#         r_ E..( 'Invalid  default @ for choices dict: @'
#                          ( d.., name ) )
#     __ no. helpStr:
#         helpStr _ ( '|'.j..( sorted( choicesDict.keys() ) ) +
#                     '[,param=value...]' )
#     opts.add_option( '--' + name,
#                      type_'string',
#                      d.. _ d..,
#                      help _ helpStr )
#
# __ _______ __ ______
#     setLogLevel( 'info' )
#     app _ MiniEdit()
#     ### import topology if specified ###
#     app.parseArgs()
#     app.importTopo()
#
#     app.mainloop()
#
