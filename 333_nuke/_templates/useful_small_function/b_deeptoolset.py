
#######################################################################################################################

__author__ = "Boris Martinez Castillo"
__version__ = "1.0.1"
__maintainer__ = "Boris Martinez Castillo"
__email__ = "boris.vfx@outlook.com"

#######################################################################################################################


______ ?
______ ?
______ itertools


#######################################################################################################################

#TO DO:

# UBER PASS: SUPPORT FOR AOV BUNDLE IN ADDITION TO MULTI LAYERED EXR.
# SUPPORT FOR DEEP_READ IN ADDITION TO DEEP_RECOLOR.
# ERROR HANDLING: WRONG CLASS SELECTION.DONE
# REMOVE AF SPECIFIC DEPENDENCIES BEFORE PUBLISHING.
# BUILD USER INTERFACE (PYSIDE???)
# FIX DOUBLE NAMING ISSUE.DONE
# FIX WRONG SELECTION ERROR.DONE
# IMPLEMENT SWITCH FOR EASY PRECOMP.
# FIX AUTOCOMP FROM WRITE.
# FIX WHITE SPACES FROM DEFAULT LGT ELEMENT NAME.
# CHECK OUT WHAT HAPPENS IF THERE'S NO DOT FOR THE COLOR INPUT OF THE DEEP RECOLOR NODE.
# CHECK OUT PYLINT

# DEEP HOLD OUT #######################################################################################################

# GLOBALS

DOT_COUNT = 0


#  FUNCTION DEFINITIONS


___ select_node(node_class):
    """
    This function makes sure you select a node of a given class.
    :param node_class: passed class node.
    :return: selected node of class node_class.
    """
    class_ = node_class

    ___
        node = ?.sN__
        __ node.Class() __ class_:
            node['selected'].sV..(False)
            r_ node
        ____
            m.. = "Please, select a {} Node".format(class_)
            ?.m..(m..)

    except ValueError:
        m.. = "Please, select a {} Node".format(class_)
        ?.m..(m..)


___ find_dependencies(node_class):
    """
    This function will return a list with the dependencies of the selected node.
    :param node_class: passed class node.
    :return: dependencies of a selected node of class node_class.
    """
    node = select_node(node_class)
    dep_node = ?.dependencies(node)
        
    r_ dep_node


___ get_node_position(node):
    """
    This function will return the position of a node.
    :param node: a nuke node object.
    :return: return a set of coordinates.
    """
    pos_dict = {"x_pos": node.xpos(),"y_pos": node.ypos()} 
    
    r_ pos_dict


___ get_righthandside_position(node_list):
    """
    This function will return the position of the right hand side node of a selection of nodes.
    :param node_list: a list of nuke nodes.
    :return: return a set of coordinates.
    """
    x_pos_list = []
    y_pos_list = []

    ___ node __ node_list:
        pos = get_node_position(?.toNode(node))
        x_pos_list.ap..(pos["x_pos"])
        y_pos_list.ap..(pos["y_pos"])
    
    max_x_pos = max(x_pos_list)
    min_x_pos = min(x_pos_list)

    avg_y_pos = su.(y_pos_list) / le.(y_pos_list)
   
    
    r_ min_x_pos,max_x_pos,avg_y_pos


___ create_node_with_position(nodename,connect_node,x=0,y=0):
     """
     This function will create a node in a given position and connect it to a given node.
     :param nodename: nuke node class to be created.
     :param connect_node: node to connect the created node to.
     :param x: x coordinate.
     :param y: y coordinate.
     :return: created node object.
     """
     node = ?.createNode(nodename)
     node['selected'].sV..(False)

     node.setXpos(int(x))
     node.setYpos(int(y))

     node.setInput(0,connect_node)

     r_ node


___ create_node_with_position_simple(nodename,x=0,y=0):
     """
     This function will create a node in a given position.
     :param nodename: nuke node class to be created.
     :param x: x coordinate.
     :param y: y coordinate.
     :return: created node.
     """
     node = ?.createNode(nodename)
     node['selected'].sV..(False)

     node.setXpos(int(x))
     node.setYpos(int(y))


     r_ node


