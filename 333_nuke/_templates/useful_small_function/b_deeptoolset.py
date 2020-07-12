
#######################################################################################################################

__author__ _ "Boris Martinez Castillo"
__version__ _ "1.0.1"
__maintainer__ _ "Boris Martinez Castillo"
__email__ _ "boris.vfx@outlook.com"

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

DOT_COUNT _ 0


#  FUNCTION DEFINITIONS


___ select_node(node_class):
    """
    This function makes sure you select a node of a given class.
    :param node_class: passed class node.
    :return: selected node of class node_class.
    """
    class_ _ node_class

    ___
        node _ ?.sN__
        __ node.Class() __ class_:
            node['selected'].sV..(F..)
            r_ node
        ____
            m.. _ "Please, select a {} Node".f..(class_)
            ?.m..(m..)

    except ValueError:
        m.. _ "Please, select a {} Node".f..(class_)
        ?.m..(m..)


___ find_dependencies(node_class):
    """
    This function will return a list with the dependencies of the selected node.
    :param node_class: passed class node.
    :return: dependencies of a selected node of class node_class.
    """
    node _ select_node(node_class)
    dep_node _ ?.dependencies(node)
        
    r_ dep_node


___ get_node_position(node):
    """
    This function will return the position of a node.
    :param node: a nuke node object.
    :return: return a set of coordinates.
    """
    pos_dict _ {"x_pos": node.xpos(),"y_pos": node.ypos()}
    
    r_ pos_dict


___ get_righthandside_position(node_list):
    """
    This function will return the position of the right hand side node of a selection of nodes.
    :param node_list: a list of nuke nodes.
    :return: return a set of coordinates.
    """
    x_pos_list _ []
    y_pos_list _ []

    ___ node __ node_list:
        pos _ get_node_position(?.toNode(node))
        x_pos_list.ap..(pos["x_pos"])
        y_pos_list.ap..(pos["y_pos"])
    
    max_x_pos _ max(x_pos_list)
    min_x_pos _ min(x_pos_list)

    avg_y_pos _ su.(y_pos_list) / le.(y_pos_list)
   
    
    r_ min_x_pos,max_x_pos,avg_y_pos


___ create_node_with_position(nodename,connect_node,x_0,y_0):
     """
     This function will create a node in a given position and connect it to a given node.
     :param nodename: nuke node class to be created.
     :param connect_node: node to connect the created node to.
     :param x: x coordinate.
     :param y: y coordinate.
     :return: created node object.
     """
     node _ ?.createNode(nodename)
     node['selected'].sV..(F..)

     node.setXpos(in.(x))
     node.setYpos(in.(y))

     node.setInput(0,connect_node)

     r_ node


___ create_node_with_position_simple(nodename,x_0,y_0):
     """
     This function will create a node in a given position.
     :param nodename: nuke node class to be created.
     :param x: x coordinate.
     :param y: y coordinate.
     :return: created node.
     """
     node _ ?.createNode(nodename)
     node['selected'].sV..(F..)

     node.setXpos(in.(x))
     node.setYpos(in.(y))


     r_ node


___ d_dot_parent(parentname,nodename,connect_node,x_0,y_0):
    """
    This functions will create a custom "dDot" node.
    :param parentname: name of the dDot.
    :param nodename: nuke node class to be created. 
    :param connect_node: node to connect the created node to.
    :param x: x coordinate.
    :param y: y coordinate.
    :return: created dDot node object.
    """
    parentName _ parentname
    parentKnob _ ?.T_K..('parent', 'parent')

    newDot _ create_node_with_position(nodename,connect_node,x,y)
    newDot.knob('label').sV..('[value name]')
    newDot.knob('name').sV..(parentName)
    newDot.knob('tile_color').sV..(0)
    newDot.knob('note_font_size').sV..(33)
    newDot.aK..(parentKnob)

    r_ newDot


