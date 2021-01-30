###########################################################################################################
#
#  scriptCleanup
#
#  @author simon jokuschies
#  @version 1.1
#  @contact info@leafpictures.de
#  @website www.leafpictures.de
#  @pluginurl: www.leafpictures.de/code/script-cleanup
#
#  description:
#  collect all nodes that are not connected to any node and/ or which output is not used at all in the current script.
#  Hold Shift and press C. This opens the scriptCleanup window in which you can choose to select:
#
#  dependent nodes: Node's output is not used; Nodes that are connected to the node's output
#                   (all nodes that read information from this node)
#
#  dependency nodes: Node's input is not used; Nodes that are connected to the node's input
#                   (all nodes referred to by this node)
#
#  if nothing is select: check for all nodes that don't have any inputs connected
#
#  in both methods (dependent/dependencies) these node connection options are included:
#  connection via expressions
#  connection via visible input pipes
#  connection via hidden input pipes
#
#
#  after clicking the "collect" button the window shows unused nodes depending on the selected mode: nodes that are
#  not connected to any node and/ or which output is not used at all.
#
#  The nodes table shows a row for each unused node:
#      # a button with the name of the unused node. By clicking it the dag gets navigated to the node
#      # a checkbox for batch processing disable/enable (se below)
#      # a button to remove the node
#
#  At the bottom of the window you have three buttons:
#  # toggle check/uncheck nodes: check or uncheck all unused nodes in the table
#  # disable all checked nodes: click this button to disable all checked nodes. If a checkbox is unchecked then
#    the unused node will be enabled
#  # remove all checked nodes: click this button to remove all checked nodes
#
#  instalation
#
#  put the whole scriptCleanup folder in your nuke home directory
#  in init.py in your nuke home directory add this line (without "#"):
#
#  nuke.pluginAddPath("scriptCleanup")
#
#
#  Version info
#
#  v1.1
#  - Make ready for Nuke 11
#
#  v1.0
#  - Initial release
#
##########################################################################################################

# ignore_list
# ignore all nodes that are from one of these node classes
ignore_list _ ["BackdropNode"]

# no need to change anything from here. Edit only if you exactly know what you're doing

______ ?

___
    ____ ?.?G.. ______ _
    ____ ?.?C.. ______ _
______ ImportError:
    ____ ?.?G.. ______ _
    ____ ?.?C.. ______ _
    ____ ?.?W.. ______ _


___ collect_nodes(mode):
    """
    get all nodes of the search of selected dependent/ dependencies
    @param mode: list mode of dependents/ dependencies searching mode
    :return: list nodes to cleanup
    """

    cleanup_list _ # list
    dependent_ _ mode[0]
    dependencies_ _ mode[1]

    ___ node __ ?.allNodes

        __ node.Class() __ ignore_list:
            c___

        __ dependent_ an. dependencies_:
            __ le.(node.dependent()) __ 0 an. le.(node.dependencies()) __ 0 an. node.minInputs() > 0 an. node.maxOutputs() > 0:
                cleanup_list.ap..(node)

        ____ dependent_ an. no. dependencies_ an. node.maxOutputs() > 0:
            __ le.(node.dependent()) __ 0:
                cleanup_list.ap..(node)

        ____ no. dependent_ an. dependencies_ an. node.minInputs() > 0 an. node.maxOutputs() > 0:
            __ le.(node.dependencies()) __ 0:
                cleanup_list.ap..(node)

        ____
            __ node.minInputs() > 0 an. node.inputs() __ 0:
                cleanup_list.ap..(node)

    r_ cleanup_list


___ cleanup
    """
    show cleanup window
    :return: None
    """

    g__ c
    c _ CleanModeDialog()
    c.raise_()
    c.s__