___ d_dot_parent(parentname,nodename,connect_node,x=0,y=0):
    """
    This functions will create a custom "dDot" node.
    :param parentname: name of the dDot.
    :param nodename: nuke node class to be created. 
    :param connect_node: node to connect the created node to.
    :param x: x coordinate.
    :param y: y coordinate.
    :return: created dDot node object.
    """
    parentName = parentname
    parentKnob = ?.Text_Knob('parent', 'parent')

    newDot = create_node_with_position(nodename,connect_node,x,y)
    newDot.knob('label').sV..('[value name]')
    newDot.knob('name').sV..(parentName)
    newDot.knob('tile_color').sV..(0)
    newDot.knob('note_font_size').sV..(33)
    newDot.addKnob(parentKnob)

    r_ newDot


___ build_depth_setup(node_list):
    """
    This functions will create a custom depth from deep setup.
    :param node_list: a list of nuke nodes.
    :return: none.
    """
    positions = get_righthandside_position(node_list)

    deep_merge = create_node_with_position_simple("DeepMerge",positions[1] +  500, positions[2]+100)
    deep_merge['selected'].sV..(True)

    deep_to_image = ?.createNode("DeepToImage")
    deep_to_image_pos = get_node_position(deep_to_image)
    deep_to_image.setYpos(deep_to_image_pos["y_pos"] + 50)

    unpremult = ?.createNode("Unpremult")
    unpremult['channels'].sV..("Zdepth")
    deep_to_image_pos = get_node_position(unpremult)
    unpremult.setYpos(deep_to_image_pos["y_pos"] + 25)
    
    expression = ?.createNode("Expression")
    expression['channel3'].sV..("depth")
    expression['expr3'].sV..("Zdepth.red == 0 ? inf : Zdepth.red")
    expression_pos = get_node_position(expression)
    expression.setYpos(expression_pos["y_pos"] + 25)

    
    remove = ?.createNode("Remove")
    remove["operation"].sV..("keep")
    remove["channels"].sV..("rgba")
    remove["channels2"].sV..("depth")
    remove_pos = get_node_position(remove)
    remove.setYpos(remove_pos["y_pos"] + 25)
    

    deep_write =  create_node_with_position("AFWrite",remove,get_node_position(remove)["x_pos"],get_node_position(remove)["y_pos"] + 200) 

    counter = 0 

    ___ node __ node_list:
        deep_merge.setInput(counter,?.toNode(node))
        counter += 1
    r_


___ get_asset_name(sourcenode):
    """
    This functions will retrieve the asset name found in the publish info / layer knob.
    :param sourcenode:
    :return:
    """
    source_node = ?.toNode(sourcenode)
    target_class = "DeepRead"
    dep_nodes = ?.dependencies(source_node)
    
    ___ node __ dep_nodes:
        __ node.Class() __ target_class:
            ___
                asset_name = node["sg_layer"].value()
                __ asset_name __ "":
                    default_asset_name =  "element_01"
                    r_ default_asset_name
                ____
                    r_ asset_name
            except ValueError:
                print "no asset name found"
                asset_name = "element_01"    
                r_ asset_name
        ____
            r_ get_asset_name(node.name())