___ build_depth_setup(node_list):
    """
    This functions will create a custom depth from deep setup.
    :param node_list: a list of nuke nodes.
    :return: none.
    """
    positions _ get_righthandside_position(node_list)

    deep_merge _ create_node_with_position_simple("DeepMerge",positions[1] +  500, positions[2]+100)
    deep_merge['selected'].sV..(T..)

    deep_to_image _ ?.createNode("DeepToImage")
    deep_to_image_pos _ get_node_position(deep_to_image)
    deep_to_image.setYpos(deep_to_image_pos["y_pos"] + 50)

    unpremult _ ?.createNode("Unpremult")
    unpremult['channels'].sV..("Zdepth")
    deep_to_image_pos _ get_node_position(unpremult)
    unpremult.setYpos(deep_to_image_pos["y_pos"] + 25)
    
    expression _ ?.createNode("Expression")
    expression['channel3'].sV..("depth")
    expression['expr3'].sV..("Zdepth.red == 0 ? inf : Zdepth.red")
    expression_pos _ get_node_position(expression)
    expression.setYpos(expression_pos["y_pos"] + 25)

    
    remove _ ?.createNode("Remove")
    remove["operation"].sV..("keep")
    remove["channels"].sV..("rgba")
    remove["channels2"].sV..("depth")
    remove_pos _ get_node_position(remove)
    remove.setYpos(remove_pos["y_pos"] + 25)
    

    deep_write _  create_node_with_position("AFWrite",remove,get_node_position(remove)["x_pos"],get_node_position(remove)["y_pos"] + 200)

    counter _ 0

    ___ node __ node_list:
        deep_merge.setInput(counter,?.toNode(node))
        counter +_ 1
    r_


___ get_asset_name(sourcenode):
    """
    This functions will retrieve the asset name found in the publish info / layer knob.
    :param sourcenode:
    :return:
    """
    source_node _ ?.toNode(sourcenode)
    target_class _ "DeepRead"
    dep_nodes _ ?.dependencies(source_node)
    
    ___ node __ dep_nodes:
        __ node.Class() __ target_class:
            ___
                asset_name _ node["sg_layer"].v..
                __ asset_name __ "":
                    default_asset_name _  "element_01"
                    r_ default_asset_name
                ____
                    r_ asset_name
            except ValueError:
                print "no asset name found"
                asset_name _ "element_01"
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

    
    deep_node _ ?.sN__
    dependencies _ find_dependencies(node_class)
    asset_name _ get_asset_name(deep_node.name())

    pos1 _ get_node_position(deep_node)
    pos2 _ get_node_position(dependencies[1])

    deep_holdout _ create_node_with_position("DeepHoldout2",deep_node,pos1["x_pos"],pos1["y_pos"] + 100)
    dot _ create_node_with_position("Dot",dependencies[1],pos2["x_pos"],pos2["y_pos"]+ 200)
    
    pos3 _ get_node_position(deep_holdout)
    pos4 _ get_node_position(dot)

    deep_merge _ create_node_with_position("DeepMerge",deep_holdout,pos3["x_pos"] + 150,pos3["y_pos"]- 50)
    deep_holdout.setInput(1,deep_merge)

    merge _ create_node_with_position("Merge2",deep_holdout,pos3["x_pos"],pos3["y_pos"]+ 100)
    merge.setInput(1,dot)
    merge['operation'].sV..("difference")

    merge2 _ create_node_with_position("Merge2",dot,pos4["x_pos"]-35,pos4["y_pos"]+ 100)
    merge2.setInput(1,merge)
    merge2['operation'].sV..("divide")
    
    pos5 _ get_node_position(merge2)

    shuffle _ create_node_with_position("Shuffle",merge2,pos5["x_pos"],pos5["y_pos"]+ 100)
    shuffle['label'].sV..("ALPHA TO RGB")
    channels _ ["red","green","blue","alpha"]

    ___ channel __ channels:
        shuffle[channel].sV..("alpha")

    pos6 _ get_node_position(shuffle)

    string _ str.lower(asset_name + "_" + "holdout") + "_" + str(DOT_COUNT)

    
    __ ?.toNode(string):

        DOT_COUNT +_ 1
        string _ str.lower(asset_name + "_" + "holdout") + "_" + str(DOT_COUNT)
    
    switch _ create_node_with_position("Switch",shuffle,pos6["x_pos"],pos6["y_pos"]+ 200)

    pos7 _ get_node_position(switch)

    switch_dot _ create_node_with_position_simple("Dot",pos7["x_pos"]-150,pos7["y_pos"])
    
    switch.setInput(1,switch_dot)
    switch['label'].sV..("[value which]")


    last_dot _ d_dot_parent(string,"Dot",switch,pos7["x_pos"]+35,pos7["y_pos"]+ 500)

    pos8 _ get_node_position(last_dot)

    #AFwrite = create_node_with_position("AFWrite",last_dot,pos8["x_pos"]-15,pos8["y_pos"]+ 100)

    r_ deep_holdout


