#
# Python code by Timur Khodzhaev
#
# - www.chimuru.com
# - chimuru@gmail.com
#
# List of functions:

# topInput() - returns knob value of the first node of the certain class found upstream of the node pipe
# topInputKnob() - returns knob of the first node of the certain class found upstream of the node pipe
# topInputNode(node,ch_class,input=0) - returns node from upstream

# ensureMatrix() - make sure returned vbalue is always a Matrix
# ensureFloat() - make sure returned value is always Float
# getKnobViews(knob) - return list of views for the knob
# animCurveMinMax(curve) - returns min/max values on animated curve (minValue frame number , minValue, maxValue frame number, maxValue)
# getTrackNames(node) - Returns a list of tracks in a Tracker4 node

# emptyInput(node,start_input=0) - returns first empty input
# nonEmptyInput(node,start_input=0) - returns first non empty input
# shiftConnections(node,start=0) - shifts connection pipes


# Finds node of certain class in the input pipe upstream and if there is a knob
# specified returns its value
_____ ?
_____ re
_____ __

___ topInput(node,input,ch_class,knob,ch_frame):
    __ node:
        input_node_node.input(input)
        __ input_node:
            __ input_node.C..  __ ch_class :
                __ input_node.knob(knob):
                    r_ input_node[knob].getValueAt(ch_frame)
            ____
                __ input_node.C.. __'JoinViews':
#                    print nuke.views()
#                    print nuke.thisView()
                    current_view_?.views().index(?.thisView())
                    r_ topInput(input_node,current_view,ch_class,knob,ch_frame)
                ____
                    r_ topInput(input_node,0,ch_class,knob,ch_frame)
        ____
            r_ N..

# Finds node of certain class in the input pipe upstream and if there is a knob
# specified returns its object

___ topInputKnob(node,ch_class,knob,input_0):
    __ node:
        input_node_node.input(input)
        __ input_node:
            __ nodeClass(input_node) __ ch_class :
                __ input_node.knob(knob):
                    r_ input_node[knob]
            ____
                __ nodeClass(input_node)__'JoinViews':
#                    print nuke.views()
#                    print nuke.thisView()
                    current_view_?.views().index(?.thisView())
                    r_ topInputKnob(input_node,current_view,ch_class,knob)
                ____
                    r_ topInputKnob(input_node,ch_class,knob)
        ____
            r_ N..

# Finds node of certain class in the input pipe upstream and 
# returns node onject

___ topInputNode(node,ch_class,input_0):
    __ node:
        input_node_node.input(input)
        __ input_node:
            __ nodeClass(input_node) __ ch_class :
                r_ input_node
            ____
                __ nodeClass(input_node)__'JoinViews':
#                    print nuke.views()
#                    print nuke.thisView()
                    current_view_?.views().index(?.thisView())
                    r_ topInputNode(input_node,current_view,ch_class)
                ____
                    r_ topInputNode(input_node,ch_class)
        ____
            r_ N..

##########################################################
#
# Volume Holdout matrix knob work abound
# in matrix node direct expression is used to refer to the certain element in the array
# of the transfrom matrix. When there is no object returned there is an exception raised 
# because None object is unsubscriptable
# this function is workaroud to make sure returned value is always a list or 0

___ ensureMatrix(v.. ):
    __ (type(v.. ) __ list):
        r_ v..
    ____
        r_ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
___ ensureFloat(v.. ):
    __ (type(v.. ) __ fl..):
        r_ v..
    ____
        r_ 0

#########################################################
#
# Returns a list of view for knob
# parse toScript of the knob to get named views
#

___ getKnobViews(knob):
    __ knob:
        s_knob.toScript()
        pt_re.compile('\w+\s\{')
        ss_re.findall(pt,s)
        result _[]
        ___ i __ ss:
#            ss=i.lstrip(' ').split(' ')[0]
            __ i:
                __ no.(i __ result):
                    result.ap..(i[0:-2])
        r_ result


#########################################################
#
# Returns a node Class even for Group nodes
# by default Nuke returns Group for all Group nodes
# this script reads aditional knob nodeClass and returns its value 
#