___ create_deep_holdout_setup(node_class):
    """
    This functions will create a custom deep holdout setup.
    :param node_class: a nuke class node.
    :return:
    """
    g__ DOT_COUNT

    
    deep_node = ?.sN__
    dependencies = find_dependencies(node_class)
    asset_name = get_asset_name(deep_node.name())

    pos1 = get_node_position(deep_node)
    pos2 = get_node_position(dependencies[1])

    deep_holdout = create_node_with_position("DeepHoldout2",deep_node,pos1["x_pos"],pos1["y_pos"] + 100)
    dot = create_node_with_position("Dot",dependencies[1],pos2["x_pos"],pos2["y_pos"]+ 200)
    
    pos3 = get_node_position(deep_holdout)
    pos4 = get_node_position(dot)

    deep_merge = create_node_with_position("DeepMerge",deep_holdout,pos3["x_pos"] + 150,pos3["y_pos"]- 50)
    deep_holdout.setInput(1,deep_merge)

    merge = create_node_with_position("Merge2",deep_holdout,pos3["x_pos"],pos3["y_pos"]+ 100)
    merge.setInput(1,dot)
    merge['operation'].sV..("difference")

    merge2 = create_node_with_position("Merge2",dot,pos4["x_pos"]-35,pos4["y_pos"]+ 100)
    merge2.setInput(1,merge)
    merge2['operation'].sV..("divide")
    
    pos5 = get_node_position(merge2)

    shuffle = create_node_with_position("Shuffle",merge2,pos5["x_pos"],pos5["y_pos"]+ 100)
    shuffle['label'].sV..("ALPHA TO RGB")
    channels = ["red","green","blue","alpha"]

    ___ channel __ channels:
        shuffle[channel].sV..("alpha")

    pos6 = get_node_position(shuffle)

    string = str.lower(asset_name + "_" + "holdout") + "_" + str(DOT_COUNT)

    
    __ ?.toNode(string):

        DOT_COUNT += 1
        string = str.lower(asset_name + "_" + "holdout") + "_" + str(DOT_COUNT)
    
    switch = create_node_with_position("Switch",shuffle,pos6["x_pos"],pos6["y_pos"]+ 200)

    pos7 = get_node_position(switch)

    switch_dot = create_node_with_position_simple("Dot",pos7["x_pos"]-150,pos7["y_pos"])
    
    switch.setInput(1,switch_dot)
    switch['label'].sV..("[value which]")


    last_dot = d_dot_parent(string,"Dot",switch,pos7["x_pos"]+35,pos7["y_pos"]+ 500)

    pos8 = get_node_position(last_dot)

    #AFwrite = create_node_with_position("AFWrite",last_dot,pos8["x_pos"]-15,pos8["y_pos"]+ 100)

    r_ deep_holdout


___ check_upstream_match(sourcenode,targetnode):
    """
    This function will try to match a given upstream node class match.
    :param sourcenode: a source nuke node.
    :param targetnode: a target nuke node.
    :return:
    """
    source_node = ?.toNode(sourcenode)
    target_node = ?.toNode(targetnode)
    dep_nodes = ?.dependencies(source_node)
    
    __ target_node __ dep_nodes:
        print "MATCHHHH!"
        r_ True
    ____
        print "KEEP LOOKING"
        ___ node __ dep_nodes:
            r_ check_upstream_match(node.name(),targetnode)


___ iterate_deep_holdout_setup():
    """
    This function will iterate over a set of DeepRecolor nodes and create a holdout setup for each.
    :return: none
    """
    names = []
    deep_holdouts = []
    selected_nodes = []


    ___ i __ ?.sN..:

        __ i.Class() != "DeepRecolor":
            ?.m..("Please, select only DeepRecolor Nodes")
            r_
        ____
            names.ap..(i.name())
            i['selected'].sV..(False)

    #build_depth_setup(names)

    ___ e __ names:
        node = ?.toNode(e)
        class_ = node.Class()
        node['selected'].sV..(True)
        setup = create_deep_holdout_setup(class_)
        deep_holdouts.ap..(setup.name())
   
    counter = 0

    ___ ho __ deep_holdouts:
        hold_out = ?.toNode(ho)
        depp = ?.dependencies(hold_out)
        deep_merge = depp[1].name()

        ___ name __ names:
           __ check_upstream_match(ho,name):
                print "ALELUYA"
           ____ no. check_upstream_match(ho,name):
                ?.toNode(deep_merge).setInput(counter,?.toNode(name))
                counter += 1
            
  
# UBER PASS #######################################################################################################


___ get_middle_position():
    """
    This function will compute a set of coordinates of convenience.
    :return: a set of coordinates.
    """
    x_pos_list = []
    y_pos_list = []

    ___ node __ ?.sN..:
        pos = get_node_position(node)
        x_pos_list.ap..(pos["x_pos"])
        y_pos_list.ap..(pos["y_pos"])
    
    max_x_pos = max(x_pos_list)
    min_x_pos = min(x_pos_list)
    
    avg_y_pos = su.(y_pos_list) / le.(y_pos_list)

    diff = max_x_pos - min_x_pos
    offset = diff / 2
    
    r_ min_x_pos,offset,avg_y_pos


___ create_rgba_deep_recolor(channels):
    """
    This function will compute a set of coordinates of convenience.
    :param channels:
    :return: a colection of DeepRecolor node objects.
    """
    new_deep_recolor_names = []    

    ___ node __ ?.sN..:

        dependencies = ?.dependencies(node)
        deep = dependencies[0]
        flat = dependencies[1]
    
        pos_x = get_node_position(node)["x_pos"]
        pos_y = get_node_position(node)["y_pos"]

        deep_recolor = create_node_with_position("DeepRecolor", deep, pos_x -150,pos_y  +450 )
        deep_recolor.setInput(1,flat) 
        deep_recolor['tile_color'].sV..(4278239231)
    

        deep_recolor['channels'].sV..(channels)
        
        new_deep_recolor_names.ap..(deep_recolor.name())

    r_ new_deep_recolor_names