___ check_upstream_match(sourcenode,targetnode):
    """
    This function will try to match a given upstream node class match.
    :param sourcenode: a source nuke node.
    :param targetnode: a target nuke node.
    :return:
    """
    source_node _ ?.toNode(sourcenode)
    target_node _ ?.toNode(targetnode)
    dep_nodes _ ?.dependencies(source_node)
    
    __ target_node __ dep_nodes:
        print "MATCHHHH!"
        r_ T..
    ____
        print "KEEP LOOKING"
        ___ node __ dep_nodes:
            r_ check_upstream_match(node.name(),targetnode)


___ iterate_deep_holdout_setup():
    """
    This function will iterate over a set of DeepRecolor nodes and create a holdout setup for each.
    :return: none
    """
    names _ []
    deep_holdouts _ []
    selected_nodes _ []


    ___ i __ ?.sN..:

        __ i.Class() !_ "DeepRecolor":
            ?.m..("Please, select only DeepRecolor Nodes")
            r_
        ____
            names.ap..(i.name())
            i['selected'].sV..(F..)

    #build_depth_setup(names)

    ___ e __ names:
        node _ ?.toNode(e)
        class_ _ node.Class()
        node['selected'].sV..(T..)
        setup _ create_deep_holdout_setup(class_)
        deep_holdouts.ap..(setup.name())
   
    counter _ 0

    ___ ho __ deep_holdouts:
        hold_out _ ?.toNode(ho)
        depp _ ?.dependencies(hold_out)
        deep_merge _ depp[1].name()

        ___ name __ names:
           __ check_upstream_match(ho,name):
                print "ALELUYA"
           ____ no. check_upstream_match(ho,name):
                ?.toNode(deep_merge).setInput(counter,?.toNode(name))
                counter +_ 1
            
  
# UBER PASS #######################################################################################################


___ get_middle_position():
    """
    This function will compute a set of coordinates of convenience.
    :return: a set of coordinates.
    """
    x_pos_list _ []
    y_pos_list _ []

    ___ node __ ?.sN..:
        pos _ get_node_position(node)
        x_pos_list.ap..(pos["x_pos"])
        y_pos_list.ap..(pos["y_pos"])
    
    max_x_pos _ max(x_pos_list)
    min_x_pos _ min(x_pos_list)
    
    avg_y_pos _ su.(y_pos_list) / le.(y_pos_list)

    diff _ max_x_pos - min_x_pos
    offset _ diff / 2
    
    r_ min_x_pos,offset,avg_y_pos


___ create_rgba_deep_recolor(channels):
    """
    This function will compute a set of coordinates of convenience.
    :param channels:
    :return: a colection of DeepRecolor node objects.
    """
    new_deep_recolor_names _ []

    ___ node __ ?.sN..:

        dependencies _ ?.dependencies(node)
        deep _ dependencies[0]
        flat _ dependencies[1]
    
        pos_x _ get_node_position(node)["x_pos"]
        pos_y _ get_node_position(node)["y_pos"]

        deep_recolor _ create_node_with_position("DeepRecolor", deep, pos_x -150,pos_y  +450 )
        deep_recolor.setInput(1,flat) 
        deep_recolor['tile_color'].sV..(4278239231)
    

        deep_recolor['channels'].sV..(channels)
        
        new_deep_recolor_names.ap..(deep_recolor.name())

    r_ new_deep_recolor_names


