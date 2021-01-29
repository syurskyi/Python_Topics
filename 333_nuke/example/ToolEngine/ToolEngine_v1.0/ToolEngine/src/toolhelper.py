########################################################################################################################
#
# helper module
# this module provides important functionality for the main module
#
########################################################################################################################


import os
import json
import nuke
import config


def reload_tools_menu(notify=True):
    """
    advanced load_tools function
    reload tools directory and scan for new toolsets
    If something is found display a message
    @param notify: Bool if True show message when found new tool
    :return: None
    """

    # save existing tools in list
    all_tools_before = get_all_tools()

    # reload tools dir
    load_tools()

    # save tools in list after scanning
    all_tools_after = get_all_tools()

    # check for difference
    dif_list = [tool for tool in all_tools_after if tool not in all_tools_before]
    dif_msg = "\n".join(dif_list)

    # show message of new tools
    if notify and dif_msg != "":
        nuke.message("{} new tools found:\n\n{}".format(len(dif_list), dif_msg))


def get_all_tools():
    """
    scan tools dir and get a list of all tools
    assert that all tools menus are uppercase
    :return: list list of all tools
    """

    all_tools = []

    for item in nuke.menu("Nodes").findItem("ToolEngine").items():
        # check only for tools menus which are uppercase
        if item.name().isupper():

            # iterate through each tool menu and save all its tools
            tool_menu = nuke.menu("Nodes").findItem("{}/{}".format("ToolEngine", item.name()))
            try:
                for tool in tool_menu.items():
                    all_tools.append("{}/{}".format(tool_menu.name(), tool.name()))
            except:
                continue

    return all_tools


def load_tools(notify=False):
    """
    load tools from tools root directory
    :return: None
    """

    settings = load_settings()
    build_tools_menu(settings["tools_root"])


def load_settings():
    """
    load settings file and return values
    if settings file / folder doesn't exist then create it
    :return: dict settings_data
    """

    # settings file
    settings_file = config.PATH_SETTINGS_FILE

    # make sure the settings directory exists
    if not os.path.isdir(os.path.dirname(settings_file)):
        os.makedirs(os.path.dirname(settings_file))

    # if the settings file doesn't exist then create it
    if not os.path.isfile(settings_file):
        with open(settings_file, "w") as f:
            f.write('{"tools_root": ""}')

    # load the settings file
    with open(settings_file, "r") as f:
        settings_data = json.load(f)

    return settings_data
    

def get_tools_categories(tools_root):
    """
    get a list of all tool categories
    scan the tools_root for dirs and skip tool categories that mustn't
    be loaded regarding to the config's TOOLSDIR_IGNORE and TOOLS_TEMP values
    :param tools_root: String full path of tools root
    :return: list list of all categories
    """

    if not os.path.isdir(tools_root):
        return []

    tools_categories = []

    for item in os.listdir(tools_root):
        item_full_path = os.path.join(tools_root, item)
        if os.path.isdir(item_full_path) and item != config.TOOLS_TEMP and item not in config.TOOLSDIR_IGNORE:
            tools_categories.append(item)

    return tools_categories


def build_tools_menu(tools_root):
    """
    scan tools_dir and dynamically build tools structure
    :param tools_root: String full path of tools root
    :return: None
    """

    if not os.path.isdir(tools_root):
        if tools_root == "":
            print "ToolEngine: tools_root not set. You can set it via 'ToolEngine->settings'"
        else:
            print "ToolEngine: tools_root '{}' doesn't exist".format(tools_root)
        return

    te_menu = nuke.menu("Nodes").findItem("ToolEngine")

    # scan for tools dirs
    tool_categories = get_tools_categories(tools_root)
    for category in tool_categories:

        category_menu = te_menu.addMenu(category.upper())

        # create toolsets
        item_full_path = os.path.join(tools_root, category)
        for tool in os.listdir(item_full_path):

            if os.path.splitext(tool)[1] == ".nk":
                toolset_path = os.path.join(item_full_path, tool)
                category_menu.addCommand(tool.replace(".nk", ""), lambda toolset_path=toolset_path: insert_toolset(toolset_path, delete=False), icon="")

    # temp tools
    te_menu.addSeparator()
    temp_menu = te_menu.addMenu(config.TOOLS_TEMP.upper())

    # create temp toolsets
    temp_dir = os.path.join(tools_root, config.TOOLS_TEMP)
    if not os.path.isdir(temp_dir):
        os.makedirs(temp_dir)

    for tool in os.listdir(temp_dir):
        if os.path.splitext(tool)[1] == ".nk":
            toolset_path = os.path.join(tools_root, config.TOOLS_TEMP, tool)
            temp_menu.addCommand(os.path.splitext(tool)[0], lambda toolset_path=toolset_path: insert_toolset(toolset_path, delete=True))


def insert_toolset(toolpath, delete=False):
    """
    insert toolset
    if it is a temp tool then the delete flag is set to True thus it will be removed after inserting
    :param path: String full path of toolset
    :param delete: if True delete the toolset after importing; default: False
    :return: None
    """

    if not os.path.isfile(toolpath):
        nuke.message("The tool cannot be found")
        return

    nuke.nodePaste(toolpath)

    if delete:
        # physically delete the toolset
        os.remove(toolpath)

        # remove command from menu bar
        toolset_name = os.path.splitext(os.path.basename(toolpath))[0]
        nuke.menu("Nodes").findItem("{}/{}".format("ToolEngine", config.TOOLS_TEMP.upper())).removeItem(toolset_name)