___ uberpass_function():
    """
    This function will deep merge all elemenents together, thus creating the so called uber pass.

    """
    node_list = []

    ___ node __ ?.sN..:
        node_list.ap..(node)

    rgb_deep_recolor = create_rgba_deep_recolor("rgba")
    
    ___ node __ node_list:
        node['selected'].sV..(True)

    deep_merge = create_node_with_position_simple("DeepMerge",get_middle_position()[0] + get_middle_position()[1],get_middle_position()[2] + 400)

    deep_to_image = create_node_with_position("DeepToImage",deep_merge,get_node_position(deep_merge)["x_pos"],get_node_position(deep_merge)["y_pos"] + 200)

    deep_to_image_pos = get_node_position(deep_to_image)

    switch = create_node_with_position("Switch",deep_to_image,deep_to_image_pos["x_pos"],deep_to_image_pos["y_pos"]+ 200)
    switch_pos = get_node_position(switch)
    switch_dot = create_node_with_position_simple("Dot",switch_pos["x_pos"]-150,switch_pos["y_pos"])
    switch.setInput(1,switch_dot)
    switch['label'].sV..("[value which]")

    string = "uberpass_color_output"
    last_dot = d_dot_parent(string,"Dot",switch,switch_pos["x_pos"]+35,switch_pos["y_pos"]+ 100)

    write = create_node_with_position("Write",last_dot,get_node_position(last_dot)["x_pos"],get_node_position(last_dot)["y_pos"] + 200)
    write['channels'].sV..('all')

    ___ name __ rgb_deep_recolor:
       ?.toNode(name)['selected'].sV..(True)

    deep_deep_merge = create_node_with_position_simple("DeepMerge",get_middle_position()[0] + get_middle_position()[1] - 800,get_middle_position()[2] + 200)

    deep_deep_merge_pos = get_node_position(deep_deep_merge)

    string_deep = "uberpass_deep_output"
    last_dot_deep = d_dot_parent(string_deep,"Dot",deep_deep_merge,deep_deep_merge_pos["x_pos"]+35,deep_deep_merge_pos["y_pos"]+ 100)

    deep_write =  create_node_with_position("DeepWrite",deep_deep_merge,get_node_position(deep_deep_merge)["x_pos"],get_node_position(deep_deep_merge)["y_pos"] + 200) 



# DEPTH FOR DEFOCUS #######################################################################################################


___ depth_for_defocus():
    """
    This function will create a custom depth from deep setup.
    """
    node_list = []

    ___ node __ ?.sN..:
        node_list.ap..(node)

    rgb_deep_recolor = create_rgba_deep_recolor("all")
    
    ___ name __ rgb_deep_recolor:
        ?.toNode(name)['selected'].sV..(True)

    deep_merge = create_node_with_position_simple("DeepMerge",get_middle_position()[0] + get_middle_position()[1],get_middle_position()[2] + 400)

    deep_to_image = create_node_with_position("DeepToImage",deep_merge,get_node_position(deep_merge)["x_pos"],get_node_position(deep_merge)["y_pos"] + 100)

    unpremult = create_node_with_position("Unpremult",deep_to_image,get_node_position(deep_to_image)["x_pos"],get_node_position(deep_to_image)["y_pos"] + 100)    
    unpremult['channels'].sV..("Zdepth")

    expression = create_node_with_position("Expression",unpremult,get_node_position(unpremult)["x_pos"],get_node_position(unpremult)["y_pos"] + 100)    
    expression['channel3'].sV..("depth")
    expression['expr3'].sV..("Zdepth.red == 0 ? 15000 : Zdepth.red")

    remove = create_node_with_position("Remove",expression,get_node_position(expression)["x_pos"],get_node_position(expression)["y_pos"] + 100)  
    remove["operation"].sV..("keep")
    remove["channels"].sV..("rgba")
    remove["channels2"].sV..("depth")

    pos6 = get_node_position(remove)

    string = "depth_from_deep"

    last_dot = d_dot_parent(string,"Dot",remove,pos6["x_pos"]+35,pos6["y_pos"]+ 100)

    AFwrite = create_node_with_position("Write",last_dot,get_node_position(last_dot)["x_pos"],get_node_position(last_dot)["y_pos"] + 100)
    AFwrite['channels'].sV..('all')