___ uberpass_function():
    """
    This function will deep merge all elemenents together, thus creating the so called uber pass.

    """
    node_list _ []

    ___ node __ ?.sN..:
        node_list.ap..(node)

    rgb_deep_recolor _ create_rgba_deep_recolor("rgba")
    
    ___ node __ node_list:
        node['selected'].sV..(T..)

    deep_merge _ create_node_with_position_simple("DeepMerge",get_middle_position()[0] + get_middle_position()[1],get_middle_position()[2] + 400)

    deep_to_image _ create_node_with_position("DeepToImage",deep_merge,get_node_position(deep_merge)["x_pos"],get_node_position(deep_merge)["y_pos"] + 200)

    deep_to_image_pos _ get_node_position(deep_to_image)

    switch _ create_node_with_position("Switch",deep_to_image,deep_to_image_pos["x_pos"],deep_to_image_pos["y_pos"]+ 200)
    switch_pos _ get_node_position(switch)
    switch_dot _ create_node_with_position_simple("Dot",switch_pos["x_pos"]-150,switch_pos["y_pos"])
    switch.setInput(1,switch_dot)
    switch['label'].sV..("[value which]")

    string _ "uberpass_color_output"
    last_dot _ d_dot_parent(string,"Dot",switch,switch_pos["x_pos"]+35,switch_pos["y_pos"]+ 100)

    write _ create_node_with_position("Write",last_dot,get_node_position(last_dot)["x_pos"],get_node_position(last_dot)["y_pos"] + 200)
    write['channels'].sV..('all')

    ___ name __ rgb_deep_recolor:
       ?.toNode(name)['selected'].sV..(T..)

    deep_deep_merge _ create_node_with_position_simple("DeepMerge",get_middle_position()[0] + get_middle_position()[1] - 800,get_middle_position()[2] + 200)

    deep_deep_merge_pos _ get_node_position(deep_deep_merge)

    string_deep _ "uberpass_deep_output"
    last_dot_deep _ d_dot_parent(string_deep,"Dot",deep_deep_merge,deep_deep_merge_pos["x_pos"]+35,deep_deep_merge_pos["y_pos"]+ 100)

    deep_write _  create_node_with_position("DeepWrite",deep_deep_merge,get_node_position(deep_deep_merge)["x_pos"],get_node_position(deep_deep_merge)["y_pos"] + 200)



# DEPTH FOR DEFOCUS #######################################################################################################


___ depth_for_defocus():
    """
    This function will create a custom depth from deep setup.
    """
    node_list _ []

    ___ node __ ?.sN..:
        node_list.ap..(node)

    rgb_deep_recolor _ create_rgba_deep_recolor("all")
    
    ___ name __ rgb_deep_recolor:
        ?.toNode(name)['selected'].sV..(T..)

    deep_merge _ create_node_with_position_simple("DeepMerge",get_middle_position()[0] + get_middle_position()[1],get_middle_position()[2] + 400)

    deep_to_image _ create_node_with_position("DeepToImage",deep_merge,get_node_position(deep_merge)["x_pos"],get_node_position(deep_merge)["y_pos"] + 100)

    unpremult _ create_node_with_position("Unpremult",deep_to_image,get_node_position(deep_to_image)["x_pos"],get_node_position(deep_to_image)["y_pos"] + 100)
    unpremult['channels'].sV..("Zdepth")

    expression _ create_node_with_position("Expression",unpremult,get_node_position(unpremult)["x_pos"],get_node_position(unpremult)["y_pos"] + 100)
    expression['channel3'].sV..("depth")
    expression['expr3'].sV..("Zdepth.red == 0 ? 15000 : Zdepth.red")

    remove _ create_node_with_position("Remove",expression,get_node_position(expression)["x_pos"],get_node_position(expression)["y_pos"] + 100)
    remove["operation"].sV..("keep")
    remove["channels"].sV..("rgba")
    remove["channels2"].sV..("depth")

    pos6 _ get_node_position(remove)

    string _ "depth_from_deep"

    last_dot _ d_dot_parent(string,"Dot",remove,pos6["x_pos"]+35,pos6["y_pos"]+ 100)

    AFwrite _ create_node_with_position("Write",last_dot,get_node_position(last_dot)["x_pos"],get_node_position(last_dot)["y_pos"] + 100)
    AFwrite['channels'].sV..('all')