c_ CleanModeDialog(?W..):
    """
    dialog to ask for cleanup mode (dependent and dependencies)
    """

    ___ -
        s_(CleanModeDialog, self).- ()
        sQT..("Please choose the cleanup mode")
        setFixedWidth(550)

        # buildUI
        create_widgets()
        create_layouts()
        create_signals()

    ___ create_widgets
        check_dependent _ QCheckBox("dependent: Node's output is not used (all nodes that read information from this node)")
        check_dependent.setChecked(T..)
        check_dependencies _ QCheckBox("dependencies: Node's input is not used (all nodes referred to by this node)")
        check_dependencies.setChecked(T..)
        push_collect _ ?PB..("collect")
        push_collect.setStyleSheet("QPushButton{background-color: rgba(51, 204, 255, 150);}")
        push_cancel _ ?PB..("cancel")

    ___ create_layouts
        layout_master _ ?VB..
        layout_master.aW..(check_dependent)
        layout_master.aW..(check_dependencies)

        layout_push _ QHBoxLayout()
        layout_push.aW..(push_collect)
        layout_push.aW..(push_cancel)
        layout_master.addLayout(layout_push)

        sL..(layout_master)

    ___ create_signals
        push_cancel.c__.c..(close)
        push_collect.c__.c..(process_cleanup)

    ___ process_cleanup
        """
        process cleanup and create cleanup table
        :return: None
        """

        cleanup_list _ collect_nodes([check_dependent.isChecked(), check_dependencies.isChecked()])
        populate(cleanup_list)
        sQT..("cleanup script")

    ___ populate(self, cleanup_list):
        """
        create widgets for each cleanup node
        @param: cleanup_list: list of nodes to cleanup
        :return: None
        """

        ___
            group_cleanup.setParent(N..)
            push_close.setParent(N..)
        ______ E.., e:
            p..

        table_cleanup _ QTableWidget()

        checkboxes _ # list

        # set dimensions
        table_cleanup.setRowCount(le.(cleanup_list))
        table_cleanup.setColumnCount(3)
        table_cleanup.setColumnWidth(0, 250)
        table_cleanup.horizontalHeader().setStretchLastSection(T..)

        # header
        table_cleanup.setHorizontalHeaderItem(0, QTableWidgetItem("node"))
        table_cleanup.setHorizontalHeaderItem(1, QTableWidgetItem("check"))
        table_cleanup.setHorizontalHeaderItem(2, QTableWidgetItem("delete"))

        r _ 0
        ___ node __ cleanup_list:

            # node
            push_node _ ?PB..(node.n..
            push_node.setProperty("node", node.n..
            table_cleanup.setCellWidget(r, 0, push_node)
            push_node.c__.c..(jump_to_node)

            # push checkbox
            widget _ ?W..()
            layout_widget _ QHBoxLayout()
            checkbox _ QCheckBox()
            checkbox.setProperty("node", node.n..
            layout_widget.addStretch()
            layout_widget.aW..(checkbox)
            layout_widget.addStretch()
            widget.sL..(layout_widget)
            table_cleanup.setCellWidget(r, 1, widget)
            checkboxes.ap..(checkbox)

            # remove push
            push_remove_node _ ?PB..("delete")
            push_remove_node.setProperty("node", node.n..
            push_remove_node.setStyleSheet("QPushButton{background-color: rgb(90,30,30);}")
            table_cleanup.setCellWidget(r, 2, push_remove_node)
            push_remove_node.c__.c..(l___ r_r, node_node: remove_node(r, node.name()))

            r +_ 1

        # resize main
        resize(QSize(width(), 200 + (r * 40)))

        group_cleanup _ QGroupBox()
        layout_cleanup_master _ ?VB..
        layout_cleanup_master.aW..(table_cleanup)

        push_toggle _ ?PB..("toggle check/uncheck nodes")
        push_disable_checked _ ?PB..("disable all checked nodes")
        push_remove_checked _ ?PB..("remove all checked nodes")
        layout_cleanup_push _ QHBoxLayout()
        layout_cleanup_push.aW..(push_toggle)
        layout_cleanup_push.aW..(push_disable_checked)
        layout_cleanup_push.aW..(push_remove_checked)
        layout_cleanup_master.addLayout(layout_cleanup_push)
        group_cleanup.sL..(layout_cleanup_master)

        push_toggle.c__.c..(toggle_checkboxes)
        push_disable_checked.c__.c..(disable_checked)
        push_remove_checked.c__.c..(remove_nodes)

        push_close _ ?PB..("close")
        push_close.c__.c..(close)
        layout_master.aW..(group_cleanup)
        layout_master.aW..(push_close)

    ___ jump_to_node
        """
        jump to clicked node name
        :return: None
        """

        node _ ?.tN..(sender().property("node"))
        node.selectOnly()
        ?.zoom(1, (node.xpos(), node.ypos()))

    ___ remove_node(self, row, node):
        """
        remove node
        @param row: int row to remove from table
        @param node: String name of node to remove
        :return: None
        """

        ?.delete(?.tN..(node))
        process_cleanup()

    ___ remove_nodes
        """
        remove all checked nodes
        :return: None
        """

        ___ c __ checkboxes:
            __ c.isChecked
                ?.delete(?.tN..(c.property("node")))

        cleanup_list _ collect_nodes([check_dependent.isChecked(), check_dependencies.isChecked()])
        process_cleanup()

    ___ disable_checked
        """
        disable checked nodes
        :return: None
        """

        ___ c __ checkboxes:
            ___
                disable _ ?.tN..(c.property("node"))["disable"].sV..(c.isChecked())
            ______ E.., e:
                c___

    ___ toggle_checkboxes
        """
        toggle check/uncheck checkboxes
        :return: None
        """

        __ checkboxes[0].isChecked
            ___ c __ checkboxes:
                c.setChecked(F..)
        ____
            ___ c __ checkboxes:
                c.setChecked(T..)

    ___ keyPressEvent(self, event):
        """
        close on escape key pressed
        :return: None
        """

        __ event.key() __ __.Key_Escape:
            c__