# SPLIT LAYERS #######################################################################################################


___ splitLayers( node ):

    '''
    Splits each and every layer from the selected node into their own pipes
    '''
    
    ch = node.channels()
    
    layers = []
    valid_channels = ['red', 'green', 'blue', 'alpha', 'black', 'white']
    
    ___ each __ ch:
        layer_name = each.split( '.' )[0]
        tmp = []
        ___ channel __ ch:
            __ channel.startswith( layer_name ) __ True:
                tmp.ap..( channel )
        __ le.( tmp ) < 4:
            ___ i __ ra..( 4 - le.( tmp ) ):
                tmp.ap..( layer_name + ".white" )
        __ tmp no. __ layers:
            layers.ap..( tmp )
            
    ___ each __ layers:
        layer = each[0].split( '.' )[0]
        ch1 = each[0].split( '.' )[1]
        ch2 = each[1].split( '.' )[1]
        ch3 = each[2].split( '.' )[1]
        ch4 = each[3].split( '.' )[1]
        
        __ ch1 no. __ valid_channels:
            ch1 = "red red"
        ____
            ch1 = '%s %s' % ( ch1, ch1 )
            
        __ ch2 no. __ valid_channels:
            ch2 = "green green"
        ____
            ch2 = '%s %s' % ( ch2, ch2 )
            
        __ ch3 no. __ valid_channels:
            ch3 = "blue blue"
        ____
            ch3 = '%s %s' % ( ch3, ch3 )
            
        __ ch4 no. __ valid_channels:
            ch4 = "alpha alpha"
        ____
            ch4 = '%s %s' % ( ch4, ch4 )
            
        prefs = "in %s %s %s %s %s" % (layer, ch1, ch2, ch3, ch4)
        shuffle = ?.createNode( 'Shuffle', prefs, inpanel=False )
        shuffle.knob( 'label' ).sV..( layer )
        shuffle.setInput( 0, node )

        AFwrite = create_node_with_position("AFWrite",shuffle,get_node_position(shuffle)["x_pos"],get_node_position(shuffle)["y_pos"] + 100)
        AFwrite['channels'].sV..('all')


# AUTO DDOT COMP  #######################################################################################################


___ d_dot_connect(nodename,connect_node,x=0,y=0):
    """

    :param nodename: nuke node class to be created.
    :param connect_node: nuke node to connect to.
    :param x: x coordinate.
    :param y: y coordinate.
    :return: created node object.
    """
    parent_node = ?.toNode(connect_node)
    childKnob = ?.Text_Knob('child', 'child')

    dot = create_node_with_position(nodename,parent_node,x,y)
    dot.knob('label').sV..(connect_node)
    dot.knob('tile_color').sV..(0)
    dot.knob('hide_input').sV..(True)
    dot.knob('note_font').sV..('italic')
    dot.knob('note_font_size').sV..(22)
    dot.addKnob(childKnob)

    r_ dot


___ gather_holdout_dot_names():
    """
    This function will get all names of selected Ddots.
    :return: a list of node names.
    """
    holdout_dots_names = [node['name'].value() ___ node __ ?.sN.. __ node['parent']]
    
    r_ holdout_dots_names


___ find_holdout_source_elements(houldout_names):
    """
    This function will get all names of selected Ddots.
    :param houldout_names: a list of node names.
    :return:
    """
    houldout_processed_list = [] 
        
    ___ name __ houldout_names:
        _ = "_".join(name.split('_')[:-2])
        __ ?.toNode(_):
            houldout_processed_list.ap..(_)
        ____
            print "no corresponding element found for {}".format(name)
    
    r_ houldout_processed_list