# SPLIT LAYERS #######################################################################################################


___ splitLayers( node ):

    '''
    Splits each and every layer from the selected node into their own pipes
    '''
    
    ch _ node.channels()
    
    layers _ []
    valid_channels _ ['red', 'green', 'blue', 'alpha', 'black', 'white']
    
    ___ each __ ch:
        layer_name _ each.split( '.' )[0]
        tmp _ []
        ___ channel __ ch:
            __ channel.startswith( layer_name ) __ T..:
                tmp.ap..( channel )
        __ le.( tmp ) < 4:
            ___ i __ ra..( 4 - le.( tmp ) ):
                tmp.ap..( layer_name + ".white" )
        __ tmp no. __ layers:
            layers.ap..( tmp )
            
    ___ each __ layers:
        layer _ each[0].split( '.' )[0]
        ch1 _ each[0].split( '.' )[1]
        ch2 _ each[1].split( '.' )[1]
        ch3 _ each[2].split( '.' )[1]
        ch4 _ each[3].split( '.' )[1]
        
        __ ch1 no. __ valid_channels:
            ch1 _ "red red"
        ____
            ch1 _ '@ @' % ( ch1, ch1 )
            
        __ ch2 no. __ valid_channels:
            ch2 _ "green green"
        ____
            ch2 _ '@ @' % ( ch2, ch2 )
            
        __ ch3 no. __ valid_channels:
            ch3 _ "blue blue"
        ____
            ch3 _ '@ @' % ( ch3, ch3 )
            
        __ ch4 no. __ valid_channels:
            ch4 _ "alpha alpha"
        ____
            ch4 _ '@ @' % ( ch4, ch4 )
            
        prefs _ "in @ @ @ @ @" % (layer, ch1, ch2, ch3, ch4)
        shuffle _ ?.createNode( 'Shuffle', prefs, inpanel_F.. )
        shuffle.knob( 'label' ).sV..( layer )
        shuffle.setInput( 0, node )

        AFwrite _ create_node_with_position("AFWrite",shuffle,get_node_position(shuffle)["x_pos"],get_node_position(shuffle)["y_pos"] + 100)
        AFwrite['channels'].sV..('all')


# AUTO DDOT COMP  #######################################################################################################


___ d_dot_connect(nodename,connect_node,x_0,y_0):
    """

    :param nodename: nuke node class to be created.
    :param connect_node: nuke node to connect to.
    :param x: x coordinate.
    :param y: y coordinate.
    :return: created node object.
    """
    parent_node _ ?.toNode(connect_node)
    childKnob _ ?.T_K..('child', 'child')

    dot _ create_node_with_position(nodename,parent_node,x,y)
    dot.knob('label').sV..(connect_node)
    dot.knob('tile_color').sV..(0)
    dot.knob('hide_input').sV..(T..)
    dot.knob('note_font').sV..('italic')
    dot.knob('note_font_size').sV..(22)
    dot.aK..(childKnob)

    r_ dot


___ gather_holdout_dot_names():
    """
    This function will get all names of selected Ddots.
    :return: a list of node names.
    """
    holdout_dots_names _ [node['name'].v.. ___ node __ ?.sN.. __ node['parent']]
    
    r_ holdout_dots_names


