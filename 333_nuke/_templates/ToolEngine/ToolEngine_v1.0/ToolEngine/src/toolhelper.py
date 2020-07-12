########################################################################################################################
#
# helper module
# this module provides important functionality for the main module
#
########################################################################################################################


______ __
______ j___
______ ?
______ c..


___ reload_tools_menu notify_T..
    """
    advanced load_tools function
    reload tools directory and scan for new toolsets
    If something is found display a message
    @param notify: Bool if True show message when found new tool
    :return: None
    """

    # save existing tools in list
    all_tools_before _ g..

    # reload tools dir
    l..

    # save tools in list after scanning
    all_tools_after _ g..

    # check for difference
    dif_list _ tool ___ ? __ a.. __ ? no. __ a..
    dif_msg _ "\n".join(dif_list)

    # show message of new tools
    __ notify and dif_msg !_ "":
        ?.m..("{} new tools found:\n\n{}".f..(le.(dif_list), dif_msg))


___ get_all_tools():
    """
    scan tools dir and get a list of all tools
    assert that all tools menus are uppercase
    :return: list list of all tools
    """

    all_tools _ []

    ___ item __ ?.menu("Nodes").findItem("ToolEngine").items():
        # check only for tools menus which are uppercase
        __ item.name().isupper():

            # iterate through each tool menu and save all its tools
            tool_menu _ ?.menu("Nodes").findItem("{}/{}".f..("ToolEngine", item.name()))
            ___
                ___ tool __ tool_menu.items():
                    all_tools.ap..("{}/{}".f..(tool_menu.name(), tool.name()))
            ______
                continue

    r_ all_tools


___ load_tools(notify_F..):
    """
    load tools from tools root directory
    :return: None
    """

    settings _ load_settings()
    build_tools_menu(settings["tools_root"])


___ load_settings():
    """
    load settings file and return values
    if settings file / folder doesn't exist then create it
    :return: dict settings_data
    """

    # settings file
    settings_file _ config.PATH_SETTINGS_FILE

    # make sure the settings directory exists
    __ no. __.path.isdir(__.path.dirname(settings_file)):
        __.makedirs(__.path.dirname(settings_file))

    # if the settings file doesn't exist then create it
    __ no. __.path.isfile(settings_file):
        w__ o..(settings_file, "w") __ f:
            f.write('{"tools_root": ""}')

    # load the settings file
    w__ o..(settings_file, "r") __ f:
        settings_data _ j___.load(f)

    r_ settings_data
    

___ get_tools_categories(tools_root):
    """
    get a list of all tool categories
    scan the tools_root for dirs and skip tool categories that mustn't
    be loaded regarding to the config's TOOLSDIR_IGNORE and TOOLS_TEMP values
    :param tools_root: String full path of tools root
    :return: list list of all categories
    """

    __ no. __.path.isdir(tools_root):
        r_ []

    tools_categories _ []

    ___ item __ __.listdir(tools_root):
        item_full_path _ __.path.join(tools_root, item)
        __ __.path.isdir(item_full_path) and item !_ config.TOOLS_TEMP and item no. __ config.TOOLSDIR_IGNORE:
            tools_categories.ap..(item)

    r_ tools_categories


___ build_tools_menu(tools_root):
    """
    scan tools_dir and dynamically build tools structure
    :param tools_root: String full path of tools root
    :return: None
    """

    __ no. __.path.isdir(tools_root):
        __ tools_root __ "":
            print "ToolEngine: tools_root not set. You can set it via 'ToolEngine->settings'"
        ____
            print "ToolEngine: tools_root '{}' doesn't exist".f..(tools_root)
        r_

    te_menu _ ?.menu("Nodes").findItem("ToolEngine")

    # scan for tools dirs
    tool_categories _ get_tools_categories(tools_root)
    ___ category __ tool_categories:

        category_menu _ te_menu.aM..(category.upper())

        # create toolsets
        item_full_path _ __.path.join(tools_root, category)
        ___ tool __ __.listdir(item_full_path):

            __ __.path.splitext(tool)[1] __ ".nk":
                toolset_path _ __.path.join(item_full_path, tool)
                category_menu.aC..(tool.replace(".nk", ""), lambda toolset_path_toolset_path: insert_toolset(toolset_path, delete_F..), icon_"")

    # temp tools
    te_menu.addSeparator()
    temp_menu _ te_menu.aM..(config.TOOLS_TEMP.upper())

    # create temp toolsets
    temp_dir _ __.path.join(tools_root, config.TOOLS_TEMP)
    __ no. __.path.isdir(temp_dir):
        __.makedirs(temp_dir)

    ___ tool __ __.listdir(temp_dir):
        __ __.path.splitext(tool)[1] __ ".nk":
            toolset_path _ __.path.join(tools_root, config.TOOLS_TEMP, tool)
            temp_menu.aC..(__.path.splitext(tool)[0], lambda toolset_path_toolset_path: insert_toolset(toolset_path, delete_T..))


___ insert_toolset(toolpath, delete_F..):
    """
    insert toolset
    if it is a temp tool then the delete flag is set to True thus it will be removed after inserting
    :param path: String full path of toolset
    :param delete: if True delete the toolset after importing; default: False
    :return: None
    """

    __ no. __.path.isfile(toolpath):
        ?.m..("The tool cannot be found")
        r_

    ?.nodePaste(toolpath)

    __ delete:
        # physically delete the toolset
        __.remove(toolpath)

        # remove command from menu bar
        toolset_name _ __.path.splitext(__.path.basename(toolpath))[0]
        ?.menu("Nodes").findItem("{}/{}".f..("ToolEngine", config.TOOLS_TEMP.upper())).removeItem(toolset_name)