___ nodeClass(node):
    __ node:
        __ ( 'nodeClass' __ node.knobs().k..  ) :
            r_ node['nodeClass'].v.. ()
        ____
            r_ node.C..



#########################################################
#
# Returns a 4 values for a animated curve with min and max values
# (minValue frame number , minValue, maxValue frame number, maxValue)
# 
#

___ animCurveMinMax(curve):
    ___
        minX,minY_1000000000000,1000000000000
        maxX,maxY_-100000000000,-1000000000000
        ___ i __ curve.keys
            __ i.y<minY:
                minX,minY_i.x,i.y
            __ i.y>maxY:
                maxX,maxY_i.x,i.y
        r_ minX,minY,maxX,maxY

    except Exception,e:
        print('Error:: %s' % e)

#########################################################
#
# Returns a list of tracks in a Tracker4 node
# its actually parse toScript so it could break on Nuke version up
# 
#
___ getTrackNames(node):
    k_node['tracks']
    s_node['tracks'].toScript().s..(' \n} \n{ \n ')
    s.pop(0)
    ss_str(s)[2:].s..('\\n')
    ss.pop(-1)
    ss.pop(-1)
    outList_[]
    ___ i __ ss:
        outList.ap..(i.s..('"')[1])
    r_ outList


#########################################################
#
# Functions to work with help buttons in nodes
# returns url for specified node
#
# Uses nodeClass function from this module
#

___ getHelpUrl(node_N..):

    # url will be used in case of unknown class or node is not provided

    mySite_'www.chimuru.com'

    # Check if there is override for default value
    __ __.getenv('TK_HELP_URL'):
        mySite___.getenv('TK_HELP_URL')

    __ node:
        # Reading os environment variable to find file with help urls
        __ __.getenv('TK_HELP_FILE'):
            helpFile___.getenv('TK_HELP_FILE')

            # opening help Settings file to read settings
            settings_[]
            __ __.pa__.isfile( helpFile ):
                prefFile _ open(helpFile,"r")
                prefContent _ prefFile.r..
                prefFile.close()

                ___ i __ prefContent:
                    key,v.. _ i.rstrip().s..('::')
                    settings.ap..((key,v.. ))
         
            ndClass_nodeClass(node)

            # Look through list of values from settings to see if there a url for that node
            url_mySite
            ___ key,v..  __ settings:
                __ ndClass__key:
                    url_v..

        # if help settings file is not defined return my site            
        ____
            url_mySite

    # if no node provided return my site
    ____
        url_mySite

    r_ url

#########################################################
#
# Functions to work with input pipes
#
# returns first empty input pipe starting from start_input pipe
#
___ emptyInput(node,start_input_0):
    inputs_node.inputs()
    ___ input __ ra..(start_input,inputs):
        __ node.input(input)__N..:
            r_ input
    r_ N..

#########################################################
#
# Functions to work with input pipes
#
# returns first not empty input pipe starting from start_input pipe
#
___ nonEmptyInput(node,start_input_0):
    inputs_node.inputs()
    ___ input __ ra..(start_input,inputs):
        __ node.input(input)!_N..:
            r_ input
    r_ N..

#########################################################
#
# Functions to work with input pipes
#
# shifts connection pipes to get rid of empty connections
# made for CountSheet rewiring but might be usefull for 3dScenes and merges as well
#
___ shiftConnections(node,start_0):
    inputs_node.inputs()
    ___ input __ ra..(start,inputs):
        node.setInput(input, node.input(input+1))
    __ emptyInput(node)__start:
            shiftConnections(node, start)
    __ emptyInput(node):
         shiftConnections(node, emptyInput(node))
    r_ node

#
# Functions to find file in plugin path folders
#
# looks through all folders and returns path list if file is found
#
___ where(filename):
    file_list_[]
    ___ pa__ __ ?.pluginPath
        check_file_'%s%s%s' % (pa__, __.sep, filename)
        __ __.pa__.isfile( check_file ):
            file_list.ap..(check_file)
    __ file_list:
        file_list.reverse()

    r_ file_list