___ find_holdout_source_elements(houldout_names):
    """
    This function will get all names of selected Ddots.
    :param houldout_names: a list of node names.
    :return:
    """
    houldout_processed_list _ []
        
    ___ name __ houldout_names:
        _ _ "_".join(name.split('_')[:-2])
        __ ?.toNode(_):
            houldout_processed_list.ap..(_)
        ____
            print "no corresponding element found for {}".f..(name)
    
    r_ houldout_processed_list


___ create_and_connect_child_dots(holdouts,color):
    """

    :param holdouts:
    :param color:
    """
    multiply_list _ []
    counter _ 0
    adder _ 0
    adder_x _ 0
    pos_f_x _ N..
    pos_f_y _ N..


    ___ f,b __ itertools.izip(holdouts,color):

        __ counter __ 0 :

            pos_f_x _ get_node_position(?.toNode(f))["x_pos"]
            pos_f_y _ get_node_position(?.toNode(f))["y_pos"]
      
            child_holdout_dot _ d_dot_connect("Dot",f,pos_f_x,pos_f_y + 1000)
            child_color_dot _ d_dot_connect("Dot",b,pos_f_x - 200,pos_f_y + 1200)
            
            multiply _ create_node_with_position("Multiply",child_color_dot,pos_f_x - 35 ,pos_f_y + 1190)
            multiply.setInput(0,child_color_dot)
            multiply.setInput(1,child_holdout_dot)
            multiply['label'].sV..("DEEP HOLDOUT MULT BY ZERO")
            multiply['value'].sV..(0)
    
            multiply_list.ap..(multiply)
            counter +_ 1

        ____

            adder +_ 1000
            adder_x +_ - 1000
            child_holdout_dot _ d_dot_connect("Dot",f,pos_f_x  + adder_x ,pos_f_y + 1000 + adder)
            child_color_dot _ d_dot_connect("Dot",b,pos_f_x - 200  + adder_x ,pos_f_y + 1200 + adder)
                        
            multiply _ create_node_with_position("Multiply",child_color_dot,pos_f_x - 35  + adder_x ,pos_f_y + 1190 + adder )
            adder_x _ 0
                
            multiply.setInput(0,child_color_dot)
            multiply.setInput(1,child_holdout_dot)
            multiply['label'].sV..("DEEP HOLDOUT MULT BY ZERO")
            multiply['value'].sV..(0)


            multiply_list.ap..(multiply)
          
    counter  _ 0
    holder _ []
    
    ___ i __ ra..(le.(multiply_list)):

        __ counter __ 0:

            x _ get_node_position(multiply_list[i])["x_pos"]
            y _ get_node_position(multiply_list[i])["y_pos"]

            counter +_ 1
        
        ____
            
            x _ get_node_position(multiply_list[i])["x_pos"]
            y _ get_node_position(multiply_list[i])["y_pos"]
      
            merge _ create_node_with_position_simple("Merge2",pos_f_x,y)
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
        depth_from_deep _ ?.PS_K..('depth_from_deep', 'depth_from_deep', 'depth_for_defocus()')
        create_holdouts _ ?.E_K..('mode','build mode  ', ['contact sheet','extract'])
        deep_uberpass _ ?.E_K..('mode','build mode  ', ['contact sheet','extract'])
        auto_comp.clearFlag(?.ST..)
        author _ ?.T_K..("written by Boris Martinez")
        #ADD KNOBS
        ___ i __ (frame_range,frame_display,analysis_mode,author):
            aK..(i)
        #SET KNOB DEFAULT VALUES
        get_frame_range()

    ___ giveFrameRangeValue
        r_ frame_range.v..

    ___ get_frame_range
        __ giveFrameRangeValue() __ "global":
            first_frame _ ?.root().firstFrame()
            last_frame _ ?.root().lastFrame()
            txt _ str(in.(first_frame)) + '-' + str(in.(last_frame))
            frame_display.sV..(txt)
        ____ giveFrameRangeValue() __ "input":
            print "here should come the read frame range"
            node _ ?.sN__
            first_frame _ node.firstFrame()
            last_frame _ node.lastFrame()
            txt _ str(in.(first_frame)) + '-' + str(in.(last_frame))
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