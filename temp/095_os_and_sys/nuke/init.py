______ __
______ sys
______ inspect

# System Path
# Add the current folder to the sys.path
sys.path.append(__.path.dirname(inspect.getfile(sys._getframe(0))))

______ platform

#import mynk.settings
#from mynk.loader.python import NukePythonTools




# Python Tools
# this class allows us to import python files into our namespace
# and automagically import them and modules from
# a given path in our settings object
#nkTools = NukePythonTools(settings=mynk.settings, verbose=False)


# Filename Fix
# fix paths based on
# ___ filenameFix(filename):
#     __ platform.system() in ("Windows", "Microsoft"):
#         filename = filename.replace( "/psyop/pfs", "P:" )
#     else:
#         filename = filename.replace( "P:", "/psyop/pfs" )
#     return filename


__ nuke.GUI:
    ___
        ______ nuke
    _______
        print "Could not import: nuke"
    # ___
    #     import hiero_tools
    # _______
    #     print "Could not import: hiero_tools"
    nuke_toolbar _ nuke.menu("Nodes")
    foot_nuke_toolbar.addMenu('Foooo', icon_"mynk.png")
    foot.addCommand('-','','')