___ create_and_connect_child_dots(holdouts,color):
    """

    :param holdouts:
    :param color:
    """
    multiply_list = []
    counter = 0
    adder = 0
    adder_x = 0
    pos_f_x = N..
    pos_f_y = N..


    ___ f,b __ itertools.izip(holdouts,color):

        __ counter __ 0 :

            pos_f_x = get_node_position(?.toNode(f))["x_pos"]
            pos_f_y = get_node_position(?.toNode(f))["y_pos"]
      
            child_holdout_dot = d_dot_connect("Dot",f,pos_f_x,pos_f_y + 1000)
            child_color_dot = d_dot_connect("Dot",b,pos_f_x - 200,pos_f_y + 1200)        
            
            multiply = create_node_with_position("Multiply",child_color_dot,pos_f_x - 35 ,pos_f_y + 1190)
            multiply.setInput(0,child_color_dot)
            multiply.setInput(1,child_holdout_dot)
            multiply['label'].sV..("DEEP HOLDOUT MULT BY ZERO")
            multiply['value'].sV..(0)
    
            multiply_list.ap..(multiply)
            counter += 1

        ____

            adder += 1000
            adder_x += - 1000  
            child_holdout_dot = d_dot_connect("Dot",f,pos_f_x  + adder_x ,pos_f_y + 1000 + adder)
            child_color_dot = d_dot_connect("Dot",b,pos_f_x - 200  + adder_x ,pos_f_y + 1200 + adder)        
                        
            multiply = create_node_with_position("Multiply",child_color_dot,pos_f_x - 35  + adder_x ,pos_f_y + 1190 + adder )
            adder_x = 0 
                
            multiply.setInput(0,child_color_dot)
            multiply.setInput(1,child_holdout_dot)
            multiply['label'].sV..("DEEP HOLDOUT MULT BY ZERO")
            multiply['value'].sV..(0)


            multiply_list.ap..(multiply)
          
    counter  = 0
    holder = []
    
    ___ i __ ra..(le.(multiply_list)):

        __ counter __ 0:

            x = get_node_position(multiply_list[i])["x_pos"]
            y = get_node_position(multiply_list[i])["y_pos"]

            counter += 1
        
        ____
            
            x = get_node_position(multiply_list[i])["x_pos"]
            y = get_node_position(multiply_list[i])["y_pos"]
      
            merge = create_node_with_position_simple("Merge2",pos_f_x,y)
            merge['operation'].sV..('disjoint-over')
            holder.ap..(merge)

            __ le.(holder) __ 1:
                merge.setInput(0,multiply_list[i-1])
                merge.setInput(1,multiply_list[i])
                
            ____ le.(holder) > 1:
                print holder[i-2].name() 
                merge.setInput(0,holder[i-2])
                merge.setInput(1,multiply_list[i])


#  CLASS DEFINITIONS


c_ modalPanel(?.PythonPanel):

    ___  -

        ?.PythonPanel. - (self,"b_deep toolset")
        #CREATE KNOBS
        depth_from_deep = ?.PyScript_Knob('depth_from_deep', 'depth_from_deep', 'depth_for_defocus()')
        create_holdouts = ?.Enumeration_Knob('mode','build mode  ', ['contact sheet','extract'])
        deep_uberpass = ?.Enumeration_Knob('mode','build mode  ', ['contact sheet','extract'])
        auto_comp.clearFlag(?.STARTLINE)
        author = ?.Text_Knob("written by Boris Martinez")
        #ADD KNOBS
        ___ i __ (frame_range,frame_display,analysis_mode,author):
            addKnob(i)
        #SET KNOB DEFAULT VALUES
        get_frame_range()

    ___ giveFrameRangeValue
        r_ frame_range.value()

    ___ get_frame_range
        __ giveFrameRangeValue() __ "global":
            first_frame = ?.root().firstFrame()
            last_frame = ?.root().lastFrame()
            txt = str(int(first_frame)) + '-' + str(int(last_frame))
            frame_display.sV..(txt)
        ____ giveFrameRangeValue() __ "input":
            print "here should come the read frame range"
            node = ?.sN__
            first_frame = node.firstFrame()
            last_frame = node.lastFrame()
            txt = str(int(first_frame)) + '-' + str(int(last_frame))
            frame_display.sV..(txt)
        ____ giveFrameRangeValue() __ "custom":
            frame_display.sV..("")
            print "here the user decides"

    ___ knobChanged(self,knob):
        __ knob.name() __ "fRange":
            get_frame_range()
                      







__ __name__ __  "__main__":
    #uberpass_function()
    iterate_deep_holdout_setup()
    #depth_for_defocus()
    #create_and_connect_child_dots(gather_holdout_dot_names(),find_holdout_source_elements(gather_holdout_dot_names()))    