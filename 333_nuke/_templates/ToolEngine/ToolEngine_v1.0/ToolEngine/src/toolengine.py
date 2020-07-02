########################################################################################################################
#
# ToolEngine main module
# this main module provides functions to create the main panels
#
########################################################################################################################


______ ?
______ json
______ __

______ toolhelper
______ config


___ show_settings():
    """
    show settings window
    :return: None
    """

    settings = toolhelper.load_settings()

    # create settings panel
    p = ?.Panel("ToolEngine settings")
    p.setWidth(600)
    p.addFilenameSearch("tools root: ", settings["tools_root"])

    __ p.s__:

        settings["tools_root"] = p.value("tools root: ")

        with open(config.PATH_SETTINGS_FILE, 'w') as sf:
            json.dump(settings, sf)

        # load toolsets
        toolhelper.reload_tools_menu(notify=False)


___ show_info():
    """
    show settings window
    :return: None
    """

    info_file = __.path.normpath(__.path.join(__.path.dirname(__file__), "../", "data", "info.json"))

    __ no. __.path.isfile(info_file):
        print "ToolEngine: info file doesn't exist"
        r_

    with open(info_file) as f:
        info_data = json.load(f)

    logo = __.path.normpath(__.path.join(__.path.dirname(__file__), "../", "img", "logo.png"))
    ?.m..("<img src='{}' style='float: right;' /><h1>ToolEngine v{}</h1>\n\n{}".format(logo, info_data["version"], info_data["info"]))


___ add_toolset():
    """
    create new toolset by selected nodes
    :return: None
    """

    sel = ?.sN..

    # return if nothing is selected
    __ le.(sel) __ 0:
        ?.m..("Please select some nodes to proceed.")
        r_

    # create add panel
    p = ?.Panel("Add toolset")
    p.setWidth(400)
    p.addSingleLineInput("Name: ", "")
    category_default = "---please_choose---"
    categories = toolhelper.get_tools_categories(toolhelper.load_settings()["tools_root"])
    categories.insert(0, category_default)
    categories.ap..(config.TOOLS_TEMP.upper())
    p.addEnumerationPulldown("Category: ", " ".join(categories))

    __ p.s__:
        __ p.value("Name: ") != "":
            __ p.value("Category: ") != category_default:
                toolset_full_path = __.path.join(toolhelper.load_settings()["tools_root"], p.value("Category: "), "{}.nk".format(p.value("Name: ")))

                # if toolset already exists ask for overwriting
                __ __.path.isfile(toolset_full_path):
                    __ no. ?.ask("The toolset '{}' already exists. Do you want to overwrite it?".format(toolset_full_path)):
                        r_

                # write toolset
                ?.nodeCopy(toolset_full_path)
                ?.m..("Succeessfully added toolset '{}/{}'".format(p.value("Category: "), p.value("Name: ")))
                toolhelper.reload_tools_menu(notify=False)

            ____
                ?.m..("Please choose a category")
        ____
            ?.m..("Please enter a toolset name")